from django.forms import ModelForm
from .models import Foo


class FooForm(ModelForm):
    class Meta:
        model = Foo
        fields = ['name', 'description']
