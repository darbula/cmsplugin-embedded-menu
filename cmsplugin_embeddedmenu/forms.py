from django.forms import ModelForm
from django.utils.safestring import SafeText
from cms.models.pagemodel import Page
from .models import (
    MenuPluginSettings,
)


class EmbedPagesAdminForm(ModelForm):

    class Meta:
        model = MenuPluginSettings
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(EmbedPagesAdminForm, self).__init__(*args, **kwargs)
        choices = [self.fields['root'].choices.__iter__().next()]
        for page in Page.objects.public():
            choices.append((
                page.id,
                SafeText(''.join([
                    u"&nbsp;"*len(page.node.path),
                    page.__unicode__()
                ]))
            ))

        self.fields['root'].choices = choices
