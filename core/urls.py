from django.contrib.auth import views as auth_views
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView


from . import views
from . import forms

app_name = 'core'

urlpatterns = [
    path('', views.index, name="index"),
    path('contact/', views.contact, name="contact"),
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('login/', LoginView.as_view(template_name='core/login.html', authentication_form=forms.LoginForm), name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
]
