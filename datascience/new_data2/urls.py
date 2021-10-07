from django.urls import path
from new_data2 import views

urlpatterns = [
    path('',views.home2),
    path('index/',views.index)
]

