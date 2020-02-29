from rest_framework.viewsets import ModelViewSet


from account.models import User
from account.serializers import UserSerializer

# Create your views here.


class UserViewSet(ModelViewSet):
    http_method_names = ('post',)
    queryset = User.objects.all()
    serializer_class = UserSerializer
