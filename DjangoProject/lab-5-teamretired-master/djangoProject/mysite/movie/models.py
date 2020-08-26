from django.db import models

# Create your models here.

class Album(models.Model):
#The following is a method of Album class
   def __str__(self):
     #show the album_title, artist
      return  self.mainActor + ", " + self.filmTitle + ", " + self.director+ ", " + self.genre
#end of __str__()


   # holds the name of the mainActor max length 250 chars
   mainActor = models.CharField(max_length = 250)
##
   # holds filmTitle name
   filmTitle = models.CharField(max_length = 500)
##
   # holds the director name
   director = models.CharField(max_length = 100)
##
   # holds genre name
   genre = models.CharField(max_length = 1000)
#end of class Album()

# Create your models here.
