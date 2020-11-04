from django.contrib import admin
from web.models import Person, Category, Quote





class QuoteAdmin(admin.ModelAdmin):
    list_display = ['content', 'person', 'display_category']
    Quote.display_category.short_description = 'Categories'


# Register Quote model
admin.site.register(Quote, QuoteAdmin)
admin.site.register(Person)
admin.site.register(Category)