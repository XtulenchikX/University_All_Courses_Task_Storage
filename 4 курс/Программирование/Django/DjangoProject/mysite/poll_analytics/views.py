from blog.models import Poll, Choice
from django.http import HttpResponse
import csv
from django.db.models import Sum
import io
import base64
import matplotlib.pyplot as plt
from matplotlib import use
from rest_framework.response import Response
from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


class PollAnalyticsView(APIView):
    @swagger_auto_schema(
        operation_description="Get poll analytics",
        manual_parameters=[
            openapi.Parameter('poll_id', openapi.IN_QUERY, description="Poll ID", type=openapi.TYPE_INTEGER,
                              required=True)
        ],
        responses={
            200: openapi.Response(
                description="Successful response",
                examples={
                    "application/json": {
                        "question": "Ваш любимый сезон года?",
                        "choices": [
                            {"choice_text": "Зима", "votes": 25, "percentage": 25.0},
                            {"choice_text": "Лето", "votes": 50, "percentage": 50.0},
                            {"choice_text": "Осень", "votes": 15, "percentage": 15.0},
                            {"choice_text": "Весна", "votes": 10, "percentage": 10.0}
                        ],
                        "date_conducted": "2023-10-01T12:00:00"
                    }
                }
            ),
            400: openapi.Response(description="Invalid request"),
            404: openapi.Response(description="Client Error")
        }
    )
    def get(self, request, *args, **kwargs):
        poll_id = request.query_params.get('poll_id')
        if poll_id:
            try:
                poll_id = int(poll_id)
            except ValueError:
                return Response({"error": "poll_id must be an integer"}, status=400)
        if not poll_id:
            return Response({"error": "poll_id is required"}, status=400)

        try:
            poll = Poll.objects.get(id=poll_id)
        except Poll.DoesNotExist:
            return Response({"error": "Poll not found"}, status=404)

        choices = Choice.objects.filter(poll=poll)
        total_votes = sum(choice.votes for choice in choices)
        choices_data = [
            {
                "choice_text": choice.text,
                "votes": choice.votes,
                "percentage": (choice.votes / total_votes * 100) if total_votes > 0 else 0
            }
            for choice in choices]

        data = {
            "question": poll.question,
            "choices": choices_data,
            "date_conducted": poll.created_date.strftime('%Y-%m-%dT%H:%M:%S')
        }

        return Response(data)


class PollListView(APIView):
    @swagger_auto_schema(
        operation_description="Get a list of polls",
        manual_parameters=[
            openapi.Parameter('sort_by', openapi.IN_QUERY, description="Sort by (votes / date)",
                              type=openapi.TYPE_STRING),
            openapi.Parameter('order', openapi.IN_QUERY, description="Order of sort (asc / desc)",
                              type=openapi.TYPE_STRING)
        ],
        responses={
            200: openapi.Response(
                description="Successful response",
                examples={
                    "application/json": [
                        {
                            "id": 1,
                            "question": "Какой ваш любимый праздник?",
                            "created_date": "2023-10-01T12:00:00",
                            "total_votes": 100
                        },
                        {
                            "id": 2,
                            "question": "Какой у вас рабочиц график?",
                            "created_date": "2023-09-25T12:00:00",
                            "total_votes": 80
                        }
                    ]
                }
            ),
            400: openapi.Response(description="Invalid request")
        }
    )
    def get(self, request):
        sort_by = request.query_params.get('sort_by')
        order = request.query_params.get('order', 'desc')

        if order not in ['asc', 'desc']:
            return Response({"error": "order must be 'asc' or 'desc'"}, status=400)

        order_prefix = '' if order == 'asc' else '-'

        if sort_by == 'votes':
            polls = Poll.objects.annotate(total_votes=Sum('choices__votes')).order_by(f'{order_prefix}total_votes')
        elif sort_by == 'date':
            polls = Poll.objects.all().order_by(f'{order_prefix}created_date')
        else:
            polls = Poll.objects.all().order_by(f'{order_prefix}created_date')

        polls_data = []
        for poll in polls:
            choices = Choice.objects.filter(poll=poll)
            total_votes = sum(choice.votes for choice in choices)
            poll_data = {
                "id": poll.id,
                "question": poll.question,
                "created_date": poll.created_date.strftime('%Y-%m-%dT%H:%M:%S'),
                "total_votes": total_votes
            }
            polls_data.append(poll_data)

        return Response(polls_data)


class PollExportJSONView(APIView):
    def get(self, request):
        polls = Poll.objects.all()
        polls_data = []
        for poll in polls:
            choices = Choice.objects.filter(poll=poll)
            total_votes = sum(choice.votes for choice in choices)
            poll_data = {
                "id": poll.id,
                "question": poll.question,
                "created_date": poll.created_date.strftime('%Y-%m-%dT%H:%M:%S'),
                "total_votes": total_votes,
                "choices": [{"choice_text": choice.text, "votes": choice.votes} for choice in choices]
            }
            polls_data.append(poll_data)
        return Response(polls_data, content_type="application/json")


class PollExportCSVView(APIView):
    def get(self, request):
        polls = Poll.objects.all()
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="polls.csv"'

        response.write('\ufeff'.encode('utf8'))  # Add BOM to handle UTF-8 in Excel
        writer = csv.writer(response)
        writer.writerow(['ID', 'Question', 'Created Date', 'Total Votes', 'Choices'])

        for poll in polls:
            choices = Choice.objects.filter(poll=poll)
            total_votes = sum(choice.votes for choice in choices)
            choices_text = "; ".join([f"{choice.text} ({choice.votes})" for choice in choices])
            created_date = poll.created_date.strftime('%Y-%m-%d %H:%M:%S')
            writer.writerow([poll.id, poll.question, created_date, total_votes, choices_text])

        return response


use('Agg')


class PollChartView(APIView):
    @swagger_auto_schema(
        operation_description="Get graphic of poll | base64",
        manual_parameters=[
            openapi.Parameter('poll_id', openapi.IN_QUERY, description="Poll ID",
                              type=openapi.TYPE_INTEGER, required=True)
        ],
        responses={
            200: openapi.Response(
                description="Successful response",
                examples={
                    "application/json": {
                        "chart": "data:image/png;base64,..."
                    }
                }
            ),
            400: openapi.Response(description="Invalid request"),
            404: openapi.Response(description="Client error")
        }
    )
    def get(self, request, *args, **kwargs):
        poll_id = request.query_params.get('poll_id')
        if poll_id:
            try:
                poll_id = int(poll_id)
            except ValueError:
                return Response({"error": "poll_id must be an integer"}, status=400)
        if not poll_id:
            return Response({"error": "poll_id is required"}, status=400)

        try:
            poll = Poll.objects.get(id=poll_id)
        except Poll.DoesNotExist:
            return Response({"error": "Poll not found"}, status=404)

        choices = Choice.objects.filter(poll=poll)
        choice_texts = [choice.text for choice in choices]
        votes = [choice.votes for choice in choices]

        plt.figure(figsize=(10, 6))
        plt.bar(choice_texts, votes, color='gray')
        plt.xlabel('Варианты')
        plt.ylabel('Голоса')
        plt.tight_layout()

        buffer = io.BytesIO()
        plt.savefig(buffer, format='png')
        buffer.seek(0)
        image_png = buffer.getvalue()
        buffer.close()

        image_base64 = base64.b64encode(image_png).decode('utf-8')
        image_data = f"data:image/png;base64,{image_base64}"

        plt.close()

        return Response({"chart": image_data})
