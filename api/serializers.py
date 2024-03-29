

from rest_framework import serializers
from crud.models import Person, PersonProfile, ClassRoom


class PersonSerializer(serializers.Serializer):
    name = serializers.CharField()
    email = serializers.EmailField()
    age = serializers.IntegerField()
    department = serializers.CharField()


class PersonModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ["id", "name", "age", "email", "department"]


class ClassRoomModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassRoom
        fields = ["id", "name"]



class PersonProfileSerializer(serializers.ModelSerializer):
    # classroom = ClassRoomModelSerializer()
    # person = PersonSerializer()
    class Meta:
        model = PersonProfile
        fields = ["id", "profile_picture", "bio", "address", "classroom", "person"]

    def get_fields(self):
        fields = super().get_fields()
        request = self.context.get('request')
        if request and request.method.lower() == "get":
            fields["person"] = PersonSerializer()
        return fields




