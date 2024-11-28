from datetime import datetime
import argparse
import shutil
import os
import logging
import sys


class InitException(Exception):
  pass
  
def main(args):
  year = str(args.year)
  if os.path.isdir(year):
    raise InitException(f"Directory {year} already exists")
  os.mkdir(year)
  for i in range(1,26):
    shutil.copytree("templ", f"{year}/{i:02d}")
  print(f"Initialized {year}")

if __name__ == "__main__":
  current_year = datetime.now().year
  parser = argparse.ArgumentParser()
  parser.add_argument("year", type=int, default=current_year, nargs='?')
  args = parser.parse_args()
  try:
    main(args)
  except InitException as e:
    logging.error(e)
    sys.exit(1)
