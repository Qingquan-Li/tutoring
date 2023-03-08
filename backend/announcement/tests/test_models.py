import datetime

from django.test import TestCase
from django.contrib.auth import get_user_model
from django.utils import timezone

from announcement.models import Announcement


class AnnouncementModelTest(TestCase):

    @classmethod
    def setUpTestData(cls) -> None:

        User = get_user_model()
        cls.user_a = User.objects.create(email='alice@email.com',
                                         password='testpass123')
        cls.user_b = User.objects.create(email='bob@email.com',
                                         password='testpass123')

        cls.announcement = Announcement.objects.create(
            # id,
            # created_time,
            # modified_time,
            # version,
            # is_active,
            created_by = User.objects.get(email='alice@email.com'),
            modified_by = User.objects.get(email='alice@email.com'),
            content="Original content.",
            start_time=timezone.make_aware(
                datetime.datetime(2023, 3, 7, 0, 0, 0, 0),
                timezone.get_current_timezone()),
            end_time=timezone.make_aware(
                datetime.datetime(2023, 3, 11, 0, 0, 0, 0),
                timezone.get_current_timezone()),
        )

    def test_version(self) -> None:
        expected_content = f'{self.announcement.version}'
        self.assertEqual(expected_content, '1')

    def test_is_active(self) -> None:
        self.assertTrue(self.announcement.is_active)

    def test_created_by(self) -> None:
        expected_content = f'{self.announcement.created_by}'
        self.assertEqual(expected_content, 'alice@email.com')

    def test_original_content(self) -> None:
        expected_content = f'{self.announcement.content}'
        self.assertEqual(expected_content, "Original content.")

    def test_updated_content_and_modified_by(self) -> None:
        self.announcement.content = 'Updated content!'
        self.announcement.modified_by = self.user_b
        self.announcement.save()
        expected_content = f'{self.announcement.content}'
        self.assertEqual(expected_content, "Updated content!")
        expected_content = f'{self.announcement.modified_by}'
        self.assertEqual(expected_content, 'bob@email.com')

    def test_start_time(self) -> None:
        expected_content = f'{self.announcement.start_time}'
        # 11/06/2022 2am to 03/12/2023 2am, Eastern Standard Time (EST), UTC -5
        self.assertEqual(expected_content, '2023-03-07 00:00:00-05:00')

    def test_end_time(self) -> None:
        expected_content = f'{self.announcement.end_time}'
        self.assertEqual(expected_content, '2023-03-11 00:00:00-05:00')


"""
$ python manage.py test announcement.tests.test_models --settings=a_project_config.settings.local
Found 7 test(s).
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
.......
----------------------------------------------------------------------
Ran 7 tests in 0.008s

OK
Destroying test database for alias 'default'...
"""
