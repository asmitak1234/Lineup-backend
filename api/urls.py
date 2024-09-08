# /* // # <!-- Made By - Asmita Kumari --> */


from django.urls import path
from . import views

urlpatterns = [
    path("notes/", views.NoteListCreate.as_view(), name="note-list"),
    # path("notes/delete/<int:pk>/", views.NoteDelete.as_view(), name="delete-note"),
    path('notes/<int:pk>/', views.NoteRetrieveUpdate.as_view(), name='note-retrieve-update'),
    path('notes/<int:pk>/delete/', views.NoteDelete.as_view(), name='note-delete'),
    path('user/', views.UserDetailView.as_view(), name='user-detail'), 
]