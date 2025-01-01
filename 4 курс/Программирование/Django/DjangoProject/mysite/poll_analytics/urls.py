from django.urls import path
from .views import PollAnalyticsView, PollListView, PollExportJSONView, PollExportCSVView, PollChartView
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Poll Analytics API",
        default_version='v1',
        description="Analytics API",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('poll-analytics/', PollAnalyticsView.as_view(), name='poll_analytics'),
    path('poll-list/', PollListView.as_view(), name='poll_list'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('export/json/', PollExportJSONView.as_view(), name='poll_export_json'),
    path('export/csv/', PollExportCSVView.as_view(), name='poll_export_csv'),
    path('poll-chart/', PollChartView.as_view(), name='poll_chart'),
]
