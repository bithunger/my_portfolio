from django.shortcuts import render
from .models import Home, About, Service, Project, ProjectDetails, Education, Skill, SkillAttribute, Settings, Contact
from django.conf import settings
from django.core.mail import send_mail


def home(request):
    data = Home.objects.all().first()
    return render(request, 'home.html', {'data':data})

def about(request):
    data = About.objects.all().first()
    services = Service.objects.all()
    return render(request, 'about.html', {'data':data, 'services':services})

def education(request):
    data = Education.objects.all()
    return render(request, 'education.html', {'data':data})

def projects(request):
    des = Project.objects.all().first()
    projects = ProjectDetails.objects.all()
    
    return render(request, 'project.html', {'des':des, 'projects': projects})

def skills(request):
    des = Skill.objects.all().first()
    skills = SkillAttribute.objects.all()
    return render(request, 'skills.html', {'des':des, 'skills': skills})

def contact(request):
    data = Settings.objects.all().first()
    
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        content = request.POST['message']
        
        if name != '':
            Contact.objects.create(
                name = name,
                email = email,
                message = content
            )
        
            subject = 'Contact to me'
            message = f'Name: {name}\nEmail: {email}\n\n\nMessage:- {content}'
            email_from = settings.EMAIL_HOST_USER
            recipient_list = ['nurhosainlikhon@gmail.com', ]
            send_mail( subject, message, email_from, recipient_list, fail_silently=True)
    
    return render(request, 'contact.html', {'data':data})
# Create your views here.
