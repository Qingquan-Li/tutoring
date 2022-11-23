from rest_framework import serializers

from tutoring_info.models import Meeting
from tutoring_info.models import Registration


class MeetingListSerializer(serializers.ModelSerializer):
    meeting_time = serializers.DateTimeField(format="%m/%d/%Y %H:%M")

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
            # "additional_notes",
            # "registration_set",  # reverse relationship
        )

    def to_representation(self, instance):
        """
        Change from display `publisher.id` to display
        a dict of publisher's fields.
        """
        rep = super(MeetingListSerializer, self).to_representation(instance)
        rep['publisher'] = {
            'name':
            instance.publisher.first_name + ' ' + instance.publisher.last_name,
            'avatar_url':
            instance.publisher.profile.avatar_url,
            'institution':
            instance.publisher.profile.institution.name,
            'department':
            instance.publisher.profile.department.name,
            # 'introduction':
            # instance.publisher.profile.introduction,
        }
        # This way can not handle the timezone issue:
        # rep['meeting_time'] = instance.meeting_time.strftime(
        #     "%Y-%m-%d %H:%M:%S")
        return rep


class MeetingDetailSerializer(serializers.ModelSerializer):
    meeting_time = serializers.DateTimeField(format="%m/%d/%Y %H:%M")
    created_time = serializers.DateTimeField(format="%m/%d/%Y %H:%M")
    modified_time = serializers.DateTimeField(format="%m/%d/%Y %H:%M")

    class Meta:
        model = Meeting
        fields = "__all__"

    def to_representation(self, instance):
        """
        Change from display `publisher.id` to display
        a dict of publisher's fields.
        """
        rep = super(MeetingDetailSerializer, self).to_representation(instance)
        rep['publisher'] = {
            'name':
            instance.publisher.first_name + ' ' + instance.publisher.last_name,
            # 'email':
            # instance.publisher.email,
            'avatar_url':
            instance.publisher.profile.avatar_url,
            'institution':
            instance.publisher.profile.institution.name,
            'department':
            instance.publisher.profile.department.name,
            'introduction':
            instance.publisher.profile.introduction,
        }
        return rep


##############################################################################


class RegistrationListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Registration
        fields = "__all__"
        read_only_fields = ('is_active', )

    def to_representation(self, instance):
        """Change from display `meeting.id` to display `meeting.subject`."""
        rep = super(RegistrationListSerializer,
                    self).to_representation(instance)
        rep['meeting'] = instance.meeting.subject
        return rep
