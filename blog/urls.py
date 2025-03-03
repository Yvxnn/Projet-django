from django.urls import path,include
from blog import views
from django.conf import settings
from django.conf.urls.static import static

app_name="blog"

urlpatterns = [
    path("", views.index, name="index"),
    path("Contact/", views.contact, name="contact"),
    path("About/", views.about, name="about"),
    path("Blog/<slug:slug>/", views.blog_single, name="article"),
    path("Blog/<slug:slug>/delete/<int:id>", views.commentaire_delete, name="delete_comment"),
    path("Blog/<slug:slug>/update/<int:id>", views.commentaire_update, name="update_comment"),
    path("Blog/", views.blog, name="blog"),
    path("Dashboard/", views.darshbord, name="board"),
    path("Dashboard/ajout", views.ajout_article, name='add'),
    path("Dashboard/edit/<slug:slug>/", views.update_article, name="edit"),
    path("Dashboard/delete/<slug:slug>/", views.delete_article, name="delete"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
