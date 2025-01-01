from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.models import Group
from django.http import HttpResponseForbidden, JsonResponse
from .models import Post, Poll, Choice
from .forms import PostForm
import logging

logger = logging.getLogger(__name__)


def is_admin(user):
    return user.is_superuser


def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    polls = Poll.objects.all()
    return render(request, 'blog/post_list.html', {'posts': posts, 'polls': polls})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})


@login_required
@user_passes_test(is_admin)
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})


@login_required
@user_passes_test(is_admin)
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})


def polls_list(request):
    polls = Poll.objects.all()
    return render(request, 'blog/poll_list.html', {'polls': polls})


def poll_vote(request, pk):
    poll = get_object_or_404(Poll, pk=pk)

    if request.user in poll.voted_users.all():
        return redirect('poll_results', pk=poll.pk)

    if request.method == "POST":
        choice_id = request.POST.get("choice")
        if choice_id:
            choice = get_object_or_404(Choice, pk=choice_id, poll=poll)
            choice.votes += 1
            choice.save()
            poll.voted_users.add(request.user)
            poll.save()
            return redirect('poll_results', pk=poll.pk)

    return render(request, 'blog/poll_vote.html', {'poll': poll})


def poll_results(request, pk):
    poll = get_object_or_404(Poll, pk=pk)

    if request.user not in poll.voted_users.all():
        return redirect('poll_vote', pk=poll.pk)

    return render(request, 'blog/poll_results.html', {'poll': poll})


@login_required
@user_passes_test(is_admin)
def poll_new(request):
    if request.method == "POST":
        question = request.POST.get("question")
        choices_text = request.POST.get("choices")
        if question and choices_text:
            choices = choices_text.splitlines()

            poll = Poll.objects.create(question=question, created_date=timezone.now())

            for choice_text in choices:
                if choice_text.strip():
                    Choice.objects.create(poll=poll, text=choice_text.strip())

            return redirect('polls_list')
    return render(request, 'blog/poll_new.html')


@login_required
@user_passes_test(is_admin)
def poll_edit(request, pk):
    poll = get_object_or_404(Poll, pk=pk)
    if request.method == "POST":
        question = request.POST.get("question")
        choices = request.POST.getlist("choices")
        if question and choices:
            poll.question = question
            poll.save()
            poll.choices.all().delete()
            for choice_text in choices:
                Choice.objects.create(poll=poll, text=choice_text)
            return redirect('polls_list')
    return render(request, 'blog/poll_edit.html', {'poll': poll})


@login_required
@user_passes_test(is_admin)
def poll_delete(request, pk):
    poll = get_object_or_404(Poll, pk=pk)
    poll.delete()
    return redirect('polls_list')


def polls_stat(request):
    if request.method == "GET":
        return render(request, 'blog/polls_stat.html')
    elif request.method == "POST":
        sort_by = request.POST.get("sort_by")

        polls = Poll.objects.all()
        if sort_by == "popularity_desc":
            polls = polls.annotate(total_votes=Sum('choices__votes')).order_by('-total_votes')
        elif sort_by == "popularity_asc":
            polls = polls.annotate(total_votes=Sum('choices__votes')).order_by('total_votes')
        elif sort_by == "date_asc":
            polls = polls.order_by('created_date')
        elif sort_by == "date_desc":
            polls = polls.order_by('-created_date')

        polls_data = [{"id": poll.id, "question": poll.question} for poll in polls]
        return JsonResponse({"polls": polls_data})


def poll_stats(request, pk):
    poll = get_object_or_404(Poll, pk=pk)
    choices = poll.choices.all()
    choices_data = [{"text": choice.text, "votes": choice.votes} for choice in choices]
    return JsonResponse({"question": poll.question, "choices": choices_data})


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            common_users_group = Group.objects.get(name='CommonUsers')
            user.groups.add(common_users_group)
            login(request, user)
            return redirect('post_list')
        else:
            logger.error("Ошибки формы регистрации: %s", form.errors)
    else:
        form = UserCreationForm()
    return render(request, 'blog/register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('post_list')
        else:
            logger.error("Ошибки формы входа: %s", form.errors)
    else:
        form = AuthenticationForm()
    return render(request, 'blog/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('post_list')
