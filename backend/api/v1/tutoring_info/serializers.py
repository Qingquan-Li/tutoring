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

        """
        -> Fix Bug: If user did not add profile on Admin->Users->Add user page, then error:
        File "/home/jake/tutoring/backend/api/v1/tutoring_info/serializers.py", line 37, in to_representation
            instance.publisher.profile.avatar_url,
        File "/home/jake/tutoring/backend/.venv/lib/python3.8/site-packages/django/db/models/fields/related_descriptors.py", line 461, in __get__
            raise self.RelatedObjectDoesNotExist(
        accounts.models.CustomUser.profile.RelatedObjectDoesNotExist: CustomUser has no profile.
        -> How to fix:
        Use `hasattr(self, 'related_object')` to check if a related object exists.
        Reference: https://docs.djangoproject.com/en/4.1/topics/db/examples/one_to_one/
        """
        if hasattr(instance.publisher, 'profile'):
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
        else:
            rep['publisher'] = {
                'name':
                instance.publisher.first_name + ' ' + instance.publisher.last_name,
                'avatar_url': None,
                'institution': None,
                'department': None,
                # 'introduction': None,
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
        if hasattr(instance.publisher, 'profile'):
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
        else:
            rep['publisher'] = {
            'name':
            instance.publisher.first_name + ' ' + instance.publisher.last_name,
            # 'email':
            # instance.publisher.email,
            'avatar_url': None,
            'institution': None,
            'department': None,
            'introduction': None,
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
