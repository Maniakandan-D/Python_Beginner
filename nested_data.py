albums = [
    ("welcome to my nightmare", "alice cooper", 1975,
     [
         (1, "welcome to my nightmare"),
         (2, "devil's food"),
         (3, "the black widow"),
         (4, "some folks"),
     ]
     ),
    ("bad company", "bad company", 1974,
     [
         (1, "can't get enough"),
         (2, "rock steady"),
         (3, "ready for love"),
         (4, "don't let me down"),
         (5, "bad company"),
     ]
     ),
    ("night flight", "budgie", 1981,
     [
         (1, "I turned to stone"),
         (2, "keeping a rendezvous"),
         (3, "reaper of the glory"),
         (4, "she used me up"),
     ]
     ),
    ("more mayhem", "imelda may", 2011,
     [
         (1, "pulling the ring"),
         (2, "psyco"),
         (3, "mayhem"),
         (4, "kentish town walts")
     ]
     )
]
for name, artist, year, songs in albums:
    print("album: {}, artist: {}, year: {}, songs: {}"
          .format(name, artist, year, songs))

print()

album = albums[2]
print(album)

songs = albums[3]
print(songs)

song = songs[3]
print(songs)
print(songs[1])

print()

print(albums[3])
print(albums[3][3])
print(albums[3][3][2])
print(albums[3][3][2][1])



