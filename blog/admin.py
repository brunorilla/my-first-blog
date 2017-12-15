from django.contrib import admin
from .models import Post
from .models import Categoria
from .models import Book

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


class BookAdmin(admin.ModelAdmin):
	list_display = ["__str__","titulo"]
	class Meta:
		model = Book

admin.site.register(Post,PostAdmin)
admin.site.register(Categoria,CategoriaAdmin)
admin.site.register(Book,BookAdmin)