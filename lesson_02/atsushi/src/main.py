import songName
import genre
import song
import music

songname = songName.Songname("ちょ")

genre = genre.Genre("Punk")

song = song.Song(songname,genre)
print(songname.get(), " " + genre.get())





