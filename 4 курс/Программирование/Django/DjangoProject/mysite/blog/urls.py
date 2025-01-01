from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.post_list, name="post_list"),
    path("post/<int:pk>/", views.post_detail, name="post_detail"),
    path("post/new/", views.post_new, name="post_new"),
    path("post/<int:pk>/edit/", views.post_edit, name="post_edit"),
    path("polls/", views.polls_list, name="polls_list"),
    path("polls/<int:pk>/vote/", views.poll_vote, name="poll_vote"),
    path("polls/<int:pk>/results/", views.poll_results, name="poll_results"),
    path("polls/new/", views.poll_new, name="poll_new"),
    path("polls/<int:pk>/edit/", views.poll_edit, name="poll_edit"),
    path("polls/<int:pk>/delete/", views.poll_delete, name="poll_delete"),
    path("polls/statistics/", views.polls_stat, name="polls_stat"),
    path("accounts/", include("allauth.urls")),
]
