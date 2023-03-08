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


class Announcement(CommonInfo):
    content = models.TextField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    # Without `related_name`:
    # announcement.Announcement.created_by: (fields.E304) Reverse accessor
    # 'CustomUser.announcement_set' for 'announcement.Announcement.created_by'
    # clashes with reverse accessor for 'announcement.Announcement.modified_by'.
    # # HINT: Add or change a related_name argument to the definition for
    # 'announcement.Announcement.created_by' or 'announcement.Announcement.modified_by'.
    created_by = models.ForeignKey(to=CustomUser,
                                   on_delete=models.SET_NULL,
                                   to_field='id',
                                   null=True,
                                   editable=False,
                                   related_name='created_by_announcements')
    modified_by = models.ForeignKey(to=CustomUser,
                                    on_delete=models.SET_NULL,
                                    to_field='id',
                                    null=True,
                                    editable=False,
                                    related_name='modified_by_announcements')

    def __str__(self):
        # If you don’t set list_display, the admin site will display a single
        # column that displays the __str__() representation of each object.
        return self.content
