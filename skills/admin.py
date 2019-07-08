from django.contrib import admin
from skills.models import Skill

class SkillAdmin(admin.ModelAdmin):
    pass

admin.site.register(Skill, SkillAdmin)
