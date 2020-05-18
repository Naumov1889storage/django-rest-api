from rest_framework import serializers
from base.models import Post
from django import forms


class PostSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='owner.username')

    class Meta:
        model = Post
        fields = (
            'title',
            'description',
            'username'
        )
