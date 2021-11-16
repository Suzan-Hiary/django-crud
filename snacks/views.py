from django.shortcuts import render
from django.views.generic import ListView , DeleteView ,UpdateView , DetailView , CreateView
from django.urls import reverse_lazy, reverse
from .models import Snack



class SnackListView(ListView):
    template_name = 'list_view.html'
    model=Snack
    
class SnackDetailView(DetailView):
    template_name='detail_view.html'
    model=Snack 
    


class SnackCreateView(CreateView):
    template_name='create_view.html'
    model=Snack
    fields = ['title', 'purchaser', 'description']

class SnackUpdateView(UpdateView):
    template_name='update_view.html'
    model=Snack
    fields = ['title', 'purchaser', 'description']

class SnackDeleteView(DeleteView):
    template_name='delete_view.html'
    model=Snack
    success_url = reverse_lazy('snacks') # when i delete , i will be redirected to homepage