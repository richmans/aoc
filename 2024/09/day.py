def parse_data(raw):
  parts = []
  is_file = True
  pos = 0
  fid = 0
  for n in raw:
    n = int(n)
    if is_file:
      parts.append([fid, pos, n])
      fid += 1
    else:
      parts.append([None, pos, n])
    pos += n
    is_file = not is_file
  return parts

def solve_part1(data):
  rev = [d for d in data[::-1] if d[0] is not None]
  res = 0
  for b in data:
    l = b[2]
    p = b[1]
    fid = b[0]
    if fid is not None:
      res += int(fid * l * (p + (l-1) / 2))
      b[0] = 0
      continue
    while l > 0:
      n = min(l, rev[0][2])
      fid = rev[0][0]
      l -= n
      res += int(fid * n * (p + (n-1) / 2))
      rev[0][2] -= n
      if rev[0][2] == 0:
        rev.pop(0)
      p += n
  return res

def solve_part2(data):
  frees = [d for d in data if d[0] is None]
  files = [d for d in data if d[0] is not None][::-1]
  res = 0
  for fi in files:
    fid = fi[0]
    l = fi[2]
    p = fi[1]
    for fr in frees:
      if fr[1] > p:
        break
      if fr[2] >= l:
        fr[2] -= l
        p = fr[1]
        fr[1] += l
        break
    res += int(fid * l * (p + (l-1) / 2))
  return res 