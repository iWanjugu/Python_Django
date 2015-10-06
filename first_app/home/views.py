from django.shortcuts import render
from .forms import StudentForm
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


    return render(request, 'index.html' ,context) #substitute {} with 'context'
#    return HttpResponse("Success")