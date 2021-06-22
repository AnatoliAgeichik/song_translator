from django.db.models.signals import pre_save, pre_delete
from django.dispatch import receiver

from .models import Singer, Translation, Track, Comment
from .service import handle_for_audit, handle_for_audit_delete
from .utils import Comment_field, Track_field, Singer_field, Translation_field


@receiver(pre_save, sender=Singer)
def audit_save(sender, instance, **kwargs):
    handle_for_audit(Singer_field, sender, instance)


@receiver(pre_save, sender=Track)
def audit_save(sender, instance, **kwargs):
    handle_for_audit(Track_field, sender, instance)


@receiver(pre_save, sender=Translation)
def audit_save(sender, instance, **kwargs):
    handle_for_audit(Translation_field, sender, instance)


@receiver(pre_save, sender=Comment)
def audit_save(sender, instance, **kwargs):
    handle_for_audit(Comment_field, sender, instance)


@receiver(pre_delete, sender=Singer)
def audit_delete(sender, instance, **kwargs):
    handle_for_audit_delete(Singer_field, sender, instance)


@receiver(pre_delete, sender=Track)
def audit_delete(sender, instance, **kwargs):
    handle_for_audit_delete(Track_field, sender, instance)


@receiver(pre_delete, sender=Translation)
def audit_delete(sender, instance, **kwargs):
    handle_for_audit_delete(Translation_field, sender, instance)


@receiver(pre_delete, sender=Comment)
def audit_delete(sender, instance, **kwargs):
    handle_for_audit_delete(Comment_field, sender, instance)
