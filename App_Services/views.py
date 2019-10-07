from django.shortcuts import render
from App_Services.loginservice.loginmodel import loginmodel
from App_Services.loginservice.loginserilizer import loginserilizer
from App_Services.roomrentailservices.roomrentmodel import roomrentmodel
from App_Services.roomrentailservices.roomrentserilizer import roomrentilizer

from App_Services.newAddedPersonServices.newpersonmodel import addroompersonmodel
from App_Services.newAddedPersonServices.newpersonserilizer import addroompersonsentilizer

from App_Services.updateuserservices.updateusermodel import updateusermodel
from App_Services.updateuserservices.updateuserserilizer import updatepersonserilizer
from rest_framework import generics
import base64
from datetime import date
from django.db import connection
from django.http import HttpResponse
from django.http import HttpRequest
import json
from django.views.decorators.csrf import csrf_exempt
import collections
import datetime

# Create your views here.
class saveRoomRentInfo(generics.ListCreateAPIView):
    queryset=roomrentmodel.objects.all()
    serializer_class=roomrentilizer
    def perform_create(self,serializer):
        print(self.request.data)
        rdt=self.request.data

        totalrentamount=(int(rdt["roomrent"])+int(rdt["internet"])+int(rdt["powerbill"])+
        int(rdt["waterbill"])+int(rdt["provisionsbill"])+
        int(rdt["maintainencebill"])+int(rdt["otherbills"])+int(rdt["ricebill"])++int(rdt["sweeperbill"]))
        uname=rdt["username"]
        print(totalrentamount)

        count=saveRoomRentInfo.getexactuser(uname)
        allusers=saveRoomRentInfo.getallusers(uname)
        maxval=saveRoomRentInfo.getmaxvalue(uname)
        
        divisionamount=totalrentamount/count
        userid=savenewpersonInfo.getuserid(uname)

        serializer.save(roomrent=str(round(int(rdt["roomrent"])/count)),internet=str(round(int(rdt["internet"])/count)),powerbill= str(round(int(rdt["powerbill"])/count)),
        ricebill=str(round(int(rdt["ricebill"])/count)),maintainencebill=str(round(int(rdt["maintainencebill"])/count)),
        sweeperbill=str(round(int(rdt["sweeperbill"])/count)),provisionsbill=str(round(int(rdt["provisionsbill"])/count)),waterbill=str(round(int(rdt["waterbill"])/count)),
        comments=rdt["comments"],unbillamount=str(round(divisionamount)),
        totalamount=str(round(divisionamount)),name=allusers[count-1][0],personid=maxval,childid=userid)

        saveRoomRentInfo.setAllDatatoReminingRoomMents(rdt,count,allusers,divisionamount,maxval,serializer,userid)

    def getexactuser(uname):
        cursor = connection.cursor()
        status='Active'
        cursor.execute("select count(ID) from Room_Rent_Details where ID = (select ID from user_login_details where USERNAME = '" + uname + "') and PERSON_STATUS='" + status + "' ")
        row = cursor.fetchone()
        if(row is None):
            return 'N'
        return int(row[0])
    
    def getallusers(uname):
        cursor = connection.cursor()
        cursor.execute("select NAME from Room_Rent_Details where ID = (select ID from user_login_details where USERNAME = '" + uname + "')")
        row = cursor.fetchall()
        if(row is None):
            return 'N'
        return row
    
    def getmaxvalue(uname):
        cursor = connection.cursor()
        cursor.execute('''SELECT max(PERSON_ID) FROM Room_Rent_Details''')
        row = cursor.fetchone()
        if(row is None):
            x=1
            return int(x)
        return int(row[0]+1)

    def setAllDatatoReminingRoomMents(rdetails,countt,allusers,divamount,maxval,ser,id):
        k=countt-1
        for i in range(k):
            print('--------------------------------------------------------------------------------------')
            print(i)
            maxval=maxval+1
            ser.save(roomrent=str(round(int(rdetails["roomrent"])/countt)),internet=str(round(int(rdetails["internet"])/countt)),powerbill= str(round(int(rdetails["powerbill"])/countt)),
            ricebill=str(round(int(rdetails["roomrent"])/countt)),maintainencebill=str(round(int(rdetails["maintainencebill"])/countt)),
            sweeperbill=str(round(int(rdetails["sweeperbill"])/countt)),provisionsbill=str(round(int(rdetails["provisionsbill"])/countt)),waterbill=str(round(int(rdetails["waterbill"])/countt)),
            comments=rdetails["comments"],unbillamount=str(round(divamount)),
            totalamount=str(round(divamount)),name=allusers[i][0],personid=maxval,childid=id)
   
class getloginview(generics.ListCreateAPIView):
    queryset=loginmodel.objects.all()
    serializer_class=loginserilizer
    
    def perform_create(self,serializer):
        print(self.request.data['password'])
        password=self.request.data['password']
        encriptedpassword=base64.b64encode(password.encode('utf-8'))
        maxId=getloginview.getuniqueid()
        serializer.save(id=maxId,password=encriptedpassword)
        # serializer.save(id=2,password=encriptedpassword)

    def getuniqueid():
        cursor = connection.cursor()
        cursor.execute('''SELECT max(ID) FROM user_login_details''')
        row = cursor.fetchone()
        if(row[0] is None):
            return 1
        return row[0]+1

    def getexactuser(uname):
        cursor = connection.cursor()
        cursor.execute("select * from user_login_details where USERNAME = '" + uname + "'")
        row = cursor.fetchone()
        if(row is None):
            return 'N'
        return 'Y'
    def gethisdata(uname):
        cursor = connection.cursor()
        userid=savenewpersonInfo.getuserid(uname)
        # cursor.execute("select rrd.name,pd.Address,pd.street,rrd.room_rent,rrd.internet,rrd.power_bill,rrd.maintainence_bill,rrd.sweeper_bill,rrd.provisions_bill,rrd.water_bill,rrd.unbilled_amount,rrd.total_amt_to_pay,rrd.Bill_generated_date,rrd.status from Room_Rent_Details rrd left join  Person_Details pd on rrd.id=pd.id where rrd.CHILD_ID = '" + str(userid) + "' order by BILL_GENERATED_DATE")
        cursor.execute("select rrd.name,pd.Address,pd.street,rrd.room_rent,rrd.internet,rrd.power_bill,rrd.maintainence_bill,rrd.sweeper_bill,rrd.provisions_bill,rrd.water_bill,rrd.unbilled_amount,rrd.total_amt_to_pay,rrd.Bill_generated_date,rrd.status from Room_Rent_Details rrd ,Person_Details pd where pd.id=('" + str(userid) + "' ) and rrd.CHILD_ID =('" + str(userid) + "')")
        rowd = cursor.fetchall()
        print('-----------')
        print(len(rowd))
        collist=cursor.description
        if(rowd is None):
            return 'N'
        jdata= getloginview.convertdatatojson(collist,rowd)
        return jdata
    def convertdatatojson(collist,rowlist):
        columnlist=[]
        mainlist=[]
        length=len(collist)
        for cl in collist:
            columnlist.append(cl[0])
        for row in rowlist:
            dic=collections.OrderedDict()
            for i in range(length):
                dic[columnlist[i]]=row[i]
            mainlist.append(dic)
        return json.dumps(mainlist)
    def myconverter(o):
        if isinstance(o, datetime.datetime):
            return "{}-{}-{}".format(o.year, o.month, o.day)
    def getactiveinfo(uname):
        status='Active'
        cursor = connection.cursor()
        userid=savenewpersonInfo.getuserid(uname)
        cursor.execute("select TOTAL_AMT_TO_PAY,UNBILLED_AMOUNT,STATUS,PERSON_STATUS,PERSON_ID,NAME from room_rent_details where (to_date(BILL_GENERATED_DATE,'dd-mm-YYYY')) BETWEEN (SELECT ADD_MONTHS((LAST_DAY(SYSDATE)+1),-1) FROM DUAL) AND (select last_day(sysdate) from dual) and PERSON_STATUS='" + status + "' and child_id=('" + str(userid) + "')")
        rowd = cursor.fetchall()
        collist=cursor.description
        if(rowd is None):
            return 'N'
        jdata= getloginview.convertdatatojson(collist,rowd)
        return jdata


@csrf_exempt
def loginview(HttpRequest):
    print('-------------------------------------------------------------------------------')
    if not HttpRequest.body:
        return HttpResponse(json.dumps({'message':"N"})) 
    requestdata=json.loads(HttpRequest.body)
    username=requestdata["username"]
    print(requestdata["username"])
    if not requestdata:
        return HttpResponse(json.dumps({'message':"N"}),content_type="application/json")   
    if requestdata:
        isrowdatafound=getloginview.getexactuser(username)
        # return HttpResponse(json.dumps({'usernme':rowdata[0],'password':rowdata[1]}) )
        if(isrowdatafound =='Y'):
            return HttpResponse(json.dumps({'message':"Y"}))   
        else:
            return HttpResponse(json.dumps({'message':"N"}))  

@csrf_exempt
def gethistoricaldata(HttpRequest):
    print('re----------------------------------------------------------------------------------------')
    print(HttpRequest.body)
    requestdata=json.loads(HttpRequest.body)
    username=requestdata["username"]
    rowdata=getloginview.gethisdata(username)
    return HttpResponse(rowdata)

#Create or add new person
class savenewpersonInfo(generics.ListCreateAPIView):
    queryset=addroompersonmodel.objects.all()
    serializer_class=addroompersonsentilizer
    def perform_create(self,serializer):
        print('-------------------------------------------testing------------------------------------------------------------------')
        print(self.request.data)
        rdt=self.request.data
        uname=rdt["username"]
        fname=rdt["fname"]
        lname=rdt["lname"]
        addeddate=rdt["addeddate"]
        comm=rdt["comm1"]
        maxval=savenewpersonInfo.getmaxvalue(uname)
        userid=savenewpersonInfo.getuserid(uname)

        serializer.save(personid=maxval,name=fname,lname=lname,personaddeddate=addeddate,personcomments=comm,id=userid)
    
    def getmaxvalue(uname):
        cursor = connection.cursor()
        cursor.execute('''SELECT max(PERSON_ID) FROM Room_Rent_Details''')
        row = cursor.fetchone()
        if(row[0] is None):
            x=1
            return int(x)
        return int(row[0]+1)
    def getuserid(uname):
        cursor = connection.cursor()
        cursor.execute("select ID from user_login_details where USERNAME = '" + uname + "'")
        row = cursor.fetchone()
        return row[0]
 

#get active data
@csrf_exempt          
def getuserdata(HttpRequest):
    requestdata=json.loads(HttpRequest.body)
    username=requestdata["username"]
    rowdata=getloginview.getactiveinfo(username)
    return HttpResponse(rowdata)

#update user rent info
class updateRoomRentInfo(generics.UpdateAPIView):
    queryset=roomrentmodel.objects.all()
    serializer_class=updatepersonserilizer

    def perform_update(self, serializer):
        serializer.save()

    def get_object(self):
        queryset = self.filter_queryset(self.get_queryset())
        pkid=self.request.data["personid"]
        username=self.request.data["username"]
        print('started-------------------------------------------------------------------------------------------------------------')
        obj = queryset.get(pk=pkid)
        self.check_object_permissions(self.request, obj)
        print('ended-------------------------------------------------------------------------------------------------------------')
        return obj
     
        

        

    

        




        
        

