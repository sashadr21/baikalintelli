from rest_framework import serializers
from .models import *

class DataSienceCollectionSerializer(serializers.ModelSerializer):

    class Meta:
        model = DataSienceCollection
        fields = '__all__'
        extra_kwargs = {'user': {'required': False}}


class LocalSienceThemeSerializer(serializers.ModelSerializer):

    class Meta:
        model = LocalSienceTheme
        fields = '__all__'
        extra_kwargs = {'user': {'required': False}}



class SchemaTableSectionSerializer(serializers.ModelSerializer):

    class Meta:
        model = SchemaTableSection
        fields = '__all__'
        extra_kwargs = {'user': {'required': False}}



class JSONCollectionSerializer(serializers.ModelSerializer):

    class Meta:
        model = JSONCollection
        fields = '__all__'
        extra_kwargs = {'user': {'required': False}}