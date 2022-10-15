from django.db import models


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


class Feedback(CommonInfo):
    subject = models.CharField(max_length=200)
    message = models.TextField()
    email = models.EmailField()

    def __str__(self):
        # If you don’t set list_display, the admin site will display a single
        # column that displays the __str__() representation of each object.
        return self.subject
