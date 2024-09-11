from django.urls import path
from threads.views import homeView, threadView

urlpatterns = [
    path('', homeView, name="home"),
    path('threads/<str:chat_name>/<str:username>', threadView, name="threads"),
]