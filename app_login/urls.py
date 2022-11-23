
from django.urls import path
from app_login import views



app_name='app_login'
urlpatterns = [
    path('signup/',views.sign_up,name="signup" ),
    path('signin/',views.login_page,name="signin" ),
    path('logout/',views.logout_page,name="logout" ),
    path('profile/',views.profile,name="profile" ),
    path('change_profile/',views.user_change,name="user_change" ),
    path('password/', views.pass_change, name='pass_change'),

    ]
