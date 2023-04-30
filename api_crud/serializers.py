
from django.contrib.auth.models import User
from rest_framework import serializers
from .models import ClassRoom, Person, PersonProfile

class DynamicFieldsModelSerializer(serializers.ModelSerializer):
    """
    A ModelSerializer that takes an additional `fields` argument that
    controls which fields should be displayed.
    """

    def __init__(self, *args, **kwargs):
        # Don't pass the 'fields' arg up to the superclass
        fields = kwargs.pop('fields', None)

        # Instantiate the superclass normally
        super().__init__(*args, **kwargs)

        if fields is not None:
            # Drop any fields that are not specified in the `fields` argument.
            allowed = set(fields)
            existing = set(self.fields)
            for field_name in existing - allowed:
                self.fields.pop(field_name)

class ClassRoomSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = ClassRoom
        fields = ['uuid', 'created_at', 'update_at', 'name']


class PersonSerializer(DynamicFieldsModelSerializer):
    classroom = serializers.SlugRelatedField(slug_field='uuid', queryset=ClassRoom.objects.all())
    profile = serializers.SerializerMethodField()
    class Meta:
        model = Person
        read_only_fields = ['uuid', 'update_at', 'created_at']
        fields = read_only_fields + ['name', 'age', 'email', 'classroom', 'is_active', 'profile']

    def get_fields(self):
        fields = super().get_fields()
        request = self.context.get('request')
        if request and request.method.lower() == "get":
            fields["classroom"] = ClassRoomSerializer()
        return fields
    def get_profile(self, person_obj):
        try:
            profile = person_obj.person_profile
        except:
            return None
        serializer = PersonProfileSerializer(profile)
        return serializer.data

class PersonProfileSerializer(DynamicFieldsModelSerializer):
    person = serializers.SlugRelatedField(slug_field='uuid', queryset=Person.objects.all())
    class Meta:
        model = PersonProfile
        fields = ["uuid", "created_at", "update_at", "person", "profile_picture", "address"]

    def get_fields(self):
        fields = super().get_fields()
        request = self.context.get('request')
        if request and request.method.lower() == 'get':
            fields['person'] = PersonSerializer()
        return fields


class UserSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = User
        fields = ["username", "email", "is_superuser", "is_staff"]