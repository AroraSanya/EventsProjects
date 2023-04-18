from rest_framework import serializers, status
from Accounts.models import *
from Events.models import *
from django.http import HttpResponse
from django.shortcuts import render,redirect
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated 
from rest_framework.decorators import api_view,permission_classes
from django.contrib.auth import authenticate,login as auth,logout
from rest_framework.views import APIView
from rest_framework import generics
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from django.urls import reverse
from django_rest_passwordreset.signals import reset_password_token_created
from django.core.mail import send_mail 
from .serializers import *
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.db.models import signals
from Events.serializers import *
from rest_framework.generics import RetrieveAPIView,ListAPIView
from .signals import *


class ProfileView(ListAPIView):
    #queryset = User.objects.all()
    serializer_class = JoineventsSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        events = Join_events.objects.filter(user=user)
        return events
    

    def list(self, request, *args, **kwargs):
        user = self.request.user
        users =self.get_queryset()
        events_serializer = self.get_serializer(users, many=True)
        for u in users:
            empty_event =[]
            empty_event.append(u.event.title)
        joining = empty_event
        return Response({'id':user.id,'email':user.email,'event':joining})


class RegisteredView(APIView):
    queryset=User.objects.all()
    serializer_class=UserSerializer


    def post(self, request):
        serializer = ProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.create(validated_data=request.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,
                        status=status.HTTP_400_BAD_REQUEST)

    
       
    
@api_view(http_method_names=('post',))
def login_user_token(request):
    username=request.data['username']
    password=request.data['password']
    print(username)
    user=authenticate(username=username,password=password)
    print(user) 
    auth(request,user)
    user= User.objects.get(username=username)
    token=Token.objects.create(user=user)
    return Response({'token':token.key},status=status.HTTP_200_OK)

@api_view()
@permission_classes([IsAuthenticated])
def logout_users(request):
    try:
        token=Token.objects.get(user_id=request.user.id)
        token.delete()
        logout(request)
    except:
        return Response({'message':"NOT_LOGGED_OUT"})
    return Response({'user':"LOGGED_OUT"}) 


    

class ChangePasswordView(APIView):
    permission_classes = [IsAuthenticated]
    

    def post(self, request): 
            serializer = ChangePasswordSerializer(data=request.data, context = {'user':request.user})
            
            if serializer.is_valid():
                return Response({"msg":"changed succesfully"})
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)



    


    

       
