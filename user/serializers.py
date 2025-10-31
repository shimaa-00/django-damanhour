from rest_framework import serializers
from .models import CustomUser
class UserSerializer (serializers.ModelSerializer):
    class Meta :
        model = CustomUser
        fields = ["id" , "email" ,"name","password"]
        extra_kwargs = {
            "password": {"write_only" :True}
        }
    def create(self, validated_data):
        return CustomUser.objects.create_user(
            name = validated_data.get('name'),
            email = validated_data.get('email'),
            password = validated_data.get('password'),
        )
    def update (self , instance , validated_data):
        if 'password' in validated_data:
            passw = validated_data.pop("password")
            instance.set_password(passw)
            return super().update (instance , validated_data)