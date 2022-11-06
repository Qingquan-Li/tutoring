from rest_framework import serializers

from feedback.models import Feedback


class FeedbackListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Feedback
        fields = "__all__"
        read_only_fields = ('is_active',)
