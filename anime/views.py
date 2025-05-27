from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.pagination import LimitOffsetPagination
from rest_framework_simplejwt.authentication import JWTAuthentication


from .graphql_client import search_anime_by_name_or_genre
from .models import Anime, Rating
from .utils import save_anime_list_to_db_task

from users.models import CustomUser as User, UserPreferences

import csv
import io
import requests
from dateutil.parser import parse



class AnimeSearchView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        name = request.query_params.get('name')
        genre = request.query_params.get('genre')

        try:
            anime_list = search_anime_by_name_or_genre(name=name, genre=genre)
            
            save_anime_list_to_db_task.delay(anime_list)          # Saving fetched data using celery in Anime model
            
            return Response(anime_list)
        except requests.exceptions.RequestException as e:
            return Response({"error": str(e)}, status=500)




class AnimeRecommendationView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            prefs, _ = UserPreferences.objects.get_or_create(user=request.user)
        except Exception as e:
            return Response({"error": f"Failed to retrieve user preferences: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        genres = prefs.favorite_genres or []
        watched_ids = prefs.watched_anime_ids or []

        if not genres:
            return Response({"message": "No favorite genres set in user preferences."}, status=status.HTTP_400_BAD_REQUEST)

        queryset = Anime.objects.filter(
            genre__iregex='|'.join(genres)
        ).exclude(id__in=watched_ids).order_by('-rating')

        paginator = LimitOffsetPagination()
        paginated_queryset = paginator.paginate_queryset(queryset, request)

        data = [{
            "id": anime.id,
            "name": anime.name,
            "genre": anime.genre,
            "type": anime.type,
            "episodes": anime.episodes,
            "rating": anime.rating,
            "members": anime.members
        } for anime in paginated_queryset]

        return paginator.get_paginated_response(data)
