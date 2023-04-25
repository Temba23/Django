from rest_framework import serializers
from .models import ClassRoom, Person, PersonProfile

class ClassRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassRoom
        fields = ['uuid', 'created_at', 'update_at', 'name']


class PersonSerializer(serializers.ModelSerializer):
    classroom = serializers.SlugRelatedField(slug_field='uuid', queryset=ClassRoom.objects.all())
    class Meta:
        model = Person
        read_only_fields = ['uuid', 'update_at', 'created_at']
        fields = read_only_fields + ['name', 'age', 'email', 'classroom', 'is_active']

    def get_fields(self):
        fields = super().get_fields()
        request = self.context.get('request')
        if request and request.method.lower() == "get":
            fields["classroom"] = ClassRoomSerializer()
            return fields


class PersonProfileSerializer(serializers.ModelSerializer):
    person = serializers.SlugRelatedField(slug_field='uuid', queryset=Person.objects.all())
    class Meta:
        model = PersonProfile
        fields = ["uuid", "created_at", "update_at", "person", "profile_picture", "address"]