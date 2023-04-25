from rest_framework.generics import ListAPIView
from .viewsets import ListCreateUpdateDestroyViewSet, CreateUpdateDestroyViewSet

from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import ClassRoom, Person, PersonProfile
from .serializers import ClassRoomSerializer, PersonSerializer, PersonProfileSerializer
"""

Get, Post, Put, Patch, Delete => These are HTTP Methods
List, Retrieve, Create, Update, Partial Update, Destroy => Actions (Django Specific)

slug == uniquely defined
"""

class ClassRoomViewSet(ListCreateUpdateDestroyViewSet):
    lookup_field = "uuid"
    lookup_url_kwarg = "uuid"
    serializer_class = ClassRoomSerializer
    queryset = ClassRoom.objects.all()


    def get_serializer_class(self):
        if self.action == 'person':
            return PersonSerializer
        return ClassRoomSerializer

    @action(detail=True)
    def people(self, *args, **kwargs):
        classroom_obj = self.get_object()
        person = Person.objects.filter(classroom=classroom_obj)
        serializer = self.get_serializer(person, many=True)
        return Response(serializer.data)

class PersonViewSet(ModelViewSet):
    lookup_field = "uuid"
    lookup_url_kwarg = "uuid"
    serializer_class = PersonSerializer
    queryset = Person.objects.all()


class ClassRoomPersonView(ListAPIView):
    serializer_class = PersonSerializer


    def get_queryset(self):
        classroom_uuid = self.kwargs['uuid']
        return Person.objects.filter(classroom__uuid=classroom_uuid)


class PersonProfileViewSet(CreateUpdateDestroyViewSet):
    serializer_class = PersonProfileSerializer
    lookup_field = "uuid"
    lookup_url_kwarg = "uuid"
    queryset = PersonProfile.objects.all()


