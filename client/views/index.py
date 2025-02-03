from django.shortcuts                   import render, get_object_or_404
from django.contrib.auth.decorators     import login_required
from authentification.decorators          import client_required
from superviseur.models.project          import Project



@login_required(login_url='client_login')
@client_required
def index1(request, project_id):
    project = get_object_or_404(Project, polygon_id=project_id, client=request.user.client)
    return render(request, 'website/index1.html', {'project': project})