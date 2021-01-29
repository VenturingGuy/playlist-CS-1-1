from Song import Song

class Playlist:
    def __init__(self):
        self.__first_song = None

    def add_song(self, title):

        # Creates a new Song object called new_song, points to the top song in the Playlist using the Song object's
        # set_next_song method, and places the newly defined Song object at the top of the Playlist.

        new_song = Song(title)
        new_song.set_next_song(self.__first_song)
        self.__first_song = new_song

    def find_song(self, title):

        # Creates a new variable called current_song and sets equal to the value of the first Song object in the Playlist.
        # Additionally, a counter variable called song_no is set to 0.
        # Assuming that current_song is not None, that is, there ARE songs left to search for in the playlist,
        # current_song's title is compared to the title argument (input from main).
        # If they match, the current song_no is returned. Otherwise, song_no goes up by one, and current_song is set to its next_song value.
        # Assuming this is not the case (either nothing is found or there was nothing to search to begin with), -1 (False) is returned instead.

        current_song = self.__first_song
        song_no = 0
        while current_song != None:
            if current_song.get_title() == title:
                return song_no
            else:
                song_no += 1
                current_song = current_song.get_next_song()
        return -1

    def remove_song(self, title):

        # Creates two varaibles, current_song and previous_song. current_song is set to the first (top) song in the Playlist, while previous_song is set to None.
        # While current_song exists, current_song's title value is compared to the title argument (main.py input).
        # If it matches, it checks if the previous_song has a value or not. If it does, the value of the previous_song's next song is set to the current_song's next song.
        # If there is no previous_song value (in other words, if the removed song is at the top), the first song of the Playlist becomes the next song in the Playlist.
        # If the title doesn't match, previous_song is assigned the current_song's value, and the current_song then becomes the next song in the playlist.

        current_song = self.__first_song
        previous_song = None
        
        while current_song != None:  
            if current_song.get_title() == title:  
                if previous_song != None:
                    previous_song.set_next_song(current_song.get_next_song())
                else:
                    self.__first_song = current_song.get_next_song()
                return True
            previous_song = current_song
            current_song = current_song.get_next_song()
      
        return False

    def length(self):

        # Creates a pointer and counter variable.
        # While the pointer (current_song) points to an actual value (in other words, as long as a song exists in the Playlist),
        # the counter variable will continue to go up by 1. Once this is complete, the counter value is returned.

        current_song = self.__first_song
        counter = 0
        while current_song != None:
            counter += 1
            current_song = current_song.get_next_song()
        return counter

    def print_songs(self):

        # Similar to the above length function, a pointer and counter are defined.
        # However, this time the counter is not returned, instead being used to number each value as it is printed
        # alongside each Song's title value (from top down).

        current_song = self.__first_song
        counter = 0
        while current_song != None:
            print(f"{counter + 1}. {current_song.get_title()}")
            current_song = current_song.get_next_song()
            counter += 1

    def insert_song(self, title, index):

        new_song = Song(title)
        current_song = self.__first_song
        previous_song = None
        counter = 1
        if current_song == None:
            new_song.set_next_song(self.__first_song)
            self.__first_song = new_song
            return True
        while current_song != None:  
            if counter == index:
                if previous_song != None:
                    new_song.set_next_song(current_song)
                    previous_song.set_next_song(new_song)
                elif previous_song == None:
                    new_song.set_next_song(self.__first_song)
                    self.__first_song = new_song
                return True
            counter += 1
            previous_song = current_song
            current_song = current_song.get_next_song()

