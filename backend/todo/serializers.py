from rest_framework import routers, serializers, viewsets
from .models import Todo, EmailQueue

class TodoSerializer(serializers.Serializer):
    class Meta:
        model = Todo
        fields = "__all__"

class EmailQueueSerializer(serializers.Serializer):
    class Meta:
        model = EmailQueue
        fields = "__all__"