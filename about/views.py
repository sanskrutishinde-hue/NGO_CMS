from django.shortcuts import render
from .models import OurStory, CoreValue, Program, TeamMember


def about_us(request):
    story = OurStory.objects.first()
    core_values = CoreValue.objects.all()
    programs = Program.objects.all()
    team_members = TeamMember.objects.all()

    context = {
        'story': story,
        'core_values': core_values,
        'programs': programs,
        'team_members': team_members,
    }

    return render(request, 'about/about.html', context)