# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-01-25 15:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('document', '0117_auto_20190118_1214'),
    ]

    operations = [
        migrations.AddField(
            model_name='documentfield',
            name='hidden_always',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='documentfielddetector',
            name='category',
            field=models.CharField(blank=True, choices=[('simple_config', 'Simple field detectors loaded and managed via "Documents: Import Simple Field Detection Config" admin task.')], db_index=True, help_text='Field detector category used for technical needs e.g. for determining \nwhich field detectors were created automatically during import process.', max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='documentfielddetector',
            name='definition_words',
            field=models.TextField(blank=True, help_text='\\n-separated list of definition words (in lowercase) expected \nto be in the text unit. Definition words are checked after the exclude regexps. If definition words are assigned \nto the field detector then get_definitions() function is executed on the text unit. If it finds nothing then skip the\ntext unit. If the text unit contains one of the definitions from this field then: If there are no include regexps \nthen the whole text unit matches the field detector. If there are include regexps then check against them.', null=True),
        ),
        migrations.AlterField(
            model_name='documentfielddetector',
            name='detected_value',
            field=models.CharField(blank=True, help_text="Assigns this string value to \nthe field if this field detector matches. Makes sense for choice/multi-choice/string fields only which don't have \nan extraction function which will be applied to the matching text.", max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='documentfielddetector',
            name='exclude_regexps',
            field=models.TextField(blank=True, help_text='\\n-separated regexps excluding sentences from possible match. \nExclude regexps are checked before include regexps or definition words. If one of exclude regexps matches text of a \ntext unit then the field detector exits and skips this text unit. Whole text unit does not need to match an \nexclude regexp. The regexps are searched in the text unit.', null=True),
        ),
        migrations.AlterField(
            model_name='documentfielddetector',
            name='extraction_hint',
            field=models.CharField(blank=True, choices=[('TAKE_FIRST', 'TAKE_FIRST'), ('TAKE_SECOND', 'TAKE_SECOND'), ('TAKE_LAST', 'TAKE_LAST'), ('TAKE_MIN', 'TAKE_MIN'), ('TAKE_MAX', 'TAKE_MAX')], db_index=True, default='TAKE_FIRST', help_text='Hint for selection one of multiple possible\nvalues found by an extraction function of the corresponding field type. Example: Date field finds 5 dates and the last\nof them should be taken.', max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='documentfielddetector',
            name='include_regexps',
            field=models.TextField(blank=True, help_text='\\n-separated list of regexps to which \nshould be found in the text unit for it to match the field detector. Include regexps are checked after the definition \nwords and include regexps. An include regexp does not need to match the whole sentence but it only should be found in \nthe sentence. Example: "house" - will match any sentence containing this word. Please avoid using ".*" and similar \nunlimited multipliers. They can cause catastrophic backtracking and slowdown or crash the whole system. \nUse ".{0,100}" or similar instead.', null=True),
        ),
        migrations.AlterField(
            model_name='documentfielddetector',
            name='regexps_pre_process_lower',
            field=models.BooleanField(default=False, help_text='Bring sentence/paragraph to lower case before processing with this field detector.'),
        ),
        migrations.AlterField(
            model_name='documentfielddetector',
            name='regexps_pre_process_remove_numeric_separators',
            field=models.BooleanField(default=False, help_text='Remove numeric separators in the\nsentence/paragraph before processing for easier matching numbers. Example: 2,000 => 2000 e.t.c. This allows \nrepresenting number templates in regexps in easier form.'),
        ),
        migrations.AlterField(
            model_name='documentfielddetector',
            name='text_part',
            field=models.CharField(choices=[('FULL', 'FULL'), ('BEFORE_REGEXP', 'BEFORE_REGEXP'), ('AFTER_REGEXP', 'AFTER_REGEXP')], db_index=True, default='FULL', help_text='Defines which part of the matching \nsentence / paragraph should be passed to the extraction function of the corresponding field type. \nExample: "2019-01-23 is the Start date and 2019-01-24 is the end date." If include regexp is "is.{0,100}Start" and \ntext part = BEFORE_REGEXP then "2019-01-23 " will be passed to get_dates().', max_length=30),
        ),
    ]