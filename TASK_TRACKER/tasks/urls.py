from django.urls import path
from .views import *
app_name = "tasks"
urlpatterns = [
    path("", index, name="index"),

    path("register/", register_view),
    path("login/", login_view),
    path("logout/", logout_view),

    path("toggle/<int:task_id>/", toggle),
    path("delete/<int:task_id>/", delete),
]