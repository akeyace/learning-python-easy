import genre
import songName
import song
import music

genre1 = genre.Genre("Soul")
genre2 = genre.Genre("fork")
print(genre1.get())

song_name1 = songName.Songname("talking about")
song_name2 = songName.Songname("神田川")
print(song_name1.get())

song1 = song.Song(song_name1, genre1)
song2 = song.Song(song_name2, genre2)
print(song1.get())
print(song2.get())

songs = [song1, song2]
print(songs)

music = music.Music(songs)
print(music.get())