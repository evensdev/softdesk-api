from django.contrib import admin
from .models import User, Project, Contributor, Issue, Comment


class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'age', 'can_be_contacted', 'can_data_be_shared']


class ProjectAdmin(admin.ModelAdmin):
    list_display = ['name']


class ContributorAdmin(admin.ModelAdmin):
    list_display = ['user', 'project']


class IssueAdmin(admin.ModelAdmin):
    list_display = ['project', 'status', 'priority', 'tag', 'assignee']


class CommentAdmin(admin.ModelAdmin):
    list_display = ['issue', 'author', 'content']


admin.site.register(User, UserAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Contributor, ContributorAdmin)
admin.site.register(Issue, IssueAdmin)
admin.site.register(Comment, CommentAdmin)
