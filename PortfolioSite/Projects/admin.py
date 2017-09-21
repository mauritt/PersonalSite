from django.contrib import admin
from .models import Project, Host, Project_type

admin.site.register(Project)
admin.site.register(Host)
admin.site.register(Project_type)
