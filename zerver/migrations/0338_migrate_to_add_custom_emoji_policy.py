# Generated by Django 3.2.2 on 2021-05-15 18:01

from django.db import migrations
from django.db.backends.postgresql.schema import BaseDatabaseSchemaEditor
from django.db.migrations.state import StateApps


def migrate_to_add_custom_emoji_policy(
    apps: StateApps, schema_editor: BaseDatabaseSchemaEditor
) -> None:
    Realm = apps.get_model("zerver", "Realm")
    Realm.ADD_CUSTOM_EMOJI_MEMBERS_ONLY = 1
    Realm.ADD_CUSTOM_EMOJI_ADMINS_ONLY = 2
    Realm.objects.filter(add_emoji_by_admins_only=False).update(
        add_custom_emoji_policy=Realm.ADD_CUSTOM_EMOJI_MEMBERS_ONLY
    )
    Realm.objects.filter(add_emoji_by_admins_only=True).update(
        add_custom_emoji_policy=Realm.ADD_CUSTOM_EMOJI_ADMINS_ONLY
    )


def reverse_migrate_to_add_custom_emoji_policy(
    apps: StateApps, schema_editor: BaseDatabaseSchemaEditor
) -> None:
    Realm = apps.get_model("zerver", "Realm")
    Realm.ADD_CUSTOM_EMOJI_MEMBERS_ONLY = 1
    Realm.ADD_CUSTOM_EMOJI_ADMINS_ONLY = 2
    Realm.objects.filter(add_custom_emoji_policy=Realm.ADD_CUSTOM_EMOJI_MEMBERS_ONLY).update(
        add_emoji_by_admins_only=False
    )
    Realm.objects.filter(add_custom_emoji_policy=Realm.ADD_CUSTOM_EMOJI_ADMINS_ONLY).update(
        add_emoji_by_admins_only=True
    )


class Migration(migrations.Migration):
    dependencies = [
        ("zerver", "0337_realm_add_custom_emoji_policy"),
    ]

    operations = [
        migrations.RunPython(
            migrate_to_add_custom_emoji_policy,
            reverse_code=reverse_migrate_to_add_custom_emoji_policy,
            elidable=True,
        ),
    ]
