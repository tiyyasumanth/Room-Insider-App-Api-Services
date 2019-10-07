from django.db import models
from datetime import date
from django.contrib.auth.models import UserManager

class addroompersonmodel(models.Model):
    id=models.IntegerField(db_column="ID",editable=False)
    roomrent=models.TextField(db_column="ROOM_RENT",default='')
    internet=models.TextField(db_column="INTERNET",default='')
    powerbill=models.TextField(db_column="POWER_BILL",default='')
    ricebill=models.TextField(db_column="RICE_BILL",default='')
    numberofunits=models.TextField(db_column="NUMBER_OF_UNITS_CURRENT_BILL",editable=False,default='')
    maintainencebill=models.TextField(db_column="MAINTAINENCE_BILL",default='')
    sweeperbill=models.TextField(db_column="SWEEPER_BILL",default='')
    provisionsbill=models.TextField(db_column="PROVISIONS_BILL",default='')
    waterbill=models.TextField(db_column="WATER_BILL",default='')
    comments=models.TextField(db_column="COMMENTS",default='')
    billgenerateddata=models.TextField(db_column="BILL_GENERATED_DATE",default='',editable=False)
    paymentduedate=models.TextField(db_column="PAYMENT_DUE_DATE",default='',editable=False)
    paymenttype=models.TextField(db_column="PAYMENT_TYPE",default="")
    unbillamount=models.TextField(db_column="UNBILLED_AMOUNT",default="")
    totalamount=models.TextField(db_column="TOTAL_AMT_TO_PAY",default="")
    status=models.TextField(db_column="STATUS",default="NotPaid")
    personid=models.AutoField(db_column="PERSON_ID",primary_key=True)

    name=models.TextField(db_column="NAME",editable=False)
    lname=models.TextField(db_column="LAST_NAME",editable=False)
    personaddeddate=models.TextField(db_column="PERSON_ADDED_DATE",editable=False)
    personcomments=models.TextField(db_column="COMMENTS1",editable=False)
    childid=models.TextField(db_column="CHILD_ID",editable=False,default="")
    pstatus=models.TextField(db_column="Person_Status",editable=False,default="Active")

    # objects = UserManager()

    
    class Meta:
        managed = False
        db_table='Room_Rent_Details'