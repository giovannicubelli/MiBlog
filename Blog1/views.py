from django.shortcuts import render, redirect, get_object_or_404
from .models import Autor, Categoria, Post
from .forms import AutorForm, CategoriaForm, PostForm, BusquedaPostForm

def home(request): 
    posts = Post.objects.all().order_by('-fecha_publicacion')
    busqueda_form = BusquedaPostForm()
    return render(request, 'Blog1/home.html', {'posts': posts, 'busqueda_form': busqueda_form})

def crear_autor(request): 
    if request.method == 'POST':
        form = AutorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Blog1:home') # Redirige usando el namespace de la app
    else:
        form = AutorForm()
    return render(request, 'Blog1/crear_autor.html', {'form': form})

def lista_autores(request):
    autores = Autor.objects.all()
    return render(request, 'Blog1/autores_list.html', {'autores': autores})

def detalle_autor(request, pk):
    autor = get_object_or_404(Autor, pk=pk)
    return render(request, 'Blog1/autor_detail.html', {'autor': autor})

def lista_categorias(request):
    categorias = Categoria.objects.all()
    return render(request, 'Blog1/categorias_list.html', {'categorias': categorias})

def crear_categoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog:home') # Redirige a home o a una lista de categorías
    else:
        form = CategoriaForm()
    return render(request, 'blog/crear_categoria.html', {'form': form})

def crear_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST) # , request.FILES si usas ImageField
        if form.is_valid():
            form.save()
            return redirect('blog:home')
    else:
        form = PostForm()
    return render(request, 'blog/crear_post.html', {'form': form})

def buscar_posts(request):
    posts_encontrados = []
    busqueda_form = BusquedaPostForm(request.GET or None) # Muestra el formulario incluso si no hay GET

    if request.GET and busqueda_form.is_valid():
        termino = busqueda_form.cleaned_data.get('termino_busqueda')
        if termino:
            posts_encontrados = Post.objects.filter(titulo__icontains=termino)

    return render(request, 'blog/resultados_busqueda.html', {
        'busqueda_form': busqueda_form,
        'posts_encontrados': posts_encontrados
    })

def detalle_post(request, pk): # Opcional: Para ver un post individual
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/detalle_post.html', {'post': post})