from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Person
from .forms import FormPessoa


def index(request):
    return HttpResponse('Django 2.0!')

def listar_pessoas(request):
    pessoa = Person.objects.all()
    return render(request, 'clientes/listar_pessoas.html', {'p1': pessoa})


def  cadastrar_pessoa(request):
    # passar os dados preenchidos no formulário para a variável form
    form = FormPessoa(request.POST or None, request.FILES or None) # Passar todo conteúdo do FormPessoa por meio do método POST
                                                         # Para a variável form. request.FILES quando tem aruivo armazenado, tipo foto
    if form.is_valid(): #Verificar se o preenchimento do formuário é válido para salvar
        form.save()
        return redirect('listar')  # Se salvar no BD, chama o método listar pessoas
    return render(request, 'clientes/nova_pessoa.html', {'novaP': form})  # Se não salvar volta para a mesma página de cadastro

def alterar_pessoa(request, id):

    pessoa = get_object_or_404 (Person, pk=id) #Tenta pegar o objeto no BD, se não existir retorna um 404
    form = FormPessoa (request.POST or None, request.FILES or None, instance = pessoa)

    if form.is_valid():
        form.save()
        return redirect('listar')
    return render(request, 'clientes/nova_pessoa.html', {'novaP': form})



def deletar_pessoa(request, id):
    #pessoa = get_object_or_404(Person, pk=id)
    pessoa = Person.objects.get(pk=id)

    if request.method == 'POST':
        pessoa.delete()
        return redirect('listar')

    return render(request, 'clientes/delete_pessoa.html', {'del': pessoa})

