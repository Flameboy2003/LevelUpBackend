from django.urls import path
from . import views

urlpatterns = [
    path('polls/create/', views.create_poll),
    path('polls/', views.list_polls),
    path('poll-vote/', views.save_vote),
]
