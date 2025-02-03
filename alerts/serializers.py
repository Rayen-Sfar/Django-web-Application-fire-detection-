from rest_framework import serializers
from superviseur.models.parcelle import Parcelle

class ParcelleSerializer(serializers.ModelSerializer):
    coordinates = serializers.SerializerMethodField()

    class Meta:
        model = Parcelle
        fields = ['id', 'polygon', 'coordinates']

    def get_coordinates(self, obj):
        # Extraire les coordonnées du polygone
        geometry = obj.polygon
        coordinates = geometry.coords[0]  # Assurez-vous de l'ordre des coordonnées
        
        # Formatage des coordonnées
        return [{'latitude': coord[0], 'longitude': coord[1]} for coord in coordinates]