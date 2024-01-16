from django.contrib import admin
from django.urls import path, include
from signupapis.views import UserSignupViewset
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'signup', UserSignupViewset)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls))
]
