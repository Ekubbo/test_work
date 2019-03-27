from django.contrib import admin
from .models import Account, Transaction
from django.contrib import auth
from .forms import TransactionForm


class AccountAdmin(admin.ModelAdmin):
    model = Account
    list_display = ('last_name', 'first_name', 'phone', 'cart_number', 'balance', )
    search_fields = ('cart_number', 'last_name', 'phone', )
    ignore_delete_permission = {'transaction'}

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return self.readonly_fields + ('cart_number', 'balance')
        return self.readonly_fields

    def get_deleted_objects(self,  objs, request):
        to_delete, model_count, perms_needed, protected = super(AccountAdmin, self).get_deleted_objects(objs, request)
        perms_needed -= self.ignore_delete_permission
        return to_delete, model_count, perms_needed, protected

    def has_delete_permission(self, request, obj=None):
        return True


class TransactionAdmin(admin.ModelAdmin):
    models = Transaction
    form = TransactionForm
    list_display = ('account', 'amount', 'transaction_type', 'date', )
    list_filter = ['transaction_type', 'date', ]
    readonly_fields = ("date", )
    autocomplete_fields = ['account']

    def has_delete_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False


admin.site.register(Account, AccountAdmin)
admin.site.register(Transaction, TransactionAdmin)
admin.site.unregister(auth.models.User)
admin.site.unregister(auth.models.Group)
admin.site.site_header = "Administration"
