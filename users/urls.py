from django.urls import path
from django.contrib.auth.views import LogoutView,LoginView
from .views import UserCreationView,profile,CodeSentView
urlpatterns = [
    path('login/', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', UserCreationView.as_view(), name='register'),
    path('profile/', profile, name='profile'),
    path('code-sent/', CodeSentView.as_view(), name='code_sent'),
]