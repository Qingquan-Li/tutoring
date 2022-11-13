from django.test import TestCase

from contact_us.models import Message


class MessageModelTest(TestCase):

    @classmethod
    def setUpTestData(cls) -> None:
        """
        https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Testing
        setUpTestData() is called once at the beginning of the test
        run for class-level setup. You'd use this to create objects
        that aren't going to be modified or changed in any of the test methods.
        """
        Message.objects.create(
            # id,
            # created_time,
            # modified_time,
            # version,
            # is_active,
            name='Taylor Swift',
            email='taylorswift@email.com',
            content='Thanks for your tutoring, I got an A+ in the final 😀',
        )

    def test_version(self) -> None:
        message = Message.objects.get(id=1)
        # self.assertEqual(message.version, '1')
        # AssertionError: 1 != '1'
        self.assertEqual(f'{message.version}', '1')

    def test_is_active(self) -> None:
        message = Message.objects.get(id=1)
        self.assertTrue(message.is_active)

    def test_name(self) -> None:
        message = Message.objects.get(id=1)
        self.assertEqual(message.name, 'Taylor Swift')

    def test_email(self) -> None:
        message = Message.objects.get(id=1)
        self.assertEqual(message.email, 'taylorswift@email.com')

    def test_content(self) -> None:
        message = Message.objects.get(id=1)
        self.assertEqual(
            message.content,
            'Thanks for your tutoring, I got an A+ in the final 😀')


"""
$ python manage.py test contact_us.tests.test_models --settings=a_project_config.settings.local
Found 5 test(s).
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
.....
----------------------------------------------------------------------
Ran 5 tests in 0.002s

OK
Destroying test database for alias 'default'...
"""
