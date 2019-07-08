from django.shortcuts import render
from skills.models import Skill

def skill_index(request):
    skills = Skill.objects.all()
    context = {'skills': skills}
    return render(request, 'skill_index.html', context)

