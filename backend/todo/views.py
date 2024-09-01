from django.shortcuts import render
from .models import Todo, EmailQueue
from .serializers import TodoSerializer, EmailQueueSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

class TodoViewSet(viewsets.ModelViewSet):
    serializer_class = TodoSerializer
    queryset = Todo.objects.all()

    def create(self, request, *args, **kwargs):
        print(request.data)
        try:
            response = super().create(request, *args, **kwargs)
            return response
        except Exception as e:
            return Response(str(e), status=404, template_name=None, content_type=None)

