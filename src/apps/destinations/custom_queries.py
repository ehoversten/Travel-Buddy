from django.db.models import Q # will implement search later
from django.db import models


class DestinationQuerySet(models.query.QuerySet):
    def completed(self):
        return self.filter(completed=True)
