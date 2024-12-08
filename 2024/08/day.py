from itertools import combinations

def parse_data(raw):
  ants = {}
  lines = raw.split('\n')
  w = len(lines[0])
  h = len(lines)
  for (y, line) in enumerate(lines):
    for (x, c) in enumerate(line):
      if c == '.':
        continue
      if c not in ants:
        ants[c] = []
      ants[c].append((x, y))
  return ants, w, h

def solve_part1(data):
  ants, w, h = data
  anti = set()
  for a in ants:
    for (x, y), (x2,y2) in combinations(ants[a], 2):
      dx = x2 - x
      dy = y2 - y
      
      ax = x - dx
      ay = y - dy
      if 0 <= ax < w and 0 <= ay < h:
        anti.add((ax, ay))
        
      ax2 = x2 + dx
      ay2 = y2 + dy
      if 0 <= ax2 < w and 0 <= ay2 < h:
        anti.add((ax2, ay2))
        
  return len(anti)

def solve_part2(data):
  ants, w, h = data
  anti = set()
  for a in ants:
    for (x, y), (x2,y2) in combinations(ants[a], 2):
      dx = x2 - x
      dy = y2 - y
      ax, ay = x, y
      while 0 <= ax < w and 0 <= ay < h:
        anti.add((ax, ay))
        ax = ax - dx
        ay = ay - dy
      
      ax2, ay2 = x2, y2
      while 0 <= ax2 < w and 0 <= ay2 < h:
        anti.add((ax2, ay2))
        ax2 = ax2 + dx
        ay2 = ay2 + dy
  return len(anti)
example_answer_b = 34