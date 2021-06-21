from django.urls import path
from .views import HomeView, ProfileEditView  # 追加

app_name = 'accounts'
urlpatterns = [
    path('home/', HomeView.as_view(), name='home'),
    path('edit_profile/', ProfileEditView.as_view(), name='edit_profile'),  # 追加

]