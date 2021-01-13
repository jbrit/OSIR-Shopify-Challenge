from django.forms import ModelForm
from core.models import ImageItem

class ImageForm(ModelForm):
    class Meta:
        model = ImageItem
        fields = ['name','description','image','public']