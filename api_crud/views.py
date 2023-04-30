from rest_framework.generics import ListAPIView
from django.contrib.auth.models import User
from .viewsets import ListCreateUpdateDestroyViewSet, CreateUpdateDestroyViewSet, ListUpdateDestroyViewSet

from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
# from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import SearchFilter
from rest_framework.permissions import AllowAny

from django_filters.rest_framework import DjangoFilterBackend

# from rest_framework.pagination import LimitOffsetPagination



from .models import ClassRoom, Person, PersonProfile
from .permissions import IsSuperAdminUser
from .serializers import ClassRoomSerializer, PersonSerializer, PersonProfileSerializer, UserSerializer
"""

Get, Post, Put, Patch, Delete => These are HTTP Methods
List, Retrieve, Create, Update, Partial Update, Destroy => Actions (Django Specific)

slug == uniquely defined
"""

class ClassRoomViewSet(ListCreateUpdateDestroyViewSet):

    lookup_field = "uuid"
    lookup_url_kwarg = "uuid"
    filter_backends = [SearchFilter, DjangoFilterBackend]
    search_fields = ["name", ]
    filterset_fields = ["name", ]
    # serializer_class = ClassRoomSerializer
    # pagination_class = LimitOffsetPagination
    queryset = ClassRoom.objects.all()


    def get_serializer_class(self):
        if self.action == 'person':
            return PersonSerializer
        return ClassRoomSerializer

    def get_permissions(self):
        if self.action == 'list':
            return [AllowAny(), ]
        elif self.action in ['create', 'destroy']:
            return [IsSuperAdminUser(), ]
        elif self.action in ['update', 'people', 'partial_update']:
            return [IsAuthenticated(), ]



    @action(detail=True)
    def people(self, *args, **kwargs):
        classroom_obj = self.get_object()
        person = Person.objects.filter(classroom=classroom_obj)
        page = self.paginate_queryset(person)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(person, many=True)
        return Response(serializer.data)

class PersonViewSet(ModelViewSet):
    # authentication_classes = [TokenAuthentication, ]
    # permission_classes = [IsAuthenticated, ]
    lookup_field = "uuid"
    lookup_url_kwarg = "uuid"
    serializer_class = PersonSerializer
    queryset = Person.objects.all()

    def get_serializer_class(self):
        if self.action == "profile":
            return PersonProfileSerializer
        return PersonSerializer
    @action(detail=True)
    def profile(self, *args, **kwargs):
        person = self.get_object()
        try:
            p_profile = person.person_profile # Here person_profile is a related name.
        except:
            return Response({
                "message": "Profile for this person doesn't exist."
            })
        serializer = self.get_serializer(p_profile, fields=['uuid', 'created_at', 'profile_picture', 'address'])
        return Response(serializer.data)

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



class UserPersonViewSet(ListUpdateDestroyViewSet):
    serializer_class = UserSerializer
    lookup_field = "username"
    lookup_url_kwarg = "username"
    filter_backends = [SearchFilter, ]
    search_fields = ["username", ]
    queryset = User.objects.all()
