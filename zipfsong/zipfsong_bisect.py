#!/usr/bin/env python2

import sys
import bisect

class Song(object):
	
	def __init__(self, pos, plays, name):
		self.pos = pos
		self.plays = plays
		self.name = name
		self.quality = self.plays * self.pos

	def __cmp__(self, other):
		comp = cmp(self.quality, other.quality)
		if comp == 0: return cmp(self.pos, other.pos)
		return -comp

def main():
	line = sys.stdin.readline().split()
	num_of_all = int(line[0])
	num_of_best = int(line[1])
	best_songs = [None] * num_of_best

	# first 'num_of_best' songs will be inserted no matter what
	for pos in xrange(1, num_of_best+1):
		line = sys.stdin.readline()
		line = line.split()
		song = Song(pos, int(line[0]), line[1])
		best_songs[pos-1] = song

	# sort them and set the bar for quality check
	best_songs.sort()
	worst = best_songs[-1].quality

	# the rest of the songs will be inserted only if they pass the quality check
	for pos in xrange(num_of_best+1, num_of_all+1):
		line = sys.stdin.readline()
		line = line.split()
		song = Song(pos, int(line[0]), line[1])
		if song.quality > worst:
			bisect.insort(best_songs, song)
			worst = best_songs[-1].quality
			# we dont want to use more space than necessary
			del best_songs[-1]

	# print best songs
	for i in xrange(num_of_best):
		print best_songs[i].name

if __name__ == '__main__':
	#import cProfile
	#cProfile.run('main()', sort='time')
	main()

