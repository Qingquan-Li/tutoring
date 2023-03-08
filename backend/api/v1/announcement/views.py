from rest_framework import generics

from announcement.models import Announcement
from .serializers import AnnouncementListSerializer


class AnnouncementList(generics.ListAPIView):
    """ List: Meeting """
    queryset = Announcement.objects.all()
    serializer_class = AnnouncementListSerializer
    ordering_fields = ['start_time']
