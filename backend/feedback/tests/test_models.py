from django.test import TestCase

from feedback.models import Feedback


class FeedbackModelTest(TestCase):

    @classmethod
    def setUpTestData(cls) -> None:
        """
        https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Testing
        setUpTestData() is called once at the beginning of the test
        run for class-level setup. You'd use this to create objects
        that aren't going to be modified or changed in any of the test methods.
        """
        Feedback.objects.create(
            # id,
            # created_time,
            # modified_time,
            # version,
            # is_active,
            subject='First Feedback',
            message='Details of the first feedback.',
            email='taylorswift@email.com',
        )

    def test_version(self) -> None:
        feedback = Feedback.objects.get(id=1)
        # self.assertEqual(feedback.version, '1')
        # AssertionError: 1 != '1'
        self.assertEqual(f'{feedback.version}', '1')

    def test_is_active(self) -> None:
        feedback = Feedback.objects.get(id=1)
        self.assertTrue(feedback.is_active)

    def test_subject(self) -> None:
        feedback = Feedback.objects.get(id=1)
        self.assertEqual(feedback.subject, 'First Feedback')

    def test_message(self) -> None:
        feedback = Feedback.objects.get(id=1)
        self.assertEqual(feedback.message, 'Details of the first feedback.')

    def test_email(self) -> None:
        feedback = Feedback.objects.get(id=1)
        self.assertEqual(feedback.email, 'taylorswift@email.com')


"""
$ python manage.py test feedback.tests.test_models --settings=a_project_config.settings.local
Found 5 test(s).
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
.....
----------------------------------------------------------------------
Ran 5 tests in 0.002s

OK
Destroying test database for alias 'default'...
"""
