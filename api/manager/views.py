from functools import partial
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Requests
from .serializers import RequestsSerializer

# Request API VIew
class RequestAPIView(APIView):

    def get(self, request, *args, **kwargs):
        """
        List all requests.
        """
        groups = Requests.objects.filter(isDone=True)
        serializer = RequestsSerializer(groups, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        """
        Create new request.
        """
        data = {
            'manager': request.data.get('manager'),
            'client': request.data.get('client'),
            'request_notes': request.data.get('request_notes'),
        }

        serializer = RequestsSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

# Request Detail API View
class RequestDetailAPIView(APIView):

    def get_request_object(self, user_id):
        """
        Helper method to get the user object with given user id
        """

        try:
            return Requests.objects.get(client=user_id)
        except Requests.DoesNotExist:
            return None

    def get(self, request, user_id, *args, **kwargs):
        """
        Retrieve client request.
        """
        groups = Requests.objects.filter(client__id=user_id)
        serializer = RequestsSerializer(groups, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, user_id, *args, **kwargs):
        """
        Updates the request with the given user_id if it exists.
        """

        request_instance = self.get_request_object(user_id)

        if not request_instance:
            return Response(
                {
                    "message": "Object with request_id does not exist."
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        data = {
            'request_notes': request.data.get('request_notes')
        }

        serializer = RequestsSerializer(instance=request_instance, data=data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)