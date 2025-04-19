from django.urls import path
from .views import ShortenURLView, RedirectURLView,URLStatsView

urlpatterns = [
    path('shorten/', ShortenURLView.as_view(), name='shorten_url'),
    path('<str:short_code>/', RedirectURLView.as_view(), name='redirect_url'),
    path('<str:short_code>/stats/', URLStatsView.as_view(), name='url_stats'),
]
