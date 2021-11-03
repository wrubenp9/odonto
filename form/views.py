from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.contrib import messages

from .models import Anamnese as AnamneseModel
from .forms import AnamneseForm


User = get_user_model()

#exibir os dados do banco
@login_required
def anamnese(request):
    template_name = 'anamnese.html'
    question = AnamneseModel.objects.all()
    context = {
        'question': question
    }
    return render(request, template_name, context)

#adicionar dados logo de inicio
@login_required
def anamnese_new(request):
    template_name = 'anamnese.html'
    form = AnamneseForm(request.POST or None)
    
    if form.is_valid():
        form.save()
        
        return redirect('home')
        
    else:
        context = {
            'form': form
        }
        return render(request, template_name, context)
    



@login_required
def anamnese_edit(request, id):
    template_name = 'anamnese-edit.html'
    question = get_object_or_404(AnamneseModel, pk=id)
    form = AnamneseForm(instance=question)

    if(request.method == 'POST'):
        if form.is_valid():
            form = AnamneseForm(request.POST, instance=question)
            # user.gestante = form.cleaned_data['gestante']
            # user.hemorragia = form.cleaned_data['hemorragia']
            # user.pressao = form.cleaned_data['pressao']
            # user.alergia = form.cleaned_data['alergia']
            # user.doenca_sistemica = form.cleaned_data['doenca_sistemica']
            # user.medicamento = form.cleaned_data['medicamento']

            question.save()
            return redirect('/')
        else:
            context = {
                'form':form,
            }