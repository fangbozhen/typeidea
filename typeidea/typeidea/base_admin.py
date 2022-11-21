from django.contrib import admin


class BaseOwnerAdmin(object):

    exclude = ('owner', )

    def get_queryset(self, request):
        request = self.request
        qs = super().get_list_queryset()
        return qs.filter(owner=request.user)

    def save_model(self, request, obj, form, change):
        self.new_obj.owner = self.request.user
        return super().save_models()
