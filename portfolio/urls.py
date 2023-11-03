from django.urls import path
from .views import *
urlpatterns = [
    path('',PortfolioView.as_view(),name='portfolio' ),
    path('details/<str:uuid>',PortfolioDetailsView.as_view(),name='portfolio_details'),
]