from django.urls import path 


from . import views

urlpatterns = [ 
    path('signup/', views.MySignupView.as_view(), name='user-signup'),
    path('login/', views.MyLoginView.as_view(), name='user-login'),
    path('logout/', views.MyLogoutView.as_view(), name='user-logout'),
]