from rest_framework import serializers
from .models import *

class BookSerializers(serializers.ModelSerializer):
    class Meta:
        model= Book
        fields = "__all__"
        
        
class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model= UserTbl
        fields = "__all__"
        
        
class LoanSerializers(serializers.ModelSerializer):
    class Meta:
        model= Loan
        fields = "__all__"