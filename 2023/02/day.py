def parse_data(raw):
  r = []
  for l in raw.split('\n'):
    if len(l) == 0:
      continue
    gname, content = l.split(': ')
    gid = int(gname[5:])
    game = [{t.split(' ')[1]: int(t.split(' ')[0]) for t in g.split(', ')} for g in content.split('; ')]
    r.append((gid, game))
  return r

def possible(game, max):
  for d in game:
    for c, cnt in d.items():
      if c not in max or cnt > max[c]:
        return False
  return True

def solve_part1(data):
  max = {'red': 12, 'green': 13, 'blue': 14}
  sum = 0
  for gid, g in data:
    if possible(g, max):
      sum += gid
  return sum

def power(game):
  min = {'red': 0, 'green': 0, 'blue': 0}
  for d in game:
    for c, cnt in d.items():
      if c in min and cnt > min[c]:
        min[c] = cnt
  return min['red'] * min['green'] * min['blue']

def solve_part2(data):
  sum = 0
  for gid, g in data:
    sum += power(g)
  return sum