def parse_data(raw):
  return [[int(x) for x in line.split()] for line in raw.splitlines()]

def is_safe(l):
  d = [l[n] - l[n-1] for n in range(1, len(l))]
  return (all(x > 0 for x in d) or all(x < 0 for x in d)) and all(abs(x) < 4 for x in d)

def solve_part1(data):
  return len([1 for l in data if is_safe(l)])

def maybe_safe(l):
  if is_safe(l):
    return True
  for i in range(len(l)):
    s = l[:i] + l[i+1:]
    if is_safe(s):
      return True
  return False
  
def solve_part2(data):
  return len([1 for l in data if maybe_safe(l)])