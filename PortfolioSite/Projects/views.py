from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Project, Project_type, Host


def portfolio(request, project_type):
    proj_type_id = get_object_or_404(Project_type, name__iexact = project_type)
    examples = Project.objects.all().filter(project_type = proj_type_id.id)
    context = {'project_type':project_type,'examples':examples}

    if project_type.lower() == 'video':
        return HttpResponse("this works")
