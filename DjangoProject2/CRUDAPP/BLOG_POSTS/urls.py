from django.urls import path

from . import views

urlpatterns = [
    path('a/', views.index, name='index'),
    path('',views.blogger_create,name='form'),
    path('list/', views.blogger_list, name='list'),
    path('<id>/delete/', views.blogger_delete, name='delete'),
]