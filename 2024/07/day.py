def parse_data(raw):
  return [[int(x) for x in l.split()] for l in raw.replace(':', '').split('\n')]

def valid(x, conc=False):
  t = x[0]
  p = x[1:][::-1]
  while len(p) > 1 and t > 0:
    if t % p[0] == 0:
      z = [t // p[0]] + p[1:][::-1]
      if valid(z, conc):
        return True
    if conc and str(t).endswith(str(p[0])):
      cut = len(str(p[0])) 
      nt = str(t)[:-cut]
      if len(nt) == 0:
        return False
      #print("cut",t, p[0], cut, nt)
      nt = int(nt)
      z = [nt] + p[1:][::-1]
      if valid(z, conc):
        return True
    t -= p[0]
    p = p[1:]
  return t == p[0]
  
def solve_part1(data):
  return sum([x[0] for x in data if valid(x)])

def solve_part2(data):
  return sum([x[0] for x in data if valid(x, True)])