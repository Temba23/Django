from django.urls import path
from .views import home
from .views import name_func, template, inside_template, students, about



urlpatterns = [
    path('template/', template, name='template'),
path('inside-template/', inside_template, name='inside_template'),
    # path("<str:name>/", name_func),
    path('students/', students, name='students'),
    path('about/', about, name='about'),

    path("", home)
]
# url ma - use garney _ use nagarney
# url ma username kitw id lekherw tannu parcha main id siddhai expose garnu hundaina.


