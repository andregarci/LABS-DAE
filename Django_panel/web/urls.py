from django.urls import path

from . import views

app_name = 'web'

urlpatterns = [
    path('', views.AlumnoView.as_view(),name='index'),
    path('eliminar-alumno/<int:pk>/', views.AlumnoeEliminarView.as_view(), name='eliminar_alumno'),

    path('profesor/', views.ProfesorView.as_view(), name='Profesores'),
    path('eliminar-profesor/<int:pk>/', views.ProfesorEliminarView.as_view(), name='eliminar_profesor'),
]