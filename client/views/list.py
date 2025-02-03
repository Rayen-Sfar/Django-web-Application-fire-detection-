import json # Importation du module json pour la manipulation des données JSON
from django.shortcuts                   import render, get_object_or_404
from django.contrib.auth.decorators     import login_required
from authentification.decorators          import client_required
from superviseur.models.data             import Data
from superviseur.models.node             import Node
from superviseur.models.parcelle         import Parcelle
from superviseur.models.project          import Project


@login_required(login_url='client_login')
@client_required
def node_list(request, project_id):
    project = get_object_or_404(Project, polygon_id=project_id, client=request.user.client)
    parcelles = Parcelle.objects.filter(project=project)    # Récupération des parcelles associées au projet
    all_nodes = [] # Initialisation de la liste pour stocker les données de tous les nœuds

    for parcelle in parcelles:
        nodes = Node.objects.filter(parcelle=parcelle)
         # Création d'une liste de dictionnaires contenant les informations des nœuds et leurs dernières données
        node_data = [{
            'id': node.id,
            'name': node.name,
            'latitude': node.position.x,  
            'longitude': node.position.y, 
            'ref': node.reference,
            'last_data': get_last_data(node)
        } for node in nodes]
         # Ajout des données des nœuds à la liste générale
        all_nodes.extend(node_data)

    #* Vérifiez que le JSON est bien formé et non vide
    json_data = json.dumps(all_nodes, default=str)
    if not json_data:
        json_data = '[]'  # Utilisation d'un tableau vide si le JSON est invalide

    # Création du contexte pour le rendu du template
    context = {
        'project': project,
        'nodes': all_nodes,
        'last_data': json_data
    }

    return render(request, 'website/node_list.html', context)


# Fonction pour récupérer les dernières données d'un nœud
def get_last_data(node):
    try:
        # Récupération de la dernière instance de données associée au nœud
        last_data = Data.objects.filter(node=node).latest('published_date')
        # Retour des données de "last_data" formatées sous forme de dictionnaire
        return {
            'temperature': last_data.temperature,
            'humidity': last_data.humidity,
            'rssi': node.RSSI,
            'fwi': node.FWI,
            'prediction_result': node.detection,
            'pressure': last_data.pressur,
            'gaz': last_data.gaz,
            'wind_speed': last_data.wind,
            'rain_volume': last_data.rain,
        }
    except Data.DoesNotExist:
        return {}