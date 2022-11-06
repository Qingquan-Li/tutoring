from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response

from feedback.models import Feedback
from .serializers import FeedbackListSerializer


class FeedbackList(generics.CreateAPIView):
    """ Create: Feedback """
    queryset = Feedback.objects.all()
    serializer_class = FeedbackListSerializer

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
                'message': 'Feedback created',
                'data': serializer.data,
            },
            status=status.HTTP_201_CREATED,
            headers=headers
        )
