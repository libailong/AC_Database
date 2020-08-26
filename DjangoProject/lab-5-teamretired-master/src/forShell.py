# Date: 8 March 2019
# Name(s): Matt Marconi and Steve Li


# A sample code for pasting into the Django shell.
# Check your notes and slides to learn to use the shell utility.

# above code is all on one line
#a = Album(artist = "The Bill-Browns", album_title = "Ready or not", genre="Rock", album_logo = "Find-Link-Of-Image-Online")
from movie.models import Album
a = Album(mainActor = "Robert Downey Jr. ", filmtitle = "The Avengers ", director = "Joss Whedon ", genre = "Action")
# Now save your object and Django will populate the Database!
a.save()

from movie.models import Album
a = Album(mainActor = "Robert Downey Jr. ", filmTitle = "The Avengers: Age of Ultron ", director = "Joss Whedon ", genre = "Action")
a.save()

from movie.models import Album
a = Album(mainActor = "Robert Downey Jr. ", filmTitle = "The Avengers: Infinity War ", director = "Anthony Russo ", genre = "Action")
a.save()

from movie.models import Album
a = Album(mainActor = "Robert Downey Jr. ", filmTitle = "The Avengers: End Game ", director = "Anthony Russo ", genre = "Action")
a.save()

from movie.models import Album
a = Album(mainActor = "Robert Downey Jr. ", filmTitle = "Ironman ", director = "Jon Favreau ", genre = "Action")
a.save()



# show the ID (primary key)
a.id
