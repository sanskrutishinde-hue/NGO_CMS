from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

from .models import Banner, VisionMission, Statistic, Initiative


def home(request):
    banners = Banner.objects.filter(status=True)
    vision_mission = VisionMission.objects.first()
    statistics = Statistic.objects.filter(status=True)
    initiatives = Initiative.objects.filter(status=True)

    context = {
        'banners': banners,
        'vision_mission': vision_mission,
        'statistics': statistics,
        'initiatives': initiatives,
    }

    return render(request, 'home.html', context)


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()

    return render(request, 'register.html', {'form': form})


@login_required
def dashboard(request):
    return render(request, 'dashboard.html')