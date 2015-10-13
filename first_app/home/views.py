from django.shortcuts import render
from .forms import StudentForm
from .forms import FeedbackForm
from .models import Student
from django.core.mail import send_mail

# from django.http import HttpResponse

# Create your views here.


def index(request):
    #for a dynamic homepage add the 'context' variable
    # form = StudentForm()
    # print (request.POST) #prints ut on the terminal(server) what has been POSTed

    #changing /saving POSTed information to another page
    form = StudentForm(request.POST or None)

    # BEFORE form is vali - this context is what wil be seen on screen
    context = {
        "hello_message" : "Register new student",
        "form": form
    }

    # AFTER form is valid - this context is what wil be seen on screen
    if form.is_valid():
        #form.save()
        #overiding the 'save' command

        instance = form.save(commit=False)
        full_name = form.cleaned_data.get('full_name')
        if full_name == "Jacob":
            full_name = "Developer"
        instance.full_name = full_name
        instance.save()

        context = {
            "hello_message": "Student Saved!"
            }


    return render(request, 'index.html', context) #substitute {} with 'context'
#    return HttpResponse("Success")


def feedback(request):
    form = FeedbackForm(request.POST or None)
    if form.is_valid():
        # for key, value in form.cleaned_data.items():
        #     print(key, value)

        #to send email if form is valid
        from_email = form.cleaned_data.get('email')
        full_name = form.cleaned_data.get('full_name')
        message = form.cleaned_data.get('message')
        prepared_message = "You have feedback from {} saying'{}'".format(full_name, message)
        send_mail('New Feedback Given', prepared_message, from_email,
    ['i.wanjugu@yahoo.com'], fail_silently=False)
    context= {
        "form": form
    }
    return render(request, 'feedback.html', context)


def students(request):
    students = Student.objects.all # All the objects
    context = {'students':students}
    return render(request, 'students.html', context)