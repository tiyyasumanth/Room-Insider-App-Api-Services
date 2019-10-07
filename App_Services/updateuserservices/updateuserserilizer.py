from rest_framework import serializers
from App_Services.updateuserservices.updateusermodel import updateusermodel
from django.contrib.auth.models import UserManager

class updatepersonserilizer(serializers.ModelSerializer):
    objects = UserManager()
    class Meta:
        model=updateusermodel
        fields='__all__'