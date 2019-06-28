from django.forms import ModelForm
from .models import Person

class FormPessoa(ModelForm):
    class Meta:
        model = Person
        fields = ( 'primeiro_nome',
                  'sobrenome',
                  'idade',
                  'salario',
                  'bio',
                  'photo' )