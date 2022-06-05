from rest_framework import serializers
from api.models import Note


class NotesListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = '__all__'
