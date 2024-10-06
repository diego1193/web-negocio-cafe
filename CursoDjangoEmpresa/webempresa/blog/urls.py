from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog, name="blog"),
    path('category/<int:category_id>/', views.category, name="category") # pasa a entero la id de la entrada y lo convierte a entero ya q por defecto es str
]