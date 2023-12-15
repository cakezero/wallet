from django.urls import path
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('new_account/', views.new_account, name='new_account'),
    path('balance/<str:coin_address>/', views.balance, name='balance'),
    path('send_tx/', views.send_tx, name='send'),
    path('market_data/<str:contract_address>/<int:days>/', views.market_data, name='market_data'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name="crypto_wallet/login.html"), name='login'),
    path('logout/', views.logout, name='logout')
]