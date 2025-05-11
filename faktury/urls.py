from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('nova/', views.nova_faktura, name='nova_faktura'),
    path('<int:faktura_id>/', views.detail, name='detail'),
    path('<int:faktura_id>/uprav/', views.upravit_fakturu, name='uprav_fakturu'),
    path('<int:faktura_id>/pdf/', views.export_pdf, name='export_pdf'),
    path('<int:faktura_id>/email/', views.posli_email, name='posli_email'),
]