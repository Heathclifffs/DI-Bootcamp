class Song():
	def __init__(self,Lyrics):
		self.lyrics=Lyrics
	def sing_me_a_song(self):
		for e in self.lyrics:
			print(e)		
stairway= Song(["There’s a lady who's sure","all that glitters is gold", "and she’s buying a stairway to heaven"])
stairway. sing_me_a_song()
