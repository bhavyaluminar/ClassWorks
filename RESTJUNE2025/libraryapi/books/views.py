from django.shortcuts import render

# Create your views here.
#Using Mixin Class

#get/post/put/delete
from rest_framework import viewsets, mixins, generics, status, permissions
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from books.models import Book
from books.serializers import BookSerializer

#
# class BookList(mixins.CreateModelMixin,mixins.ListModelMixin,generics.GenericAPIView):
#
#
#      queryset=Book.objects.all()
#      serializer_class=BookSerializer
#      def get(self,request):
#          return self.list(request)
#      def post(self,request):
#          return self.create(request)
#
# class BookList(generics.ListCreateAPIView):
#         queryset=Book.objects.all()
#         serializer_class=BookSerializer


# class BookDetail(mixins.UpdateModelMixin,mixins.DestroyModelMixin,mixins.RetrieveModelMixin,generics.GenericAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer
#     def get(self,request,pk):
#         return self.retrieve(request,pk)
#     def put(self,request,pk):
#         return self.update(request,pk)
#     def delete(self,request,pk):
#         return self.destroy(request,pk)
#
# class BookDetail(generics.RetrieveUpdateDestroyAPIView):
#         queryset = Book.objects.all()
#         serializer_class = BookSerializer


class BookView(viewsets.ModelViewSet):
        permission_classes=[IsAuthenticated]
        queryset = Book.objects.all()
        serializer_class = BookSerializer


#register -post

from django.contrib.auth.models import User
from books.serializers import UserSerializer
class UserView(viewsets.ModelViewSet):
        queryset = User.objects.all()
        serializer_class = UserSerializer
from rest_framework.views import APIView
class LogoutView(APIView):
        permission_classes=[IsAuthenticated]
        def get(self,request):
                self.request.user.auth_token.delete() #to delete the token inside Token table
                return Response({"msg":"logout Successfully"},status=status.HTTP_200_OK)





#SEARCHAPI View
from django.db.models import Q
# class SearchAPIView(APIView):
#     def get(self,request):
#             query=self.request.query_params.get('search')
#
#             if query:
#                     b=Book.objects.filter(Q(title__icontains=query)|
#                                           Q(author__icontains=query)|
#                                           Q(price__icontains=query)|
#                                           Q(language__icontains=query)|
#                                           Q(pages__icontains=query))
#                     if not b.exists():#if Queryset empty
#                             return Response({"msg": "No Search Results"}, status=status.HTTP_200_OK)
#
#                     books=BookSerializer(b,many=True)
#                     return Response(books.data,status=status.HTTP_200_OK)
#             else:#if keyword empty
#                     return Response({"msg":"No Search Results"},status=status.HTTP_200_OK)
from rest_framework import filters
class SearchAPIView(generics.ListAPIView):
        permission_classes=[IsAuthenticated,]
        queryset = Book.objects.all()
        serializer_class = BookSerializer
        filter_backends = (filters.SearchFilter,)
        search_fields = ('title','author','price','pages','language')


