from django.shortcuts import redirect
from django.contrib.auth.views import (
    LoginView, 
    LogoutView,
)
from django.contrib.auth import login
from django.views.generic import FormView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy as rl




class MySignupView(FormView):
    template_name = 'accounts/user_signup.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True

    def get_success_url(self):
        return rl('task-list')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(MySignupView, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('task-list')
        return super(MySignupView, self).get(*args, **kwargs)

class MyLoginView(LoginView):
    template_name = 'accounts/user_login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return rl('task-list')


class MyLogoutView(LogoutView):
    next_page = 'user-login'