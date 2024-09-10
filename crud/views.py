from rest_framework import viewsets
from .models import Artist
from rest_framework.pagination import LimitOffsetPagination
from .const import *
from .serialiser import ArtistSerializer
from rest_framework.response import Response
from rest_framework.throttling import UserRateThrottle

class CustomPagination(LimitOffsetPagination):
    default_limit = PAGINATION_DEFAULT_LIMIT
    limit_query_param = PAGINATION_LIMIT_QUERY_PARAM
    offset_query_param = PAGINATION_OFFSET_QUERY_PARAM

class ArtistViewSet(viewsets.ModelViewSet):
    throttle_classes = [UserRateThrottle]
    throttle_scope = 'artists'
    pagination_class = CustomPagination
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer

    def destroy(self, request, *args, **kwargs):
        super().destroy(request, *args, **kwargs)
        return Response(status=200, data={'message': 'Artist deleted successfully.'})