import uuid

from django.db import models



# THis is an abstract class. Abstract class ley chai database ma chuttai table banudaina.
class TimeStampModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class UUIDModel(TimeStampModel):
    uuid = models.UUIDField(default=uuid.uuid4(), editable=False)

    class Meta:
        abstract = True

class ClassRoom(UUIDModel):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Person(UUIDModel):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    age = models.PositiveIntegerField()
    classroom = models.ForeignKey(ClassRoom, on_delete=models.CASCADE, related_name="classroom_people")
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class PersonProfile(UUIDModel):
    person = models.OneToOneField(Person, on_delete=models.CASCADE, related_name="person_profile")
    profile_picture = models.FileField(upload_to="api_crud", null=True, blank=True)
    address = models.CharField(max_length=50)