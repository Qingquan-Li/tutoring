from django.contrib import admin

from .models import Announcement


class AnnouncementAdmin(admin.ModelAdmin):

    def save_model(self, request, obj, form, change):
        """
        References:
        docs.djangoproject.com/en/4.1/ref/contrib/admin/#django.contrib.admin.ModelAdmin.save_model
        books.agiliq.com/projects/django-admin-cookbook/en/latest/current_user.html
        """
        if not obj.pk:
            obj.created_by = request.user
        obj.modified_by = request.user
        # obj.modified_at = timezone.now()
        super().save_model(request, obj, form, change)

    model = Announcement
    readonly_fields = (
        "created_time",
        "modified_time",
        "created_by",
        "modified_by",
        "version",
    )

    list_display = ("content", "start_time", "end_time",
                    "get_created_by_first_name_last_name",
                    "get_modified_by_first_name_last_name")

    def get_created_by_first_name_last_name(self, obj):
        return obj.created_by.first_name + ' ' + obj.created_by.last_name
    get_created_by_first_name_last_name.short_description = 'Created_by'
    get_created_by_first_name_last_name.admin_order_field = 'created_by__first_name'

    def get_modified_by_first_name_last_name(self, obj):
        return obj.modified_by.first_name + ' ' + obj.modified_by.last_name
    get_modified_by_first_name_last_name.short_description = 'Modified_by'
    get_modified_by_first_name_last_name.admin_order_field = 'modified_by__first_name'


admin.site.register(Announcement, AnnouncementAdmin)
