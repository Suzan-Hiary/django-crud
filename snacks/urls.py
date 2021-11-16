from .views import SnackCreateView , SnackDeleteView ,SnackDetailView ,SnackListView ,SnackUpdateView
from django.urls import path 



urlpatterns=[
    path('' , SnackListView.as_view() , name='snacks'),
    path('<int:pk>/detail/' , SnackDetailView.as_view() , name='detail'),
    path('create/' , SnackCreateView.as_view() , name='create'),
    path('<int:pk>/update/' , SnackUpdateView.as_view() , name='update'),
    path('<int:pk>/delete/' , SnackDeleteView.as_view() , name='delete'),
]