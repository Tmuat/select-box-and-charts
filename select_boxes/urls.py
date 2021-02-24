from django.urls import path

from select_boxes import views

urlpatterns = [
    path('', views.select, name='selects'),
]
