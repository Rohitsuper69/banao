from django.urls import path
from blog import views

urlpatterns = [
    path('', views.dashboard_view, name='dashboard'),
    path('create_blog/',views.create_blog, name='create_blog'),
    path('view_blog/',views.view_blog, name='view_blog'),
    path('viewmy_blog/',views.viewmy_blog, name='viewmy_blog'),

]
