
from rest_framework import serializers

from books.models import Book

class BookSerializer(serializers.ModelSerializer):
    # image_url = serializers.SerializerMethodField()

    class Meta:
        model = Book
        fields = '__all__'



    # def get_image_url(self, obj):
    #     request = self.context.get('request')
    #     photo_url = obj.image.url
    #     return request.build_absolute_uri(photo_url)

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