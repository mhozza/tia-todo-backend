from rest_framework import viewsets

from .models import ToDo
from .serializers import ToDoSerializer


class ToDoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer
