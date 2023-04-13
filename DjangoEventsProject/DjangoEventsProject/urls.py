"""
URL configuration for DjangoEventsProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path,include
from django.conf import settings
from Accounts.views import *
from Events.views import *
from rest_framework.routers import DefaultRouter
from django.views.decorators.csrf import csrf_exempt

router = DefaultRouter()
router.register('eventss', EventViewSet, basename='Events')
router.register('searchevents', SearchEventsViewSet, basename='Events')

urlpatterns = [
    path('admin/', admin.site.urls),
     path('',include(router.urls)),
    path('login_usertoken/',login_user_token,name='loginusertoken'),
    path('logout_usertoken/',logout_users,name='loginusertoken'),
    path('register/',RegisteredView.as_view(),name='product-list'),
    path('change_pass/',ChangePasswordView.as_view(),name='changepass'),
    path('Events_Join/',Events_JoinView.as_view(),name='Events_Joins'),
    path('event/left/<int:pk>',Leftevent.as_view(),name='left-event'),
    path('Events_Joins/',EventslistJoinView.as_view(),name='Events_Joins'),
    path('api/password_reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),
  
]
