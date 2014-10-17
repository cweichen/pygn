from __future__ import print_function
import sys, pygn, json


clientID = '' # Enter your Client ID from developer.gracenote.com here
userID = '' # Get a User ID from pygn.register() - Only register once per end-user

print('\nSearch for artist "Kings of Convenience"\n')
result = pygn.search(clientID=clientID, userID=userID, artist='Kings of Convenience')
print(json.dumps(result, sort_keys=True, indent=4))

print('\nSearch for album "Prism" by "Katy Perry"\n')
result = pygn.search(clientID=clientID, userID=userID, artist='Katy Perry', album='Prism')
print(json.dumps(result, sort_keys=True, indent=4))

print('\nSearch for track "Drop" by "Cornelius"\n')
result = pygn.search(clientID=clientID, userID=userID, artist='Cornelius', track='Drop')
print(json.dumps(result, sort_keys=True, indent=4))

print('\nSearching by album TOC\n')
result = pygn.search(clientID=clientID, userID=userID, toc='150 20512 30837 50912 64107 78357 90537 110742 126817 144657 153490 160700 175270 186830 201800 218010 237282 244062 262600 272929')
print(json.dumps(result, sort_keys=True, indent=4))

print('\nGetting artist discography for "Daft Punk"\n')
result = pygn.get_discography(clientID=clientID, userID=userID, artist='Daft Punk')
print(json.dumps(result, sort_keys=True, indent=4))


# Example how to create a radio playlist by mood peaceful
result = pygn.createRadio(clientID, userID, mood='65322', popularity ='1000', similarity = '1000')
print(json.dumps(result, sort_keys=True, indent=4))

# Example how to create a radio playlist by genre classical music
result = pygn.createRadio(clientID, userID, genre='36061', popularity ='1000', similarity = '1000')
print(json.dumps(result, sort_keys=True, indent=4))

# Example how to create a radio playlist by era 1970
result = pygn.createRadio(clientID, userID, era='29486', popularity ='1000', similarity = '1000')
print(json.dumps(result, sort_keys=True, indent=4))

# Example how to create a radio playlist by artist and track
result = pygn.createRadio(clientID, userID, artist='Indila', track='Derniere Danse', mood='', era='', genre='36061', popularity ='', similarity = '1000')
print(json.dumps(result, sort_keys=True, indent=4))

# Example to trigger an event: track played
result = pygn.radioEvent(clientID, userID, radioID='84f652bfae095ee31c859a7f80ed9f6e', gnID='36890081-978D4C7F39C122C877CFF0CE946B4880', event ='TRACK_PLAYED', count='10')
print(json.dumps(result[0], sort_keys=True, indent=4))

# Example give feedback: track liked
result = pygn.radioEvent(clientID, userID, radioID='84f652bfae095ee31c859a7f80ed9f6e', gnID='36890081-978D4C7F39C122C877CFF0CE946B4880', event ='TRACK_LIKED', count='10')
print(json.dumps(result[0], sort_keys=True, indent=4))
