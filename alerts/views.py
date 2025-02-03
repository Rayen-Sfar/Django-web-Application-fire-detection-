from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from superviseur.models.project import Project
from superviseur.models.parcelle import Parcelle
from client.models import Client
from .serializers import ParcelleSerializer  # Importez le serializer

@csrf_exempt
def send_alert(request):
    if request.method == 'GET':
        try:
            # Étape 1: Filtrage des projets
            client = Client.objects.get(username="sfrayen")
            projects = Project.objects.filter(client=client, polygon_id=9)

            if not projects.exists():
                return JsonResponse({'error': 'No projects found'}, status=404)

            # Étape 2: Extraire le polygone de la première parcelle associée
            parcell = Parcelle.objects.filter(project=projects.first()).first()

            if not parcell or not parcell.polygon:
                return JsonResponse({'error': 'No polygon found for the project'}, status=404)

            # Utilisation du serializer pour formater les données
            serializer = ParcelleSerializer(parcell)

            # Étape 3: Préparation des données JSON
            alert_data = {
                'parcel_id': parcell.id,  # Utilisez parcell.id pour l'ID de la parcelle
                'message': 'Fire detected in this parcel !!!',
                'coordinates': serializer.data['coordinates']
            }

            return JsonResponse(alert_data, safe=False)

        except Client.DoesNotExist:
            return JsonResponse({'error': 'Client not found'}, status=404)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)