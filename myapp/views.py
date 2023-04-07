from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseNotFound
from django.template import loader
from .models import Student, Experience


def home(request):

    context = {
        "experiences": Experience.objects.all()
    }

    return render(request, template_name="index.html", context=context)


    # return render(request, template_name="index.html")


def name_func(request, name):
    data = {
        "ram": "ram bahadur",
        "hari": "hari krishna"
    }
    name = data.get(name)
    if not name:
        return HttpResponseNotFound("INVALID URL")
    return HttpResponse(f"<h1>Hello i am {name}.</h1>", )


def template(request):
    context = {"name": "jon snow", "age": 25,
               "hobbies": ["singing", "sports", "movies"]}  # context should always be a dictionary.
    # template = loader.get_template("myapp/home.html")
    #
    # template_data = template.render(context, request)
    # return HttpResponse(template_data)
    return render(request, template_name="myapp/home.html", context=context)


def inside_template(request):
    return render(request, template_name="inside_home.html")


def about(request):
    return render(request, template_name="about.html, context=context")


def students(request):
    student = Student.objects.get(id=3)
    # context = {"name": student.name, "age": student.age, "department": student.department}
    context = {
        "infos": Student.objects.all()
    }

    return render(request, "students.html", context)




    # if name.lower() == 'ram':
    #     return HttpResponse(f"<h1>Hello i am {name} krishna.</h1>", )
    # elif name.lower() == 'hari':
    #     return HttpResponse(f"<h1>Hello i am {name} bahadur.</h1>")
    # else:
    #     return HttpResponse(f"<h1>Hello i am {name}.</h1>", )

# django-admin startproject python_project
# python manage.py startapp <appname>
# python manage.py runserver
