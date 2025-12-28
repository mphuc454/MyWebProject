from django.urls import path

from webapp import views

urlpatterns = [
    path('home', views.home, name='home'),
    path('home/<int:id>', views.detail, name='detail')
]