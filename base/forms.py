from django.forms import ModelForm
from .models import Room

class RoomForm(ModelForm):
    print(Room,'000---0000')
    class Meta:
        model = Room
        fields = '__all__'
        # exclude = ['host', 'participants']

