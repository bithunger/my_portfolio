from django.shortcuts import render
from .models import Home, About, Service, Project, ProjectDetails, Education, Skill, SkillAttribute, Settings

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
    return render(request, 'contact.html', {'data':data})
# Create your views here.
