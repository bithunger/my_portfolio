from django.contrib import admin
from .models import Home, About, Project, ProjectDetails, Education, Skill, SkillAttribute, Settings, Service, Contact

class HomeAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'image', 'cv')
admin.site.register(Home, HomeAdmin)

class AbutAdmin(admin.ModelAdmin):
    list_display = ('about_des', 'sub_des')
admin.site.register(About, AbutAdmin)

class ServiceAdmin(admin.ModelAdmin):
    list_display = ('icon', 'service_title', 'service_des')
admin.site.register(Service, ServiceAdmin)

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('project_des',)
admin.site.register(Project, ProjectAdmin)

class ProjectAttributeAdmin(admin.ModelAdmin):
    list_display = ('project_title', 'image', 'link')
admin.site.register(ProjectDetails, ProjectAttributeAdmin)

class EducationAdmin(admin.ModelAdmin):
    list_display = ('level_name', 'session', 'institute_name', 'result')
admin.site.register(Education, EducationAdmin)

class SkillAdmin(admin.ModelAdmin):
    list_display = ('skill_des',)
admin.site.register(Skill, SkillAdmin)

class  SkillAttributeAdmin(admin.ModelAdmin):
    list_display = ('skill_name', 'percent')
admin.site.register(SkillAttribute, SkillAttributeAdmin)

class  SettingsAdmin(admin.ModelAdmin):
    list_display = ('logo_name', 'img', 'email', 'phone', 'whatsapp', 'address', 'facebook', 'linkedin', 'github')
admin.site.register(Settings, SettingsAdmin)

class  ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'message')
admin.site.register(Contact, ContactAdmin)

# Register your models here.
