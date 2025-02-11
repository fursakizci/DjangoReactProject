from .views import main, RoomView
from django.urls import path, include

urlpatterns = [
    path('room', RoomView.as_view()), #thats means call the main function
    path('', main)
]
