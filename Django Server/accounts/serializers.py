from dj_rest_auth.serializers import UserDetailsSerializer
from rest_framework import serializers

class CustomUserDetailsSerializer(UserDetailsSerializer):
    nickname = serializers.CharField(max_length=50, blank=False)

    def validate_nickname(self, value):
        if not value:
            raise serializers.ValidationError("Nickname cannot be empty.")
        return value

    class Meta(UserDetailsSerializer.Meta):
        fields = UserDetailsSerializer.Meta.fields + ('nickname',)
