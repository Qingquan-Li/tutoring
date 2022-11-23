from django.contrib import admin

from .models import Message


class MessageAdmin(admin.ModelAdmin):
    # fields = (
    #     "is_active",
    #     "name",
    #     "email",
    #     "content",
    #     "created_time",
    #     "modified_time",
    #     # 'version",
    # )
    model = Message
    readonly_fields = (
        "created_time",
        "modified_time",
        # "version",
    )

    list_display = ("content", "name", "email", "created_time")
    
    search_fields = ("content",)


admin.site.register(Message, MessageAdmin)
