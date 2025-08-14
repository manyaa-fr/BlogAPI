from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse

# Root endpoint so "/" doesn't 404
def home(request):
    return JsonResponse({
        "status": "success",
        "message": "Blog API is running 🚀",
        "docs": "List of API endpoints",
        "endpoints": {
            "Posts list": "/api/posts/",
            "Post detail": "/api/posts/<id>/",
            "Create post": "/api/posts/create/",
            "Update post": "/api/posts/<id>/update/",
            "Delete post": "/api/posts/<id>/delete/"
        }
    })

urlpatterns = [
    path("", home, name="home"),       # 👈 This fixes the 404 at root
    path("admin/", admin.site.urls),
    path("api/", include("posts.urls")),
    path("api/token/", include("token_auth.urls")),  # if you have JWT token auth
]
