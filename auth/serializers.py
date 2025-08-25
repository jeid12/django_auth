from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.conf import settings

AUTH_ROLES = getattr(settings, "AUTH_ROLES", (("user", "User"), ("admin", "Admin")))
AUTH_DEFAULT_ROLE = getattr(settings, "AUTH_DEFAULT_ROLE", "user")
class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    role = serializers.ChoiceField(choices=AUTH_ROLES, default=AUTH_DEFAULT_ROLE)

    def create(self, validated_data):
        user = get_user_model().objects.create(
              email=validated_data["email"],
              first_name=validated_data.get("first_name", ""),
              last_name=validated_data.get("last_name", ""),
              role=validated_data.get("role", ""),
          )
        user.set_password(validated_data["password"])
        user.save()
        return user
    class Meta:
        model = get_user_model()
        fields = ("email", "first_name", "last_name", "role", "password")
        extra_kwargs = {
            "password": {"write_only": True}
        }
