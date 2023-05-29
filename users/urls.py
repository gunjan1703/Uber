from django.urls import path,include
from .views import *
from users.views import *

urlpatterns =[
    path('get-all-students', GetStudentView.as_view()),
    path('get-and-save-orders',GetOrdersView.as_view()),
    path('delete-student/int:pk>',DeleteStudentView.as_view())

  
]

