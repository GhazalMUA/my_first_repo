from django.contrib import admin
from .models import Article, Category, RegisteringModel

class CategoryAdmin(admin.ModelAdmin):
    list_display=('position', 'slug' , 'status')
    list_filter=('status',)
    search_fields=('title', 'slug')
    prepopulated_fields={'slug':('title',)}
admin.site.register(Category, CategoryAdmin)


class ArticleAdmin(admin.ModelAdmin):
    list_display=('slug' , 'jpublish' , 'status' )# 'category_to_str')
    list_filter=('publish' , 'status')
    search_fields=('title', 'description')
    prepopulated_fields={'slug':('title',)}
    ordering=['-status' , '-publish']
   
#    def category_to_str(self,obj):
#        return ",".join([category.title for category in obj.category.all()])
#    category_to_str.short_description='دسته بندی'
    
admin.site.register(Article, ArticleAdmin)




class RegisteringAdmin(admin.ModelAdmin):
    list_display=('first_name','last_name','birth_date','phone_number','email_address','address')
    search_fields=('first_name','last_name')

admin.site.register(RegisteringModel, RegisteringAdmin)    
    