from django.db import models
from django.utils import timezone

class ProjectTeam(models.Model):
    """
      Class representing Project teams
    """
    name = models.CharField('Project Name', max_length=20)
    created_at = models.DateTimeField('datetime', default=timezone.now)

    def __str__(self):
        return self.name

class Department(models.Model):
    name = models.CharField('Department', max_length=20)
    created_at = models.DateField('Datetime', default=timezone.now)

    def __str__(self):
        return self.name

class ProjectMember(models.Model):
    first_name = models.CharField('First', max_length=20)
    last_name = models.CharField('Last', max_length=20)
    email = models.EmailField('Email', blank=True)
    project = models.ForeignKey(
        ProjectTeam, verbose_name='ProjectName', on_delete=models.PROTECT,
    )
    department = models.ManyToManyField(
        Department, verbose_name='Department',
    )
    create_at = models.DateTimeField('Day', default=timezone.now)

    def __str__(self):
        return '{0}{1} [{2}]'.format(self.last_name, self.first_name, self.project)


