
from rest_framework import serializers
from app1.models import Recipe

class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Recipe
        fields='__all__'
from django.contrib.auth.models import User
class UserSerializer(serializers.ModelSerializer):

    #password=serializers.CharField(write_only=True)
    class Meta:
        model=User
        fields=['username','password','email','first_name','last_name']

    def create(self,validated_data):  #calls create() function after validation from register view

        user=User.objects.create_user(**validated_data) #to encrypt the password we use orm query
                                                        #User.objects.create_user while creating an user object
        return user

from app1.models import Review
class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model=Review
        fields=['recipe','rating','comment','user','id']
        read_only_fields=['id','user']
