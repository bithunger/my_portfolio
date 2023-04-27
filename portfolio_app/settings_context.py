from .models import Settings

def settings(request):
    return {'settingsData':Settings.objects.all().first()}