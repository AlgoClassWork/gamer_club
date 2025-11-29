from django.views.generic import ListView
from .models import Game

class GameListView(ListView):
    model = Game
    template_name = 'game_list.html'
    context_object_name = 'games'