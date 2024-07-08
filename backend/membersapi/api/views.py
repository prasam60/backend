from rest_framework import viewsets
from ..models import Member
from .serializers import MemberModelSerializer

class MembersViewSet(viewsets.ModelViewSet):
    queryset = Member.objects.all()
    serializer_class = MemberModelSerializer