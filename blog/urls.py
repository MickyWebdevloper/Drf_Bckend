from django.urls import path

from . import views

app_name = "store"

urlpatterns = [
    path("api/", views.BlogPostListView.as_view(), name="store_home"),
    path("api/category/", views.CategoryListView.as_view(), name="categories"),
    path("api/<slug:slug>/", views.BlogPost.as_view(), name="product"),
    path("api/category/<slug:category>/", views.CategoryItemView.as_view(), name="category_item"),
    # path("api/category/detail/<slug:category>/", views.CategoryView.as_view(), name="category_detail"),
]
