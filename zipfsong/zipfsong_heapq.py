#!/usr/bin/env python2

import sys
import heapq

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
	best_songs = []

	
	for pos in xrange(1, num_of_all+1):
		line = sys.stdin.readline()
		line = line.split()
		song = Song(pos, int(line[0]), line[1])
		heapq.heappush(best_songs, song)

	for i in xrange(num_of_best):
		song = heapq.heappop(best_songs)
		print song.name

if __name__ == '__main__':
	#import cProfile
	#cProfile.run('main()', sort='time')
	main()
