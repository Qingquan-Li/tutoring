from django.urls import path
from .views import MeetingList
from .views import MeetingDetail
from .views import RegistrationList
from .views import RegistrationListForAMeeting

# docs.djangoproject.com/en/4.1/intro/tutorial03/#namespacing-url-names
app_name = 'api_v1_tutoring_info'

urlpatterns = [
    path('meetings/', MeetingList.as_view(), name='meeting-list'),
    path('meetings/<int:pk>/', MeetingDetail.as_view(), name='meeting-detail'),
    path('registrations/',
         RegistrationList.as_view(),
         name='registration-list'),
    path('meetings/<int:pk>/registrations/',
         RegistrationListForAMeeting.as_view(),
         name='registration-list-for-a-meeting'),
]
