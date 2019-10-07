from rest_framework import serializers
from App_Services.loginservice.loginmodel import loginmodel

class loginserilizer(serializers.ModelSerializer):
    class Meta:
        model=loginmodel
        fields='__all__'
    