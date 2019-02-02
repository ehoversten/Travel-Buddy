from datetime import datetime

from django.contrib.auth import get_user_model
from django.db import models
from django.db.models.signals import post_save, pre_save
from django.urls import reverse

from .signals import destination_pre_save_receiver
from .custom_queries import DestinationQuerySet
User = get_user_model()
now = str(datetime.now())

# implement adding images later


class DestinationManager(models.Manager):
    def get_queryset(self):
        return DestinationQuerySet(self.model, using=self._db)

    def get_by_id(self, id):
        qs = self.get_queryset().filter(id=id)
        if qs.count() == 1:
            return qs.first()
        return None

    def completed(self):  # Product.objects.featured()
        return self.get_queryset().completed()

    def update(self, request):  # adds or removes the authenticated user
        pass
    # def search(self, query):
    #     return self.get_queryset().active().search(query)

    def new(self, form, user=None):
        user_obj = user.id
        created = False
        obj = None
        errors = []
        if len(form.cleaned_data['description']) < 5:
            state = ' Description must be at least 5 characters'
            errors.append(state)
            form.add_error('description', state)
        if not form.cleaned_data['start_date']:
            state = ' Please select a Departure date'
            errors.append(state)
            form.add_error('description', state)
        if not form.cleaned_data['end_date']:
            errors.append('End date is required')

        if not errors:
            errors=None
            created = True
            obj = Destination.objects.create(location=form.cleaned_data['location'], description=form.cleaned_data['description'], planner=user, start_date=form.cleaned_data['start_date'], end_date=form.cleaned_data['end_date'])
            obj.users_on_trip.add(user_obj) # find a way of using the user model here instead --idk--?
            return (obj, errors,created)
        else:
            return (obj, errors, created)
        return obj, created


class Destination(models.Model):
    slug = models.SlugField(blank=True, unique=True)
    location = models.CharField(max_length=255)
    description = models.TextField()
    start_date = models.DateField(auto_now=False)
    end_date = models.DateField(auto_now=False)
    timestamp = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)

    planner = models.ForeignKey(
        User, related_name="user_planner", on_delete=models.CASCADE)
    users_on_trip = models.ManyToManyField(User, related_name="others_on_trip")

    def get_absolute_url(self):
        return reverse('travel:detail', args=[str(self.slug)])

    def __str__(self):
        return str(self.location)

    objects = DestinationManager()


pre_save.connect(destination_pre_save_receiver, sender=Destination)
