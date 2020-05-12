from django.db import models


class TextComment(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    content = models.TextField(db_index=True)
