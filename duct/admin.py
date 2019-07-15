from django.contrib import admin
from duct.models import User
# Register your models here.


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'name')
    # raw_id_fields = ('reserve', 'user',)
    # search_fields = (
    #     'currency__code', 'address'
    # )
    # autocomplete_fields = ('currency', 'user')