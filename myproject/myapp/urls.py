from django.urls import path
from .views import ForecastAPIView, ForecastAPICreateMock

urlpatterns = [
    # we want requests with company_id and date
    path('api/data/<int:id>/<str:date>/', ForecastAPIView.as_view(), name='data-api'),
    path('api/create-mock/', ForecastAPICreateMock.as_view(), name='create-mock'),
]