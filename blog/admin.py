from django.contrib import admin
from blog.models import Categorie, Tag, Article, Commentaire, Like
from blog.form import ArticleForm


class CategorieAdmin(admin.ModelAdmin):
    list_display = ('nom', 'statut', 'created_at', 'last_updated_at')
    list_display_links = ['nom']
    list_filter = ('statut',)
    search_fields = ('nom',)
    date_hierarchy = 'created_at'
    ordering = ['nom']
    list_per_page = 10

    fieldsets = [
        (
            'Infos',
            {
                'fields': ['nom', 'description'],
            },
        ),
        (
            'Standards',
            {
                'fields': ['statut', ]
            }
        ),
    ]

    actions = ('active', 'desactive')

    def active(self, request, queryset):
        queryset.update(statut=True)
        self.message_user(request, 'La sélection a été activée avec succès')

    active.short_description = 'Activer'

    def desactive(self, request, queryset):
        queryset.update(statut=False)
        self.message_user(request, 'La sélection a été désactivée avec succès')

    desactive.short_description = 'Désactiver'


class TagAdmin(admin.ModelAdmin):
    list_display = ['nom', 'statut', 'created_at', 'last_updated_at']
    list_display_links = ['nom']
    list_filter = ('statut',)
    search_fields = ('nom',)
    date_hierarchy = 'created_at'
    ordering = ['nom']
    list_per_page = 10

    fieldsets = [
        (
            'Infos',
            {
                'fields': ['nom'],
            },
        ),
        (
            'Standards',
            {
                'fields': ['statut', ]
            }
        ),
    ]

    actions = ('active', 'desactive')

    def active(self, request, queryset):
        queryset.update(statut=True)
        self.message_user(request, 'La sélection a été activée avec succès')

    active.short_description = 'Activer'

    def desactive(self, request, queryset):
        queryset.update(statut=False)
        self.message_user(request, 'La sélection a été désactivée avec succès')

    desactive.short_description = 'Désactiver'


class ArticleAdmin(admin.ModelAdmin):
    form = ArticleForm
    list_display = ['titre', 'resume', 'statut', 'date_de_publicatio', 'created_at', 'last_updated_at', 'nombre_likes', 'est_publie']
    list_display_links = ['titre']
    list_filter = ('statut',)
    search_fields = ('titre',)
    date_hierarchy = 'created_at'
    ordering = ['titre']
    list_per_page = 10

    fieldsets = [
        (
            'Infos',
            {
                'fields': ['titre', 'resume', 'contenu', 'couverture', 'est_publie'],
            },
        ),
        (
            'Organisation',
            {
                'fields': ['auteur_id', 'categorie_id', 'tag_ids']
            }
        ),
        (
            'Standards',
            {
                'fields': ['statut', ]
            }
        ),
    ]

    readonly_fields = ['nombre_likes']  # Rendre ce champ non modifiable

    def nombre_likes(self, obj):
        return obj.likes.count()  # Compte les likes liés à cet article

    nombre_likes.short_description = "Nombre de Likes"  # Label affiché dans l'admin


class CommentaireAdmin(admin.ModelAdmin):
    list_display = ['auteur_id', 'contenu', 'created_at', 'last_updated_at']
    list_display_links = ['auteur_id']
    list_filter = ('statut', 'article_id')
    date_hierarchy = 'created_at'
    ordering = ['-created_at']
    list_per_page = 10

    fieldsets = [
        (
            'Infos',
            {
                'fields': ['auteur_id', 'article_id', 'contenu'],
            },
        ),
        (
            'Standards',
            {
                'fields': ['statut', ]
            }
        ),
    ]


# Enregistrement des modèles
admin.site.register(Categorie, CategorieAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Commentaire, CommentaireAdmin)