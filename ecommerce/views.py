from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response
from rest_framework import status
from .models import User, Social
from .serializers import UserSerializer
from .serializers import SocialSerializer
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from rest_framework import status,generics,parsers

class UserListCreateView(generics.GenericAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    parser_classes = [parsers.MultiPartParser]

    def get(self, request, format=None):
        user = User.objects.all()
        serializer = UserSerializer(user, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserDetail(generics.GenericAPIView):
    serializer_class = UserSerializer
    parser_classes = [parsers.MultiPartParser]
    def get_object(self, id):
        try:
            return User.objects.get(pk=id)
        except User.DoesNotExist:
            return None
    
    def get(self, request, id, format=None):
        user = self.get_object(id)
        if user:
            serializer = UserSerializer(user)
            return Response(serializer.data)
        return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, id, format=None):
        user = get_object_or_404(User, pk=id)
        serializer = UserSerializer(user, data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
    def delete(self, request, id, format=None):
        user = self.get_object(id)
        if user:
            user.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    # def patch(self, request, id, format=None):
    #     user = self.get_object(id)
    #     if user:
    #         serializer = UserSerializer(user, data=request.data, partial=True)
    #         if serializer.is_valid():
    #             serializer.save()
    #             return Response(serializer.data)
    #         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    #     return Response(status=status.HTTP_404_NOT_FOUND)
    
    # from django.shortcuts import get_object_or_404

    def patch(self, request, id, format=None):
        user = get_object_or_404(User, pk=id)
        serializer = UserSerializer(user, data=request.data, partial=True)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



# social
    
class SocialListCreateView(generics.GenericAPIView):
    queryset = Social.objects.all()
    serializer_class = SocialSerializer
    parser_classes = [parsers.MultiPartParser]

    def get(self, request, format=None):
        social = Social.objects.all()
        serializer = SocialSerializer(social, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SocialDetail(generics.GenericAPIView):
    serializer_class = SocialSerializer
    parser_classes = [parsers.MultiPartParser]
    def get_object(self, id):
        try:
            return Social.objects.get(pk=id)
        except Social.DoesNotExist:
            return None
    
    def get(self, request, id, format=None):
        social = self.get_object(id)
        if social:
            serializer = SocialSerializer(social)
            return Response(serializer.data)
        return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, id, format=None):
        social = get_object_or_404(Social, pk=id)
        serializer = SocialSerializer(social, data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
    def delete(self, request, id, format=None):
        social = self.get_object(id)
        if social:
            social.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_404_NOT_FOUND)

    def patch(self, request, id, format=None):
        social = get_object_or_404(Social, pk=id)
        serializer = SocialSerializer(social, data=request.data, partial=True)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
