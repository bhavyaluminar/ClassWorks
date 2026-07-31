from django.http import Http404
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView

from recipes.models import Recipe, Review
from recipes.serializers import RecipeSerializer, UserSerializer, ReviewSerializer

# Create your views here.

from django.contrib.auth.models import User
#Recipe API
class RecipeView(viewsets.ModelViewSet):

    queryset=Recipe.objects.all()
    serializer_class=RecipeSerializer

#Register
class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

from django.db.models import Q
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
# class SearchAPIView(APIView):
#     def get(self,request):
#         query=self.request.query_params.get('search')
#         if query:
#             recipes = Recipe.objects.filter(Q(recipe_name__icontains=query)|
#                                         Q(ingredients__icontains=query)|
#                                         Q(instructions__icontains=query)|
#                                         Q(mealtype__icontains=query)|
#                                         Q(cuisine__icontains=query))
#
#
#             r=RecipeSerializer(recipes,many=True)
#             return Response(r.data,status=status.HTTP_200_OK)
#


class LogoutView(APIView):
    permission_classes=[IsAuthenticated]
    def get(self,request):
        self.request.user.auth_token.delete()
        return Response({'msg':'logout successfully'},status=status.HTTP_200_OK)




from rest_framework import filters,generics
class SearchAPIView(generics.ListAPIView):
        queryset = Recipe.objects.all()
        serializer_class = RecipeSerializer
        filter_backends = (filters.SearchFilter,)
        search_fields = ('recipe_name','ingredients','instructions','mealtype','cuisine')


class CreateReview(APIView):
    permission_classes = [IsAuthenticated,]
    def post(self,request):
        print(request.data)
        print(request.user)
        r=ReviewSerializer(data=request.data)
        if r.is_valid():
            r.save(user=request.user)
            return Response(r.data,status=status.HTTP_201_CREATED)

        return Response(r.errors,status=status.HTTP_400_BAD_REQUEST)

class ReadReview(APIView):
    def get(self,request,pk): #here pk means Recipeid
        # try:
        #     r=Recipe.objects.get(pk=pk)
        # except:
        #     raise Http404
        #
        # rev=Review.objects.filter(recipe=r) #fetches the reviews related to recipe
                                              #object
        #Or we can simply write it as below:
        
        rev=Review.objects.filter(recipe_id=pk)
        reviews=ReviewSerializer(rev,many=True)
        return Response(reviews.data,status=status.HTTP_200_OK)
