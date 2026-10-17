from django.contrib import admin
from django.urls import path
from one import views

urlpatterns = [
    path('admin/', admin.site.urls),

    # Authentication
    path('', views.login_user, name='login_user'),
    path('register/', views.register_user, name='register_user'),
    path('logout/', views.logout_user, name='logout_user'),

    # Task management
    path('home/', views.home_addtask, name='home_addtask'),
    path('viewtask/', views.home_viewtask, name='home_viewtask'),
    path('delete/<int:task_id>/', views.home_deletetask, name='home_deletetask'),
    path('edit/<int:task_id>/', views.edit_task, name='edit_task'),
]

