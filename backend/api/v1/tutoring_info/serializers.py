from rest_framework import serializers

from tutoring_info.models import Meeting
from tutoring_info.models import Registration


class MeetingListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Meeting
        fields = (
            "id",
            # "created_time",
            # "modified_time",
            # "version",
            "is_active",
            "publisher",  # foreign_key
            "subject",
            "summary",
            "way_of_meeting",
            "meeting_time",
            "additional_notes",
            # "registration_set",  # reverse relationship
        )

    def to_representation(self, instance):
        """Change from display `publisher.id` to display publisher's name."""
        rep = super(MeetingListSerializer, self).to_representation(instance)
        rep['publisher'] = instance.publisher.first_name + ' ' + instance.publisher.last_name
        return rep


class MeetingDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Meeting
        fields = "__all__"

    def to_representation(self, instance):
        """Change from display `publisher.id` to display publisher's name."""
        rep = super(MeetingDetailSerializer, self).to_representation(instance)
        rep['publisher'] = instance.publisher.first_name + ' ' + instance.publisher.last_name
        return rep


##############################################################################


class RegistrationListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Registration
        fields = "__all__"
        read_only_fields = ('is_active',)

    def to_representation(self, instance):
        """Change from display `meeting.id` to display `meeting.subject`."""
        rep = super(RegistrationListSerializer, self).to_representation(instance)
        rep['meeting'] = instance.meeting.subject
        return rep
