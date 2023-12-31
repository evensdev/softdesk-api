from django.db import models
from django.contrib.auth.models import User


class User(models.Model):
    username = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.PositiveIntegerField(null=True, blank=True)
    can_be_contacted = models.BooleanField(default=False)
    can_data_be_shared = models.BooleanField(default=False)


class Project(models.Model):
    name = models.CharField(max_length=200)
    contributors = models.ManyToManyField(User, through='Contributor')


class Contributor(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)


class Issue(models.Model):
    STATUS_CHOICES = [
        ('OPEN', 'Open'),
        ('CLOSED', 'Closed'),
    ]
    PRIORITY_CHOICES = [
        ('LOW', 'Low'),
        ('MEDIUM', 'Medium'),
        ('HIGH', 'High'),
    ]
    TAG_CHOICES = [
        ('BUG', 'Bug'),
        ('TASK', 'Task'),
        ('IMPROVEMENT', 'Improvement'),
    ]
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    status = models.CharField(max_length=6, choices=STATUS_CHOICES, default='OPEN')
    priority = models.CharField(max_length=6, choices=PRIORITY_CHOICES, default='LOW')
    tag = models.CharField(max_length=12, choices=TAG_CHOICES, default='TASK')
    assignee = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)


class Comment(models.Model):
    issue = models.ForeignKey(Issue, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
