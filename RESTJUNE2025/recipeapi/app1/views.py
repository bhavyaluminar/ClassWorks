from django.shortcuts import render
from rest_framework import viewsets

from app1.models import Recipe

from app1.serializers import RecipeSerializer,UserSerializer


class RecipeView(viewsets.ModelViewSet):
    queryset=Recipe.objects.all()
    serializer_class=RecipeSerializer

from django.contrib.auth.models import User
class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.response import Response
class LogoutView(APIView):
    permission_classes=[IsAuthenticated,]
    def get(self,request):
        self.request.user.auth_token.delete() #Deletes the token from Token Table for the logged in user
        return Response({'msg':'logout successfully'},status=status.HTTP_200_OK)

#create review
#get reviews
from app1.models import Review
from app1.serializers import ReviewSerializer
from django.http import Http404
class Allreviews(APIView):

    def get(self,request,pk):
        try:
            r=Recipe.objects.get(id=pk) #reads the recipe object
        except:
            raise Http404

        rev=Review.objects.filter(recipe=r) #reads all Reviews related to the recipe object from Review table

        reviews=ReviewSerializer(rev,many=True) #converts the data into json (serialization)
        return Response(reviews.data,status=status.HTTP_200_OK) #sends the response back to client
from rest_framework import viewsets
class CreateReview(viewsets.ModelViewSet):
    queryset=Review.objects.all()
    serializer_class=ReviewSerializer
    permission_classes=[IsAuthenticated]

    def perform_create(self,serializer):
        serializer.save(user=self.request.user)








