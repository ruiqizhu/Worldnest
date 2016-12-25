from django.db import models
import datetime
from django.utils import timezone

# event information
class PostEvent(models.Model):
    # user who posts the event
    user = models.IntegerField(default=0)
    title = models.CharField(max_length=200,default="")
    organizer = models.CharField(max_length=30,default="")
    # event location
    address = models.CharField(max_length = 200, default="")
    city = models.CharField(max_length = 200, default="")
    state = models.CharField(max_length = 200, default="")
    # event time
    start_time = models.DateTimeField(default = timezone.now())
    end_time = models.DateTimeField(default = timezone.now())
    # event info
    description = models.CharField(max_length=1000, default="")
    image = models.CharField(max_length=500,
        default="")
    ticket = models.CharField(max_length=500,default="")
    event_page = models.CharField(max_length=500,default="")
    # event category
    event_type = models.CharField(max_length = 200, default="")
    event_topic = models.CharField(max_length = 200, default="")
    # whther it is liked
    like = models.BooleanField(default=False)
    participate = models.BooleanField(default=False)
    # how suitable the event is for the user
    score = models.IntegerField(default=0)
    # latitude and longtitude
    lat = models.FloatField(default=0)
    lng = models.FloatField(default=0)

    def __str__(self): 
        return self.title

# information on the user
# registration system created though Registration Redux
class UserInfo(models.Model):
    user_id = models.IntegerField(default=0)
    image = models.CharField(max_length=300,default="")
    description = models.CharField(max_length=300,default="")
    # event types values
    attraction = models.IntegerField(default=1)
    trip = models.IntegerField(default=1)
    workshop = models.IntegerField(default=1)
    concert = models.IntegerField(default=1)
    conference = models.IntegerField(default=1)
    convention = models.IntegerField(default=1)
    gala = models.IntegerField(default=1)
    festival = models.IntegerField(default=1)
    game = models.IntegerField(default=1)
    networking = models.IntegerField(default=1)
    social = models.IntegerField(default=1)
    seminar = models.IntegerField(default=1)
    expo = models.IntegerField(default=1)
    # event topic values
    business = models.IntegerField(default=1)
    charity = models.IntegerField(default=1)
    culture = models.IntegerField(default=1)
    education = models.IntegerField(default=1)
    fashion = models.IntegerField(default=1)
    entertainment = models.IntegerField(default=1)
    food = models.IntegerField(default=1)
    politics = models.IntegerField(default=1)
    health = models.IntegerField(default=1)
    hobbies = models.IntegerField(default=1)
    lifestyle = models.IntegerField(default=1)
    music = models.IntegerField(default=1)
    performing = models.IntegerField(default=1)
    religion = models.IntegerField(default=1)
    technology = models.IntegerField(default=1)
    holiday = models.IntegerField(default=1)
    sports = models.IntegerField(default=1)
    travel = models.IntegerField(default=1)
    expo = models.IntegerField(default=1)

   





