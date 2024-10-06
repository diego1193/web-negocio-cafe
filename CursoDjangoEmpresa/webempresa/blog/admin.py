from django.contrib import admin
from .models import Category, Post

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ("created", "updated")


class PostAdmin(admin.ModelAdmin):
    readonly_fields = ("created", "updated")
    list_display = ("title", "author", "published", "post_categories")
    ordering = ("author", "published") # Primero se ordena por author y luego por la fecha de publicacion
    search_fields = (
        "title", 
        "content", 
        "author__username", 
        "categories__name"
        ) # especificar que campo vamos a buscar si es una relacion
    date_hierarchy = "published" # Buscar por fecha encima del filtro
    list_filter = ('author__username',"categories__name") # Filtrar por relaciones es mucho mejor

    # Crear nuestro propios campos
    def post_categories(self, obj): # El objeto de cada fila
        return ", ".join([c.name for c in obj.categories.all().order_by("name")])
    
    post_categories.short_description = "Categorías"
        

admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
