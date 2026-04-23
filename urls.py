from django.urls import path
from tasks.views import index, toggle, delete

urlpatterns = [
    path('', index),
    path('toggle/<int:task_id>/', toggle),
    path('delete/<int:task_id>/', delete),
]