from django.db import models
# TODO: Add model called User
# TODO: with Fiields : First Name, Last Name, Email
# TODO: MAKE MIGRATIONS
# TODO: Script populating with fake data
# TODO: confirm populating by admin page
# TODO: View extension for /user, this will be HTML list of the user names and emails,
# TODO: Using template taging to generate content from the User models
# TODO: Change urls.py to deal with Changes in user extensions
# Create your models here.
class User(models.Model):
    First_Name = models.CharField(max_length=264)
    Last_Name = models.CharField(max_length=264)
    Email = models.EmailField(max_length=254)

    def __str__(self):
        return self.name
