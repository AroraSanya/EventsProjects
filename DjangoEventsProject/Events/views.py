from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render,redirect
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import serializers, status
from Accounts.models import *
from Events.models import *
from rest_framework.serializers import ModelSerializer
from rest_framework.decorators import api_view,permission_classes
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
import django_filters
from rest_framework.serializers import ModelSerializer
from rest_framework import permissions
from rest_framework.views import APIView
from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics
from .serializers import *
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.db.models import signals
from django.core.mail import send_mail
from django.conf import settings
from django.http import JsonResponse
from .signals import *


class Events_JoinView(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class=JoineventsSerializer
   

    def create(self, request): 
             
            request.data['user'] = request.user.id     
            serializer = JoineventsSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.error_messages,
                            status=status.HTTP_400_BAD_REQUEST)
    

class Leftevent(APIView):
     def post(self, request,pk):
            print(pk)
            event=Join_events.objects.get(event_id=pk, user_id=request.user.id )
            event.is_registered=False
            event.save()
            return Response({"msg":"event_left Successfully"})

     
class EventViewSet(ModelViewSet):
        permission_classes = [permissions.IsAuthenticated,permissions.IsAdminUser]   
        serializer_class = EventSerializer
        queryset = Event.objects.all()
            
class EventFilterSet(django_filters.FilterSet):
    title= django_filters.CharFilter(lookup_expr='contains')

    class Meta:
        model = Event
        fields = ['title']

class SearchEventsViewSet(ModelViewSet):
    serializer_class =EventSerializer
    queryset = Event.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_class=EventFilterSet
        
class EventslistJoinView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Event.objects.all()
    serializer_class=EventSerializer


class ReportView(APIView):
     
     def post(self,request):
        events = Event.objects.prefetch_related('atendees').filter(start_datetime__range=[request.data["from"], request.data["to"]])
        serializer = ReportSerializer(events, many=True)
        return Response({'msg': serializer.data})
     

