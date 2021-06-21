from django.db.models.signals import pre_save
from django.dispatch import receiver

from .models import Singer, Translation, Track, Comment
from .service import handle_for_audit


@receiver(pre_save, sender=Singer)
def audit_save(sender, instance, **kwargs):
    fields = ["name", "owner"]
    handle_for_audit(fields, sender, instance)


@receiver(pre_save, sender=Track)
def audit_save(sender, instance, **kwargs):
    fields = ["track_name", "text", "original_language", "singer", "owner"]
    handle_for_audit(fields, sender, instance)


@receiver(pre_save, sender=Translation)
def audit_save(sender, instance, **kwargs):
    fields = ["track_id", "text", "language", "auto_translate", "owner"]
    handle_for_audit(fields, sender, instance)


@receiver(pre_save, sender=Comment)
def audit_save(sender, instance, **kwargs):
    fields = ["track_id", "message", "mark", "owner"]
    handle_for_audit(fields, sender, instance)
