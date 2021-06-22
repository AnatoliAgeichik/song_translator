from rest_framework.pagination import PageNumberPagination
from rest_framework.exceptions import NotFound as NotFoundError
from rest_framework.response import Response
from rest_framework import status

from .models import AuditTable


class PaginationSingers(PageNumberPagination):
    page_size = 16
    max_page_size = 128


class PaginationTracks(PageNumberPagination):
    page_size = 10
    max_page_size = 100


class PaginationComments(PageNumberPagination):
    page_size = 2


class PaginationTranslation(PageNumberPagination):
    page_size = 2

    def generate_response(self, query_set, serializer_obj, request):
        try:
            page_data = self.paginate_queryset(query_set, request)
        except NotFoundError:
            return Response({"error": "No results found for the requested page"}, status=status.HTTP_400_BAD_REQUEST)

        serialized_page = serializer_obj(page_data, many=True)
        return self.get_paginated_response(serialized_page.data)


def add_to_audit(table_name, record_id, field_name, old_value, new_value, owner):
    AuditTable.objects.create(table_name=table_name, record_id=record_id, field_name=field_name,
                              old_value=old_value, new_value=new_value, author=owner)


def handle_for_audit(fields, sender, instance):
    if instance.id:
        obj = sender.objects.get(id=instance.id)
        if obj == instance.id:
            print("delete")
        for field in fields:
            field_object = sender._meta.get_field(field)
            field_value_old = field_object.value_from_object(obj)
            field_value_new = field_object.value_from_object(instance)
            if field_value_old != field_value_new:
                add_to_audit(sender, instance.id, field, field_value_old, field_value_new, instance.owner)
    else:
        for field in fields:
            field_object = sender._meta.get_field(field)
            field_value_new = field_object.value_from_object(instance)
            add_to_audit(sender, None, field, None, field_value_new, instance.owner)


def handle_for_audit_delete(fields, sender, instance):
    for field in fields:
        field_object = sender._meta.get_field(field)
        field_value_old = field_object.value_from_object(instance)
        add_to_audit(sender, instance.id, field, field_value_old, None, instance.owner)
