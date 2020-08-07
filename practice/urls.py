from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('ques/<str:ques_id>', views.ques, name="ques"),
    path('addques/', views.addques, name="addques"),
    path('submit/<int:ques_id>', views.submit, name="submit"),
    path('submission/<int:sub_id>', views.submission, name="submission")
]