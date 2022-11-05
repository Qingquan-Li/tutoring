from django.contrib import admin
from django.db.models import Count

from .models import Meeting, Registration


class MeetingAdmin(admin.ModelAdmin):

    def save_model(self, request, obj, form, change):
        """
        References:
        docs.djangoproject.com/en/4.1/ref/contrib/admin/#django.contrib.admin.ModelAdmin.save_model
        books.agiliq.com/projects/django-admin-cookbook/en/latest/current_user.html
        """
        obj.publisher = request.user
        super().save_model(request, obj, form, change)

    model = Meeting
    readonly_fields = (
        "created_time",
        "modified_time",
        "version",
    )

    list_display = ("subject", "meeting_time", "way_of_meeting",
                    "get_publisher_first_name_last_name",
                    "num_of_registrations")

    search_fields = ("subject", )

    def get_publisher_first_name_last_name(self, obj):
        return obj.publisher.first_name + ' ' + obj.publisher.last_name
    get_publisher_first_name_last_name.short_description = 'Publisher'
    get_publisher_first_name_last_name.admin_order_field = 'publisher__first_name'

    def num_of_registrations(self, obj):
        """
        Calculate the number of registrations with `annotate()` and `Count()`
        https://stackoverflow.com/questions/32443471/
        """
        return obj.num_of_registrations
    num_of_registrations.admin_order_field = "num_of_registrations"

    def get_queryset(self, request):
        """
        The get_queryset method on a ModelAdmin returns a QuerySet
        of all model instances that can be edited by the admin site.
        One use case for overriding this method is to show objects
        owned by the logged-in user.
        Reference:
        docs.djangoproject.com/en/4.1/ref/contrib/admin/#django.contrib.admin.ModelAdmin.get_queryset
        """
        qs = super().get_queryset(request)
        if request.user.is_superuser or request.user.groups.filter(name='administrator').exists():
            # return qs
            return qs.annotate(num_of_registrations=Count("registration"))
        # return qs.filter(publisher=request.user)
        return qs.filter(publisher=request.user).annotate(num_of_registrations=Count("registration"))


admin.site.register(Meeting, MeetingAdmin)


class RegistrationAdmin(admin.ModelAdmin):

    model = Registration
    readonly_fields = (
        "created_time",
        "modified_time",
    )

    list_display = ("get_full_name", "email", "meeting", "created_time")

    # search_fields = ("subject",)

    def get_full_name(self, obj):
        return obj.first_name + ' ' + obj.last_name

    get_full_name.short_description = 'Name'
    get_full_name.admin_order_field = 'first_name'

    def get_queryset(self, request):
        """
        The get_queryset method on a ModelAdmin returns a QuerySet
        of all model instances that can be edited by the admin site.
        One use case for overriding this method is to show objects
        owned by the logged-in user.
        Reference:
        docs.djangoproject.com/en/4.1/ref/contrib/admin/#django.contrib.admin.ModelAdmin.get_queryset
        """
        qs = super().get_queryset(request)
        if request.user.is_superuser or request.user.groups.filter(name='administrator').exists():
            return qs
        return qs.filter(meeting__publisher=request.user)

    search_fields = ("first_name", "last_name", "email")

    list_filter = (
        # "meeting",  # list all meetings for a tutor
        # You can limit the choices of a related model to the objects
        # involved in that relation using RelatedOnlyFieldListFilter.
        ("meeting", admin.RelatedOnlyFieldListFilter),
    )


admin.site.register(Registration, RegistrationAdmin)
