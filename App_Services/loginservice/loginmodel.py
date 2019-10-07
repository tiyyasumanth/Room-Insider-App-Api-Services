from django.db import models
from datetime import date

class loginmodel(models.Model):
    id=models.IntegerField(db_column="ID",primary_key=True,editable=False)
    username=models.TextField(db_column="USERNAME")
    password=models.TextField(db_column="PASSWORD")
    createddate=models.TextField(db_column="CREATEDDATE",default=date.today().strftime("%d-%m-%Y"),editable=False)
    
    class Meta:
        managed=True
        db_table='user_login_details'