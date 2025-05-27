# 🎌 Anime Recommender System

An intelligent, personalized anime recommendation backend built with Django, PostgreSQL, and Celery. It leverages the AniList GraphQL API to dynamically fetch anime data based on user input, and provides recommendations tailored to each user's preferences.

---

## 🚀 Features

- 🔐 **JWT Authentication** (Register/Login/Logout)
- 🔍 **Dynamic Anime Search** using AniList GraphQL API
- 💾 **Asynchronous Saving** of searched anime to PostgreSQL via Celery
- 🎯 **Personalized Recommendations** based on user preferences
- ❤️ **User Preferences API** (genres, watched anime, language, rating thresholds)
- 🌐 **Deployed on AWS Elastic Beanstalk** via Docker and CI/CD

---

## 🧱 Tech Stack

| Layer         | Technology                  |
|---------------|-----------------------------|
| Backend       | Django, Django REST Framework |
| Auth          | Simple JWT (Access/Refresh Tokens) |
| Database      | PostgreSQL                  |
| Async Tasks   | Celery + Redis              |
| External API  | AniList GraphQL             |
| Containerization | Docker                   |
| Deployment    | AWS Elastic Beanstalk       |
| CI/CD         | GitHub Actions              |

---

## 🛠️ Setup Instructions

### Clone & Run

```bash
git clone https://github.com/PrabhatTheCoder/Anime-Recommeder.git
cd Anime-Recommeder
docker-compose up --build



📦 API Endpoints
**Base URL: http://35.154.74.55/
**
🔐 Authentication
POST /auth/register/ – Register new user

POST /auth/login/ – Login to get JWT tokens

POST /auth/logout/ – Logout using refresh token

GET /auth/get-access-token/ – Get new access token using refresh

🎬 Anime
GET /anime/search/?name=xyz&genre=abc
→ Searches anime via AniList and asynchronously stores in DB

GET /anime/recommendations/?offset=0&limit=10
→ Returns recommendations personalized to user preferences

👤 User Preferences
GET /user/list-preferences/ – View user preferences

POST /user/preferences/ – Save/update preferences


🔁 Recommendation Logic
Matches favorite genres (regex match)

Filters out watched anime

Respects language, type, rating threshold, and disliked genres

Returns top-rated matching anime


⚙️ Async Processing
Search queries fetch real-time data from AniList GraphQL API and Celery saves fetched results to the database in the background.
save_anime_list_to_db_task.delay(anime_list)

☁️ Deployment (AWS Elastic Beanstalk)
Dockerized application deployed using Elastic Beanstalk
Environment config and dependencies managed via .ebextensions/
Auto-deployments via GitHub Actions CI/CD

📌 To-Do
 Implement frontend UI using React/Vue
 Add user-based collaborative filtering model


# Register
curl -X POST http://35.154.74.55/auth/register/ -H "Content-Type: application/json" \
     -d '{"email": "admin@gmail.com", "name": "admin", "password": "admin"}'

# Login
curl -X POST http://35.154.74.55/auth/login/ -H "Content-Type: application/json" \
     -d '{"email": "admin@gmail.com", "password": "admin"}'

# Get Access Token from Refresh
curl -X GET 'http://35.154.74.55/auth/get-access-token/?refresh=<refresh_token>'

# Search
curl -X GET http://35.154.74.55/anime/search/?name=Naruto \
     -H "Authorization: Bearer <access_token>"

# Save Preferences
curl -X POST http://35.154.74.55/user/preferences/ -H "Authorization: Bearer <access_token>" \
     -H "Content-Type: application/json" -d '{
       "favorite_genres": ["Action", "Sci-Fi"],
       "watched_anime_ids": ["2025"],
       "preferred_type": "TV",
       "language_preference": "Hindi",
       "disliked_genres": "Horror",
       "min_rating_threshold": "7.0"
     }'

# Get Recommendations
curl -X GET http://35.154.74.55/anime/recommendations/?offset=10&limit=10 \
     -H "Authorization: Bearer <access_token>"

# Logout
curl -X POST http://35.154.74.55/auth/logout/ \
     -H "Content-Type: application/json" \
     -H "Authorization: Bearer <access_token>" \
     -d '{"refresh": "<refresh_token>"}'
