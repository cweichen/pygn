#pygn

pygn (pronounced "pigeon") is a simple Python client for the <a href="http://www.gracenote.com">Gracenote</a> Music API, which can retrieve Artist, Album and Track metadata with the most common options.

pygn allows you to look up artists, albums, and tracks in the Gracenote database, and returns a number of metadata fields, including:

* Basic metadata like Artist Name, Album Title, Track Title
* Descriptors like Genre, Origin, Mood, Tempo
* Related content like Album Art, Artist Image, Biographies
* Creating a radio playlist up to 25 titles based on track, artist, mood, era and genre
* Trigger events in the radio playlist as track played , track skipped, track_like/dislike
 

##Installation

Since pygn is (so far) contained in a single Python file, no installer is provided. Simply copy pygn.py to your working directory, or to your Python site-packages/dist-packages directory, and call 'import pygn'!

##Getting Started

You will need a Gracenote Client ID to use this module. Please visit https://developer.gracenote.com to get yours.

Each installed application also needs to have a User ID, which may be obtained by registering your Client ID with the Gracenote API. To do this, do:

	import pygn

	clientID = '*******-************************' # Enter your Client ID here
	userID = pygn.register(clientID)

This registration should be done only once per application to avoid hitting your API quota (i.e. definitely do NOT do this before every query). The userID can be stored in persistent storage (e.g. on the filesystem) and used for all subsequent pygn function calls.

Once you have your Client ID and User ID, you can start making queries.

To search for the Kings of Convenience track "Homesick" from their album "Riot On An Empty Street", do:

	metadata = pygn.search(clientID=clientID, userID=userID, artist='Kings Of Convenience', album='Riot On An Empty Street', track='Homesick')

The returned gnmetadata object is a Python dict containing multiple metadata fields.
	
	{
	    "album_art_url": "https://web.content.cddbp.net/cgi-bin/content-thin?id=8D43DA988315CC43&client=3675392&class=cover&origin=front&size=medium&type=image/jpeg&tag=02EtNKHYoxbmX81TvhkE3fi9TqbeRGUtLtq0..8BHgwpPbeO8Qr83xuw", 
	    "album_artist_name": "Kings Of Convenience", 
	    "album_gnid": "59247312-2ED193587EF0504C7A0C416ED66DA962", 
	    "album_title": "Riot On An Empty Street", 
	    "album_year": "2004", 
	    "artist_bio_url": "https://web.content.cddbp.net/cgi-bin/content-thin?id=22DA84B96832BF4F&client=3675392&class=biography&type=text/plain&tag=02UUefhCnS5BJ-esbokzJX7W22Yod1K16ehzV.cY7h1ReCwW.77g89DQ", 
	    "artist_era": {
	        "1": {
	            "ID": "29483", 
	            "TEXT": "2000's"
	        }
	    }, 
	    "artist_image_url": "https://web.content.cddbp.net/cgi-bin/content-thin?id=797304D567E8970F&client=3675392&class=image&size=medium&type=image/jpeg&tag=02pI.mKJmjXrmvZQ6Q18X8klZChtwp7oGtZDaoINl3OcH7owTe-soMkw", 
	    "artist_origin": {
	        "1": {
	            "ID": "29896", 
	            "TEXT": "Scandinavia"
	        }, 
	        "2": {
	            "ID": "29990", 
	            "TEXT": "Norway"
	        }
	    }, 
	    "artist_type": {
	        "1": {
	            "ID": "29422", 
	            "TEXT": "Male"
	        }, 
	        "2": {
	            "ID": "29432", 
	            "TEXT": "Male Duo"
	        }
	    }, 
	    "genre": {
	        "1": {
	            "ID": "25312", 
	            "TEXT": "Alternative & Punk"
	        }, 
	        "2": {
	            "ID": "35477", 
	            "TEXT": "Indie Rock"
	        }, 
	        "3": {
	            "ID": "25460", 
	            "TEXT": "Indie Pop"
	        }
	    }, 
	    "mood": {
	        "1": {
	            "ID": "42949", 
	            "TEXT": "Melancholy"
	        }, 
	        "2": {
	            "ID": "65343", 
	            "TEXT": "Light Melancholy"
	        }
	    }, 
	    "review_url": "https://web.content.cddbp.net/cgi-bin/content-thin?id=4045DA976DB1DEFA&client=3675392&class=review&type=text/plain&tag=02z.AZyq.HafSMqFFd.hLuKZpc.Vz8gOn-1fx8bdQM5Rih9jAIIEO9Mg", 
	    "tempo": {
	        "1": {
	            "ID": "34283", 
	            "TEXT": "Medium Tempo"
	        }, 
	        "2": {
	            "ID": "34289", 
	            "TEXT": "Medium Slow"
	        }, 
	        "3": {
	            "ID": "34311", 
	            "TEXT": "60s"
	        }
	    }, 
	    "track_artist_name": "", 
	    "track_gnid": "59247313-E198021B46C38679362C35619E93396B", 
	    "track_number": "1", 
	    "track_title": "Homesick"
	}
	
Note that URLs to related content (e.g. Album Art, Artist Image, etc) are not valid forever, so your application should download the content you want relatively soon after the lookup and cache it locally.

The search function requires a clientID, userID, and at least one of either artist, album, or track to be specified.

For example, you can do

	metadata = pygn.search(clientID=clientID, userID=userID, artist='CSS')

which will return the same gnmetadata object with metadata for the top album by CSS (which happens to be 'Cansei De Ser Sexy' at time of writing), with track-specific fields being blank

Calling:

	metadata = pygn.search(clientID=clientID, userID=userID, artist='Jaga Jazzist', album='What We Must')

will return a gnmetadata object with metadata for Jaga Jazzist's "What We Must" album, again with track-specific fields empty

#Rhythm API 
The Rhythm API generates a playlist based on a song, an artist, a genre, a mood, an era or any combination of these inputs.

A radio is set up as follows:

createRadio(clientID='', userID='', artist='', track='', mood='', era='', genre='', popularity ='', similarity = '', count='10')

artist: the track artist
track: the title of the song
mood: a mood ID from the moods below
era: an era ID from the eras below
genre: a genre ID from the genres below
popularity: The popularity threshold of the song, 0 means any popularity, 1000 means only the most popular songs. 
Similarity: How similar should the playlist be to the seed. This parameter determines how narrow the playlist is. 1000 set the
count: Number of songs in the intially created playlist, specify any number between 2 and 25 to generate a playlist

#Events 
TRACK_PLAYED - track marked as played. Moves the play queue (drops track being played and adds additional track to end of queue)
TRACK_SKIPPED - track marked as skipped. Moves the play queue.
TRACK_LIKE - track marked as liked. Does not move the play queue.
TRACK_DISLIKE - track marked as disliked. Refreshes the playlist queue.
ARTIST_LIKE - artist marked as liked. Does not move the play queue.
ARTIST_DISLIKE  - artist marked as disliked. Refreshes the playlist queue.


