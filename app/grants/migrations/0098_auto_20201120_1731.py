# Generated by Django 2.2.4 on 2020-11-20 17:31

from django.db import migrations, models
import django.db.models.deletion
import grants.utils


class Migration(migrations.Migration):

    dependencies = [
        ('grants', '0097_merge_20201120_1338'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grantclr',
            name='customer_name',
            field=models.CharField(blank=True, default='', help_text='used to genrate <customer_name>/round_num/sub_round_slug', max_length=15),
        ),
        migrations.AlterField(
            model_name='grantclr',
            name='display_text',
            field=models.CharField(blank=True, help_text='sets the custom text in CLR banner on the landing page', max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='grantclr',
            name='logo',
            field=models.ImageField(blank=True, help_text='sets the background in CLR banner on the landing page', max_length=500, null=True, upload_to=grants.utils.get_upload_filename),
        ),
        migrations.AlterField(
            model_name='grantclr',
            name='owner',
            field=models.ForeignKey(blank=True, help_text='sets the owners profile photo in CLR banner on the landing page', null=True, on_delete=django.db.models.deletion.SET_NULL, to='dashboard.Profile'),
        ),
        migrations.AlterField(
            model_name='grantclr',
            name='round_num',
            field=models.PositiveIntegerField(help_text='CLR Round Number. used to genrate customer_name/<round_num>/sub_round_slug'),
        ),
        migrations.AlterField(
            model_name='grantclr',
            name='sub_round_slug',
            field=models.CharField(blank=True, default='', help_text='used to genrate customer_name/round_num/<sub_round_slug>', max_length=25),
        ),
    ]