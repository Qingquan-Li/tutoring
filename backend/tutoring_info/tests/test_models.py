import datetime

from django.test import TestCase
from django.contrib.auth import get_user_model
from django.utils import timezone

from tutoring_info.models import Meeting
from tutoring_info.models import Registration


class MeetingModelTest(TestCase):

    @classmethod
    def setUpTestData(cls) -> None:

        User = get_user_model()
        User.objects.create(email='bob@email.com',
                                  password='testpass123')

        cls.meeting = Meeting.objects.create(
            # id,
            # created_time,
            # modified_time,
            # version,
            # is_active,
            # publisher=User.objects.get(email='bob@email.com'),
            publisher=User.objects.get(pk=1),
            subject='Subject of Meeting 1',
            summary='The summary of the first meeting.',
            way_of_meeting='online and in-person',
            # RuntimeWarning: DateTimeField Meeting.meeting_time received
            # a naive datetime (2022-10-24 14:00:00) while time zone
            # support is active.
            # meeting_time='2022-10-24 14:00:00',
            meeting_time=timezone.make_aware(
                datetime.datetime(2022, 10, 24, 0, 0, 0, 0),
                timezone.get_current_timezone()),
            additional_notes="Here's some additional notes..."
        )

    def test_version(self) -> None:
        expected_content = f'{self.meeting.version}'
        self.assertEqual(expected_content, '1')

    def test_is_active(self) -> None:
        self.assertTrue(self.meeting.is_active)

    def test_publisher(self) -> None:
        expected_content = f'{self.meeting.publisher}'
        self.assertEqual(expected_content, 'bob@email.com')

    def test_subject(self) -> None:
        expected_content = f'{self.meeting.subject}'
        self.assertEqual(expected_content, 'Subject of Meeting 1')

    def test_summary(self) -> None:
        expected_content = f'{self.meeting.summary}'
        self.assertEqual(expected_content,
                         'The summary of the first meeting.')

    def test_way_of_meeting(self) -> None:
        expected_content = f'{self.meeting.way_of_meeting}'
        self.assertEqual(expected_content, 'online and in-person')

    def test_meeting_time(self) -> None:
        expected_content = f'{self.meeting.meeting_time}'
        self.assertEqual(expected_content, '2022-10-24 00:00:00-04:00')

    def test_additional_notes(self) -> None:
        expected_content = f'{self.meeting.additional_notes}'
        self.assertEqual(expected_content,
                         "Here's some additional notes...")

    # https://docs.djangoproject.com/en/4.1/ref/models/instances/#get-absolute-url
    # def test_get_absolute_url(self) -> None:
    #     # This will also fail if the urlconf is not defined.
    #     self.assertEqual(
    #         self.meeting.get_absolute_url(),
    #         '/meeting/{id}/{slug}'.format(id=self.meeting.pk)


class RegistrationModelTest(TestCase):

    @classmethod
    def setUpTestData(cls) -> None:

        Meeting.objects.create(
            publisher=get_user_model().objects.create_user(
                email='bob@email.com', password='testpass123'),
            subject='Subject of Meeting 1',
            summary='The summary of the first meeting.',
            way_of_meeting='online and in-person',
            meeting_time=timezone.make_aware(
                datetime.datetime(2022, 10, 24, 0, 0, 0, 0),
                timezone.get_current_timezone()),
            additional_notes="Here's some additional notes..."
        )

        cls.registration = Registration.objects.create(
            # id,
            meeting=Meeting.objects.get(pk=1),
            first_name='John',
            last_name='Joe',
            email='johnjoe@email.com',
            # cunyfirst_id='24263901',
            cunyfirst_id=None,
        )

    def test_meeting(self) -> None:
        expected_content = f'{self.registration.meeting}'
        self.assertEqual(expected_content, 'Subject of Meeting 1')

    def test_first_name(self) -> None:
        expected_content = f'{self.registration.first_name}'
        self.assertEqual(expected_content, 'John')

    def test_last_name(self) -> None:
        expected_content = f'{self.registration.last_name}'
        self.assertEqual(expected_content, 'Joe')

    def test_email(self) -> None:
        expected_content = f'{self.registration.email}'
        self.assertEqual(expected_content, 'johnjoe@email.com')

    def test_cunyfirst_id(self) -> None:
        # expected_content = f'{self.registration.cunyfirst_id}'
        # self.assertEqual(expected_content, '24263901')
        assert self.registration.cunyfirst_id is None


"""
$ python manage.py test tutoring_info.tests.test_models --settings=a_project_config.settings.local
Found 13 test(s).
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
.............
----------------------------------------------------------------------
Ran 13 tests in 0.068s

OK
Destroying test database for alias 'default'...
"""
