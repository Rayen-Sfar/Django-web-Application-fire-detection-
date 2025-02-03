from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from superviseur.models.supervisor import Supervisor
from .forms import SupervisorLoginForm,ClientLoginForm
from django.contrib.auth.hashers import check_password
from client.models                  import Client
import logging
# Initialisation du logger pour enregistrer les messages de log
logger = logging.getLogger(__name__)

def client_login(request):
    if request.method == 'POST':
        form_client = ClientLoginForm(request.POST)
        if form_client.is_valid():
             # Récupération de l'email et mot de passe depuis les données nettoyées du formulaire
            email = form_client.cleaned_data['email']
            password = form_client.cleaned_data['password']
            try:
                # Récupération de la classe Client correspondant à l'email
                client = Client.objects.get(email=email)
                # Vérification si le mot de passe fourni correspond au mot de passe stocké
                if check_password(password, client.password):
                    # Connexion de l'utilisateur
                    login(request, client.user)
                     # Mise à jour de la session
                    request.session['client_authenticated'] = True
                    request.session['supervisor_authenticated'] = False
                     # Récupération de l'URL de redirection
                    next_url = request.POST.get('next', 'select_project_of_project')
                    return redirect(next_url)
                else:
                    # Ajout d'une erreur au formulaire si l'email ou le mot de passe est invalide
                    form_client.add_error(None, "Invalid email or password!!!")
            except Client.DoesNotExist:
                # Ajout d'une erreur au formulaire si le client n'existe pas
                form_client.add_error(None, "Invalid email or password!!!")
         # Rendu du formulaire avec les erreurs si le formulaire n'est pas valide
        return render(request, 'pages/client.html', {'form_client': form_client})
    # Si la méthode de requête n'est pas POST, instanciation d'un formulaire vide
    form_client = ClientLoginForm()
    return render(request, 'pages/client.html', {'form_client': form_client})


# Définition de la vue pour la connexion des superviseurs
def supervisor_login(request):
    # Vérification si la méthode de requête est POST
    if request.method == 'POST':
    # Instanciation du formulaire avec les données POST
        form = SupervisorLoginForm(request.POST)
        # Vérification si le formulaire est valide
        if form.is_valid():
# Récupération de l'email depuis les données nettoyées du formulaire
            email = form.cleaned_data['email']   
# Récupération de l'objet Supervisor correspondant à l'email       
            supervisor = Supervisor.objects.get(email=email)     
 # Connexion de l'utilisateur associé au superviseur     
            login(request, supervisor.user) 
            # Mise à jour de la session pour indiquer que le superviseur est authentifié
            request.session['supervisor_authenticated'] = True
            #request.session['client_authenticated'] = False
            next_url = request.POST.get('next', 'dashboard_super')
            return redirect(next_url) # Redirection vers l'URL suivante
        # Rendu du formulaire avec les erreurs si le formulaire n'est pas valide
        return render(request, 'pages/supervisor.html', {'form': form})
    # Si la méthode de requête n'est pas POST, instanciation d'un formulaire vide
    form = SupervisorLoginForm()
    # Rendu de la page de connexion du superviseur avec le formulaire vide
    return render(request, 'pages/supervisor.html', {'form': form})

def sign_out(request):
    # Vérification si le superviseur est authentifié dans la session
    if request.session.get('supervisor_authenticated'): 
        request.session.flush() # Vidage de toutes les données de session
        logout(request)# Déconnexion de l'utilisateur
# Redirection vers la page de connexion des superviseurs
    return redirect('supervisor_login')

def sign_out_client(request):
    if request.session.get('client_authenticated'):
        request.session.flush()
        logout(request)
    return redirect('client_login')
