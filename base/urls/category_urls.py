from django.urls import path
from base.views import category_views as views


urlpatterns = [
    path('category/', views.CategoryViewset, name='category'),
]
