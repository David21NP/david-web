from django.views.generic import DetailView, ListView

from .models import Post


class PostList(ListView):
    queryset = Post.objects.filter(status=1).order_by("-created_on")
    template_name = "blog/index.html"


class PostDetail(DetailView):
    model = Post
    template_name = "blog/post_detail.html"
