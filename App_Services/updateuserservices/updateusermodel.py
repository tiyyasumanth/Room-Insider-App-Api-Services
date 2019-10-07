from django.db import models
from datetime import date

class updateusermodel(models.Model):
    # id=models.IntegerField(db_column="ID",editable=False,default=0)
    unbillamount=models.TextField(db_column="UNBILLED_AMOUNT")   
    status=models.TextField(db_column="STATUS")
    personid=models.AutoField(db_column="PERSON_ID",primary_key=True)
    # name=models.TextField(db_column="NAME",editable=False,default="")
    pstatus=models.TextField(db_column="PERSON_STATUS")

    class Meta:
        managed = False
        db_table='Room_Rent_Details'