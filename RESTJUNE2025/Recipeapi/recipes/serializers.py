
from rest_framework import serializers


from recipes.models import Review,Recipe
class RecipeSerializer(serializers.ModelSerializer):
   class Meta:
        model = Recipe
        fields = '__all__'


from rest_framework import serializers

class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = ('recipe','comment','rating','created','user')

        read_only_fields = ('created','user')


from django.contrib.auth.models import User
class UserSerializer(serializers.ModelSerializer):
    password=serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields=('username','email','first_name','last_name','password')

    def create(self,validated_data):

        user=User.objects.create_user(username=validated_data['username'],
                                      email=validated_data['email'],
                                      password=validated_data['password'],
                                      first_name=validated_data['first_name'],
                                      last_name=validated_data['last_name'])
        return user