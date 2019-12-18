# Generated by Django 2.2.7 on 2019-12-18 16:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('rules', '__first__'),
        ('websiteResults', '__first__'),
        ('wcag20', '0001_initial'),
        ('reports', '0001_initial'),
        ('ruleCategories', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='PageGuidelineResult',
            fields=[
                ('result_value', models.IntegerField(default=0)),
                ('implementation_pass_fail_score', models.IntegerField(default=-1)),
                ('implementation_score', models.IntegerField(default=-1)),
                ('implementation_pass_fail_status', models.CharField(choices=[('U', 'Undefined'), ('NA', 'Not applicable'), ('NI', 'Not Implemented'), ('PI', 'Partial Implementation'), ('AC', 'Almost Complete'), ('NI-MC', 'Not Implemented with manual checks required'), ('PI-MC', 'Partial Implementation with manual checks required'), ('AC-MC', 'Almost Complete with manual checks required'), ('C', 'Complete')], default='U', max_length=8, verbose_name='Implementation Pass/Fail Status')),
                ('implementation_status', models.CharField(choices=[('U', 'Undefined'), ('NA', 'Not applicable'), ('NI', 'Not Implemented'), ('PI', 'Partial Implementation'), ('AC', 'Almost Complete'), ('NI-MC', 'Not Implemented with manual checks required'), ('PI-MC', 'Partial Implementation with manual checks required'), ('AC-MC', 'Almost Complete with manual checks required'), ('C', 'Complete')], default='U', max_length=8, verbose_name='Implementation Status')),
                ('manual_check_status', models.CharField(choices=[('NC', 'Not Checked'), ('NA', 'Not Applicable'), ('P', 'Passed'), ('F', 'Fail')], default='NC', max_length=2, verbose_name='Manual Check Status')),
                ('rules_violation', models.IntegerField(default=0)),
                ('rules_warning', models.IntegerField(default=0)),
                ('rules_manual_check', models.IntegerField(default=0)),
                ('rules_passed', models.IntegerField(default=0)),
                ('rules_na', models.IntegerField(default=0)),
                ('rules_with_hidden_content', models.IntegerField(default=0)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('slug', models.SlugField(blank=True, default='none', editable=False, max_length=32)),
                ('guideline', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wcag20.Guideline')),
            ],
            options={
                'verbose_name': 'Page Guideline Result',
                'verbose_name_plural': 'Page Guideline Results',
                'ordering': ['guideline'],
            },
        ),
        migrations.CreateModel(
            name='PageResult',
            fields=[
                ('result_value', models.IntegerField(default=0)),
                ('implementation_pass_fail_score', models.IntegerField(default=-1)),
                ('implementation_score', models.IntegerField(default=-1)),
                ('implementation_pass_fail_status', models.CharField(choices=[('U', 'Undefined'), ('NA', 'Not applicable'), ('NI', 'Not Implemented'), ('PI', 'Partial Implementation'), ('AC', 'Almost Complete'), ('NI-MC', 'Not Implemented with manual checks required'), ('PI-MC', 'Partial Implementation with manual checks required'), ('AC-MC', 'Almost Complete with manual checks required'), ('C', 'Complete')], default='U', max_length=8, verbose_name='Implementation Pass/Fail Status')),
                ('implementation_status', models.CharField(choices=[('U', 'Undefined'), ('NA', 'Not applicable'), ('NI', 'Not Implemented'), ('PI', 'Partial Implementation'), ('AC', 'Almost Complete'), ('NI-MC', 'Not Implemented with manual checks required'), ('PI-MC', 'Partial Implementation with manual checks required'), ('AC-MC', 'Almost Complete with manual checks required'), ('C', 'Complete')], default='U', max_length=8, verbose_name='Implementation Status')),
                ('manual_check_status', models.CharField(choices=[('NC', 'Not Checked'), ('NA', 'Not Applicable'), ('P', 'Passed'), ('F', 'Fail')], default='NC', max_length=2, verbose_name='Manual Check Status')),
                ('rules_violation', models.IntegerField(default=0)),
                ('rules_warning', models.IntegerField(default=0)),
                ('rules_manual_check', models.IntegerField(default=0)),
                ('rules_passed', models.IntegerField(default=0)),
                ('rules_na', models.IntegerField(default=0)),
                ('rules_with_hidden_content', models.IntegerField(default=0)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('page_number', models.IntegerField(default=-1)),
                ('url', models.URLField(default='', max_length=4096, verbose_name='Page URL')),
                ('url_encoded', models.URLField(default='', max_length=8192, verbose_name='Page URL (encoded)')),
                ('title', models.CharField(default='', max_length=512, verbose_name='Page Title')),
                ('ws_report', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='page_all_results', to='reports.WebsiteReport')),
            ],
            options={
                'verbose_name': 'Page Result',
                'verbose_name_plural': 'Page Results',
                'ordering': ['page_number'],
            },
        ),
        migrations.CreateModel(
            name='PageRuleCategoryResult',
            fields=[
                ('result_value', models.IntegerField(default=0)),
                ('implementation_pass_fail_score', models.IntegerField(default=-1)),
                ('implementation_score', models.IntegerField(default=-1)),
                ('implementation_pass_fail_status', models.CharField(choices=[('U', 'Undefined'), ('NA', 'Not applicable'), ('NI', 'Not Implemented'), ('PI', 'Partial Implementation'), ('AC', 'Almost Complete'), ('NI-MC', 'Not Implemented with manual checks required'), ('PI-MC', 'Partial Implementation with manual checks required'), ('AC-MC', 'Almost Complete with manual checks required'), ('C', 'Complete')], default='U', max_length=8, verbose_name='Implementation Pass/Fail Status')),
                ('implementation_status', models.CharField(choices=[('U', 'Undefined'), ('NA', 'Not applicable'), ('NI', 'Not Implemented'), ('PI', 'Partial Implementation'), ('AC', 'Almost Complete'), ('NI-MC', 'Not Implemented with manual checks required'), ('PI-MC', 'Partial Implementation with manual checks required'), ('AC-MC', 'Almost Complete with manual checks required'), ('C', 'Complete')], default='U', max_length=8, verbose_name='Implementation Status')),
                ('manual_check_status', models.CharField(choices=[('NC', 'Not Checked'), ('NA', 'Not Applicable'), ('P', 'Passed'), ('F', 'Fail')], default='NC', max_length=2, verbose_name='Manual Check Status')),
                ('rules_violation', models.IntegerField(default=0)),
                ('rules_warning', models.IntegerField(default=0)),
                ('rules_manual_check', models.IntegerField(default=0)),
                ('rules_passed', models.IntegerField(default=0)),
                ('rules_na', models.IntegerField(default=0)),
                ('rules_with_hidden_content', models.IntegerField(default=0)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('slug', models.SlugField(blank=True, default='none', editable=False, max_length=32)),
                ('page_result', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='page_rc_results', to='pageResults.PageResult')),
                ('rule_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ruleCategories.RuleCategory')),
                ('ws_rc_result', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='page_rc_results', to='websiteResults.WebsiteRuleCategoryResult')),
            ],
            options={
                'verbose_name': 'Page Rule Category Result',
                'verbose_name_plural': 'Page Rule Category Results',
                'ordering': ['rule_category'],
            },
        ),
        migrations.CreateModel(
            name='PageRuleScopeResult',
            fields=[
                ('result_value', models.IntegerField(default=0)),
                ('implementation_pass_fail_score', models.IntegerField(default=-1)),
                ('implementation_score', models.IntegerField(default=-1)),
                ('implementation_pass_fail_status', models.CharField(choices=[('U', 'Undefined'), ('NA', 'Not applicable'), ('NI', 'Not Implemented'), ('PI', 'Partial Implementation'), ('AC', 'Almost Complete'), ('NI-MC', 'Not Implemented with manual checks required'), ('PI-MC', 'Partial Implementation with manual checks required'), ('AC-MC', 'Almost Complete with manual checks required'), ('C', 'Complete')], default='U', max_length=8, verbose_name='Implementation Pass/Fail Status')),
                ('implementation_status', models.CharField(choices=[('U', 'Undefined'), ('NA', 'Not applicable'), ('NI', 'Not Implemented'), ('PI', 'Partial Implementation'), ('AC', 'Almost Complete'), ('NI-MC', 'Not Implemented with manual checks required'), ('PI-MC', 'Partial Implementation with manual checks required'), ('AC-MC', 'Almost Complete with manual checks required'), ('C', 'Complete')], default='U', max_length=8, verbose_name='Implementation Status')),
                ('manual_check_status', models.CharField(choices=[('NC', 'Not Checked'), ('NA', 'Not Applicable'), ('P', 'Passed'), ('F', 'Fail')], default='NC', max_length=2, verbose_name='Manual Check Status')),
                ('rules_violation', models.IntegerField(default=0)),
                ('rules_warning', models.IntegerField(default=0)),
                ('rules_manual_check', models.IntegerField(default=0)),
                ('rules_passed', models.IntegerField(default=0)),
                ('rules_na', models.IntegerField(default=0)),
                ('rules_with_hidden_content', models.IntegerField(default=0)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('slug', models.SlugField(blank=True, default='none', editable=False, max_length=32)),
                ('page_result', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='page_rs_results', to='pageResults.PageResult')),
                ('rule_scope', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rules.RuleScope')),
                ('ws_rs_result', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='page_rs_results', to='websiteResults.WebsiteRuleScopeResult')),
            ],
            options={
                'verbose_name': 'Page Rule Scope Result',
                'verbose_name_plural': 'Page Rule Scope Results',
                'ordering': ['-rule_scope'],
            },
        ),
        migrations.CreateModel(
            name='PageRuleResult',
            fields=[
                ('result_value', models.IntegerField(default=0)),
                ('implementation_pass_fail_score', models.IntegerField(default=-1)),
                ('implementation_score', models.IntegerField(default=-1)),
                ('implementation_pass_fail_status', models.CharField(choices=[('U', 'Undefined'), ('NA', 'Not applicable'), ('NI', 'Not Implemented'), ('PI', 'Partial Implementation'), ('AC', 'Almost Complete'), ('NI-MC', 'Not Implemented with manual checks required'), ('PI-MC', 'Partial Implementation with manual checks required'), ('AC-MC', 'Almost Complete with manual checks required'), ('C', 'Complete')], default='U', max_length=8, verbose_name='Implementation Pass/Fail Status')),
                ('implementation_status', models.CharField(choices=[('U', 'Undefined'), ('NA', 'Not applicable'), ('NI', 'Not Implemented'), ('PI', 'Partial Implementation'), ('AC', 'Almost Complete'), ('NI-MC', 'Not Implemented with manual checks required'), ('PI-MC', 'Partial Implementation with manual checks required'), ('AC-MC', 'Almost Complete with manual checks required'), ('C', 'Complete')], default='U', max_length=8, verbose_name='Implementation Status')),
                ('manual_check_status', models.CharField(choices=[('NC', 'Not Checked'), ('NA', 'Not Applicable'), ('P', 'Passed'), ('F', 'Fail')], default='NC', max_length=2, verbose_name='Manual Check Status')),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('rule_required', models.BooleanField(default=False)),
                ('slug', models.SlugField(blank=True, default='none', editable=False, max_length=32)),
                ('result_message', models.CharField(default='none', max_length=4096, verbose_name='Rule Result Message')),
                ('elements_passed', models.IntegerField(default=0)),
                ('elements_violation', models.IntegerField(default=0)),
                ('elements_warning', models.IntegerField(default=0)),
                ('elements_hidden', models.IntegerField(default=0)),
                ('elements_mc_identified', models.IntegerField(default=0)),
                ('elements_mc_passed', models.IntegerField(default=0)),
                ('elements_mc_failed', models.IntegerField(default=0)),
                ('elements_mc_na', models.IntegerField(default=0)),
                ('element_results_json', models.TextField(blank=True, default='')),
                ('page_gl_result', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='page_rule_results', to='pageResults.PageGuidelineResult')),
                ('page_rc_result', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='page_rule_results', to='pageResults.PageRuleCategoryResult')),
                ('page_result', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='page_rule_results', to='pageResults.PageResult')),
                ('page_rs_result', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='page_rule_results', to='pageResults.PageRuleScopeResult')),
                ('rule', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rules.Rule')),
                ('ws_rule_result', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='page_rule_results', to='websiteResults.WebsiteRuleResult')),
            ],
            options={
                'verbose_name': 'Page Rule Result',
                'verbose_name_plural': 'Page Rule Results',
                'ordering': ['-elements_violation', '-elements_warning', '-elements_mc_identified', '-elements_passed', '-elements_hidden'],
            },
        ),
        migrations.AddField(
            model_name='pageguidelineresult',
            name='page_result',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='page_gl_results', to='pageResults.PageResult'),
        ),
        migrations.AddField(
            model_name='pageguidelineresult',
            name='ws_gl_result',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='page_gl_results', to='websiteResults.WebsiteGuidelineResult'),
        ),
    ]
