from django.forms import ModelForm

from .models import NomeraUroka
from .models import NomeraKlassa
from .models import Predmety
from .models import Prepodavately
from .models import Uroki, NomeraUroka, NomeraKlassa, Predmety, Prepodavately

class UrokiForm(ModelForm):
    class Meta:
        model = Uroki
        fields = ['date_field', 'nomer_uroka', 'nomer_klassa', 'vremya_nachala_uroka', 'nazvanie_predmeta', 'prepodavatel', 'tema_uroka', 'ssylka_na_urok', 'kommentaryi']

