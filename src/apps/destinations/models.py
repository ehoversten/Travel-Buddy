from django.db import models
from datetime import datetime
from .signal import destination_pre_save_receiver
from django.db.models.signals import pre_save, post_save
# import bcrypt
from django.contrib.auth import get_user_model
User = get_user_model()
now = str(datetime.now())

class DestinationManager(models.Manager):

    def dest_validator(self, form, user_id):
        errors = []

        if not form['location']:
            errors.append("Location is required")
        if not form['description']:
            errors.append("Description is required")
        if len(form['description']) < 5:
            errors.append('Description must be at least 5 characters.')
        if not form['start_date']:
            errors.append("Please select a Departure date")
        elif form['start_date'] < now:
            errors.append('Start date must be in the future')

        if not form['end_date']:
            errors.append('End date is required')
        elif form['end_date'] < now:
            errors.append('End date must be in the future')

        if form['end_date'] < form['start_date']:
            errors.append('End date must be after start date')


        if not errors:
            this_user = User.objects.get(id=user_id)
            location = Destination.objects.create(location=form['location'], description=form['description'], planner=this_user, start_date=form['start_date'], end_date=form['end_date'])

            # before returning the location we add it to the logged-in users list.
            this_user.have_joined.add(location)

            return (True, location)
        else:
            return (False, errors)


class Destination(models.Model):
    completed       = models.BooleanField(default=False)
    location        = models.CharField(max_length=255)
    description     = models.CharField(max_length=255)
    start_date      = models.DateField(auto_now=False)
    end_date        = models.DateField(auto_now=False)
    timestamp       = models.DateTimeField(auto_now_add=True)

    planner         = models.ForeignKey(User, related_name="user_planner", on_delete=models.CASCADE)
    users_on_trip   = models.ManyToManyField(User, related_name="others_on_trip")

    def __str__(self):
        return str(self.location)

    objects = DestinationManager()

pre_save.connect(destination_pre_save_receiver, sender=Destination) 