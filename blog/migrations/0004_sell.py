# Generated by Django 3.0.1 on 2020-01-06 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_post_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sell',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sold_blog', models.CharField(max_length=100)),
                ('customer_mail', models.CharField(max_length=100)),
                ('Date', models.DateTimeField(auto_now_add=True)),
                ('price', models.IntegerField(null=True)),
            ],
        ),
    ]
