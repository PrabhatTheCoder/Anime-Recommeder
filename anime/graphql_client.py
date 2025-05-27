import requests

ANILIST_API_URL = "https://graphql.anilist.co"

def search_anime_by_name_or_genre(name=None, genre=None, per_page=10):
    query = '''
    query ($search: String, $genre: String, $perPage: Int) {
      Page(perPage: $perPage) {
        media(search: $search, genre: $genre, type: ANIME, sort: POPULARITY_DESC) {
          id
          title {
            romaji
            english
            native
          }
          genres
          episodes
          averageScore
          popularity
          coverImage {
            large
          }
          siteUrl
          format
        }
      }
    }
    '''
    variables = {
        "search": name,
        "genre": genre,
        "perPage": per_page,
    }

    response = requests.post(ANILIST_API_URL, json={"query": query, "variables": variables})
    response.raise_for_status()
    data = response.json()

    return data["data"]["Page"]["media"]

def get_recommendations_for_genres(genres, per_page=10):
    genre_filter = genres[0] if genres else None
    return search_anime_by_name_or_genre(genre=genre_filter, per_page=per_page)
