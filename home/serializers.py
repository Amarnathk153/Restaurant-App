from rest_framework import serializers
from .models import User


class CustomerSignupSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type': 'password'},
                                      write_only=True)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'email', 'last_name',
                  'phone_number', 'password', 'password2']

    def save(self):
        reg = User(
            email=self.validated_data['email'],
            username=self.validated_data['username'],
            first_name=self.validated_data['first_name'],
            last_name=self.validated_data['last_name'],
            phone_number=self.validated_data['phone_number'],
        )
        password = self.validated_data['password']
        password2 = self.validated_data['password2']
        if password != password2:
            raise serializers.ValidationError({"password":
                                              "password does not match"})
        reg.set_password(password)
        reg.save()
        return reg


# Class CustomerLoginSerializer(serializers.ModelSeri)
