from django.urls import path, include
from main import views as m_views

urlpatterns = [
path('', m_views.HomeView.as_view(), name='home')
]