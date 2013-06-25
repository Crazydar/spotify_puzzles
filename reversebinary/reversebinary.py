#!/usr/bin/env python2

def reverse_binary(bin_num):
	return int(format(bin_num, 'b')[::-1], 2)

print reverse_binary(int(raw_input()))

