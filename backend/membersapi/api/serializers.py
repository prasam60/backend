from rest_framework import serializers
from ..models import Member

class MemberModelSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()
    def get_name(self, member):
        return member.__str__()
    class Meta:
        model = Member
        fields = ('id', 'first_name', 'last_name', 'email', 'phone', 'is_admin', 'name')