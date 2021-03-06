import os
from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _
from cms.models.pluginmodel import CMSPlugin
from appconf import AppConf


# Add additional choices through the ``settings.py``.
def get_templates():
    choices = getattr(
        settings,
        'CMSPLUGIN_EMBEDDED_MENU_STYLE_CHOICES',
        [
            ("cmsplugin_embeddedmenu/layouts/default.html", _('Default')),
        ],
    )
    return choices


class ApplicationSettings(AppConf):
    TEMPLATE_PATH = os.path.join("cmsplugin_embeddedmenu", "layouts")


class MenuPluginSettings(CMSPlugin):
    """
    Stores options for cmsplugin that Embeds a menu.
    """
    menu_title = models.CharField(
        _("Menu Title"),
        blank=True,
        null=True,
        max_length=256,
        help_text=_("Title of the menu")
    )
    sub_title = models.CharField(
        _("Sub Title"),
        blank=True,
        null=True,
        max_length=256,
        help_text=_("Sub Title of the menu")
    )
    description = models.TextField(
        _("Description"),
        blank=True,
        null=True,
        help_text=_("Description for the menu")
    )
    template = models.CharField(
        _("Plugin Template"),
        choices=get_templates(),
        default=get_templates()[0][0],
        max_length=256,
        help_text=_("Use this template to render the menu.")
    )
    root = models.ForeignKey(
        "cms.Page",
        default=1,
        help_text=_("Menu tree starts from this page.")
    )
    include_root = models.BooleanField(
        _("Include Root"),
        default=False,
        help_text=_("Shall the menu also include the root menu item specified?")
    )
    start_level = models.IntegerField(
        _("Start Level"),
        default=0,
        help_text=_("Should the root page also be included in the output?")
    )
    show_depth = models.IntegerField(
        _("Depth"),
        default=0,
        help_text=_("How many levels deep to look for menu items to show?")
    )

    def __unicode__(self):
        return u'%s' % self.menu_title
