from django.urls import path
from django.urls import include

urlpatterns = [
    # path('tutoring-info/', include('api.v1.tutoring_info.urls')),
    path('', include('api.v1.tutoring_info.urls')),
    path('', include('api.v1.contact_us.urls')),
    path('', include('api.v1.announcement.urls')),
]
