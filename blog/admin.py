from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.text import Truncator
from .models import CustomUser, Article


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('apercu_title', 'apercu_content', 'pub_date', 'state')
    list_filter = ('title', 'content',)
    prepopulated_fields = {'slug': ('title', )}

    fieldsets = (
        # FieldSet 1 : meta-info (titre, auteur…)
        ('General', {
            'classes': ['collapse', ],
            'fields': ('title', 'slug')
        }),
        # FieldSet 2 : content of the article
        ('Content of the article', {
            'description': 'The article is a step to our big dream',
            'fields': ('content',)
        }),
    )

    def apercu_content(self, article):
        return Truncator(article.content).chars(40, truncate='...')

    def apercu_title(self, article):
        return Truncator(article.title).chars(30, truncate='...')

    apercu_content.short_description = "Aperçu du contenu"


admin.site.register(Article, ArticleAdmin)
admin.site.register(CustomUser, UserAdmin)
