from django.urls import path
from api.views import NotesListApiView, NoteReadUpdateDeleteApiView, NoteCreateApiView


urlpatterns = [
    path('notes/', NotesListApiView.as_view(), name='notes list'),
    path('notes/<int:pk>/', NoteReadUpdateDeleteApiView.as_view(), name='note rud'),
    path('notes/create/', NoteCreateApiView.as_view(), name='create note'),
]
