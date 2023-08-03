# from django.shortcuts import get_object_or_404
from rest_framework import generics

# from . import models
from .models import Course
from .serializers import CourseSerializer


class CourseListView(generics.ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class Course(generics.RetrieveAPIView):
    lookup_field = "slug"
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


# class CategoryItemView(generics.ListAPIView):
#     serializer_class = BlogPostSerializer

#     def get_queryset(self):
#         try:
#             category_name = get_object_or_404(Category, name=self.kwargs.get("category"))
#             return models.BlogPost.objects.filter(category=category_name)
#         except Category.DoesNotExist:
#             return models.BlogPost.objects.none()


# class CategoryView(generics.RetrieveAPIView):
#     lookup_field = "slug"
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer


# class CategoryListView(generics.ListAPIView):
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer
