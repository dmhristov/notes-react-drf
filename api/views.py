from django.shortcuts import render
from django.views.generic import TemplateView
from rest_framework import generics
from api.models import Note
from api.serializers import NotesListSerializer


class NotesListApiView(generics.ListAPIView):
    queryset = Note.objects.all().order_by('-updated')
    serializer_class = NotesListSerializer


class NoteReadUpdateDeleteApiView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = NotesListSerializer

    def get_queryset(self):
        return Note.objects.filter(pk=self.kwargs['pk'])

class NoteCreateApiView(generics.CreateAPIView):
    serializer_class = NotesListSerializer
