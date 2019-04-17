# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2019-04-17 13:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cmsplugin_embeddedmenu', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menupluginsettings',
            name='cmsplugin_ptr',
            field=models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='cmsplugin_embeddedmenu_menupluginsettings', serialize=False, to='cms.CMSPlugin'),
        ),
        migrations.AlterField(
            model_name='menupluginsettings',
            name='template',
            field=models.CharField(choices=[(b'cmsplugin_embeddedmenu/layouts/default.html', b'Default'), ('cmsplugin_embeddedmenu/layouts/popover_submenu.html', 'Popover Submenu'), ('cmsplugin_embeddedmenu/layouts/zavodi.html', 'Zavodi'), ('cmsplugin_embeddedmenu/layouts/plavi_gumbi.html', 'Plavi Gumbi'), ('cmsplugin_embeddedmenu/layouts/glavni_meni.html', 'Glavni Meni'), ('cmsplugin_embeddedmenu/layouts/top_meni.html', 'Top Meni'), ('cmsplugin_embeddedmenu/layouts/slika_i_opis.html', 'Slika I Opis')], help_text='Use this template to render the menu.', max_length=256, verbose_name='Plugin Template'),
        ),
    ]
