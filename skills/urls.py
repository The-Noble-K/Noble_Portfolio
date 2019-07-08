from django.urls import path
from skills import views

urlpatterns = [
    path("", views.skill_index, name="skill_index")
]
