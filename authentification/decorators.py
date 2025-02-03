# authentication/decorators.py
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.decorators     import login_required

# Définition d'une fonction de décorateur client_required
def client_required(view_func):
    # Application des décorateurs login_required et user_passes_test à view_func
    decorated_view_func = login_required(user_passes_test(
        # Vérifie si l'utilisateur est authentifié et possède l'attribut 'client'

        lambda u: u.is_authenticated and hasattr(u, 'client'),
        login_url='client_login'
    )(view_func))
        # Retourne la vue décorée

    return decorated_view_func

# Définition d'une fonction de décorateur supervisor_required

def supervisor_required(view_func):
        # Application des décorateurs login_required et user_passes_test à view_func

    decorated_view_func = login_required(user_passes_test(
        # Vérifie si l'utilisateur est authentifié et possède l'attribut 'supervisor'

        lambda u: u.is_authenticated and hasattr(u, 'supervisor'),
        # URL de redirection si l'utilisateur n'est pas authentifié ou ne possède pas l'attribut 'supervisor'

        login_url='supervisor_login'
    )(view_func))
    return decorated_view_func
