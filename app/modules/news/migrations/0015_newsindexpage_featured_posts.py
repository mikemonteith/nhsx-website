# Generated by Django 3.0.4 on 2020-04-15 11:07

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0014_auto_20200415_1014'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsindexpage',
            name='featured_posts',
            field=wagtail.core.fields.StreamField([('link', wagtail.core.blocks.PageChooserBlock(label='Page', page_type=['news.News'], required=True))], blank=True),
        ),
    ]
