from rest_framework import serializers
from App_Services.roomrentailservices.roomrentmodel import roomrentmodel
from django.contrib.auth.models import UserManager

class roomrentilizer(serializers.ModelSerializer):
    objects = UserManager()
    class Meta:
        model=roomrentmodel
        fields='__all__'