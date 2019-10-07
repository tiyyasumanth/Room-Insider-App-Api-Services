from rest_framework import serializers
from App_Services.newAddedPersonServices.newpersonmodel import addroompersonmodel
from django.contrib.auth.models import UserManager

class addroompersonsentilizer(serializers.ModelSerializer):
    objects = UserManager()
    class Meta:
        model=addroompersonmodel
        fields='__all__'