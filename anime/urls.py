from django.urls import path, include
from .views import AnimeSearchView, AnimeRecommendationView


urlpatterns = [
    path('search/', AnimeSearchView.as_view()),
    path('recommendations/', AnimeRecommendationView.as_view())
    
]