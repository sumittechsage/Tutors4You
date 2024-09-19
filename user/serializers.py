from rest_framework import serializers
from .models import User
from utils.user_utils import UserUtils

class RegisterationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        read_only_fields = ['id', 'is_superuser']


    def validate_password(self, password):
          return UserUtils.validate_password(password) 
    

class UserProfileSerializer(serializers.Serializer):
    full_name = serializers.SerializerMethodField(read_only = True)
    class Meta:
        model = User
        fields = ['id', 'full_name', 'email', 'avtar']

    
    def get_full_name(self, user):
        name = f"{user.first_name} {user.last_name}"
        return name.strip()