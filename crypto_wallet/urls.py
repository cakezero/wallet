from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('new-account/', views.new_account, name='new_account'),
    path('balance/<str:address>/', views.balance, name='balance'),
    path('send_tx/', views.send_tx, name='send'),
    path('market_data/<str:address>/<str:days>/', views.market_data, name='market_data')
]