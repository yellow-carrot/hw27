from django.urls import path

from ads.views import AdListView, AdDetailView, AdDeleteView, AdCreateView, AdUpdateView, AdImageView

urlpatterns = [
    path('', AdListView.as_view()),
    path('create/', AdCreateView.as_view()),
    path('<int:pk>/', AdDetailView.as_view()),
    path('<int:pk>/update/', AdUpdateView.as_view()),
    path('<int:pk>/delete/', AdDeleteView.as_view()),
    path('<int:pk>/upload_image/', AdImageView.as_view()),
]
