from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from manager.models import Requests
from .models import ClientGroup, Document, Membership
from .serializers import ClientGroupSerializer, DocumentSerializer, MembershipSerializer

# Client Group API VIew
class ClientGroupAPIView(APIView):

    def get(self, request, *args, **kwargs):
        """
        List all client groups.
        """
        groups = ClientGroup.objects.all()
        serializer = ClientGroupSerializer(groups, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        """
        Create new client group.
        """
        data = {
            'client_group_name': request.data.get('client_group_name'),
            'manager': request.data.get('manager')
        }

        serializer = ClientGroupSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

# Client Group Detail View
class ClientGroupDetailAPIView(APIView):

    def get(self, request, manager_id, *args, **kwargs):
        """
        Get group association.
        """
        group = ClientGroup.objects.filter(manager__id=manager_id)
        serializer = ClientGroupSerializer(group, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

# Membership API VIew
class MembershipAPIView(APIView):
    
    def get(self, request, *args, **kwargs):
        """
        List all membership.
        """
        memberships = Membership.objects.all()
        serializer = MembershipSerializer(memberships, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

# Membership Detail API View
class MembershipDetailAPIView(APIView):
    
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
class DocumentAPIView(APIView):

    def get(self, request, *args, **kwargs):
        """
        List all documents.
        """
        documents = Document.objects.all()
        serializer = DocumentSerializer(documents, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        """
        Create new document.
        """
        data = {
            'document': request.data.get('document'),
            'client': request.data.get('client'),
            'request': request.data.get('request'),
            'manager': request.data.get('manager')
        }

        serializer = DocumentSerializer(data=data)

        # Update request status from manager
        update_request = Requests.objects.get(id=request.data.get("request"))
        update_request.isDone = True
        update_request.save()

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Document API Detail View
class DocumentDetailAPIView(APIView):

    def get_document_object(self, user_id):
        """
        Helper method to get the user object with given user id
        """

        try:
            return Document.objects.get(client=user_id)
        except Document.DoesNotExist:
            return None

    def get(self, request, client_id, *args, **kwargs):
        """
        List specific client documents.
        """
        documents = Document.objects.filter(client__id=client_id)
        serializer = DocumentSerializer(documents, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, client_id, *args, **kwargs):
        """
        Updates the document with the given client_id if it exists.
        """

        document_instance = self.get_document_object(client_id)

        if not document_instance:
            return Response(
                {
                    "message": "Object with document_id does not exist."
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        data = {
            'document': request.data.get('document')
        }

        serializer = DocumentSerializer(instance=document_instance, data=data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, client_id, *args, **kwargs):
        """
        Delete document.
        """
        document_instance = self.get_document_object(client_id)

        if not document_instance:
            return Response(
                {
                    "message": "Object with document_id does not exist."
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        document_instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)