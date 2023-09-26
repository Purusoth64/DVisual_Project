"""
URL configuration for Dvisual_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from config_details.views import *
from config.views import *
# from Tableau.views import *
from report.views import *
from django.conf.urls.static import static
from Minio.view import *
from Minio.get import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('dvisual_config/',Dvisual_Config_View.as_view()),
    path('dvisual_config/<int:pk>',Dvisual_Config_View.as_view()),
    path('dvisual_config_details/', Dvisual_Config_Detail_View.as_view()),
    path('dvisual_config_details/<int:pk>', Dvisual_Config_Detail_View.as_view()),
    path('dvisual_report',Report_Api.as_view()),
    path('dvisual_report/<int:pk>',Report_Api.as_view()),
    path('link',Remove_Duplicate.as_view()),
    path('downloadlink',Get_Api.as_view()),
    path('downloadlink/<int:pk>',Get_Api.as_view()),

    # path('download',PDFDownloader.as_view())
]#+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
