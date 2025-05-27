from django.urls import path
from .views import RegisterUserView, LoginUserView, LogoutUserView, GetAccessTokenView, UserPreferencesView

urlpatterns = [
    path('preferences/', UserPreferencesView.as_view()),
    path('list-preferences/', UserPreferencesView.as_view()),
    path('register/',RegisterUserView.as_view(), name='register'),
    path('get-access-token/', GetAccessTokenView.as_view(), name='get-access-token'), 
    path('login/', LoginUserView.as_view(), name='login'),
    path('logout/', LogoutUserView.as_view(), name='logout')
]
