from django.test import TestCase
from django.contrib.auth import get_user_model

from accounts.models import Institution, Department, Profile


class CustomUserWithProfileModelTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        """
        https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Testing
        setUpTestData() is called once at the beginning of the test
        run for class-level setup. You'd use this to create objects
        that aren't going to be modified or changed in any of the test methods.
        """
        User = get_user_model()
        User.objects.create_user(
            # username='Alice',
            email='alice@email.com',
            password='testpass123')
        User.objects.create_superuser(
            # username='Bob',
            email='bob@email.com',
            password='testpass123')
        Institution.objects.create(name='BMCC-CUNY')
        Institution.objects.create(name='CCNY-CUNY')
        Department.objects.create(name='Math')
        Department.objects.create(name='Computer Science')
        Profile.objects.create(
            user=User.objects.get(email='alice@email.com'),
            avatar_url='https://placekitten.com/g/200/200',
            institution=Institution.objects.get(name='BMCC-CUNY'),
            department=Department.objects.get(name='Math'),
        )
        Profile.objects.create(
            user=User.objects.get(email='bob@email.com'),
            avatar_url='https://placekitten.com/g/300/300',
            institution=Institution.objects.get(name='CCNY-CUNY'),
            department=Department.objects.get(name='Computer Science'),
        )

    def test_create_user(self):
        user = get_user_model().objects.get(email='alice@email.com')
        self.assertEqual(user.email, 'alice@email.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)
        # profile = Profile.objects.get(pk=1)
        profile = Profile.objects.get(
            avatar_url='https://placekitten.com/g/200/200')
        self.assertEqual(profile.user.email, 'alice@email.com')
        self.assertEqual(profile.avatar_url,
                         'https://placekitten.com/g/200/200')
        self.assertEqual(profile.institution.name, 'BMCC-CUNY')
        self.assertEqual(profile.department.name, 'Math')

    def test_create_superuser(self):
        admin_user = get_user_model().objects.get(email='bob@email.com')
        self.assertEqual(admin_user.email, 'bob@email.com')
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)
        profile = Profile.objects.get(pk=2)
        # profile = Profile.objects.get(
        #     avatar_url='https://placekitten.com/g/300/300')
        self.assertEqual(profile.user.email, 'bob@email.com')
        self.assertEqual(profile.avatar_url,
                         'https://placekitten.com/g/300/300')
        self.assertEqual(profile.institution.name, 'CCNY-CUNY')
        self.assertEqual(profile.department.name, 'Computer Science')


"""
$ python manage.py test accounts.tests.test_models --settings=a_project_config.settings.local
Found 2 test(s).
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
..
----------------------------------------------------------------------
Ran 2 tests in 0.139s

OK
Destroying test database for alias 'default'...
"""
