"""
URL configuration for conproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
from conapp  import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.ContactView.as_view(),name="home_view"),
    path('create',views.Addcontact.as_view(),name="con_create"),
    path('viewcontact',views.ListContact.as_view(),name="con_view"),
    path('condetail/<int:id>',views.ContactDetailView.as_view(),name="con_detail"),
    path('condelete/<int:id>',views.ContactDeleteView.as_view(),name="con_delete"),
    path('conupdate/<int:id>',views.ContactUpdateView.as_view(),name="con_update"),



  


]
