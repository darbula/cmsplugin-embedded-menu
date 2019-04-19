# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations

from cmsplugin_embeddedmenu.models import get_templates

class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0011_auto_20150419_1006'),
    ]

    operations = [
        migrations.CreateModel(
            name='MenuPluginSettings',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('menu_title', models.CharField(help_text='Title of the menu', max_length=256, null=True, verbose_name='Menu Title', blank=True)),
                ('sub_title', models.CharField(help_text='Sub Title of the menu', max_length=256, null=True, verbose_name='Sub Title', blank=True)),
                ('description', models.TextField(help_text='Description for the menu', null=True, verbose_name='Description', blank=True)),
                ('template', models.CharField(help_text='Use this template to render the menu.', max_length=256, verbose_name='Plugin Template', choices=get_templates(), default=get_templates()[0][0],)),
                ('include_root', models.BooleanField(default=False, help_text='Shall the menu also include the root menu item specified?', verbose_name='Include Root')),
                ('start_level', models.IntegerField(default=0, help_text='Should the root page also be included in the output?', verbose_name='Start Level')),
                ('show_depth', models.IntegerField(default=0, help_text='How many levels deep to look for menu items to show?', verbose_name='Depth')),
                ('root', models.ForeignKey(default=1, to='cms.Page', help_text='Menu tree starts from this page.')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
