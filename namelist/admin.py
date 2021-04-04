from django.contrib import admin
from .models import ProjectTeam, ProjectMember, Department

admin.site.register(ProjectTeam)
admin.site.register(ProjectMember)
admin.site.register(Department)