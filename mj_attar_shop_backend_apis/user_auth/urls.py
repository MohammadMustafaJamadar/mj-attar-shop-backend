from django.contrib import admin
from django.urls import path, include
from user_auth.views import signup

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', signup, name='signup')
]
