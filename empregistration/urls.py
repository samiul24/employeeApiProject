from django.urls import path
from .views import Districts, District, EmpDepartment

urlpatterns = [
    path('districts/', Districts.as_view()),
    path('district/<int:pk>/', District.as_view()),
    path('departments/', EmpDepartment.as_view()),
]