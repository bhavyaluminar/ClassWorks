from django.http import Http404
from django.shortcuts import render

#API View for reading all records from Student Table
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from app1.serializers import StudentSerializer
from app1.models import Student
from rest_framework import permission_classes
from rest_framework.permissions import IsAuthenticated
@api_view(['GET','POST'])
@permission_classes[IsAuthenticated,]
def StudentList(request):
    if(request.method=="GET"):
        s=Student.objects.all()
        stu=StudentSerializer(s,many=True)
        return Response(stu.data,status=status.HTTP_200_OK)
    if(request.method=="POST"):
        s=StudentSerializer(data=request.data)
        if s.is_valid():
            s.save()
            return Response(s.data,status=status.HTTP_201_CREATED)
from rest_framework.views import APIView
# class StudentList(APIView):
#
#         def get(self,request):
#                 s=Student.objects.all()
#                 stu=StudentSerializer(s,many=True)
#                 return Response(stu.data,status=status.HTTP_200_OK)
#         def post(self,request):
#                 s=StudentSerializer(data=request.data)
#                 if s.is_valid():
#                     s.save()
#                     return Response(s.data,status=status.HTTP_201_CREATED)
from rest_framework import mixins,generics
# class StudentList(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
#     queryset=Student.objects.all()
#     serializer_class=StudentSerializer
#     def get(self, request):
#         return self.list(request)
#
#     def post(self, request):
#         return self.create(request)

# @api_view(['GET','PUT','DELETE'])
# def Studentdetail(request,pk):
#     try:
#         s = Student.objects.get(id=pk)
#     except:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#     if(request.method=="GET"):
#
#         stu=StudentSerializer(s)
#         return Response(stu.data,status=status.HTTP_200_OK)
#     if(request.method=="PUT"):
#
#         stu=StudentSerializer(s,data=request.data)
#         if stu.is_valid():
#             stu.save()
#             return Response(stu.data,status=status.HTTP_201_CREATED)
#     if (request.method == "DELETE"):
#         s.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#
# class StudentDetail(APIView):
#     def get_object(self,pk):
#         try:
#             return Student.objects.get(id=pk)
#         except:
#             raise Http404
#     def get(self,request,pk):
#         s=self.get_object(pk)
#         stu=StudentSerializer(s)
#         return Response(stu.data,status=status.HTTP_200_OK)
#     def put(self,request,pk):
#         s = self.get_object(pk)
#         stu=StudentSerializer(s,data=request.data)
#         if stu.is_valid():
#             stu.save()
#             return Response(stu.data,status=status.HTTP_201_CREATED)
#
#     def delete(self, request, pk):
#         s = self.get_object(pk)
#         s.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)



# class StudentDetail(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,
#                     generics.GenericAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer
#
#     def get(self,request,pk):
#         return self.retrieve(request,pk)
#     def put(self,request,pk):
#         return self.update(request,pk)
#
#     def delete(self, request, pk):
#         return self.destroy(request,pk)

# class StudentList(generics.ListCreateAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer
#
#
# class StudentDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer
from rest_framework import viewsets
class StudentView(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


