from .models import Post, Category
from .serializers import PostSerializer, CategorySerializer, UserSerializer
from rest_framework import serializers, status
#from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework import permissions
from .permissions import IsOwnerOrIsAdminOrReadOnly, IsOwnerOrReadOnly, IsOwnerOrIsAdminOrReadOnly
from rest_framework.reverse import reverse
from rest_framework import permissions, viewsets


# Function based views

''' @api_view(['GET', 'POST'])
def post_list(request, format=None):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        #data = JSONParser().parse(request)
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def post_detail(request, pk, format=None):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        post = Post.objects.get(pk=pk)
    except Post.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PostSerializer(post)
        return Response(serializer.data)

    elif request.method == 'PUT':
        #data = JSONParser().parse(request)
        serializer = PostSerializer(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

    elif request.method == 'DELETE':
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT) '''



# Class Based views
'''
class PostList(APIView):
    """
    List all code snippets, or create a new snippet.
    """
    def get(self, request, format = None):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        #data = JSONParser().parse(request)
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PostDetail(APIView):
    
    def get_object(self, pk):
        try:
            return Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk, format = None):
        post = self.get_object(pk)
        serializer = PostSerializer(post)
        return Response(serializer.data)

    def put(self, request, pk, format = None):
        post = self.get_object(pk)
        serializer = PostSerializer(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk, format = None):
        post = self.get_object(pk)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        '''


#using generic class based views

# class PostList(generics.ListCreateAPIView):
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly]
#     queryset = Post.objects.all()
#     print('qqqq', Post.objects.all())
#     serializer_class = PostSerializer

#     def perform_create(self, serializer):
#         serializer.save(owner=self.request.user)

# class PostDetail(generics.RetrieveUpdateDestroyAPIView):
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrIsAdminOrReadOnly]
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer

class PostViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

# class CategoryList(generics.ListAPIView):
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer

class CategoryCreate(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAdminUser]


# class CategoryDetail(generics.RetrieveAPIView):
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer


class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


# class UserList(generics.ListAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer


# class UserDetail(generics.RetrieveAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer



class ApiRoot(APIView):
    def get(self, request, format = None):
        return Response({
            'users': reverse('users', request=request, format=format),
            'posts': reverse('posts', request=request, format=format),
            'categories': reverse('categories', request=request, format=format),
            'admin-categories': reverse('admin-category', request=request, format=format)
        })