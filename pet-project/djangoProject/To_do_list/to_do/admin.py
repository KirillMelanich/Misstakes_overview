from django.contrib import admin


from to_do.models import Tag, Task


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ["tag"]
    list_filter = ["tag"]
    search_fields = ["tag"]


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ["content", "datetime", "deadline", "done"]
    list_filter = ["tag"]
    search_fields = ["tag"]
