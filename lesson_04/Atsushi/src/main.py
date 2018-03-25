import genre
import songName
import song
import music

genre1 = genre.Genre("Rock")
genre2 = genre.Genre("R&B")
genre3 = genre.Genre("Funk")
genre4 = genre.Genre("Rock")
# print(genre.get())

song_name1 = songName.Songname("7月７日")
song_name2 = songName.Songname("Talkin’ Loud")
song_name3 = songName.Songname("Watermelon Man")
song_name4 = songName.Songname("it's My Life")
# print(song_name.get())

song1 = song.Song(song_name1, genre1)
song2 = song.Song(song_name2, genre2)
song3 = song.Song(song_name3, genre3)
song4 = song.Song(song_name4, genre4)
# print(song1.get())

songs = [song1, song2, song3, song4]
# print(songs)

music = music.Music(songs)
print(music.get())


