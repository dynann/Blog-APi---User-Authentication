from django.contrib.auth import get_user_model
from rest_framework.permissions import IsAdminUser
from rest_framework import viewsets
from .models import Post
from .serializer import PostSerializer, UserSerializer
from .permissions import IsAuthorOrReadOnly
# Create your views here.

class PostViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthorOrReadOnly, )
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    
class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminUser, ]
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer