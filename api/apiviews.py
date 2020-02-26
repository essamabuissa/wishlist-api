from django.shortcuts import render
from rest_framework.filters import SearchFilter
from items.models import Item
from .serializers import ItemListSerializer , ItemDetailSerializer ,RegisterSerializer
from rest_framework.generics import ListAPIView , RetrieveAPIView ,CreateAPIView
from rest_framework.filters import OrderingFilter
from rest_framework.permissions import AllowAny
from .permissions import StaffOrUser


class ItemListView(ListAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemListSerializer
    filter_backends = [SearchFilter,OrderingFilter]
    search_fields = ['name', 'description',]
    permission_classes = [AllowAny]


class ItemDetailView(RetrieveAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemDetailSerializer
    lookup_field = "id"
    lookup_url_kwarg = "item_id"
    permission_classes = [StaffOrUser]

class Register(CreateAPIView):
    serializer_class = RegisterSerializer
