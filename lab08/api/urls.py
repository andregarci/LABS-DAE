
from django.urls import path,include

#Se esta importando el router para la class ProductoViewSet(viewsets.ModelViewSet):
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()

router.register(r'producto',views.ProductoViewSet,basename='producto')

urlpatterns = [
    path('', views.IndexView.as_view()),
    path('categoria',views.CategriaView.as_view()),
    path('categoria/<int:categoria_id>',views.CategoriaDetailView.as_view()),
    path('admin/',include(router.urls))
]
