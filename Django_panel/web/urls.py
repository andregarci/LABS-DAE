from django.urls import path

from . import views

app_name = 'web'

urlpatterns = [
    path('', views.AlumnoView.as_view(),name='index'),
    path('delete-alumno/<int:pk>/', views.AlumnoDeleteView.as_view(), name='delete_alumno'),

    path('profesor/', views.ProfesorView.as_view(), name='Profesores'),
    path('delete-profesor/<int:pk>/', views.ProfesorDeleteView.as_view(), name='delete_profesor'),
]