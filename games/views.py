from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Game

class GameListView(ListView):
    model = Game
    template_name = 'game_list.html'
    context_object_name = 'games'
    paginate_by = 5

class GameDetailView(DetailView):
    model = Game
    template_name = 'game_detail.html'
    context_object_name = 'game'

class GameCreateView(CreateView):
    model = Game
    template_name = 'game_form.html'
    fields = ['title', 'genre', 'release_year', 'description']

class GameUpdateView(UpdateView):
    model = Game
    template_name = 'game_form.html'
    fields = ['title', 'genre', 'release_year', 'description']

class GameDeleteView(DeleteView):
    model = Game
    template_name = 'game_confirm_delete.html'
    success_url = reverse_lazy('game_list')
