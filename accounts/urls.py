from django.urls import path
from .views import HomeView

app_name = 'accounts'
urlpatterns = [
    path('home/', HomeView.as_view(), name='home'),
]