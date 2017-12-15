from django.contrib import admin
from .models import Post
from .models import Categoria

class PostAdmin(admin.ModelAdmin):
	list_display = ["__str__","author","published_date","created_date"]
	list_filter = ["title","created_date"]
	search_fields = ["title"]
	class Meta:
		model = Post

class CategoriaAdmin(admin.ModelAdmin):
	list_display = ["__str__","color"]
	class Meta:
		model = Categoria

admin.site.register(Post,PostAdmin)
admin.site.register(Categoria,CategoriaAdmin)