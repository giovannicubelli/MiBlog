from django import forms
from .models import Autor, Categoria, Post

class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = '__all__'

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = '__all__'

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'

class BusquedaPostForm(forms.Form):
    termino_busqueda = forms.CharField(label='Buscar', max_length=100, required=False)
    
class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = ['nombre', 'email', 'bio']

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nombre']

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['titulo', 'contenido', 'autor', 'categoria'] # Asegúrate que autor y categoria existan
        widgets = {
            'fecha_publicacion': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }
        # Si quieres que fecha_publicacion no sea editable, puedes excluirlo o hacerlo readonly.
        # Por ahora lo dejamos así, pero se autocompleta en el modelo.

class BusquedaPostForm(forms.Form):
    termino_busqueda = forms.CharField(label="Buscar Posts por Título", max_length=100)