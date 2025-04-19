from django.urls import path
from .views import ShortenURLView, RedirectURLView,URLStatsView,DeleteURLView,UpdateURLView

urlpatterns = [
    path('shorten/', ShortenURLView.as_view(), name='shorten_url'),
    path('<str:short_code>/', RedirectURLView.as_view(), name='redirect_url'),
    path('<str:short_code>/stats/', URLStatsView.as_view(), name='url_stats'),
    path('<str:short_code>/delete/', DeleteURLView.as_view(), name='delete_url'),
    path('<str:short_code>/update/', UpdateURLView.as_view(), name='update_url'),
]
