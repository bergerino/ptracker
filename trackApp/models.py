# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Issues(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    author = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True, related_name='issueauthor')
    project = models.ForeignKey('Projects', models.DO_NOTHING, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    milestone_id = models.IntegerField(blank=True, null=True)
    iid = models.IntegerField(blank=True, null=True)
    updated_by = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)
    weight = models.IntegerField(blank=True, null=True)
    confidential = models.BooleanField()
    due_date = models.DateField(blank=True, null=True)
    moved_to = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True, related_name='issuemovedto')
    lock_version = models.IntegerField(blank=True, null=True)
    title_html = models.TextField(blank=True, null=True)
    description_html = models.TextField(blank=True, null=True)
    time_estimate = models.IntegerField(blank=True, null=True)
    relative_position = models.IntegerField(blank=True, null=True)
    service_desk_reply_to = models.CharField(max_length=255, blank=True, null=True)
    cached_markdown_version = models.IntegerField(blank=True, null=True)
    last_edited_at = models.DateTimeField(blank=True, null=True)
    last_edited_by_id = models.IntegerField(blank=True, null=True)
    discussion_locked = models.BooleanField(blank=True, null=True)
    closed_at = models.DateTimeField(blank=True, null=True)
    closed_by = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True, related_name='issueclosedby')
    state_id = models.SmallIntegerField()
    duplicated_to = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    promoted_to_epic_id = models.IntegerField(blank=True, null=True)
    health_status = models.SmallIntegerField(blank=True, null=True)
    external_key = models.CharField(max_length=255, blank=True, null=True)
    sprint_id = models.BigIntegerField(blank=True, null=True)
    blocking_issues_count = models.IntegerField()
    issue_type = models.SmallIntegerField()
    upvotes_count = models.IntegerField()
    work_item_type_id = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'issues'
        unique_together = (('project', 'external_key'), ('project', 'iid'),)


class Notes(models.Model):
    note = models.TextField(blank=True, null=True)
    noteable_type = models.CharField(max_length=255, blank=True, null=True)
    author_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    project = models.ForeignKey('Projects', models.DO_NOTHING, blank=True, null=True)
    attachment = models.CharField(max_length=255, blank=True, null=True)
    line_code = models.CharField(max_length=255, blank=True, null=True)
    commit_id = models.CharField(max_length=255, blank=True, null=True)
    noteable_id = models.IntegerField(blank=True, null=True)
    system = models.BooleanField()
    st_diff = models.TextField(blank=True, null=True)
    updated_by_id = models.IntegerField(blank=True, null=True)
    type = models.CharField(max_length=255, blank=True, null=True)
    position = models.TextField(blank=True, null=True)
    original_position = models.TextField(blank=True, null=True)
    resolved_at = models.DateTimeField(blank=True, null=True)
    resolved_by_id = models.IntegerField(blank=True, null=True)
    discussion_id = models.CharField(max_length=255, blank=True, null=True)
    note_html = models.TextField(blank=True, null=True)
    cached_markdown_version = models.IntegerField(blank=True, null=True)
    change_position = models.TextField(blank=True, null=True)
    resolved_by_push = models.BooleanField(blank=True, null=True)
    review_id = models.BigIntegerField(blank=True, null=True)
    confidential = models.BooleanField(blank=True, null=True)
    last_edited_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'notes'


class Projects(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    path = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    creator_id = models.IntegerField(blank=True, null=True)
    namespace_id = models.IntegerField()
    last_activity_at = models.DateTimeField(blank=True, null=True)
    import_url = models.CharField(max_length=255, blank=True, null=True)
    visibility_level = models.IntegerField()
    archived = models.BooleanField()
    avatar = models.CharField(max_length=255, blank=True, null=True)
    merge_requests_template = models.TextField(blank=True, null=True)
    star_count = models.IntegerField()
    merge_requests_rebase_enabled = models.BooleanField(blank=True, null=True)
    import_type = models.CharField(max_length=255, blank=True, null=True)
    import_source = models.CharField(max_length=255, blank=True, null=True)
    approvals_before_merge = models.IntegerField()
    reset_approvals_on_push = models.BooleanField(blank=True, null=True)
    merge_requests_ff_only_enabled = models.BooleanField(blank=True, null=True)
    issues_template = models.TextField(blank=True, null=True)
    mirror = models.BooleanField()
    mirror_last_update_at = models.DateTimeField(blank=True, null=True)
    mirror_last_successful_update_at = models.DateTimeField(blank=True, null=True)
    mirror_user_id = models.IntegerField(blank=True, null=True)
    shared_runners_enabled = models.BooleanField()
    runners_token = models.CharField(max_length=255, blank=True, null=True)
    build_coverage_regex = models.CharField(max_length=255, blank=True, null=True)
    build_allow_git_fetch = models.BooleanField()
    build_timeout = models.IntegerField()
    mirror_trigger_builds = models.BooleanField()
    pending_delete = models.BooleanField(blank=True, null=True)
    public_builds = models.BooleanField()
    last_repository_check_failed = models.BooleanField(blank=True, null=True)
    last_repository_check_at = models.DateTimeField(blank=True, null=True)
    only_allow_merge_if_pipeline_succeeds = models.BooleanField()
    has_external_issue_tracker = models.BooleanField(blank=True, null=True)
    repository_storage = models.CharField(max_length=255)
    repository_read_only = models.BooleanField(blank=True, null=True)
    request_access_enabled = models.BooleanField()
    has_external_wiki = models.BooleanField(blank=True, null=True)
    ci_config_path = models.CharField(max_length=255, blank=True, null=True)
    lfs_enabled = models.BooleanField(blank=True, null=True)
    description_html = models.TextField(blank=True, null=True)
    only_allow_merge_if_all_discussions_are_resolved = models.BooleanField(blank=True, null=True)
    repository_size_limit = models.BigIntegerField(blank=True, null=True)
    printing_merge_request_link_enabled = models.BooleanField()
    auto_cancel_pending_pipelines = models.IntegerField()
    service_desk_enabled = models.BooleanField(blank=True, null=True)
    cached_markdown_version = models.IntegerField(blank=True, null=True)
    delete_error = models.TextField(blank=True, null=True)
    last_repository_updated_at = models.DateTimeField(blank=True, null=True)
    disable_overriding_approvers_per_merge_request = models.BooleanField(blank=True, null=True)
    storage_version = models.SmallIntegerField(blank=True, null=True)
    resolve_outdated_diff_discussions = models.BooleanField(blank=True, null=True)
    remote_mirror_available_overridden = models.BooleanField(blank=True, null=True)
    only_mirror_protected_branches = models.BooleanField(blank=True, null=True)
    pull_mirror_available_overridden = models.BooleanField(blank=True, null=True)
    jobs_cache_index = models.IntegerField(blank=True, null=True)
    mirror_overwrites_diverged_branches = models.BooleanField(blank=True, null=True)
    external_authorization_classification_label = models.CharField(max_length=255, blank=True, null=True)
    external_webhook_token = models.CharField(max_length=255, blank=True, null=True)
    pages_https_only = models.BooleanField(blank=True, null=True)
    packages_enabled = models.BooleanField(blank=True, null=True)
    merge_requests_author_approval = models.BooleanField(blank=True, null=True)
    pool_repository_id = models.BigIntegerField(blank=True, null=True)
    runners_token_encrypted = models.CharField(max_length=255, blank=True, null=True)
    bfg_object_map = models.CharField(max_length=255, blank=True, null=True)
    detected_repository_languages = models.BooleanField(blank=True, null=True)
    merge_requests_disable_committers_approval = models.BooleanField(blank=True, null=True)
    require_password_to_approve = models.BooleanField(blank=True, null=True)
    emails_disabled = models.BooleanField(blank=True, null=True)
    max_pages_size = models.IntegerField(blank=True, null=True)
    max_artifacts_size = models.IntegerField(blank=True, null=True)
    pull_mirror_branch_prefix = models.CharField(max_length=50, blank=True, null=True)
    marked_for_deletion_at = models.DateField(blank=True, null=True)
    marked_for_deletion_by_user = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)
    remove_source_branch_after_merge = models.BooleanField(blank=True, null=True)
    suggestion_commit_message = models.CharField(max_length=255, blank=True, null=True)
    autoclose_referenced_issues = models.BooleanField(blank=True, null=True)
    project_namespace_id = models.BigIntegerField(unique=True, blank=True, null=True)
    hidden = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'projects'


class Projectspent(models.Model):
    id = models.IntegerField(blank=True, null=False, primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    creator = models.CharField(max_length=255, blank=True, null=True)
    spent = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    spent_txt = models.TextField(blank=True, null=True)

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'projectspent'


class Timelogs(models.Model):
    time_spent = models.IntegerField()
    user_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    issue = models.ForeignKey(Issues, models.DO_NOTHING, blank=True, null=True)
    merge_request_id = models.IntegerField(blank=True, null=True)
    spent_at = models.DateTimeField(blank=True, null=True)
    note = models.ForeignKey(Notes, models.DO_NOTHING, blank=True, null=True)
    project = models.ForeignKey(Projects, models.DO_NOTHING, blank=True, null=True)
    summary = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'timelogs'


class TrackappUsersspentonprojects(models.Model):
    id = models.BigAutoField(primary_key=True)
    project = models.CharField(max_length=254, blank=True, null=True)
    issue = models.CharField(max_length=254, blank=True, null=True)
    name = models.CharField(max_length=254, blank=True, null=True)
    spent = models.IntegerField()
    date_spent = models.DateTimeField(blank=True, null=True)
    note = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'trackApp_usersspentonprojects'


class Users(models.Model):
    email = models.CharField(unique=True, max_length=255)
    encrypted_password = models.CharField(max_length=255)
    reset_password_token = models.CharField(unique=True, max_length=255, blank=True, null=True)
    reset_password_sent_at = models.DateTimeField(blank=True, null=True)
    remember_created_at = models.DateTimeField(blank=True, null=True)
    sign_in_count = models.IntegerField(blank=True, null=True)
    current_sign_in_at = models.DateTimeField(blank=True, null=True)
    last_sign_in_at = models.DateTimeField(blank=True, null=True)
    current_sign_in_ip = models.CharField(max_length=255, blank=True, null=True)
    last_sign_in_ip = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    admin = models.BooleanField()
    projects_limit = models.IntegerField()
    skype = models.CharField(max_length=255)
    linkedin = models.CharField(max_length=255)
    twitter = models.CharField(max_length=255)
    failed_attempts = models.IntegerField(blank=True, null=True)
    locked_at = models.DateTimeField(blank=True, null=True)
    username = models.CharField(max_length=255, blank=True, null=True)
    can_create_group = models.BooleanField()
    can_create_team = models.BooleanField()
    state = models.CharField(max_length=255, blank=True, null=True)
    color_scheme_id = models.IntegerField()
    password_expires_at = models.DateTimeField(blank=True, null=True)
    created_by_id = models.IntegerField(blank=True, null=True)
    last_credential_check_at = models.DateTimeField(blank=True, null=True)
    avatar = models.CharField(max_length=255, blank=True, null=True)
    confirmation_token = models.CharField(unique=True, max_length=255, blank=True, null=True)
    confirmed_at = models.DateTimeField(blank=True, null=True)
    confirmation_sent_at = models.DateTimeField(blank=True, null=True)
    unconfirmed_email = models.CharField(max_length=255, blank=True, null=True)
    hide_no_ssh_key = models.BooleanField(blank=True, null=True)
    website_url = models.CharField(max_length=255)
    admin_email_unsubscribed_at = models.DateTimeField(blank=True, null=True)
    notification_email = models.CharField(max_length=255, blank=True, null=True)
    hide_no_password = models.BooleanField(blank=True, null=True)
    password_automatically_set = models.BooleanField(blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    encrypted_otp_secret = models.CharField(max_length=255, blank=True, null=True)
    encrypted_otp_secret_iv = models.CharField(max_length=255, blank=True, null=True)
    encrypted_otp_secret_salt = models.CharField(max_length=255, blank=True, null=True)
    otp_required_for_login = models.BooleanField()
    otp_backup_codes = models.TextField(blank=True, null=True)
    public_email = models.CharField(max_length=255, blank=True, null=True)
    dashboard = models.IntegerField(blank=True, null=True)
    project_view = models.IntegerField(blank=True, null=True)
    consumed_timestep = models.IntegerField(blank=True, null=True)
    layout = models.IntegerField(blank=True, null=True)
    hide_project_limit = models.BooleanField(blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    unlock_token = models.CharField(unique=True, max_length=255, blank=True, null=True)
    otp_grace_period_started_at = models.DateTimeField(blank=True, null=True)
    external = models.BooleanField(blank=True, null=True)
    incoming_email_token = models.CharField(max_length=255, blank=True, null=True)
    organization = models.CharField(max_length=255, blank=True, null=True)
    auditor = models.BooleanField()
    require_two_factor_authentication_from_group = models.BooleanField()
    two_factor_grace_period = models.IntegerField()
    last_activity_on = models.DateField(blank=True, null=True)
    notified_of_own_activity = models.BooleanField(blank=True, null=True)
    preferred_language = models.CharField(max_length=255, blank=True, null=True)
    email_opted_in = models.BooleanField(blank=True, null=True)
    email_opted_in_ip = models.CharField(max_length=255, blank=True, null=True)
    email_opted_in_source_id = models.IntegerField(blank=True, null=True)
    email_opted_in_at = models.DateTimeField(blank=True, null=True)
    theme_id = models.SmallIntegerField(blank=True, null=True)
    accepted_term_id = models.IntegerField(blank=True, null=True)
    feed_token = models.CharField(max_length=255, blank=True, null=True)
    include_private_contributions = models.BooleanField(blank=True, null=True)
    private_profile = models.BooleanField()
    roadmap_layout = models.SmallIntegerField(blank=True, null=True)
    commit_email = models.CharField(max_length=255, blank=True, null=True)
    group_view = models.IntegerField(blank=True, null=True)
    managing_group_id = models.IntegerField(blank=True, null=True)
    static_object_token = models.CharField(unique=True, max_length=255, blank=True, null=True)
    first_name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    role = models.SmallIntegerField(blank=True, null=True)
    user_type = models.SmallIntegerField(blank=True, null=True)
    static_object_token_encrypted = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users'


class Userspent(models.Model):
    id = models.IntegerField(blank=True, null=False, primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    spent = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    spent_txt = models.TextField(blank=True, null=True)

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'userspent'


class Userspentonprojects(models.Model):
    id = models.IntegerField(blank=True, null=False, primary_key=True)
    project = models.CharField(max_length=255, blank=True, null=True)
    issue = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    spent = models.TextField(blank=True, null=True)
    date_spent = models.DateTimeField(blank=True, null=True)
    note = models.TextField(blank=True, null=True)

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'userspentonprojects'
