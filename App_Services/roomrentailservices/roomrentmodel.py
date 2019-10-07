from django.db import models
from datetime import date
from django.contrib.auth.models import UserManager

class roomrentmodel(models.Model):
    id=models.IntegerField(db_column="ID",editable=False,default=0)
    roomrent=models.TextField(db_column="ROOM_RENT")
    internet=models.TextField(db_column="INTERNET")
    powerbill=models.TextField(db_column="POWER_BILL")
    ricebill=models.TextField(db_column="RICE_BILL")
    numberofunits=models.TextField(db_column="NUMBER_OF_UNITS_CURRENT_BILL",editable=False,default='')
    maintainencebill=models.TextField(db_column="MAINTAINENCE_BILL")
    sweeperbill=models.TextField(db_column="SWEEPER_BILL")
    provisionsbill=models.TextField(db_column="PROVISIONS_BILL")
    waterbill=models.TextField(db_column="WATER_BILL")
    comments=models.TextField(db_column="COMMENTS")
    billgenerateddata=models.TextField(db_column="BILL_GENERATED_DATE",default=date.today().strftime("%d-%m-%Y"),editable=False)
    paymentduedate=models.TextField(db_column="PAYMENT_DUE_DATE",default=date.today().strftime("%d-%m-%Y"),editable=False)
    paymenttype=models.TextField(db_column="PAYMENT_TYPE",default="by cash")
    unbillamount=models.TextField(db_column="UNBILLED_AMOUNT",default="")
    totalamount=models.TextField(db_column="TOTAL_AMT_TO_PAY",default="")
    status=models.TextField(db_column="STATUS",default="NotPaid")
    personid=models.AutoField(db_column="PERSON_ID",primary_key=True)
    name=models.TextField(db_column="NAME",editable=False)
    childid=models.TextField(db_column="CHILD_ID",editable=False)
    pstatus=models.TextField(db_column="Person_Status",editable=False,default="Active")

    # objects = UserManager()

    
    class Meta:
        managed = False
        db_table='Room_Rent_Details'