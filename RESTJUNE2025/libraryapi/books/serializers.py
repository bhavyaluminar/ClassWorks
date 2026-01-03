from rest_framework import serializers
from books.models import Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model=Book
        fields='__all__'
from django.contrib.auth.models import User
class UserSerializer(serializers.ModelSerializer):

    password=serializers.CharField(write_only=True)
    class Meta:
        model=User
        fields=['username','password','email','first_name','last_name']

    def create(self,validated_data):  #calls create() function after validation from register view

        user=User.objects.create_user(**validated_data) #to encrypt the password we use orm query
                                                        #User.objects.create_user while creating an user object
        return user







