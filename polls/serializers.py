from rest_framework import serializers
class TwerkSerializers(serializers.ModelSerializer):
    twerk_name=serializers.CharField()
    twerk_birth=serializers.DateField()
    twerk_numb=serializers.CharField()