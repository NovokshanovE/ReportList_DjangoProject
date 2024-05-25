from django.urls import path
from . import views

urlpatterns = [
    path('section/<str:section>/', views.section_view, name='section_view'),
    path('', views.home_view, name='home_view'),
    path('file/<int:file_id>/', views.file_detail, name='file_detail'),
]
