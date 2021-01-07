import jiosaavn
js=jiosaavn.search_for_song('scared to be lonely',False)
for t in js:
    print('Song Name - ',t['song'])
    print('Album Name - ',t['album'])
    print('Year - ',t['year'])
    print('Artists - ',t['primary_artists'])
    print('Song Link - ',t['media_url'])
    print('__________________________________________________')