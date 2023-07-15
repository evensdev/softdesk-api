from rest_framework import serializers
from .models import User, Contributor, Project, Issue, Comment


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'age', 'consent']


class ContributorSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Contributor
        fields = ['id', 'user', 'projects']


class ProjectSerializer(serializers.ModelSerializer):
    contributors = ContributorSerializer(many=True)

    class Meta:
        model = Project
        fields = ['id', 'title', 'description', 'contributors']


class IssueSerializer(serializers.ModelSerializer):
    project = ProjectSerializer()
    assignee = UserSerializer()
    tag = serializers.CharField(source='get_tag_display')

    class Meta:
        model = Issue
        fields = ['id', 'title', 'description', 'tag', 'priority', 'status', 'project', 'assignee']


class CommentSerializer(serializers.ModelSerializer):
    issue = IssueSerializer()
    author = UserSerializer()

    class Meta:
        model = Comment
        fields = ['id', 'description', 'issue', 'author']
