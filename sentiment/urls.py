from django.urls import path
from .views import home, analyze_sentiment, about

urlpatterns = [
    path('', home, name="home"),
    path('analyze/', analyze_sentiment, name="analyze_sentiment"),
    path('about/', about, name="about"),
]
