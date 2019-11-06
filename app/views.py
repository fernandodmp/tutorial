from django.http import HttpResponse

# Create your views here.
def view(request):
    html = "<h1> Hello World! </h1>"
    return HttpResponse(html)


def view_app(request):
    html = "<h1> Hello World! da Rota do App </h1>"
    return HttpResponse(html)

from app.models import Usuario
def lista_usuarios(request):
    users = Usuario.objects.all()
    user_list = "<ul>"

    for user in users:
        user_list += "<li> {} </li>".format(str(user))

    user_list += "</ul>"
    return HttpResponse(user_list)


from django.shortcuts import render
def lista_usuarios_v2(request):
    users = Usuario.objects.all()
    context_dict = {'user_list': users}
    return render(request, 'app/user_list.html', context_dict)

from app.forms import MessageForm
def message(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            return HttpResponse("<p> Sua Mensagem foi: {} </p>".
            format(form.cleaned_data['mensagem'])) 
    else:
        form = MessageForm()
        ctx = {'form':form}
        return render(request, 'app/message_form.html', context = ctx)


from app.forms import UsuarioForm
from django.shortcuts import redirect
def cria_usuario(request):
    if request.method == 'POST':
        novo_usuario = UsuarioForm(request.POST)
        if novo_usuario.is_valid():
            novo_usuario.save()
            return redirect(lista_usuarios_v2)
    else:
        form = UsuarioForm()
        ctx = {'form':form}
        return render(request, 'app/user_form.html', context = ctx)
