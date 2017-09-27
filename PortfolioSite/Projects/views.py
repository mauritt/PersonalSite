from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Project, Project_type, Host


def portfolio(request, project_type, view):
    proj_type_id = get_object_or_404(Project_type, name__iexact = project_type)
    examples = Project.objects.all().filter(project_type = proj_type_id.id)
    context = {'project_type':project_type,'examples':examples}

    if view.lower() == 'tile':
        return render(request, 'portfolio/tiledPortfolio.html', context)

    if view.lower() == 'list':
        return render(request, 'portfolio/listPortfolio.html', context)

def detail(request, project_id):
    project = get_object_or_404(Project, id = project_id)
    context = {'project': project}


    return render(request, 'portfolio/projectDetail.html', context)
