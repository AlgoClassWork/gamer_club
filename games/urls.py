from django.urls import path
from .views import *

urlpatterns = [
   path('', GameListView.as_view(), name='game_list'),
   path('game/<int:pk>/', GameDetailView.as_view(), name='game_detail'),
   path('game/new/', GameCreateView.as_view(), name='game_create'),
   path('game/update/<int:pk>/', GameUpdateView.as_view(), name='game_update'),
   path('game/delete/<int:pk>/', GameDeleteView.as_view(), name='game_delete'),
]