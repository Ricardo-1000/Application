from django.urls import path
from users.views import handle_login
from users.views import handle_logout
from users.views import register
from users.views import profile
from users.views import upload
from users.views import profile_email

app_name = 'users'

urlpatterns = [
    path('login/', view=handle_login, name='login'),
    path('logout/', view=handle_logout, name='logout'),
    path('profile/', view=profile, name='profile'),
    path('profile/email', view=profile_email, name='profile_email'),
    path('register/', view=register, name='register'),
    path('upload/', view=upload, name='upload'),
]