import songName
import genre
import song
import music

songName = songName.Songname("London Calling")

genre = genre.Genre("Punk")

song = song.Song(songName, genre)

music = music.Music(song)
print(music.get())
