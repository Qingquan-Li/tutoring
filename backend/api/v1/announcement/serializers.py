from rest_framework import serializers

from announcement.models import Announcement


class AnnouncementListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Announcement
        # fields = "__all__"
        fields = (
            "id",
            "created_time",
            "modified_time",
            "version",
            "is_active",
            "content",
            "start_time",
            "end_time",
            # "created_by",
            # "modified_by",
        )
