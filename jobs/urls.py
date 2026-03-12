from django.urls import path
from . import views

urlpatterns = [
    path("", views.dashboard, name="dashboard"),
    path("toggle-apply/<int:job_id>/", views.toggle_apply, name="toggle_apply"),
]