from django.shortcuts import render, redirect
from .models import Post

def home(request):
    if request.method == "POST":
        content = request.POST.get("content")

        if content:
            Post.objects.create(
                user=request.user,
                content=content
            )

        return redirect("/home/")

    posts = Post.objects.all().order_by("-created_at")

    return render(request, "home.html", {"posts": posts})