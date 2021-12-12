from django.urls import path
from app import views
urlpatterns = [
    path('',views.onetoone, name = "onetoone"),
    path("manytoone/",views.manytoone,name="manytoone"),
    path("manytomany/",views.manytomany,name= "manytomany")
]
