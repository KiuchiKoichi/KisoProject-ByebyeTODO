from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin

from django.contrib.auth.decorators import login_required
from django.contrib.auth import (
     get_user_model, logout as auth_logout,
)
from .forms import UserCreateForm, UserSettingForm

User = get_user_model()


class Top(generic.TemplateView):
    template_name = 'top.html'


class Index(generic.TemplateView):
    template_name = 'accounts/index.html'


class SignUpView(generic.CreateView):
    form_class = UserCreateForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


class ProfileView(LoginRequiredMixin, generic.View):

    def get(self, *args, **kwargs):
        return render(self.request, 'registration/profile.html')


class DeleteView(LoginRequiredMixin, generic.View):

    def get(self, *args, **kwargs):
        user = User.objects.get(email=self.request.user.email)
        user.is_active = False
        user.save()
        auth_logout(self.request)
        return render(self.request,'registration/delete_complete.html')


@login_required
def setting(request) -> render:
    user = request.user
    if request.method == "POST":
        form = UserSettingForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('accounts:setting')
    else:
        form = UserSettingForm(instance=user)
    return render(request, 'usersetting.html', {'form': form})
