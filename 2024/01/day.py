def parse_data(raw):
  l = raw.splitlines()
  return [int(x.split()[0]) for x in l], [int(x.split()[1]) for x in l]
  

def solve_part1(data):
  l, r = sorted(data[0]), sorted(data[1])
  return sum(abs(x-y) for x, y in zip(l, r))
  
def solve_part2(data):
  l, r = sorted(data[0]), sorted(data[1])
  return sum([li * r.count(li) for li in l])

example_answer_b = 31