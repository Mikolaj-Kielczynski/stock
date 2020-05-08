"""MasterProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path, include
from stock import views
from stock.views import EditMarketView, EditStockView, EditCompanyView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.IndexView.as_view(), name='index'),
    path('analysis/', views.AnalysisView.as_view(), name='analysis_view'),
    path('login/', views.LoginView.as_view(), name='login_view'),
    path('contact-us/', views.ContatView.as_view(), name='contat_us'),
    path('market/', views.MarketListView.as_view(), name='market_list'),
    path('delete/market/<int:id>', views.DeleteMarketView.as_view(), name='delete_market'),
    path('stock/', views.StockListView.as_view(), name='stock_list'),
    path('delete/stock/<int:id>', views.DeleteStockView.as_view(), name='delete_stock'),
    path('companies/', views.CompaniesListView.as_view(), name='companies_list'),
    path('company/<str:abbreviation>/', views.CompanyDetailView.as_view(), name='company_detail'),
    path('delete/company/<int:id>/', views.DeleteCompanyView.as_view(), name='delete_company'),
    # path('company/quotes/', views.ProfileUploadView.as_view(), name='quote_views'),
    path("login/", views.LoginView.as_view()),
    path("not_logged/", views.NotLoginView.as_view()),
    path("logout/", views.LogOutView.as_view()),
    path("registration/", views.RegistrationView.as_view()),
    path("registration_info/", views.RegistrationInfoView.as_view()),
    path("accounts/", include('django.contrib.auth.urls')),
    path('add_data/<int:id>/', views.AddDataView.as_view(), name='add_data'),
    path("edit/market/<int:pk>", EditMarketView.as_view(), name='edit_market'),
    path("edit/stock/<int:pk>", EditStockView.as_view(), name='edit_stock'),
    path("company/<int:pk>", EditCompanyView.as_view(), name='edit_company'),
]