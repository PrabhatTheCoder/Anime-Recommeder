from rest_framework import serializers
from .models import CustomUser
from .models import UserPreferences


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'email', 'name', 'phone_number', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = CustomUser(
            email=validated_data['email'],
            name=validated_data['name'],
            phone_number=validated_data.get('phone_number')
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
    
    
class UserPreferencesSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserPreferences
        fields = '__all__'
        read_only_fields = ['user']
        
    def update(self, instance, validated_data):
        append_fields = ['favorite_genres', 'watched_anime_ids', 'disliked_genres']
        for key, value in validated_data.items():
            if key in append_fields:
                existing = getattr(instance, key, [])
                if isinstance(existing, list) and isinstance(value, list):
                    updated = list(set(existing + value)) 
                    setattr(instance, key, updated)
                else:
                    setattr(instance, key, value) 
            else:
                setattr(instance, key, value) 
                
        instance.save()
        return instance
