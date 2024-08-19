from rest_framework import serializers
from home.models import Person,Team
from django.contrib.auth.models import User

class RegisterSerializer(serializers.Serializer):
    username=serializers.CharField()
    email=serializers.EmailField()
    password=serializers.CharField()
    
    def validate(self,data):
        if data['username']:
            if User.objects.filter(username=data['username']).exists():
                raise serializers.ValidationError("Username already exists.")
            
        if data['email']:
            if User.objects.filter(email=data['email']).exists():
                raise serializers.ValidationError("Username already exists.")
            
        return data
    
    def create(self, validated_data):
        user=User.objects.create(username=validated_data['username'],email=validated_data['email'])
        user.set_password(validated_data['password'])
        user.save()
        return validated_data
    
class LoginSerializer(serializers.Serializer):
    username=serializers.CharField()
    password=serializers.CharField()

class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model=Team
        fields=['team_name']
        
        
class PersonSerializer(serializers.ModelSerializer):
    team=TeamSerializer(read_only=True)
    team_info=serializers.SerializerMethodField()
    
    
    class Meta:
        model=Person
        fields='__all__'
      
    def get_team_info(self,obj):
        return "extra serializer field"
    
    
    def validate(self,data):
        spl_chars='!@#$%^&*()-+?_=,<>/'
        
        if any(c in spl_chars for c in data['name']):
            raise serializers.ValidationError("Name should not have special characters")
        
        if data['age']<18:
            raise serializers.ValidationError("Age should be above 18")
        
        return data
            