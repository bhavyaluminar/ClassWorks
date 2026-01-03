from django.shortcuts import render
from rest_framework import viewsets
from books.models import Book
from books.serializers import BookSerializer,UserSerializer


# Create your views here.
from rest_framework.permissions import IsAuthenticated
class BookView(viewsets.ModelViewSet):
    permission_classes=[IsAuthenticated,]
    queryset = Book.objects.all()
    serializer_class = BookSerializer
from django.contrib.auth.models import User
class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
from django.db.models import Q
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
class SearchAPIView(APIView):
    def get(self,request):
        query=self.request.query_params.get('search')
        if query:
            b=Book.objects.filter(Q(title__icontains=query)|Q(author__icontains=query)|
                                  Q(pages__icontains=query)|Q(price__icontains=query)|
                                  Q(language__icontains=query))
            if not b.exists(): #Queryset empty
                return Response({'msg': 'No Results'}, status=status.HTTP_200_OK)

            books=BookSerializer(b,many=True)
            return Response(books.data,status=status.HTTP_200_OK)

        else:#Keyword empty
            return Response({'msg':'No Results'},status=status.HTTP_200_OK)

class LogoutView(APIView):
    permission_classes=[IsAuthenticated,]
    def get(self,request):
        self.request.user.auth_token.delete() #Deletes the token from Token Table for the logged in user
        return Response({'msg':'logout successfully'},status=status.HTTP_200_OK)


#filter by title APIView
#filter by price
class SearchAPIView(APIView):
    def get(self,request):
        query=self.request.query_params.get('search')
        if query:
            b=Book.objects.filter(title__icontains=query)
            if not b.exists(): #Queryset empty
                return Response({'msg': 'No Results'}, status=status.HTTP_200_OK)

            books=BookSerializer(b,many=True)
            return Response(books.data,status=status.HTTP_200_OK)

        else:#Keyword empty
            return Response({'msg':'No Results'},status=status.HTTP_200_OK)






