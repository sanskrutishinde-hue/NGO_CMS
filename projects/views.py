from django.shortcuts import render, get_object_or_404
from .models import Project


def project_list(request):
    status = request.GET.get('status')

    if status:
        projects = Project.objects.filter(status=status)
    else:
        projects = Project.objects.all()

    return render(request, 'projects/projects.html', {
        'projects': projects,
        'selected_status': status,
    })


def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)

    return render(request, 'projects/project_detail.html', {
        'project': project,
    })

