"""
URL configuration for BlueBirdBanking project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from xml.etree.ElementInclude import include

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    #Sets the url path to home page index.html.
    path('', views.home, name='index'),
    #Sets the url path to Create New Account page CreateNewAccount.html.
    path('create/', views.create_account, name='create'),
    #Sets the url path to Balance Sheet page BalanceSheet.html.
    path('<int:pk>/balance/', views.balance, name='balance'),
    #Sets the url path to Add New Transaction page AddNewTransaction.html.
    path('transactions/', views.transactions, name='transactions')
]
