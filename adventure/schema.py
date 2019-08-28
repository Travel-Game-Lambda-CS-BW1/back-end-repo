from django.conf import settings
from graphene_django import DjangoObjectType
import graphene
from .models import Room

class RoomType(DjangoObjectType):

    class Meta:
        model = Room
        interfaces = (graphene.relay.Node, )

class Query(graphene.ObjectType):

    rooms = graphene.List(RoomType)

    def resolve_rooms(self, info):
        return Room.objects.all()

schema = graphene.Schema(query=Query)