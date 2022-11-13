from django.db import models

from accounts.models import CustomUser


class CommonInfo(models.Model):
    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)
    version = models.PositiveSmallIntegerField(default=0, editable=False)
    is_active = models.BooleanField(default=True)

    class Meta:
        abstract = True

    # docs.djangoproject.com/en/3.2/topics/db/models/#overriding-model-methods
    def save(self, *args, **kwargs):
        self.version = self.version + 1
        super().save(*args, **kwargs)  # Call the "real" save() method.


class Meeting(CommonInfo):
    publisher = models.ForeignKey(to=CustomUser,
                                  on_delete=models.SET_NULL,
                                  to_field='id',
                                  null=True,
                                  editable=False)
    subject = models.CharField(max_length=200)
    summary = models.TextField(
      verbose_name='Detail (introduce more about this meeting)')
    # The value stored to the database is the value in `ONLINE = ""`
    ONLINE = 'online'
    INPERSON = 'in-person'
    ONLINE_AND_INPERSON = 'online and in-person'
    CHECK_CHOICES = [
        (ONLINE, 'online'),
        (INPERSON, 'in-person'),
        (ONLINE_AND_INPERSON, 'online and in-person')
    ]
    way_of_meeting = models.CharField(choices=CHECK_CHOICES, max_length=20)
    meeting_time = models.DateTimeField()
    additional_notes = models.TextField(
        verbose_name='Additional notes (optional)', blank=True, null=True)

    def __str__(self):
        # If you don’t set list_display, the admin site will display a single
        # column that displays the __str__() representation of each object.
        return self.subject


class Registration(CommonInfo):
    meeting = models.ForeignKey(to=Meeting,
                                on_delete=models.SET_NULL,
                                to_field='id',
                                null=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    cunyfirst_id = models.CharField(verbose_name='CUNYFirst ID (optional)',
                                    max_length=20,
                                    blank=True,
                                    null=True)

    def __str__(self):
        # If you don’t set list_display, the admin site will display a single
        # column that displays the __str__() representation of each object.
        return self.first_name
