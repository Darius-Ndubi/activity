# Generated by Django 2.2 on 2019-05-12 00:07

from decimal import Decimal
from django.db import migrations, models
import simple_history.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ActivityTable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255)),
                ('table_id', models.IntegerField(blank=True, null=True)),
                ('remote_owner', models.CharField(blank=True, max_length=255)),
                ('url', models.CharField(blank=True, max_length=255)),
                ('unique_count', models.IntegerField(blank=True, null=True)),
                ('create_date', models.DateTimeField(blank=True, null=True)),
                ('edit_date', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='CollectedData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('achieved', models.DecimalField(decimal_places=2, help_text=' ', max_digits=20, verbose_name='Achieved')),
                ('description', models.TextField(blank=True, help_text=' ', null=True, verbose_name='Remarks/comments')),
                ('date_collected', models.DateTimeField(blank=True, help_text=' ', null=True)),
                ('comment', models.TextField(blank=True, help_text=' ', max_length=255, null=True, verbose_name='Comment/Explanation')),
                ('update_count_tola_table', models.BooleanField(default=False, help_text=' ', verbose_name='Would you like to update the achieved total with the row count from TolaTables?')),
                ('create_date', models.DateTimeField(blank=True, help_text=' ', null=True)),
                ('edit_date', models.DateTimeField(blank=True, help_text=' ', null=True)),
            ],
            options={
                'verbose_name_plural': 'Indicator Output/Outcome Collected Data',
                'ordering': ('agreement', 'indicator', 'date_collected', 'create_date'),
            },
        ),
        migrations.CreateModel(
            name='DataCollectionFrequency',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('frequency', models.CharField(blank=True, max_length=135, null=True)),
                ('description', models.CharField(blank=True, max_length=255, null=True)),
                ('numdays', models.PositiveIntegerField(default=0, verbose_name='Frequency in number of days')),
                ('create_date', models.DateTimeField(blank=True, null=True)),
                ('edit_date', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='DisaggregationLabel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(blank=True, max_length=765)),
                ('customsort', models.IntegerField(blank=True, null=True)),
                ('create_date', models.DateTimeField(blank=True, null=True)),
                ('edit_date', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='DisaggregationType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('disaggregation_type', models.CharField(blank=True, max_length=135)),
                ('description', models.CharField(blank=True, max_length=765)),
                ('standard', models.BooleanField(default=False, verbose_name='Standard (TolaData Admins Only)')),
                ('create_date', models.DateTimeField(blank=True, null=True)),
                ('edit_date', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='DisaggregationValue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(blank=True, max_length=765)),
                ('create_date', models.DateTimeField(blank=True, null=True)),
                ('edit_date', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ExternalService',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255)),
                ('url', models.CharField(blank=True, max_length=765)),
                ('feed_url', models.CharField(blank=True, max_length=765)),
                ('create_date', models.DateTimeField(blank=True, null=True)),
                ('edit_date', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ExternalServiceRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_url', models.CharField(blank=True, max_length=765)),
                ('record_id', models.CharField(blank=True, max_length=765, verbose_name='Unique ID')),
                ('create_date', models.DateTimeField(blank=True, null=True)),
                ('edit_date', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='HistoricalCollectedData',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('achieved', models.DecimalField(decimal_places=2, help_text=' ', max_digits=20, verbose_name='Achieved')),
                ('description', models.TextField(blank=True, help_text=' ', null=True, verbose_name='Remarks/comments')),
                ('date_collected', models.DateTimeField(blank=True, help_text=' ', null=True)),
                ('comment', models.TextField(blank=True, help_text=' ', max_length=255, null=True, verbose_name='Comment/Explanation')),
                ('update_count_tola_table', models.BooleanField(default=False, help_text=' ', verbose_name='Would you like to update the achieved total with the row count from TolaTables?')),
                ('create_date', models.DateTimeField(blank=True, help_text=' ', null=True)),
                ('edit_date', models.DateTimeField(blank=True, help_text=' ', null=True)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
            ],
            options={
                'verbose_name': 'historical collected data',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalIndicator',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('name', models.CharField(help_text=' ', max_length=255, verbose_name='Name')),
                ('number', models.CharField(blank=True, help_text=' ', max_length=255, null=True)),
                ('source', models.CharField(blank=True, help_text=' ', max_length=255, null=True)),
                ('definition', models.TextField(blank=True, help_text=' ', null=True)),
                ('justification', models.TextField(blank=True, help_text=' ', max_length=500, null=True, verbose_name='Rationale or Justification for Indicator')),
                ('unit_of_measure', models.CharField(blank=True, help_text=' ', max_length=135, null=True, verbose_name='Unit of measure*')),
                ('baseline', models.CharField(blank=True, help_text=' ', max_length=255, null=True, verbose_name='Baseline*')),
                ('baseline_na', models.BooleanField(default=False, help_text=' ', verbose_name='Not applicable')),
                ('lop_target', models.CharField(blank=True, help_text=' ', max_length=255, null=True, verbose_name='Life of Program (LoP) target*')),
                ('rationale_for_target', models.TextField(blank=True, help_text=' ', max_length=255, null=True)),
                ('target_frequency', models.IntegerField(choices=[(1, 'Life of Program (LoP) only'), (2, 'Midline and endline'), (3, 'Annual'), (4, 'Semi-annual'), (5, 'Tri-annual'), (6, 'Quarterly'), (7, 'Monthly'), (8, 'Event')], help_text=' ', null=True, verbose_name='Target frequency')),
                ('target_frequency_custom', models.CharField(blank=True, help_text=' ', max_length=100, null=True, verbose_name='First event name*')),
                ('target_frequency_start', models.DateField(blank=True, help_text=' ', null=True, verbose_name='First target period begins*')),
                ('target_frequency_num_periods', models.IntegerField(blank=True, help_text=' ', null=True, verbose_name='Number of target periods*')),
                ('means_of_verification', models.CharField(blank=True, help_text=' ', max_length=255, null=True, verbose_name='Means of Verification / Data Source')),
                ('data_collection_method', models.CharField(blank=True, help_text=' ', max_length=255, null=True, verbose_name='Data Collection Method')),
                ('data_points', models.TextField(blank=True, help_text=' ', max_length=500, null=True, verbose_name='Data Points')),
                ('responsible_person', models.CharField(blank=True, help_text=' ', max_length=255, null=True, verbose_name='Responsible Person(s) and Team')),
                ('method_of_analysis', models.CharField(blank=True, help_text=' ', max_length=255, null=True, verbose_name='Method of Analysis')),
                ('information_use', models.CharField(blank=True, help_text=' ', max_length=255, null=True, verbose_name='Information Use')),
                ('quality_assurance', models.TextField(blank=True, help_text=' ', max_length=500, null=True, verbose_name='Quality Assurance Measures')),
                ('data_issues', models.TextField(blank=True, help_text=' ', max_length=500, null=True, verbose_name='Data Issues')),
                ('indicator_changes', models.TextField(blank=True, help_text=' ', max_length=500, null=True, verbose_name='Changes to Indicator')),
                ('comments', models.TextField(blank=True, help_text=' ', max_length=255, null=True)),
                ('key_performance_indicator', models.BooleanField(default=False, help_text=' ', verbose_name='Key Performance Indicator for this program?')),
                ('create_date', models.DateTimeField(blank=True, help_text=' ', null=True)),
                ('edit_date', models.DateTimeField(blank=True, help_text=' ', null=True)),
                ('notes', models.TextField(blank=True, max_length=500, null=True)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
            ],
            options={
                'verbose_name': 'historical indicator',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='Indicator',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text=' ', max_length=255, verbose_name='Name')),
                ('number', models.CharField(blank=True, help_text=' ', max_length=255, null=True)),
                ('source', models.CharField(blank=True, help_text=' ', max_length=255, null=True)),
                ('definition', models.TextField(blank=True, help_text=' ', null=True)),
                ('justification', models.TextField(blank=True, help_text=' ', max_length=500, null=True, verbose_name='Rationale or Justification for Indicator')),
                ('unit_of_measure', models.CharField(blank=True, help_text=' ', max_length=135, null=True, verbose_name='Unit of measure*')),
                ('baseline', models.CharField(blank=True, help_text=' ', max_length=255, null=True, verbose_name='Baseline*')),
                ('baseline_na', models.BooleanField(default=False, help_text=' ', verbose_name='Not applicable')),
                ('lop_target', models.CharField(blank=True, help_text=' ', max_length=255, null=True, verbose_name='Life of Program (LoP) target*')),
                ('rationale_for_target', models.TextField(blank=True, help_text=' ', max_length=255, null=True)),
                ('target_frequency', models.IntegerField(choices=[(1, 'Life of Program (LoP) only'), (2, 'Midline and endline'), (3, 'Annual'), (4, 'Semi-annual'), (5, 'Tri-annual'), (6, 'Quarterly'), (7, 'Monthly'), (8, 'Event')], help_text=' ', null=True, verbose_name='Target frequency')),
                ('target_frequency_custom', models.CharField(blank=True, help_text=' ', max_length=100, null=True, verbose_name='First event name*')),
                ('target_frequency_start', models.DateField(blank=True, help_text=' ', null=True, verbose_name='First target period begins*')),
                ('target_frequency_num_periods', models.IntegerField(blank=True, help_text=' ', null=True, verbose_name='Number of target periods*')),
                ('means_of_verification', models.CharField(blank=True, help_text=' ', max_length=255, null=True, verbose_name='Means of Verification / Data Source')),
                ('data_collection_method', models.CharField(blank=True, help_text=' ', max_length=255, null=True, verbose_name='Data Collection Method')),
                ('data_points', models.TextField(blank=True, help_text=' ', max_length=500, null=True, verbose_name='Data Points')),
                ('responsible_person', models.CharField(blank=True, help_text=' ', max_length=255, null=True, verbose_name='Responsible Person(s) and Team')),
                ('method_of_analysis', models.CharField(blank=True, help_text=' ', max_length=255, null=True, verbose_name='Method of Analysis')),
                ('information_use', models.CharField(blank=True, help_text=' ', max_length=255, null=True, verbose_name='Information Use')),
                ('quality_assurance', models.TextField(blank=True, help_text=' ', max_length=500, null=True, verbose_name='Quality Assurance Measures')),
                ('data_issues', models.TextField(blank=True, help_text=' ', max_length=500, null=True, verbose_name='Data Issues')),
                ('indicator_changes', models.TextField(blank=True, help_text=' ', max_length=500, null=True, verbose_name='Changes to Indicator')),
                ('comments', models.TextField(blank=True, help_text=' ', max_length=255, null=True)),
                ('key_performance_indicator', models.BooleanField(default=False, help_text=' ', verbose_name='Key Performance Indicator for this program?')),
                ('create_date', models.DateTimeField(blank=True, help_text=' ', null=True)),
                ('edit_date', models.DateTimeField(blank=True, help_text=' ', null=True)),
                ('notes', models.TextField(blank=True, max_length=500, null=True)),
            ],
            options={
                'ordering': ('create_date',),
            },
        ),
        migrations.CreateModel(
            name='IndicatorType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('indicator_type', models.CharField(blank=True, max_length=135)),
                ('description', models.TextField(blank=True, max_length=765)),
                ('create_date', models.DateTimeField(blank=True, null=True)),
                ('edit_date', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Level',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=135)),
                ('description', models.TextField(blank=True, max_length=765)),
                ('create_date', models.DateTimeField(blank=True, null=True)),
                ('edit_date', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Objective',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=135)),
                ('description', models.TextField(blank=True, max_length=765)),
                ('create_date', models.DateTimeField(blank=True, null=True)),
                ('edit_date', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'ordering': ('program', 'name'),
            },
        ),
        migrations.CreateModel(
            name='PeriodicTarget',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('period', models.CharField(blank=True, max_length=255, null=True)),
                ('target', models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=20)),
                ('start_date', models.DateField(blank=True, null=True)),
                ('end_date', models.DateField(blank=True, null=True)),
                ('customsort', models.IntegerField(blank=True, null=True)),
                ('create_date', models.DateTimeField(blank=True, null=True)),
                ('edit_date', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'ordering': ('customsort', '-create_date'),
            },
        ),
        migrations.CreateModel(
            name='ReportingFrequency',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('frequency', models.CharField(blank=True, max_length=135)),
                ('description', models.CharField(blank=True, max_length=765)),
                ('create_date', models.DateTimeField(blank=True, null=True)),
                ('edit_date', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ReportingPeriod',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_date', models.DateTimeField(blank=True, null=True)),
                ('edit_date', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='StrategicObjective',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=135)),
                ('description', models.TextField(blank=True, max_length=765)),
                ('create_date', models.DateTimeField(blank=True, null=True)),
                ('edit_date', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'ordering': ('country', 'name'),
            },
        ),
    ]
