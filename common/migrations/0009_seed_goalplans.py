from django.db import migrations

def create_goalplans(apps, schema_editor):
    GoalPlan = apps.get_model('common', 'GoalPlan')

    plans = [
        {
            'length': '30',
            'name': 'Summer Shred',
            'description': 'A focused one‑month plan to boost your metabolism, lean out, and feel beach‑ready.',
            'background_image': 'goals/summer_shred.jpg',
        },
        {
            'length': '60',
            'name': 'Total Transformation',
            'description': 'Eight weeks of strength, cardio, and meal plans to reshape you from the inside out.',
            'background_image': 'goals/total_transformation.jpg',
        },
        {
            'length': '90',
            'name': 'Champion’s Journey',
            'description': 'A 12‑week periodized roadmap for peak performance, recovery, and nutrition mastery.',
            'background_image': 'goals/champions_journey.jpg',
        },
    ]

    for p in plans:
        GoalPlan.objects.update_or_create(
            length=p['length'],
            defaults={
                'name': p['name'],
                'description': p['description'],
                'background_image': p['background_image'],
            }
        )

class Migration(migrations.Migration):
    dependencies = [
        ('common', '0008_alter_goalplan_length'),
    ]
    operations = [
        migrations.RunPython(create_goalplans),
    ]
