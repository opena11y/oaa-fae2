from django.db import models
from django.contrib.auth.models import User
from registration.signals import user_registered
from timezone_field import TimeZoneField
from websiteResultGroups.models import WebsiteReportGroup

## User Profile
# The built-in Django User relation:

#class User(models.Model):
#   username      = models.CharField(max_length=30, unique=True)
#   first_name    = models.CharField(max_length=30, blank=True)
#   last_name     = models.CharField(max_length=30, blank=True)
#   email         = models.EmailField(blank=True)
#   password      = models.CharField(max_length=128)
#   is_staff      = models.BooleanField(default=False)
#   is_active     = models.BooleanField(default=True)
#   is_superuser  = models.BooleanField(default=False)
#   last_login    = models.DateTimeField()
#   date_joined   = models.DateTimeField()

# Custom classes for FAE


ACCT_TYPE_CHOICES = (
  (1, 'Standard'),
  (2, 'Level 2'),
  (3, 'Level 3'),
  (4, 'Level 4'),
  (5, 'Maximum'),
)


class UserProfile(models.Model):

    user                = models.OneToOneField(User, related_name="profile")
    acct_type           = models.IntegerField(choices=ACCT_TYPE_CHOICES, default=1)
    org                 = models.CharField(max_length=128, blank=True)
    email_announcements = models.BooleanField(default=True)

    max_archive = models.IntegerField(default=5)
    max_saved   = models.IntegerField(default=10)

    timezone = TimeZoneField(default='America/Chicago')
    
    multiple_urls_enabled           = models.BooleanField(default=False)
    website_authorization_enabled   = models.BooleanField(default=False)
    advanced_enabled                = models.BooleanField(default=False)

    ws_report_group = models.OneToOneField(WebsiteReportGroup, blank=True)
  
    def __unicode__(self):
        return self.user.username  


    def get_account_type(self):
      for shortp, longp in ACCT_TYPE_CHOICES:
          if shortp == self.acct_type:
              return longp
    
    
# creates new UserProfile when new user registers 
def user_registered_callback(sender, user, request, **kwargs):
    profile = UserProfile(user = user)
    profile.acct_type = 1
    profile.org = ''
    profile.save()
   
    # Update first and last name for user
    user.first_name = request.POST['first_name'] 
    user.last_name = request.POST['last_name']
    user.save()
 
user_registered.connect(user_registered_callback)  