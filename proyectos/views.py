from django.shortcuts import render
from .models import Proyecto
import os
from django.conf import settings

def index(request):
    proyectos = Proyecto.objects.all().order_by('-fecha_creacion')
    
    # Path to hero images folder
    hero_dir = os.path.join(settings.BASE_DIR, 'proyectos', 'static', 'hero_images')
    os.makedirs(hero_dir, exist_ok=True)
    
    valid_extensions = ('.png', '.jpg', '.jpeg', '.gif', '.webp', '.svg')
    hero_images = []
    if os.path.exists(hero_dir):
        hero_images = [f'hero_images/{f}' for f in os.listdir(hero_dir) if f.lower().endswith(valid_extensions)]
    
    hero_images.sort()
    
    context = {
        'proyectos': proyectos,
        'hero_images': hero_images,
    }
    return render(request, 'proyectos/index.html', context)
