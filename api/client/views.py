from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import mixins
from rest_framework import generics

from manager.models import Requests
from .models import ClientGroup, Document, Membership
from .serializers import ClientGroupSerializer, CreateClientGroupSerializer, DocumentSerializer, CreateDocumentSerializer, MembershipSerializer

# Client Group API VIew
class ClientGroupAPIView(generics.ListAPIView):
    """
    List all client groups.
    """

    queryset = ClientGroup.objects.all()
    serializer_class = ClientGroupSerializer

# Create Client Group
class CreateClientGroupAPIView(generics.CreateAPIView):
    """
    Create new client group.
    """

    queryset = ClientGroup.objects.all()
    serializer_class = CreateClientGroupSerializer

# Client Group Detail View based on manager ID
class ClientGroupDetailAPIView(APIView):

    def get(self, request, manager_id, *args, **kwargs):
        """
        Get group association.
        """
        group = ClientGroup.objects.filter(manager__id=manager_id)
        serializer = ClientGroupSerializer(group, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

# Membership API VIew
class MembershipAPIView(generics.ListAPIView):
    """
    List all memberships.
    """
    queryset = Membership.objects.all()
    serializer_class = MembershipSerializer

# Membership Detail API View based on Manager ID
class MembershipDetailAPIView(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):
    
    def get_group_object(self, manager_id):
        """
        Helper method to get the group object with given group id
        """
        try:
            return ClientGroup.objects.get(manager=manager_id)
        except ClientGroup.DoesNotExist:
            return None

    def get(self, request, manager_id, *args, **kwargs):
        """
        Get membership.
        """
        membership = Membership.objects.filter(group__manager__id=manager_id)
        serializer = MembershipSerializer(membership, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, manager_id, *args, **kwargs):
        """
        Create new membership.
        """

        group_instance = self.get_group_object(manager_id)

        if not group_instance:
            return Response(
                {
                    "message": "Object with group_id does not exist."
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        data = {
            'client': request.data.get('client'),
            'group': group_instance.id
        }

        serializer = MembershipSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Document API View
class DocumentAPIView(generics.ListCreateAPIView):

    """
    List all documents.
    """
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer

# Create Document API View
class CreateDocumentAPIView(generics.CreateAPIView):
    """
    Create new document.
    """
    queryset = Document.objects.all()
    serializer_class = CreateDocumentSerializer


# Document API Detail View
class DocumentDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update, or delete document details.
    """
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer
