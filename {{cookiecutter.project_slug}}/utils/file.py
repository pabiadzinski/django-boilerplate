import os
from django.conf import settings
from django.core.exceptions import ValidationError


def get_upload_path(instance, filename):
    return os.path.join(
        "images",
        "u_%d" % instance.owner.id,
        filename)


def validate_file_size(value):
    limit = settings.MAX_UPLOAD_SIZE * 1024 * 1024
    if value.size > limit:
        raise ValidationError(f'File too large. Size should not exceed {settings.MAX_UPLOAD_SIZE} MiB.')