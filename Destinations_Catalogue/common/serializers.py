from rest_framework import serializers
from .models import Comment
from ..destinations.models import Destination


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['content']



