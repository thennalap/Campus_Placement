from django.urls import path
from Student import views
urlpatterns=[
    path('register',views.addstudent,name='register'),
    path('login',views.studentlogin,name='login'),
    path('profilecreation/<int:studentid>',views.studentprofile,name='profilecreation'),
    path('uploadfile/<int:studentid>',views.update_file,name='uploadfile'),
    path('details/<int:studentid>',views.studentdetails,name='details')
]