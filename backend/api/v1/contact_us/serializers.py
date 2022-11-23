from rest_framework import serializers

from contact_us.models import Message


class MessageListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Message
        fields = "__all__"
        read_only_fields = ('is_active',)
