from django.urls import path
from . import views

urlpatterns = [
    path('section/<str:section>/', views.section_view, name='section_view'),
    path('', views.home_view, name='home_view'),
    path('file/<int:file_id>/', views.file_detail, name='file_detail'),
    path('about/', views.about, name='about'),
    # path('groups/', views.group_list, name='group_list'),
    path('groups/<int:group_id>/', views.file_list, name='file_list'),
]
