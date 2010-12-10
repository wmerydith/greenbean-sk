# Placeholder of new datastore models.

#Took out the import facebook - this is in the main file

from google.appengine.ext import db


# Enforce Twitter's 140 character limit.
def check_length(string):
  if len(string) > 140:
    raise db.BadValueError('Status cannot be more than 140 characters')
  return string

# User needs to accomodate both FB, Twitter and Google.  Not sure if this is 
# possible.
class User(db.Model):
  name = db.StringProperty(required=True)
  profile_url = db.StringProperty(required=True)
  fb_access_token = db.StringProperty(required=True)
  fb_id = db.StringProperty(required=True)
  created = db.DateTimeProperty(auto_now_add=True)
  updated = db.DateTimeProperty(auto_now=True)
  # TODO: provide a common way to define places for Users of FB, Twitter . . .
  current_location = db.ReferenceProperty(Location, required=True)

# Brag is a status message posted by a User that is bragging about an 
# accomplishment under one or more Categories.  Brags are limited to 140
# characters.  Brags are associated with a specific Location.  Brags can be
# submitted (originate) via this web application or via a 3rd party network 
# like Facebook or Twitter.
class Brag(db.Model):
  message = db.StringProperty(required=True, validator=check_length)
  create_date = db.DateTimeProperty(auto_now_add=True)
  category = db.ReferenceProperty(Category, required=True)
  user = db.ReferenceProperty(User, required=True)
  location = db.ReferenceProperty(Location, required=True)
  origin = db.StringProperty(required=True)

# Bean is a vote on a specific Brag.
class Bean(db.Model):
  brag = db.ReferenceProperty(Brag, require=True)	
  user = db.ReferenceProperty(User, required=True)
  created = db.DateTimeProperty(auto_now_add=True)

# Category provides taxonomy for Brags.
  class Category(db.Model):
    name = db.ReferenceProperty(required=True)

# Location provides place context for Brags.
  class Location(db.Model):
    city = db.StringProperty(required=True)
    state = db.StringProperty(required=True)
    country = db.StringProperty(required=True)

# These are the total Beans awarded to each Brag.
class BragBeans(db.Model):
  brag = db.ReferenceProperty(Brag, require=True)	
  bean_count = db.IntegerProperty(required=True)
  updated = db.DateTimeProperty(auto_now=True)

# These are the total Beans awarded to all the Brags of a specific User.
class UserBeans(db.Model):
  user = db.ReferenceProperty(User, required=True)
  bean_count = db.IntegerProperty(required=True)
  updated = db.DateTimeProperty(auto_now=True)

# These are the total Beans awarded to all the Brags associated to a specific
# Category.
class CategoryBeans(db.Model):
  category = db.ReferenceProperty(Category, required=True)
  bean_count = db.IntegerProperty(required=True)
  updated = db.DateTimeProperty(auto_now=True)

# Thease are all the Beans awarded to all the Brags associated to a specific
# Location.
class LocationBeans(db.Model):
  location = db.ReferenceProperty(Location, required=True)
  bean_count = db.IntegerProperty(required=True)
  updated = db.DateTimeProperty(auto_now=True)

