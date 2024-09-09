from django.urls import path
from .views import Home, Add_Employee, Delete_Employee, Update_Employee
from . import views

urlpatterns = [
    path("", Home.as_view(), name="home"),
    path('add-employee/', Add_Employee.as_view(), name="add-employee"),
    path('delete-employee/', Delete_Employee.as_view(), name="delete-employee"),
    path('update-employee/<int:id>/', Update_Employee.as_view(), name='update-employee'),
]

