from django.urls import path

from . import views

app_name = "course"

urlpatterns = [
    path("courses/", views.CourseListView.as_view(), name="courses"),
    path("courses/<slug:slug>/", views.Course.as_view(), name="course"),
]
