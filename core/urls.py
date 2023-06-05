from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name="index"),
	path('signup/', views.signup, name="signup"),
	path('not_ready/', views.not_ready, name="not_ready"),
]