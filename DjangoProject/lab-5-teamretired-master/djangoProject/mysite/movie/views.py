# Create your views here.
from django.http import Http404 # for missing albums
from django.shortcuts import render
from django.template import loader
from .models import Album


def index(request):
        all_albums = Album.objects.all()
        template = loader.get_template('movie/index.html')
        return render(request, 'movie/index.html',{'all_albums':all_albums})
# check for valid ids.


# check for valid album_ids.
def detail(request, album_id):
	try: # check to see that the album exists
		album_current = Album.objects.get(pk=album_id)
	except Album.DoesNotExist:
		#display this message
		raise Http404("Sorry to say but the album does not exist.")
	return render(request, 'movie/detail.html', {'album' : album_current})
