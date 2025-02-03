# myapp/urls.py
from django.urls import path
from .views import index,clients,project

urlpatterns = [
    path('', index.indexS, name='dashboard_super'),

    #######* CRUD OF CLIENT  ##########
    path('list_client/', clients.list_clients, name="list_client"),
    path('add_client/', clients.add_client, name="add_client"),
    path('update_client/<int:pk>/', clients.update_client, name="update_client"),
    path('delete_client/<int:pk>/', clients.delete_client, name="delete_client"),

    #######* CRUD OF Project  ##########
    path('project_list/', project.list_project, name='list_project'),
    path('add_project/', project.add_project, name= 'add_project'),
    path('update_project/<int:project_id>', project.update_project, name='update_project'),
    path('delete_project/<int:pk>', project.delete_project, name='delete_project'),
    path('add_parcelle/', project.parcelle_create, name = 'add_parcelle'),
    path('get_parcelles_for_project/', project.get_parcelles_for_project, name='get_parcelles_for_project'),


    #######* Node Related  ##########
    path('add_node/', project.node_create, name='add_node'),
    path('get_parcelles_with_nodes_for_project/', project.get_parcelles_with_nodes_for_project, name='get_parcelles_with_nodes_for_project'),
    path('get_project_details/<int:project_id>/', project.get_project_details, name='get_project_details'),
    path('update_parcels_nodes/', project.update_parcels_nodes, name='update_parcels_nodes'),
]
