from django.conf.urls import url
from django.urls import include, path
from . import views

app_name = 'shop'
urlpatterns = [
    path('', views.index, name='index'),
    path('category/<int:pk>/', views.category_detail, name='category_detail'),

]
