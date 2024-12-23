# Generated by Django 4.0.6 on 2022-08-02 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [

        migrations.CreateModel(
            name='Issues',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=254, null=True)),
                ('created_at', models.DateTimeField(blank=True, null=True)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('milestone_id', models.IntegerField(blank=True, null=True)),
                ('iid', models.IntegerField(blank=True, null=True)),
                ('weight', models.IntegerField(blank=True, null=True)),
                ('confidential', models.BooleanField()),
                ('due_date', models.DateField(blank=True, null=True)),
                ('lock_version', models.IntegerField(blank=True, null=True)),
                ('title_html', models.TextField(blank=True, null=True)),
                ('description_html', models.TextField(blank=True, null=True)),
                ('time_estimate', models.IntegerField(blank=True, null=True)),
                ('relative_position', models.IntegerField(blank=True, null=True)),
                ('service_desk_reply_to', models.CharField(blank=True, max_length=254, null=True)),
                ('cached_markdown_version', models.IntegerField(blank=True, null=True)),
                ('last_edited_at', models.DateTimeField(blank=True, null=True)),
                ('last_edited_by_id', models.IntegerField(blank=True, null=True)),
                ('discussion_locked', models.BooleanField(blank=True, null=True)),
                ('closed_at', models.DateTimeField(blank=True, null=True)),
                ('state_id', models.SmallIntegerField()),
                ('promoted_to_epic_id', models.IntegerField(blank=True, null=True)),
                ('health_status', models.SmallIntegerField(blank=True, null=True)),
                ('external_key', models.CharField(blank=True, max_length=255, null=True)),
                ('sprint_id', models.BigIntegerField(blank=True, null=True)),
                ('blocking_issues_count', models.IntegerField()),
                ('issue_type', models.SmallIntegerField()),
                ('upvotes_count', models.IntegerField()),
                ('work_item_type_id', models.BigIntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'issues',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Notes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('note', models.TextField(blank=True, null=True)),
                ('noteable_type', models.CharField(blank=True, max_length=254, null=True)),
                ('author_id', models.IntegerField(blank=True, null=True)),
                ('created_at', models.DateTimeField(blank=True, null=True)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
                ('attachment', models.CharField(blank=True, max_length=254, null=True)),
                ('line_code', models.CharField(blank=True, max_length=254, null=True)),
                ('commit_id', models.CharField(blank=True, max_length=254, null=True)),
                ('noteable_id', models.IntegerField(blank=True, null=True)),
                ('system', models.BooleanField()),
                ('st_diff', models.TextField(blank=True, null=True)),
                ('updated_by_id', models.IntegerField(blank=True, null=True)),
                ('type', models.CharField(blank=True, max_length=254, null=True)),
                ('position', models.TextField(blank=True, null=True)),
                ('original_position', models.TextField(blank=True, null=True)),
                ('resolved_at', models.DateTimeField(blank=True, null=True)),
                ('resolved_by_id', models.IntegerField(blank=True, null=True)),
                ('discussion_id', models.CharField(blank=True, max_length=254, null=True)),
                ('note_html', models.TextField(blank=True, null=True)),
                ('cached_markdown_version', models.IntegerField(blank=True, null=True)),
                ('change_position', models.TextField(blank=True, null=True)),
                ('resolved_by_push', models.BooleanField(blank=True, null=True)),
                ('review_id', models.BigIntegerField(blank=True, null=True)),
                ('confidential', models.BooleanField(blank=True, null=True)),
                ('last_edited_at', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'notes',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=254, null=True)),
                ('path', models.CharField(blank=True, max_length=254, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(blank=True, null=True)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
                ('creator_id', models.IntegerField(blank=True, null=True)),
                ('namespace_id', models.IntegerField()),
                ('last_activity_at', models.DateTimeField(blank=True, null=True)),
                ('import_url', models.CharField(blank=True, max_length=254, null=True)),
                ('visibility_level', models.IntegerField()),
                ('archived', models.BooleanField()),
                ('avatar', models.CharField(blank=True, max_length=254, null=True)),
                ('merge_requests_template', models.TextField(blank=True, null=True)),
                ('star_count', models.IntegerField()),
                ('merge_requests_rebase_enabled', models.BooleanField(blank=True, null=True)),
                ('import_type', models.CharField(blank=True, max_length=254, null=True)),
                ('import_source', models.CharField(blank=True, max_length=254, null=True)),
                ('approvals_before_merge', models.IntegerField()),
                ('reset_approvals_on_push', models.BooleanField(blank=True, null=True)),
                ('merge_requests_ff_only_enabled', models.BooleanField(blank=True, null=True)),
                ('issues_template', models.TextField(blank=True, null=True)),
                ('mirror', models.BooleanField()),
                ('mirror_last_update_at', models.DateTimeField(blank=True, null=True)),
                ('mirror_last_successful_update_at', models.DateTimeField(blank=True, null=True)),
                ('mirror_user_id', models.IntegerField(blank=True, null=True)),
                ('shared_runners_enabled', models.BooleanField()),
                ('runners_token', models.CharField(blank=True, max_length=254, null=True)),
                ('build_coverage_regex', models.CharField(blank=True, max_length=254, null=True)),
                ('build_allow_git_fetch', models.BooleanField()),
                ('build_timeout', models.IntegerField()),
                ('mirror_trigger_builds', models.BooleanField()),
                ('pending_delete', models.BooleanField(blank=True, null=True)),
                ('public_builds', models.BooleanField()),
                ('last_repository_check_failed', models.BooleanField(blank=True, null=True)),
                ('last_repository_check_at', models.DateTimeField(blank=True, null=True)),
                ('only_allow_merge_if_pipeline_succeeds', models.BooleanField()),
                ('has_external_issue_tracker', models.BooleanField(blank=True, null=True)),
                ('repository_storage', models.CharField(max_length=254)),
                ('repository_read_only', models.BooleanField(blank=True, null=True)),
                ('request_access_enabled', models.BooleanField()),
                ('has_external_wiki', models.BooleanField(blank=True, null=True)),
                ('ci_config_path', models.CharField(blank=True, max_length=254, null=True)),
                ('lfs_enabled', models.BooleanField(blank=True, null=True)),
                ('description_html', models.TextField(blank=True, null=True)),
                ('only_allow_merge_if_all_discussions_are_resolved', models.BooleanField(blank=True, null=True)),
                ('repository_size_limit', models.BigIntegerField(blank=True, null=True)),
                ('printing_merge_request_link_enabled', models.BooleanField()),
                ('auto_cancel_pending_pipelines', models.IntegerField()),
                ('service_desk_enabled', models.BooleanField(blank=True, null=True)),
                ('cached_markdown_version', models.IntegerField(blank=True, null=True)),
                ('delete_error', models.TextField(blank=True, null=True)),
                ('last_repository_updated_at', models.DateTimeField(blank=True, null=True)),
                ('disable_overriding_approvers_per_merge_request', models.BooleanField(blank=True, null=True)),
                ('storage_version', models.SmallIntegerField(blank=True, null=True)),
                ('resolve_outdated_diff_discussions', models.BooleanField(blank=True, null=True)),
                ('remote_mirror_available_overridden', models.BooleanField(blank=True, null=True)),
                ('only_mirror_protected_branches', models.BooleanField(blank=True, null=True)),
                ('pull_mirror_available_overridden', models.BooleanField(blank=True, null=True)),
                ('jobs_cache_index', models.IntegerField(blank=True, null=True)),
                ('mirror_overwrites_diverged_branches', models.BooleanField(blank=True, null=True)),
                ('external_authorization_classification_label', models.CharField(blank=True, max_length=254, null=True)),
                ('external_webhook_token', models.CharField(blank=True, max_length=254, null=True)),
                ('pages_https_only', models.BooleanField(blank=True, null=True)),
                ('packages_enabled', models.BooleanField(blank=True, null=True)),
                ('merge_requests_author_approval', models.BooleanField(blank=True, null=True)),
                ('pool_repository_id', models.BigIntegerField(blank=True, null=True)),
                ('runners_token_encrypted', models.CharField(blank=True, max_length=254, null=True)),
                ('bfg_object_map', models.CharField(blank=True, max_length=254, null=True)),
                ('detected_repository_languages', models.BooleanField(blank=True, null=True)),
                ('merge_requests_disable_committers_approval', models.BooleanField(blank=True, null=True)),
                ('require_password_to_approve', models.BooleanField(blank=True, null=True)),
                ('emails_disabled', models.BooleanField(blank=True, null=True)),
                ('max_pages_size', models.IntegerField(blank=True, null=True)),
                ('max_artifacts_size', models.IntegerField(blank=True, null=True)),
                ('pull_mirror_branch_prefix', models.CharField(blank=True, max_length=50, null=True)),
                ('marked_for_deletion_at', models.DateField(blank=True, null=True)),
                ('remove_source_branch_after_merge', models.BooleanField(blank=True, null=True)),
                ('suggestion_commit_message', models.CharField(blank=True, max_length=255, null=True)),
                ('autoclose_referenced_issues', models.BooleanField(blank=True, null=True)),
                ('project_namespace_id', models.BigIntegerField(blank=True, null=True, unique=True)),
                ('hidden', models.BooleanField()),
            ],
            options={
                'db_table': 'projects',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Timelogs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_spent', models.IntegerField()),
                ('user_id', models.IntegerField(blank=True, null=True)),
                ('created_at', models.DateTimeField()),
                ('updated_at', models.DateTimeField()),
                ('merge_request_id', models.IntegerField(blank=True, null=True)),
                ('spent_at', models.DateTimeField(blank=True, null=True)),
                ('summary', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'timelogs',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=254, unique=True)),
                ('encrypted_password', models.CharField(max_length=254)),
                ('reset_password_token', models.CharField(blank=True, max_length=254, null=True, unique=True)),
                ('reset_password_sent_at', models.DateTimeField(blank=True, null=True)),
                ('remember_created_at', models.DateTimeField(blank=True, null=True)),
                ('sign_in_count', models.IntegerField(blank=True, null=True)),
                ('current_sign_in_at', models.DateTimeField(blank=True, null=True)),
                ('last_sign_in_at', models.DateTimeField(blank=True, null=True)),
                ('current_sign_in_ip', models.CharField(blank=True, max_length=254, null=True)),
                ('last_sign_in_ip', models.CharField(blank=True, max_length=254, null=True)),
                ('created_at', models.DateTimeField(blank=True, null=True)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
                ('name', models.CharField(blank=True, max_length=254, null=True)),
                ('admin', models.BooleanField()),
                ('projects_limit', models.IntegerField()),
                ('skype', models.CharField(max_length=254)),
                ('linkedin', models.CharField(max_length=254)),
                ('twitter', models.CharField(max_length=254)),
                ('failed_attempts', models.IntegerField(blank=True, null=True)),
                ('locked_at', models.DateTimeField(blank=True, null=True)),
                ('username', models.CharField(blank=True, max_length=254, null=True)),
                ('can_create_group', models.BooleanField()),
                ('can_create_team', models.BooleanField()),
                ('state', models.CharField(blank=True, max_length=254, null=True)),
                ('color_scheme_id', models.IntegerField()),
                ('password_expires_at', models.DateTimeField(blank=True, null=True)),
                ('created_by_id', models.IntegerField(blank=True, null=True)),
                ('last_credential_check_at', models.DateTimeField(blank=True, null=True)),
                ('avatar', models.CharField(blank=True, max_length=254, null=True)),
                ('confirmation_token', models.CharField(blank=True, max_length=254, null=True, unique=True)),
                ('confirmed_at', models.DateTimeField(blank=True, null=True)),
                ('confirmation_sent_at', models.DateTimeField(blank=True, null=True)),
                ('unconfirmed_email', models.CharField(blank=True, max_length=254, null=True)),
                ('hide_no_ssh_key', models.BooleanField(blank=True, null=True)),
                ('website_url', models.CharField(max_length=254)),
                ('admin_email_unsubscribed_at', models.DateTimeField(blank=True, null=True)),
                ('notification_email', models.CharField(blank=True, max_length=254, null=True)),
                ('hide_no_password', models.BooleanField(blank=True, null=True)),
                ('password_automatically_set', models.BooleanField(blank=True, null=True)),
                ('location', models.CharField(blank=True, max_length=254, null=True)),
                ('encrypted_otp_secret', models.CharField(blank=True, max_length=254, null=True)),
                ('encrypted_otp_secret_iv', models.CharField(blank=True, max_length=254, null=True)),
                ('encrypted_otp_secret_salt', models.CharField(blank=True, max_length=254, null=True)),
                ('otp_required_for_login', models.BooleanField()),
                ('otp_backup_codes', models.TextField(blank=True, null=True)),
                ('public_email', models.CharField(blank=True, max_length=254, null=True)),
                ('dashboard', models.IntegerField(blank=True, null=True)),
                ('project_view', models.IntegerField(blank=True, null=True)),
                ('consumed_timestep', models.IntegerField(blank=True, null=True)),
                ('layout', models.IntegerField(blank=True, null=True)),
                ('hide_project_limit', models.BooleanField(blank=True, null=True)),
                ('note', models.TextField(blank=True, null=True)),
                ('unlock_token', models.CharField(blank=True, max_length=254, null=True, unique=True)),
                ('otp_grace_period_started_at', models.DateTimeField(blank=True, null=True)),
                ('external', models.BooleanField(blank=True, null=True)),
                ('incoming_email_token', models.CharField(blank=True, max_length=254, null=True)),
                ('organization', models.CharField(blank=True, max_length=254, null=True)),
                ('auditor', models.BooleanField()),
                ('require_two_factor_authentication_from_group', models.BooleanField()),
                ('two_factor_grace_period', models.IntegerField()),
                ('last_activity_on', models.DateField(blank=True, null=True)),
                ('notified_of_own_activity', models.BooleanField(blank=True, null=True)),
                ('preferred_language', models.CharField(blank=True, max_length=254, null=True)),
                ('email_opted_in', models.BooleanField(blank=True, null=True)),
                ('email_opted_in_ip', models.CharField(blank=True, max_length=254, null=True)),
                ('email_opted_in_source_id', models.IntegerField(blank=True, null=True)),
                ('email_opted_in_at', models.DateTimeField(blank=True, null=True)),
                ('theme_id', models.SmallIntegerField(blank=True, null=True)),
                ('accepted_term_id', models.IntegerField(blank=True, null=True)),
                ('feed_token', models.CharField(blank=True, max_length=254, null=True)),
                ('include_private_contributions', models.BooleanField(blank=True, null=True)),
                ('private_profile', models.BooleanField()),
                ('roadmap_layout', models.SmallIntegerField(blank=True, null=True)),
                ('commit_email', models.CharField(blank=True, max_length=254, null=True)),
                ('group_view', models.IntegerField(blank=True, null=True)),
                ('managing_group_id', models.IntegerField(blank=True, null=True)),
                ('static_object_token', models.CharField(blank=True, max_length=255, null=True, unique=True)),
                ('first_name', models.CharField(blank=True, max_length=255, null=True)),
                ('last_name', models.CharField(blank=True, max_length=255, null=True)),
                ('role', models.SmallIntegerField(blank=True, null=True)),
                ('user_type', models.SmallIntegerField(blank=True, null=True)),
                ('static_object_token_encrypted', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'users',
                'managed': False,
            },
        ),
    ]
