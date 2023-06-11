from django.urls import path
from .views import TodoListCreateAPIView, TodoRetrieveUpdateDestroyAPIView, UserRegistrationAPIView, UserLoginAPIView

urlpatterns = [
    path('todos/', TodoListCreateAPIView.as_view(), name='todo-list-create'),
    path('todos/<int:pk>/', TodoRetrieveUpdateDestroyAPIView.as_view(), name='todo-retrieve-update-destroy'),
    path('users/register/', UserRegistrationAPIView.as_view(), name='user-registration'),
    path('users/login/', UserLoginAPIView.as_view(), name='user-login'),
]
