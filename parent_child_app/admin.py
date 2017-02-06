from django.contrib import admin
from .models import Parent, Child

class ChildInline(admin.TabularInline):
    model = Child

class ParentInline(admin.ModelAdmin):
    inlines = [
        ChildInline,
    ]

# when you add a parent you can also add
# their children on the same page
admin.site.register(Parent, ParentInline);

# in case we just want to add children
admin.site.register(Child);