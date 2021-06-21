from django.views.generic.base import TemplateView
from django.views.generic.edit import UpdateView # 追加
from django.contrib.auth.mixins import LoginRequiredMixin # 追加
from .models import CustomUser
from .forms import ProfileForm  # 追加

class HomeView(TemplateView):
    template_name = 'account/home.html'

class ProfileEditView(LoginRequiredMixin, UpdateView): # 追加
   template_name = 'account/edit_profile.html'
   model = CustomUser
   form_class = ProfileForm
   success_url = '/accounts/edit_profile/'
   def get_object(self):
       return self.request.user