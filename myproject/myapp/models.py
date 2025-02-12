from django.db import models

class Forecast(models.Model):
    # class gets the data fields mentioned in assignment
    id = models.IntegerField(primary_key=True)
    company_id = models.IntegerField()
    forecast_date = models.DateField()
    values = models.JSONField(default=list)
 

