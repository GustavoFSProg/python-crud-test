from django.shortcuts import render
from django.http import HttpResponse
from .models import Usuarios

def ver_cadastro(request):
   if request.method == "GET":
       
        return render(request, './usuarios/cadastro.html')
   

def ver_usuario(request):
         
        usuarios={'usuarios': Usuarios.objects.all()}

        return render(request, './usuarios/ver_usuarios.html', usuarios )

#        return  HttpResponse(usuarios)

       
    

def ver_home(request):
   if request.method == "GET":
        return render(request, './usuarios/home.html')
   

def listagem(request):
   if request.method == "GET":
        return render(request, './usuarios/ver_usuarios.html')
   


        # if request.method == "POST":
def usuarios(request):
          nome = request.POST.get('nome')
          idade = request.POST.get('idade')
          Pessoa = Usuarios(nome=nome, idade=idade)
          Pessoa.save()
          pessoas = Usuarios.objects.all()
          return HttpResponse(pessoas)

        #   return HttpResponse("deu")


#        return  HttpResponse("DEU")
#        return render(request, './usuarios/usuarios.html', usuarios )
#        usuarios={
#          }
#        usuarios = Usuarios.objects.all()

#        return  HttpResponse(usuarios)

  

   
    


