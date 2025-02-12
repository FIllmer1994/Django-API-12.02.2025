from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Forecast
from .serializers import ForecastSerializer
from datetime import datetime

class ForecastAPIView(APIView):
    def get(self, request, id, date):
        try:
            # date is changed into useful format
            date_obj = datetime.strptime(date, "%Y-%m-%d").date()
            # at first we try if we have stored a fitting forecast for query date itself
            queryset = Forecast.objects.filter(company_id=id, forecast_date=date_obj)
            if not queryset.exists():
                # in this case we need to look into data prior to the query date
                queryset = Forecast.objects.filter(company_id=id, forecast_date__lt=date_obj)
            if not queryset.exists():
                # if we can not find a fitting forecast the api should get the following text as response
                return Response({"detail": "No data found fot the given company_id and forecast_date."}, status=status.HTTP_404_NOT_FOUND)
            # out of all forecasts in queryset we want the newest
            latest_entry=queryset.order_by('-forecast_date').first()
            # if everything went well we get the serialized data as response
            serializer = ForecastSerializer(latest_entry)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except ValueError:
            # warning if requested date wasn't in fitting format
            return Response({"detail": "Invalid date format. Use YYYY-MM-DD"}, status=status.HTTP_400_BAD_REQUEST)

# the class MyModelAPICreateMock creates some mock data that can be used for testing
class ForecastAPICreateMock(APIView):    
    def get(self, request):
        # setting up mock data values
        id1 = 1
        company_id1 = 1
        forecast_date1 = "2024-12-01"
        values1 = [1, 2, 3]
        id2 = 2
        company_id2 = 1
        forecast_date2 = "2020-03-12"
        values2 = [1, 4, 9, 16]
        id3 = 3
        company_id3 = 2
        forecast_date3 = "2023-01-01"
        values3 = [7, 7]
        try:
            # try to put mock data into database
            Forecast.objects.create(
                id = id1,
                company_id = company_id1,
                forecast_date = forecast_date1,
                values = values1
            )
            Forecast.objects.create(
                id = id2,
                company_id = company_id2,
                forecast_date = forecast_date2,
                values = values2
            )
            Forecast.objects.create(
                id = id3,
                company_id = company_id3,
                forecast_date = forecast_date3,
                values = values3
            )
            return Response({"detail": "Mock data has been created"}, status=status.HTTP_200_OK)
        except:
            return Response({"detail": "Creation of mock data failed"}, status=status.HTTP_400_BAD_REQUEST)