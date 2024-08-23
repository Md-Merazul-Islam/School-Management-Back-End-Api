from rest_framework import serializers
from .models import Profile, User

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer()

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'is_staff', 'profile','account_no']

    # def update(self, instance, validated_data):
    #     profile_data = validated_data.pop('profile', None)
    #     instance.username = validated_data.get('username', instance.username)
    #     instance.email = validated_data.get('email', instance.email)
    #     instance.save()

    #     if profile_data:
    #         profile = instance.profile
    #         profile.phone_number = profile_data.get('phone_number', profile.phone_number)
    #         profile.address = profile_data.get('address', profile.address)
    #         profile.date_of_birth = profile_data.get('date_of_birth', profile.date_of_birth)
    #         profile.department = profile_data.get('department', profile.department)
    #         profile.save()

    #     return instance
    
    
class UserRegistrationSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'confirm_password']

    def validate(self, data):
        if data['password'] != data['confirm_password']:
            raise serializers.ValidationError({"error": "Passwords don't match."})
        
        if User.objects.filter(email=data['email']).exists():
            raise serializers.ValidationError({'email': "Email already exists!"})

        if User.objects.filter(username=data['username']).exists():
            raise serializers.ValidationError({'username': "Username already exists!"})

        return data

    def create(self, validated_data):
        user = User(
            username=validated_data['username'],
            email=validated_data['email'],
        )
        user.set_password(validated_data['password'])  
        user.is_active = False
        user.save()
        return user
    
    

class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True)