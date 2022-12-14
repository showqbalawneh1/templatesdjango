
from django.urls import path,include
from dinosaur import views

urlpatterns = [
    path('',views.show)
]
