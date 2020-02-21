from users.models import User
from rest_framework import generics, permissions, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser

from django.contrib.auth import login, authenticate, user_logged_in

from users.serializers import UserSerializer
# from reFav.permissions import IsSelfOrOrgAdminOrSuperUser, IsSuperUserOrStaff


# Create your views here.
class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    # permission_classes = [
    #     IsSuperUserOrStaff,  # user.is_staff = true
    #     permissions.IsAuthenticated
    # ]

    def get_queryset(self):

            return User.objects.all()



class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializer
    # permission_classes = [
    #     permissions.IsAuthenticated,
    #     IsSelfOrOrgAdminOrSuperUser
    # ]

    def get_queryset(self):
        return User.objects.all()

    def perform_update(self, serializer):
        serializer.save(modified_by=self.request.user)


class UserCreate(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # permission_classes = [
    #     permissions.IsAuthenticated,
    #     permissions.IsAdminUser
    # ]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)


class AuthRegister(APIView):
    """
    Register a new user
    """
    serializer_class = UserSerializer
    # permission_classes = [
    #     permissions.IsAdminUser,
    #     permissions.IsAuthenticated
    # ]

    parser_classes = (MultiPartParser, FormParser, JSONParser)

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data,)

        print(request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AuthLogin(APIView):
    """ Manual implementation of login method"""

    def post(self, request, format=None):
        data = request.data
        username = data.get('username', None)
        password = data.get('password', None)

        user = authenticate(email=username, password=password)
        if user is not None:
            login(request, user)
            user_logged_in.send(sender=user.__class__, request=request, user=user)
            return Response({
                'status': 'Successful',
                'message': 'You have successfully been logged into your account.'
            }, status=status.HTTP_200_OK)

        return Response({
            'status': 'Unauthorized',
            'message': 'Username/Password combination invalid.'
        }, status=status.HTTP_401_UNAUTHORIZED)
