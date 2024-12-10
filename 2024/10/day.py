def parse_data(raw):
  return raw.splitlines()

def get_heads(data):
  nodes = {}
  w = len(data[0])
  for y, line in enumerate(data):
    for x, c in enumerate(line):
      if c == '0':
        nodes[(x, y)] = set([y*w+x])
  return nodes

def neigh(x,y,w,h):
  n = set()
  if x > 0:
    n.add((x-1,y))
  if x < w-1:
    n.add((x+1,y))
  if y > 0:
    n.add((x,y-1))
  if y < h-1:
    n.add((x,y+1))
  return n
  
def solve_part2(data):
  nodes = get_heads(data)
  nodes = {k:1 for k in nodes}
  w = len(data[0])
  h = len(data)
  for ht in range(1,10):
    new_nodes = {}
    for n, heads in nodes.items():
      for nx, ny in neigh(*n,w,h):
        nc = int(data[ny][nx])
        if nc == ht:
          ns = new_nodes.setdefault((nx,ny), 0)
          new_nodes[(nx,ny)] = ns + heads
    nodes = new_nodes
  return sum(nodes.values())

def solve_part1(data):
  nodes = get_heads(data)
  w = len(data[0])
  h = len(data)
  for ht in range(1,10):
    new_nodes = {}
    for n, heads in nodes.items():
      for nx, ny in neigh(*n,w,h):
        nc = int(data[ny][nx])
        if nc == ht:
          ns = new_nodes.setdefault((nx,ny), set())
          ns.update(heads)
    nodes = new_nodes
  return sum(len(heads) for heads in nodes.values())


example_a = example_b = """89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732"""

example_answer_b = 81