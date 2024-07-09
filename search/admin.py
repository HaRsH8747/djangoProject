from django.contrib import admin

from search.models import SearchHistory


class SearchHistoryAdmin(admin.ModelAdmin):
    list_display = ('user', 'query', 'timestamp')
    search_fields = ('user__username', 'query')


admin.site.register(SearchHistory, SearchHistoryAdmin)
