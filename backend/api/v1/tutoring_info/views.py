from rest_framework import generics
from rest_framework import permissions
from rest_framework import filters
from rest_framework import status
from rest_framework.response import Response

from tutoring_info.models import Meeting
from tutoring_info.models import Registration
from .serializers import MeetingListSerializer
from .serializers import MeetingDetailSerializer
from .serializers import RegistrationListSerializer
from .utils.pagination import CustomMeetingPagination


class MeetingList(generics.ListAPIView):
    """ List: Meeting """
    queryset = Meeting.objects.all()
    # Without `order_by` would warn:
    # TODO: After setting pagination -> queryset -> set order_by('id')
    # UnorderedObjectListWarning: Pagination may yield inconsistent results with
    # an unordered object_list: <class 'tutoring_info.models.Meeting'> QuerySet.
    # queryset = Meeting.objects.all().order_by('id')
    serializer_class = MeetingListSerializer
    # TODO: pagination
    # pagination_class = CustomMeetingPagination
    # https://www.django-rest-framework.org/api-guide/filtering/#orderingfilter
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['meeting_time']


class MeetingDetail(generics.RetrieveAPIView):
    """ Retrieve: A Meeting """
    queryset = Meeting.objects.all()
    serializer_class = MeetingDetailSerializer


class RegistrationList(generics.CreateAPIView):
    """ Create: Registration """
    queryset = Registration.objects.all()
    serializer_class = RegistrationListSerializer

    def create(self, request, *args, **kwargs):
        """Override the create function by changing the Response structure."""
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        # return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        return Response(
            {
                'status': 'ok',
                'message': 'Registration created',
                'data': serializer.data,
            },
            status=status.HTTP_201_CREATED,
            headers=headers
        )


class RegistrationListForAMeeting(generics.ListAPIView):
    """
    List: Registration List For A Meeting
    permissions: IsAdminUser
    """
    queryset = Registration.objects.all()
    serializer_class = RegistrationListSerializer
    permission_classes = (permissions.IsAdminUser,)

    # queryset = Registration.objects.all()
    # def get_queryset(self):
    #     """ If you are overriding a view method, it is important that you call 
    #     get_queryset() instead of accessing this property directly, as queryset will
    #     get evaluated once, and those results will be cached for all subsequent requests.
    #     https://www.django-rest-framework.org/api-guide/generic-views/#genericapiview
    #     """
    #     return Registration.objects.filter(meeting_id=self.kwargs.get('pk', None))

    def get_queryset(self):
        return super().get_queryset().filter(meeting_id=self.kwargs['pk'])
