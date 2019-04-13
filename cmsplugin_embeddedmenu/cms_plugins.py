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
    text_enabled = True

    def render(self, context, instance, placeholder):

        try:
            # If there's an exception (500), default context_processors may not be called.
            request = context['request']
        except KeyError:
            return _("There is no `request` object in the context.")

        root_page = instance.root
        from_level = instance.start_level
        to_level = instance.show_depth

        renderer = menu_pool.get_renderer(request)
        nodes = renderer.get_nodes(
            namespace=None,
            root_id=None,
            breadcrumb=False,
        )
        root_node = None
        for node in nodes:
            if not node.attr["is_page"]:
                continue
            if node.id == root_page.id or \
                    node.id == root_page.publisher_public_id:
                root_node = node
                break
        if root_node is not None:
            nodes = root_node.children
            for remove_parent in nodes:
                remove_parent.parent = None
            from_level += node.level + 1
            to_level += node.level + 1
            nodes = flatten(nodes)
        else:
            nodes = []

        extra_levels = to_level - from_level
        children = cut_levels(nodes, from_level, to_level,
                              extra_inactive=extra_levels,
                              extra_active=extra_levels)
        children = renderer.apply_modifiers(children, post_cut=True)

        if root_node and instance.include_root:
            children = (root_node, )

        def add_menu_levels(child, level):
            child.menu_level = level
            for child in child.children:
                add_menu_levels(child, level+1)
        for child in children:
            add_menu_levels(child, 0)

        context.update({
            'instance': instance,
            'MenuItems': children,
            'template': re.search('(\w*).html', instance.template).groups()[0],
        })
        return context

plugin_pool.register_plugin(MenuPlugin)
