from Song import Song

class Playlist:
  def __init__(self):
    self.__first_song = None


  # TODO: Create a method called add_song that creates a Song object and adds it to the playlist. This method has one parameter called title.

  def add_song(self, title):

      # Creates a new Song object called new_song, points to the top song in the Playlist using the Song object's
      # set_next_song method, and places the newly defined Song object at the top of the Playlist.

      new_song = Song(title)
      new_song.set_next_song(self.__first_song)
      self.__first_song = new_song



  # TODO: Create a method called find_song that searches for whether a song exits in the playlist and returns its index. The method has one parameters, title, which is the title of the song to be searched for. If the song is found, return its index.

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


  # TODO: Create a method called remove_song that removes a song from the playlist. This method takes one parameter, title, which is the song that should be removed. 

  def remove_song(self, title):  
        current_song = self.__first_song 
        
        if (current_song != None):  
            if (current_song.get_title() == title):  
                self.__first_song = current_song.__next_song
                current_song = None
                return

        while(current_song != None):  
            if current_song.get_title() == title:  
                break
            previous_song = current_song
            current_song = current_song.__next_song
  
        if(current_song == None):  
            return
  
        # Unlink the node from linked list  
        previous_song.__next_song = current_song.__next_song
  
        current_song = None

  # TODO: Create a method called length, which returns the number of songs in the playlist.

  def length(self):
    current_song = self.__first_song
    counter = 0
    while current_song != None:
        counter += 1
        current_song = current_song.__next_song
    return counter


  # TODO: Create a method called print_songs that prints a numbered list of the songs in the playlist.

  # Example:
  # 1. Song Title 1
  # 2. Song Title 2
  # 3. Song Title 3

  def print_songs(self):
      current_song = self.__first_song
      counter = 0
      while current_song != None:
          print(f"{counter + 1}. {current_song.get_title()}")
          current_song = current_song.get_next_song()
          counter += 1
  