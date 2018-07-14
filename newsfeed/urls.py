from django.urls import path
from .views import NewsfeedDeleteView, NewsfeedDetailView, NewsfeedCreateView, NewsfeedUpdateView

urlpatterns = [
    path('<int:pk>/<slug:slug>/', NewsfeedDetailView.as_view(), name="newsfeed"),
    path('create/', NewsfeedCreateView.as_view(), name="create"),
    path('update/<int:pk>/', NewsfeedUpdateView.as_view(), name="update"),
    path('delete/<int:pk>/', NewsfeedDeleteView.as_view(), name="delete")
]