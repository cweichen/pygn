import sys, pygn, json


clientID = '' # Enter your Client ID from developer.gracenote.com here
userID = '' # Get a User ID from pygn.register() - Only register once per end-user

print '\nSearch for artist "Kings of Convenience"\n'
result = pygn.search(clientID=clientID, userID=userID, artist='Kings of Convenience')
print json.dumps(result, sort_keys=True, indent=4)

print '\nSearch for album "Prism" by "Katy Perry"\n'
result = pygn.search(clientID=clientID, userID=userID, artist='Katy Perry', album='Prism')
print json.dumps(result, sort_keys=True, indent=4)

print '\nSearch for track "Drop" by "Cornelius"\n'
result = pygn.search(clientID=clientID, userID=userID, artist='Cornelius', track='Drop')
print json.dumps(result, sort_keys=True, indent=4)

print '\nSearching by album TOC\n'
result = pygn.search(clientID=clientID, userID=userID, toc='150 20512 30837 50912 64107 78357 90537 110742 126817 144657 153490 160700 175270 186830 201800 218010 237282 244062 262600 272929')
print json.dumps(result, sort_keys=True, indent=4)

print '\nGetting artist discography for "Daft Punk"\n'
result = pygn.get_discography(clientID=clientID, userID=userID, artist='Daft Punk')
print json.dumps(result, sort_keys=True, indent=4)

