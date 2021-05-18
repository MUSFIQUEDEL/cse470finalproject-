"""librarymanagement URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import include
from django.urls import path
from library import views
from django.contrib.auth.views import LoginView,LogoutView



urlpatterns = [ 
    path('admin/', admin.site.urls),
    path('accounts/',include('django.contrib.auth.urls') ),
    path('', views.home_view,name='home_view'),

    path('adminclick', views.adminclick_view,name='admin_click'),
    path('studentclick', views.studentclick_view,name='student_click'),


    path('adminsignup', views.adminsignup_view,name='admin_signup'),
    path('studentsignup', views.studentsignup_view,name='student_signup'),

    path('adminlogin', LoginView.as_view(template_name='library/adminlogin.html'),name='adminlogin'),
    path('studentlogin', LoginView.as_view(template_name='library/studentlogin.html'),name='studentlogin'),

    path('logout', LogoutView.as_view(template_name='library/index.html'),name='logout_view'),
    path('afterlogin', views.afterlogin_view,name='afterlogin'),

    path('addbook', views.addbook_view,name='addbook'),
    path('viewbook', views.viewbook_view,name='viewbook'),
    path('issuebook', views.issuebook_view,name='issuebook'),
    path('viewissuedbook', views.viewissuedbook_view,name='issuedbook'),
    path('viewstudent', views.viewstudent_view,name='viewstudent'),
    path('viewissuedbookbystudent', views.viewissuedbookbystudent,name='issuedbystudent'),

    path('aboutus', views.aboutus_view,name='aboutus'),
    path('contactus', views.contactus_view,name='contactus'),

]
