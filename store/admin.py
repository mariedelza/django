from django.contrib import admin
from .models import CreateBlog,Category
from .models import Contact

# Register your models here.


class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'intro', 'slug','date_added', 'auteur', 'date_update')
    
# class CommentAdmin(admin.ModelAdmin):
#     list_display=('body','email','date_added','date_update')
    
    
admin.site.register(CreateBlog, BlogAdmin)
admin.site.register(Category)
# admin.site.register(comment, CommentAdmin)
admin.site.register(Contact)

