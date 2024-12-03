import re

def parse_data(raw):
  return raw

def solve_part1(data):
  return sum([int(m.group(1)) * int(m.group(2)) for m in re.finditer(r'mul\((\d{1,3}),(\d{1,3})\)', data)])

def solve_part2(data):
  enabled = True
  r = 0
  for m in re.finditer(r"(mul)\((\d{1,3}),(\d{1,3})\)|(do)\(\)|(don't)\(\)", data):
    if m.group(1) == 'mul' and enabled:
      r += int(m.group(2)) * int(m.group(3))
    elif m.group(4) == 'do':
      enabled = True
    elif m.group(5) == 'don\'t':
      enabled = False
  return r

example_b = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"

example_answer_a = 161
example_answer_b = 48