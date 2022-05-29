from django.urls import path

from blog import views

urlpatterns = [
    path('',views.allblog,name='allblog'),
    path('<int:blog_id>/',views.detail,name='blog_detai_using_id')
]
