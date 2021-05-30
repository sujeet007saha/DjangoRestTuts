from django.urls.conf import include
from blog.models import Category
from django.urls import path, include
from .views import CategoryCreate, CategoryViewSet, PostViewSet, UserViewSet, ApiRoot
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'posts', PostViewSet)
router.register(r'categories', CategoryViewSet)


# PostList = PostViewSet.as_view({
#     'get': 'list',
#     'post': 'create'
# })
# PostDetail = PostViewSet.as_view({
#     'get': 'retrieve',
#     'put': 'update',
#     'patch': 'partial_update',
#     'delete': 'destroy'
# })

# CategoryList = CategoryViewSet.as_view({
#     'get': 'list',
# })
# CategoryDetail = CategoryViewSet.as_view({
#     'get': 'retrieve',
# })

# UserList = UserViewSet.as_view({
#     'get': 'list',
# })
# UserDetail = UserViewSet.as_view({
#     'get': 'retrieve',
# })


urlpatterns = [
    path('', include(router.urls)),
    # path('categories/', CategoryList, name='categories'),
    # path('admin/categories/', CategoryCreate.as_view(), name = "admin-category"),
    # path('categories/<int:pk>/', CategoryDetail, name='single-category'),
    # path('users/', UserList, name='users'),
    # path('users/<int:pk>/', UserDetail, name='single-user'),
    # path('posts/', PostList, name='posts'),
    # path('posts/<int:pk>/', PostDetail, name='single-post'),
]
# urlpatterns = format_suffix_patterns(urlpatterns)