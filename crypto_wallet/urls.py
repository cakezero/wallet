from django.urls import path
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('new_account/', views.new_account, name='new_account'),
    path('balance/', views.balance, name='balance'),
    path('token_balance/<str:contract_address>/', views.token_balance, name='token_balance'),
    path('send_tx/', views.send_tx, name='send'),
    path('market_data/<str:contract_address>/<int:days>/', views.market_data, name='market_data'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name="crypto_wallet/login.html"), name='login'),
    path('logout/', views.logout, name='logout')
]