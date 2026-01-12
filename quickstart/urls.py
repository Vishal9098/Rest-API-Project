from django.contrib import admin
from django.urls import path
from app.views import employeelist, userlist, employeeDetailView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/employe/', employeelist),
    path('api/employe/<int:pk>/', employeeDetailView),
    path('api/users/', userlist),
]
