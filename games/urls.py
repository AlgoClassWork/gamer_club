from django.urls import path
from .views import *

urlpatterns = [
   path('', GameListView.as_view(), name='game_list'),
   path('game/<int:pk>/', GameDetailView.as_view(), name='game_detail')
]