#pygn

pygn (pronounced "pigeon") is a simple Python client for the <a href="http://www.gracenote.com">Gracenote</a> Music API, which can retrieve Artist, Album and Track metadata with the most common options.

pygn allows you to look up artists, albums, and tracks in the Gracenote database, and returns a number of metadata fields, including:

* Basic metadata like Artist Name, Album Title, Track Title
* Descriptors like Genre, Origin, Mood, Tempo
* Related content like Album Art, Artist Image, Biographies

##Installation

Since pygn is (so far) contained in a single Python file, no installer is provided. Simply copy pygn.py to your working directory, or to your Python site-packages/dist-packages directory, and call 'import pygn'!

##Getting Started

You will need a Gracenote Client ID/Tag pair to use this module. Please contact developers@gracenote.com to get these.

Each installed application also needs to have a User ID/Tag, which may be obtained by registering your Client ID/Tag with the Gracenote API. To do this, do:

	import pygn

	clientID = '*******' # Enter your Client ID here
	clientTag = '***************' # Enter your Client Tag here
	userID, userTag = pygn.getUserID(clientID, clientTag)

This registration should be done only once per application to avoid hitting your API quota (i.e. definitely do NOT do this before every query). The userID and userTag can be stored in persistent storage (e.g. on the filesystem) and used for all subsequent pygn function calls.

Once you have your Client ID/Tag and User ID/Tag, you can start making queries.

To search for David Bowie's 'Moss Garden' from his '"Heroes"' album, do:

	metadata = pygn.lookupTrack(clientID, clientTag, userID, userTag, 'David Bowie', 'Heroes', 'Moss Garden')

The returned gnmetadata object is a Python dict containing multiple metadata fields, see pygn.py for the full list.

If you don't know which album a track is on (or don't care which album version you get), you can simply leave that parameter blank:

	metadata = pygn.lookupTrack(clientID, clientTag, userID, userTag, 'David Bowie', '', 'Moss Garden')

pygn also provides convenience functions to look up just an Artist or just an Album. Doing:

	metadata = pygn.lookupArtist(clientID, clientTag, userID, userTag, 'CSS')

will return the same gnmetadata object with metadata for the top album by the specified Artist (with track-specific fields being blank) Calling:

	metadata = pygn.lookupAlbum(clientID, clientTag, userID, userTag, 'Gotye', 'Boardface')

will return a gnmetadata object with metadata for Gotye's "Boardface" album (with track-specific fields empty again)
