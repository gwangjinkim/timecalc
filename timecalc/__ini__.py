import time
from functools import reduce


def split_lines(s):
    return s.split("\n")

def filter_empty(l):
    return [x for x in l if x != ""]

def hh_mm_to_minutes(s):
    t = time.strptime(s, "%H:%M")
    return t.tm_hour * 60 + t.tm_min

def minutes_to_hh_mm(mins):
    return '{:02d}:{:02d}'.format(*divmod(mins, 60))

def minutes_to_hh_decimal(mins):
	hours, mins = divmod(mins, 60)
	mins = mins / 60
	return round(hours + mins, 2)

def de_interleave(l):
    return l[::2], l[1::2]

def between_times(l):
    starts, ends = de_interleave(l)
    return [ minutes_to_hh_mm(hh_mm_to_minutes(e) - hh_mm_to_minutes(s)) for s, e in zip(starts, ends)]

def between_times_s(s):
    return between_times(filter_empty(split_lines(s)))

def sum_times(times):
    return minutes_to_hh_mm(reduce(lambda x, y: x + y, [hh_mm_to_minutes(x) for x in times]))

# it could pair and if last is 'x', it could calculate to 40 from the last time

def sum_pairs(s):
	l = [hh_mm_to_minutes(x) for x in filter_empty(split_lines(s))]
	starts, ends = de_interleave(l)
	diffs = [y - x for x, y in zip(starts, ends)]
	firsts, seconds = de_interleave(diffs)
	pair_sums = [x + y for x, y in zip(firsts, seconds)]
	return [minutes_to_hh_mm(x) for x in pair_sums]

def sum_pairs_decimal(s):
	l = [hh_mm_to_minutes(x) for x in filter_empty(split_lines(s))]
	starts, ends = de_interleave(l)
	diffs = [y - x for x, y in zip(starts, ends)]
	firsts, seconds = de_interleave(diffs)
	pair_sums = [x + y for x, y in zip(firsts, seconds)]
	return [minutes_to_hh_decimal(x) for x in pair_sums]	
    
# sum_pairs_decimal() is the most interesting function

calc = sum_pairs_decimal
