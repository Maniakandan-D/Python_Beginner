from nested_data import albums

SONGS_LIST_INDEX = 3  # constant doesn't change it
SONGS_TITLE_INDEX = 1  # songs index position also constant

while True:
    print("Please choose your album invalid choice exists:")
    for index, (title, artist, year, songs) in enumerate(albums):
        print("{}: {}".format(index + 1, title))

    choice = int(input())  # from user and convert it into an integer
    if 1 <= choice <= len(albums):  # code within a required range # valid choice 1 to length 0 is also invalid
        songs_list = albums[choice - 1][SONGS_LIST_INDEX]  # 3
        # binding variable called songs_list # [3] indexing 3 is
        # fourth item
    else:
        break
    print("Please choose your song:")
    for index, (track_number, song) in enumerate(songs_list):
        print("{}: {}".format(index + 1, song))
    song_choice = int(input())
    if 1 <= song_choice <= len(songs_list):
        title = songs_list[song_choice - 1][SONGS_TITLE_INDEX]
        # we get tuple from song list using the user choice is index, so we have sub 1 index is zero based
        # second item tuple SONG_TITLE_INDEX constant .constant value on line 4
        print("Playing {}".format(title))

    else:
        print("Sorry!, you Entered invalid choice")

    print("=" * 50)
