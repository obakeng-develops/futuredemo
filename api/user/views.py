from django.shortcuts import render
from rest_framework.serializers import Serializer
from rest_framework.views import APIView, set_rollback
from rest_framework.response import Response
from rest_framework import status
from .models import CustomUser, Profile
from .serializers import CustomUserSerializer, ProfileSerializer

# User API View
class CustomUserAPIView(APIView):

    def get(self, request, *args, **kwargs):
        """
        List all users.
        """
        users = CustomUser.objects.all()
        serializer = CustomUserSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        """
        Create new user.
        """
        data = {
            'email': request.data.get('email'),
            'password': request.data.get('password'),
            'is_staff': request.data.get('is_staff'),
            'is_superuser': request.data.get('is_superuser'),
            'role': request.data.get('role')
        }

        serializer = CustomUserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# User Detail View
class CustomUserDetailAPIView(APIView):

    def get_object(self, user_id):
        """
        Helper method to get the object with given user id
        """
        try:
            return CustomUser.objects.get(id=user_id)
        except CustomUser.DoesNotExist:
            return None

    def get(self, request, user_id, *args, **kwargs):
        """
        Retrieves User object with given user_id
        """
        user_instance = self.get_object(user_id)

        if not user_instance:
            return Response(
                {
                    "message": "Object with user_id does not exist."
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = CustomUserSerializer(user_instance)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, user_id, *args, **kwargs):
        """
        Updates the user with the given user_id if it exists.
        """

        user_instance = self.get_object(user_id)

        if not user_instance:
            return Response(
                {
                    "message": "Object with user_id does not exist."
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        data = {
            'email': request.data.get('email'), 
            'role': request.data.get('role'), 
            'id': request.user.id
        }

        serializer = CustomUserSerializer(instance=user_instance, data=data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Profile View
class ProfileAPIView(APIView):
    
    def get(self, request, *args, **kwargs):
        """
        List all user profiles.
        """
        users = Profile.objects.all()
        serializer = ProfileSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

# Profile Detail View
class ProfileDetailAPIView(APIView):
    
    def get_user_object(self, user_id):
        """
        Helper method to get the user object with given user id
        """

        try:
            return CustomUser.objects.get(id=user_id)
        except CustomUser.DoesNotExist:
            return None

    def get_profile_object(self, user_id):
        """
        Helper method to get the profile object with given user id
        """

        try:
            return Profile.objects.get(user=user_id)
        except Profile.DoesNotExist:
            return None

    def get(self, request, user_id, *args, **kwargs):
        """
        Retrieves Profile object with given user_id
        """
        profile_instance = self.get_profile_object(user_id)

        if not profile_instance:
            return Response(
                {
                    "message": "Object with user_id does not exist."
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = ProfileSerializer(profile_instance)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, user_id, *args, **kwargs):
        """
        Create new profile.
        """
        user_instance = self.get_user_object(user_id)

        if not user_instance:
            return Response(
                {
                    "message": "Object with user_id does not exist."
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        data = {
            'user': user_id,
            'first_name': request.data.get('first_name'),
            'last_name': request.data.get('last_name'),
        }

        serializer = ProfileSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, user_id, *args, **kwargs):
        """
        Updates the profile with the given user_id if it exists.
        """

        profile_instance = self.get_profile_object(user_id)

        if not profile_instance:
            return Response(
                {
                    "message": "Object with profile_id does not exist."
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        data = {
            'first_name': request.data.get('first_name'), 
            'last_name': request.data.get('last_name'),
        }

        serializer = ProfileSerializer(instance=profile_instance, data=data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)