def parse_data(raw):
  rules, updates = raw.split('\n\n')
  rules = [(int(a),int(b)) for a,b in [m.split('|') for m in rules.split('\n')]]
  updates = [[int(m) for m in u.split(',')] for u in updates.split('\n')]
  return rules, updates

def middle(u):
  return u[len(u)//2]

def valid(u, rules):
  pos = {}
  for i, p in enumerate(u):
    pos[p] = i
  for a,b in rules:
    if a not in pos or b not in pos:
      continue
    if pos[a] > pos[b]:
      return False
  return True
  
def solve_part1(data):
  rules, updates = data
  return sum([middle(u) for u in updates if valid(u, rules)])

def fix(u, rules):
  f = []
  u = set(u)
  r = set((a,b) for a,b in rules if a in u and b in u)
  
  while len(u) > 0:
    restrict = set(b for _, b in r)
    u2 = set()
    for x in u:
      if x not in restrict:
        f.append(x)
        r = set((a,b) for a,b in r if a != x)
      else:
        u2.add(x)
    if u2 == u:
      print('uh oh', u, f,r)
      break
    u = u2
  return f
  
def solve_part2(data):
  fixed = []
  rules, updates = data
  for u in updates:
    if valid(u, rules):
      continue
    fixed.append(fix(u, rules))
    
  return sum([middle(u) for u in fixed])