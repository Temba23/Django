from django.urls import path
from .views import home, create, update, delete, file_test, classroom, add_classroom, person_detail


urlpatterns = [

    path("create/", create, name='create'),
    path("classroom/", classroom, name='classroom'),
    path("add-classroom/", add_classroom, name='add_classroom'),
    path("file-test/", file_test, name="file_test"),
    path("update/<int:id>/", update, name="update"),
    path("delete/<int:id>/", delete, name="delete"),
    path("person/<int:id>/", person_detail, name="person_detail"),

    path("", home, name='home')

]