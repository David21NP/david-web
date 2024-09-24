from django.contrib import admin

from .models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "slug", "tag_list", "status", "created_on")
    list_filter = ("status",)
    search_fields = ["title", "content"]
    prepopulated_fields = {"slug": ("title",)}

    @admin.display(description="Tags")
    def tag_list(self, obj):
        return "\n".join(obj.tags.split(","))


admin.site.register(Post, PostAdmin)
