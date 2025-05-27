from celery import shared_task
from .models import Anime

@shared_task
def save_anime_list_to_db_task(anime_list):
    for anime_data in anime_list:
        genres = ", ".join(anime_data.get("genres", []))
        title_data = anime_data.get("title", {})
        name = title_data.get("romaji") or title_data.get("english") or title_data.get("native")

        anilist_id = anime_data.get("id")
        if not anilist_id:
            continue  # skip if no ID

        Anime.objects.update_or_create(
            anilist_id=anilist_id,
            defaults={
                "name": name,
                "genre": genres,
                "type": anime_data.get("format"),
                "episodes": anime_data.get("episodes"),
                "rating": anime_data.get("averageScore"),
                "members": anime_data.get("popularity"),
            }
        )

