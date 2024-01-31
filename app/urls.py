from django.urls import path
from . import views


urlpatterns = [
     path('', views.home, name="home"),
     path('completed/<int:item>', views.completed, name="completed"),
     path('create', views.create, name="create"),
     path('delete_item/<int:item>', views.delete_item, name="delete_item"),
     path('update_item/<int:item>', views.update_item, name="update_item"),
     
]
