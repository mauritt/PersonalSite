from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Project, Project_type, Host, Tag, Tag_Category


def portfolio(request, project_type):
    context = {}
    proj_type_id = get_object_or_404(Project_type, name__iexact = project_type)
    examples = Project.objects.all().filter(project_type = proj_type_id.id).order_by('priority')

    context['featured'] = examples[0]
    context['examples'] = examples
    context['project_type'] = project_type


    return render(request, 'portfolio/Portfolio.html', context)


def tag(request, project_type,project_tag,view):
    proj_type_id = get_object_or_404(Project_type, name__iexact = project_type)
    tag_id = get_object_or_404(Tag, name__iexact = project_tag)
    examples = Project.objects.all().filter(project_type = proj_type_id.id, tags=tag_id)
    context = {'project_type':project_type,'examples':examples}


    if view.lower() == 'tile':
        return render(request, 'portfolio/tiledPortfolio.html', context)

    if view.lower() == 'list':
        return render(request, 'portfolio/listPortfolio.html', context)




def detail(request, project_id):
    project = get_object_or_404(Project, id = project_id)
    context = {}
    context['project'] = project
    context['tag_categories'] = []
    context['tags'] = project.tags.all()
    for tag in project.tags.all():
        if tag.category not in context['tag_categories']:
            context['tag_categories'].append(tag.category)

    return render(request, 'portfolio/projectDetail.html', context)
