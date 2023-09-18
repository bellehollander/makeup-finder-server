from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.db import IntegrityError
from rest_framework.authtoken.models import Token
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response


@api_view(['POST'])
@permission_classes([AllowAny])
def login_user(request):
    # grab the username and password from the request
    username = request.data['username']
    password = request.data['password']
    # use django's built in authentication method to verify
    authenticated_user = authenticate(username=username, password=password)
    # if authentication was successful, respond with the token
    if authenticated_user is not None:
        token = Token.objects.get(user=authenticated_user)
       # data = { 'valid': True, 'token': token.key }
        data = {
            'valid': True,
            'token': token.key,
            'staff': authenticated_user.is_staff
        }
        return Response(data)
    else:
        # bad login details were provided. so we can't allow login
        data = { 'valid': False }
        return Response(data)

@api_view(['POST'])
@permission_classes([AllowAny])
def register_user(request):
    # request the data from the client
    account_type = request.data.get('account_type', None)
    email = request.data.get('email', None)
    first_name = request.data.get('first_name', None)
    last_name = request.data.get('last_name', None)
    password = request.data.get('password', None)
# check to see if all the data was provided
    if account_type is not None \
        and email is not None\
        and first_name is not None \
        and last_name is not None \
        and password is not None:

    # if it was, create a new user
        try:
            new_user = User.objects.create_user(
                username=request.data['username'],
                email=request.data['email'],
                password=request.data['password'],
                first_name=request.data['first_name'],
                last_name=request.data['last_name']
            )
            # if the email already exists, return an error
        except IntegrityError:
            return Response(
                {'message': 'An account with that email address already exists'},
                status=status.HTTP_400_BAD_REQUEST
            )
        # if the account type is admin, make the user a staff member
        if account_type == 'admin':
            new_user.is_staff = True
            new_user.save()
        # create a token for the user
        token = Token.objects.create(user=new_user)
        # return the token to the client, along with the user's staff status and valid status
        data = { 'token': token.key, 'staff': new_user.is_staff, 'valid': True }
        # return the response
        return Response(data)

    return Response({'message': 'You must provide email, password, first_name, last_name, and account_type'}, status=status.HTTP_400_BAD_REQUEST)




   
