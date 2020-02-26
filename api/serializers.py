from rest_framework import serializers
from items.models import Item , FavoriteItem
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User

        fields = ['first_name','last_name']

class ItemListSerializer(serializers.ModelSerializer):
    favourited = serializers.SerializerMethodField()
    added_by = UserSerializer()
    detail = serializers.HyperlinkedIdentityField(
        view_name = "api-detail",
        lookup_field = "id",
        lookup_url_kwarg = "item_id"
        )
    class Meta:
        model = Item
        fields = ['name','description','favourited' , 'added_by','detail']

    def get_favourited(self,obj):
        return FavoriteItem.objects.filter(item=obj).count()

class ItemDetailSerializer(serializers.ModelSerializer):
    favourited_by = serializers.SerializerMethodField()
    class Meta:
        model = Item
        fields = ['name','description','favourited_by']

    def get_favourited_by(self , obj):
        favorite= FavoriteItem.objects.filter(item = obj)
        return FavoriteSerializer(favorite,many = True).data

class FavoriteSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        fields = ['user']


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ['username', 'password', 'first_name', 'last_name']

    def create(self, validated_data):
        username = validated_data['username']
        password = validated_data['password']
        first_name = validated_data['first_name']
        last_name = validated_data['last_name']
        new_user = User(username=username, first_name=first_name, last_name=last_name)
        new_user.set_password(password)
        new_user.save()
        return validated_data
