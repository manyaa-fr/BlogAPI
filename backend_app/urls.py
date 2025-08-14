from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse

# Root endpoint for health check / portfolio showcase
def home(request):
    return JsonResponse({
        "status": "success",
        "message": "Blog API is running successfully 🚀",
        "endpoints": {
            "Posts list": "/api/posts/",
            "Post detail": "/api/posts/<id>/",
            "Create post": "/api/posts/create/",
            "Update post": "/api/posts/<id>/update/",
            "Delete post": "/api/posts/<id>/delete/"
        }
    })

urlpatterns = [
    path("", home, name="home"),              # Fixes the 502 at root
    path("admin/", admin.site.urls),
    path("api/posts/", include("posts.urls")) # Include your posts app routes
]
