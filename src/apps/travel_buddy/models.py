# from django.db import models
# from datetime import datetime
# # import bcrypt
# from django.contrib.auth import get_user_model
# User = get_user_model()
# now = str(datetime.now())

# # class UserManager(models.Manager):

# #     def reg_validator(self, form):
# #         errors = []

# #         if not form['name']:
# #             errors.append("Name field is required")
# #         if not form['username']:
# #             errors.append("Username is required")
# #         if len(form['name']) < 2:
# #             errors.append("Name must have at least 3 characters.")
# #         if len(form['username']) < 2:
# #             errors.append("Username must have at least 3 characters.")
# #         elif User.objects.filter(username=form['username']):
# #              errors.append("Account already exists.")
# #         if len(form['passwd']) < 8:
# #             errors.append("Password must have at least 8 characters.")
# #         if form['passwd'] != form['pass_confirm']:
# #             errors.append("Passwords do not match")

# #         if not errors:
# #             hash1 = bcrypt.hashpw(form['passwd'].encode(), bcrypt.gensalt())
# #             user = User.objects.create( name=form['name'], username=form['username'], passwd=hash1)
# #             # hashed_pass = bcrypt.hashpw(form['passwd'].encode(), bcrypt.gensalt())
# #             # user = User.objects.create(name=form['name'], username=form['username'], passwd=hashed_pass.decode("utf-8"))

# #             return (True, user)
# #         else:
# #             return (False, errors)

# #     def loginValidator(self, form):
# #         errors = []

# #         if not form['username'] or not form['passwd']:
# #             errors.append('Username and Password are required.')
# #         elif not User.objects.filter(username=form['username']):
# #             errors.append("Please register first")
# #         else:
# #             user = User.objects.filter(username=form['username'])
# #             if not bcrypt.checkpw(form['passwd'].encode(), user[0].passwd.encode()):
# #                 # print(bcrypt.checkpw(form['passwd'].encode(), user[0].passwd.encode()))
# #                 errors.append('Password does not match record.')

# #         if not errors:
# #             return (True, user[0])
# #         else:
# #             return (False, errors)

# class DestinationManager(models.Manager):

#     def dest_validator(self, form, user_id):
#         errors = []

#         if not form['location']:
#             errors.append("Location is required")
#         if not form['description']:
#             errors.append("Description is required")
#         if len(form['description']) < 5:
#             errors.append('Description must be at least 5 characters.')
#         if not form['start_date']:
#             errors.append("Please select a Departure date")
#         elif form['start_date'] < now:
#             errors.append('Start date must be in the future')

#         if not form['end_date']:
#             errors.append('End date is required')
#         elif form['end_date'] < now:
#             errors.append('End date must be in the future')

#         if form['end_date'] < form['start_date']:
#             errors.append('End date must be after start date')


#         if not errors:
#             this_user = User.objects.get(id=user_id)
#             location = Destination.objects.create(location=form['location'], description=form['description'], planner=this_user, start_date=form['start_date'], end_date=form['end_date'])

#             # before returning the location we add it to the logged-in users list.
#             this_user.have_joined.add(location)

#             return (True, location)
#         else:
#             return (False, errors)


# # class User(models.Model):
# #     name       = models.CharField(max_length=255)
# #     username   = models.CharField(max_length=255)
# #     passwd     = models.CharField(max_length=255)
# #     created_at = models.DateTimeField(auto_now_add=True)
# #     updated_at = models.DateTimeField(auto_now=True)

# #     def __repr__(self):
# #         return "<User: {}| {} : {} | {}>".format(self.id, self.name, self.username, self.passwd)

# #     objects = UserManager()

# #     # user_dest - ( Connects to Destination )
#     # have_joined - ( Connects to Join TABLE )

# class Destination(models.Model):
#     location      = models.CharField(max_length=255)
#     description   = models.CharField(max_length=255)
#     start_date    = models.DateField(auto_now=False)
#     end_date      = models.DateField(auto_now=False)
#     created_at    = models.DateTimeField(auto_now_add=True)
#     updated_at    = models.DateTimeField(auto_now=True)

#     planner       = models.ForeignKey(User, related_name="user_dest", on_delete=models.CASCADE)
#     users_on_trip = models.ManyToManyField(User, related_name="have_joined")

#     def __repr__(self):
#         return "<Destination: {}| {} , {} by:{}: {} to {}>".format(self.id, self.location, self.description, self.planner, self.start_date, self.end_date)

#     objects = DestinationManager()
