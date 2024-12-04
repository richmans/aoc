def parse_data(raw):
  return raw.split('\n')

def rotate(m, n):
  b = len(m) -1
  r = len(m[0]) -1
  t = [
    (0, 0, 1, 0, [(0, 1)]),
    (0, 0, 1, -1, [(0, 1),(1,0)]),
    (0, b, 0, -1, [(1, 0)]),
    (0, b, -1, -1, [(1, 0),(0,-1)]),
    (r, b, -1, 0, [(0, -1)]),
    (r, b, -1, 1, [(0, -1),(-1, 0)]),
    (r, 0, 0, 1, [(-1, 0)]),
    (r, 0, 1, 1, [(-1, 0),(0,1)])
  ][n]

  rx, ry, dx, dy, path = t
  rx -= path[0][0]
  ry -= path[0][1]
  for nrx,nry in path:
    rx += nrx
    ry += nry
    while 0 <= rx <= r and 0 <= ry <= b:
      cx, cy = rx, ry
      row = []
      while 0 <= cx <= r and 0 <= cy <= b:
        row.append(m[cy][cx]) 
        cx += dx
        cy += dy
      yield row
      rx += nrx
      ry += nry
    rx -= nrx
    ry -= nry


def pmx(m):
  for r in m:
    print(''.join(r))
  print()
  
def solve_part1(data):
  s = 0
  for a in range(8):
    for r in rotate(data, a):
      s += "".join(r).count('XMAS')
  return s

def solve_part2(m):
  b = len(m) -1
  r = len(m[0]) -1
  res =0
  for y in range(1, b):
    for x in range(1, r):
      if m[y][x] != 'A':
        continue
      x = ''.join([m[y-1][x-1], m[y-1][x+1], m[y+1][x-1], m[y+1][x+1]])
      if x in ['MSMS','MMSS','SMSM','SSMM']:
        res += 1
  return res

example_a = example_b = """MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX"""

example_answer_a = 18
example_answer_b = 9