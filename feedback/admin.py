from django.contrib import admin

from .models import Feedback


class FeedbackAdmin(admin.ModelAdmin):
    # fields = (
    #     "is_active",
    #     "subject",
    #     "message",
    #     "email",
    #     "created_time",
    #     "modified_time",
    #     # 'version",
    # )
    model = Feedback
    readonly_fields = (
        "created_time",
        "modified_time",
        # "version",
    )

    list_display = ("subject", "email", "created_time")
    
    search_fields = ("subject",)


admin.site.register(Feedback, FeedbackAdmin)
