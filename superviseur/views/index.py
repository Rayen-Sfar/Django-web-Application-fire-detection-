from django.shortcuts               import render

from django.contrib.auth.decorators import login_required

from authentification.decorators      import supervisor_required


@login_required(login_url='supervisor_login')

@supervisor_required
def indexS(request):
    return render(request, 'pages/index.html')