"""
URL configuration for makeupfinder project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.conf.urls import include
from django.urls import path
from makeupapi.views import register_user, login_user, ProductViewSet, ProductTypeViewSet, TipsViewSet, ProfilePreferencesViewSet, ProfileViewSet, MakeupPreferencesViewSet, WishlistViewSet, MakeupSkillViewSet, UserViewSet, current_user_profile
from rest_framework import routers

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'products', ProductViewSet, 'product')
router.register(r'producttypes', ProductTypeViewSet, 'producttype')
router.register(r'tips', TipsViewSet, 'tip')
router.register(r'profilepreferences', ProfilePreferencesViewSet, 'profilepreference')
router.register(r'profile', ProfileViewSet, 'profile')
router.register(r'makeuppreferences', MakeupPreferencesViewSet, 'makeuppreference')
router.register(r'wishlist', WishlistViewSet, 'wishlist')
router.register(r'makeupskill', MakeupSkillViewSet, 'makeupskill')
router.register(r'users', UserViewSet, 'user')



urlpatterns = [
    path('register', register_user),
    path('login', login_user),
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('currentuserprofile', current_user_profile)
]