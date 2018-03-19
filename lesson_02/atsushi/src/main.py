import songName
import genre
import song
import music

songname = songName.Songname("London Calling")

genre = genre.Genre("Punk")

song = song.Song(songname,genre)

music = music.Music(song)
print(songname.get(), " " + genre.get())





