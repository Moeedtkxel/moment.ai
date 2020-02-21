from rest_framework import serializers
from users.models import User


class UserSerializer(serializers.ModelSerializer):
    # username = serializers.SerializerMethodField(read_only=True)

    # def get_full_name(self, obj):
    #     return '{}'.format(obj.username)

    password = serializers.CharField(write_only=True, required=True)
    confirm_password = serializers.CharField(write_only=True, required=True)

    def create(self, validated_data):
        print("Creating user")
        return User.objects.create_user(**validated_data)

    def update(self, instance, validated_data):
        for field in validated_data:
            if field == 'password':
                confirm_password = validated_data.get('confirm_password', None)
                password = validated_data.get(field)

                if password and password == confirm_password:
                    instance.set_password(password)
            else:
                instance.__setattr__(field, validated_data.get(field))
        instance.save()
        return instance

    def validate(self, data):

        if 'password' in data.keys() and data['password']:
            print("Here")
            if 'confirm_password' not in data.keys() or data['password'] != data['confirm_password']:
                raise serializers.ValidationError("The passwords do not match")
        return data

    class Meta:
        model = User
        fields = '__all__'
