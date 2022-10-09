from django.forms import ModelForm
from . models import Trainingvalue, Word

class WordForm(ModelForm):
    class Meta:
        model = Word
        fields ='__all__'


class TrainingForm(ModelForm):
    class Meta:
        model = Trainingvalue
        fields ='__all__'
      