from django.db import models
from django.utils.safestring import mark_safe

class Home(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    img = models.ImageField(upload_to='profile/')
    cv = models.CharField(max_length=150)
    
    def image(self):
        return mark_safe('<img src="/media/%s" width=50px; height: 50px />' % (self.img))


class About(models.Model):
    about_des = models.TextField()
    sub_des = models.TextField()
    
    
class Service(models.Model):
    icon = models.ImageField(upload_to='services/')
    service_title = models.CharField(max_length=100)
    service_des = models.TextField()
    

class Project(models.Model):
    project_des = models.TextField()
    
    
class ProjectDetails(models.Model):
    img = models.ImageField(upload_to='projects/')
    project_title = models.CharField(max_length=150)
    link = models.CharField(max_length=200)
    
    def image(self):
        return mark_safe('<img src="/media/%s" width=50px; height: 50px />' % (self.img))
    
    
class Education(models.Model):
    level_name = models.CharField(max_length=100)
    session = models.CharField(max_length=50)
    institute_name = models.CharField(max_length=200)
    result = models.CharField(max_length=50)
    

class Skill(models.Model):
    skill_des = models.TextField()
    
    
class SkillAttribute(models.Model):
    skill_name = models.CharField(max_length=100)
    percent = models.CharField(max_length=10)
    
    
class Settings(models.Model):
    icon = models.ImageField(upload_to='icon/')
    logo_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=150)
    phone = models.CharField(max_length=20)
    whatsapp = models.CharField(max_length=20)
    address = models.CharField(max_length=150)
    facebook = models.CharField(max_length=200)
    github = models.CharField(max_length=200)
    linkedin = models.CharField(max_length=200)
    
    def img(self):
        return mark_safe('<img src="/media/%s" width=50px; height: 50px />' % (self.icon))
    
# Create your models here.
