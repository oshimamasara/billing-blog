from django.db import migrations, models

def set_default_code(apps, schema_editor):
    product_model = apps.get_model('blog', 'post') # app name : model name
    for row in product_model.objects.all():
        row.price = 70
        row.save()

class Migration(migrations.Migration):
    dependencies = [
        ('blog', '0002_auto_20191231_0443'),
    ]
    operations = [
        migrations.AddField(
            model_name='post',
            name='price',
            field=models.IntegerField(null=True),
        ),

        migrations.RunPython(set_default_code, reverse_code=migrations.RunPython.noop),

        migrations.AlterField(
            model_name='post',
            name='price',
            field=models.IntegerField(null=True),
        ),
    ]