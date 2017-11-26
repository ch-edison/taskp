# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework import viewsets
from django.shortcuts import render
from .Serializers import TaskSerializer
from .models import Task
from rest_framework import permissions, renderers, viewsets
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.reverse import reverse
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.views import APIView
from django.shortcuts import redirect

# Create your views here.
#the default administrator of django rest_framework
class taskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
#methods to save and return the resolution
class ProfileDetail(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'task.html'

    def get(self, request):
        serializer = TaskSerializer()
        return Response({'serializer': serializer})

    def post(self, request):
        serializer = TaskSerializer(data=request.data)
        if not serializer.is_valid():
            return Response({'serializer': serializer})
        serializer.save()
        return Response({'serializer': serializer})
