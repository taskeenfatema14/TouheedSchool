from rest_framework.serializers import ModelSerializer, ValidationError
from .models import User
from rest_framework import serializers
from django.contrib.auth import get_user_model


class UserTRialSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
        # exclude = ['last_login', 'date_joined', 'school']
    
    def get_fields(self, *args, **kwargs):
        fields = super().get_fields(*args, **kwargs)
        fields.pop('groups', None)  # Exclude 'groups' field
        return fields


class UserSerializer(ModelSerializer):
    school_name = serializers.SerializerMethodField()
    
    class Meta:
        model = User
        exclude = ['last_login', 'date_joined', 'school']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User.objects.create_user(**validated_data)
        user.set_password(password)
        user.save()
        
        return user
    
    def get_school_name(self, obj):
        if obj.school:
            return obj.school.name
        return None
    
class ForgotPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)

    def validate(self, data):
        email = data.get('email')

        if not email:
            raise ValidationError({'message': 'Email is required.'})

        user = User.objects.filter(email=email).first()

        if not user:
            raise ValidationError({'message': 'Email not found in the database.'})

        return data
        
class VerifyForgotOTPSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    otp = serializers.CharField(required=True)

    def validate(self, data):
        email = data.get('email')
        otp = data.get('otp')

        if not (email and otp):
            raise ValidationError({'message': 'Email and OTP are required.'})

        user = User.objects.filter(email=email).first()

        if not user or otp != otp:
            raise ValidationError({'message': 'Invalid email or OTP.'})

        return data
        
class SetNewPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    new_password = serializers.CharField(required=True)
    confirm_password = serializers.CharField(required=True)

    def validate(self, data):
        email = data.get('email')
        new_password = data.get('new_password')
        confirm_password = data.get('confirm_password')

        if not (email and new_password and confirm_password):
            raise ValidationError({'message': 'Email, new password, and confirm password are required.'})

        user = User.objects.filter(email=email).first()

        if not user:
            raise ValidationError({'message': 'User not found in the database.'})

        if new_password != confirm_password:
            raise ValidationError({'message': 'New password and confirm password do not match.'})

        return data
    
    def save(self):
        print("Save")
        user = User.objects.get(email=self.validated_data['email'])
        user.set_password(self.validated_data['new_password'])
        user.save()
        print("Save1")
        
# Not working
        
class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)
    confirm_password = serializers.CharField(required=True)
    model = User

    def validate(self, value):
        if (self.initial_data["old_password"] and self.initial_data["new_password"]
        ) and self.initial_data["confirm_password"]:
            if self.initial_data["new_password"] != self.initial_data["confirm_password"]:
                raise ValidationError({"password": "Passwords must match."})
            return value
        raise ValidationError(
            {
                "old_password": "This field may not be null.",
                "new_password": "This field may not be null.",
                "confirm_password": "This field may not be null.",
            }
        )

    def validate_old_password(self, old_password):
        print("in validate password")
        
        try : 
            user = self.context['request'].thisUser
        except : 
            raise serializers.ValidationError( "User Not Found")
            
        if not user.check_password(old_password):
            raise serializers.ValidationError("Old password is incorrect.")
        return old_password
    
    def save(self):
        if (
            self.validated_data["old_password"]
            and self.validated_data["new_password"]
            and self.validated_data["confirm_password"]
        ):
            user = self.context['request'].thisUser
            user.set_password(self.validated_data["new_password"])
            user.save()
        return user
    
User = get_user_model()

