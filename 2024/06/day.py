from copy import copy

def parse_data(raw):
  guard_icon = '^>v<'
  obstacles = set()
  guard =None
  rows = raw.split('\n')
  w = len(rows[0])
  h = len(rows)
  for y, r in enumerate(rows):
    for x, c in enumerate(r):
      if c == '#':
        obstacles.add((x,y))
      if c in guard_icon:
        guard = (x, y, guard_icon.index(c))
  return guard, obstacles, w, h

def sim(g, obs, w, h):
  dirs = [(0,-1), (1,0), (0,1), (-1,0)]
  x,y,d = g
  visits = {}
  while 0 <= x < w and 0 <= y < h:
    if (x,y) in visits and visits[(x,y)] == d:
      return None # loop
    visits[(x,y)] = d
    nx, ny = x+dirs[d][0], y+dirs[d][1]
    while (nx, ny) in obs:
      d = (d+1) % 4
      nx, ny = x+dirs[d][0], y+dirs[d][1]
    x,y = nx, ny
  return visits

def solve_part1(data):
  g, obs, w, h = data
  visits = sim(g, obs, w, h)
  return len(visits)

def solve_part2(data):
  g, obs, w, h = data
  res = 0
  v = set(sim(g, obs, w, h).keys())
  v.remove((g[0], g[1]))
  for x,y in v:
    o = copy(obs)
    o.add((x,y))
    v = sim(g, o, w, h)
    if v is None:
      res += 1
  return res