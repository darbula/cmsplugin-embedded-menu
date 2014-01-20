from django.utils.translation import ugettext_lazy as _
import re

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from cms.models.pluginmodel import CMSPlugin
from cms.menu_bases import CMSAttachMenu
from menus.base import (
    Menu,
    Modifier,
    NavigationNode
)
from menus.menu_pool import menu_pool
from menus.templatetags.menu_tags import (
    cut_levels,
    cut_after,
    flatten,
)
from .forms import EmbedPagesAdminForm

from .models import (
    ApplicationSettings,
    MenuPluginSettings,
)


class MenuPlugin(CMSPluginBase):
    model = MenuPluginSettings
    name = _("Embedded Menu")
    render_template = "cmsplugin_embeddedmenu/base.html"
    admin_preview = False
    form = EmbedPagesAdminForm

    def render(self, context, instance, placeholder):

        try:
            # If there's an exception (500), default context_processors may not be called.
            request = context['request']
        except KeyError:
            return _("There is no `request` object in the context.")

        root_page = instance.root
        root_page_url = root_page.get_absolute_url()
        from_level = instance.start_level
        to_level = instance.depth

        nodes = menu_pool.get_nodes(request)
        # find the root id and cut the nodes
        root_node = None
        for node in nodes:
            if node.url==root_page_url:
                root_node = node
                break
        if root_node:
            nodes = root_node.children
            for remove_parent in nodes:
                remove_parent.parent = None
            from_level += node.level + 1
            to_level += node.level + 1
            nodes = flatten(nodes)
        else:
            nodes = []

        children = cut_levels(nodes, from_level, to_level, extra_inactive=100, extra_active=100)
        children = menu_pool.apply_modifiers(children, request, post_cut=True)
        
    	if root_node and instance.include_root :
                children = (root_node, )
        context.update({
            'MenuItems': children,
            'template': re.search('(\w*).html', instance.template).groups()[0],
        })
        return context

plugin_pool.register_plugin(MenuPlugin)

