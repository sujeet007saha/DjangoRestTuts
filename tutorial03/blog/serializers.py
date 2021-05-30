from rest_framework import serializers
from .models import Category, Post
from django.contrib.auth.models import User



class UserSerializer1(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ['id', 'username']


class PostSerializer1(serializers.ModelSerializer):
    owner = UserSerializer1(many = False, read_only = True)
    #category = serializers.HyperlinkedRelatedField(many=False, read_only=True, view_name='single-category')
    #category = serializers.SlugRelatedField(many=False, read_only=True, slug_field='title')

    class Meta:
        model = Post
        fields = ['id', 'title', 'body', 'owner', 'created_at']


class PostSerializer2(serializers.ModelSerializer):
    #owner = UserSerializer1(many = False, read_only = True)
    #category = serializers.HyperlinkedRelatedField(many=False, read_only=True, view_name='single-category')
    #category = serializers.SlugRelatedField(many=False, read_only=True, slug_field='title')

    class Meta:
        model = Post
        fields = ['id', 'title', 'body', 'owner', 'created_at']



class CategorySerializer(serializers.ModelSerializer):

    posts = PostSerializer1(many = True, read_only = True, source= 'categories')

    class Meta:
        model = Category
        fields = ['id', 'title', 'posts', 'created_at']



class PostSerializer(serializers.ModelSerializer):
    owner = UserSerializer1(many = False, read_only = True)
    #category = serializers.HyperlinkedRelatedField(many=False, read_only=True, view_name='single-category')
    category = serializers.SlugRelatedField(many=False, read_only=True, slug_field='title')
    url = serializers.HyperlinkedIdentityField(view_name = "post-detail", read_only = True)

    class Meta:
        model = Post
        fields = ['id', 'url', 'title', 'body', 'owner', 'category', 'created_at']

class UserSerializer(serializers.ModelSerializer):
    posts = PostSerializer2(many = True, read_only = True)

    class Meta:
        model = User
        fields = ['id', 'username', 'posts']