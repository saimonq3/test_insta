from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register('photo', views.PhotoView, 'photo')


urlpatterns = [
    path('register/', views.RegisterView.as_view()),
    path('get-token/', obtain_auth_token),
    *router.urls
]
