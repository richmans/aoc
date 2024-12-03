#!/usr/bin/env python3
import argparse
from datetime import datetime
from aocd.models import Puzzle
import sys
import logging
import importlib


# determine current day
# if gameday, import that solution
# run solution on example
# if answer wrong, stop
# run solution on data
# submit answer
class AocException(Exception):
    pass

def load_solver(year, day):
  try:
    return importlib.import_module(f"{year}.{day:02d}.day")
  except Exception:
    raise AocException(f"Could not load solver for day {day} in {year}")

def verify_examples(solver, puzzle, part):
  fn = getattr(solver, f"solve_part{part}")
  
  for example in puzzle.examples:
    if part == 1:
      input_data = getattr(solver, "example_a", example.input_data)
      expect = str(getattr(solver, "example_answer_a", example.answer_a))
    else: 
      input_data = getattr(solver, "example_b", example.input_data)
      expect = str(getattr(solver, "example_answer_b", example.answer_b))
    
    data = solver.parse_data(input_data)
    answer = fn(data)
    if str(answer) != expect:
      logging.error(f"Example failed for part {part}. Expecting {expect} but got {answer}")
      return False
  return True
  
def run_solver(solver, puzzle, part):
  fn = getattr(solver, f"solve_part{part}")
  if not verify_examples(solver, puzzle, part):
    raise AocException(f"Examples for part {part} failed")
  logging.info(f"Example for part {part} passed. Proceeding to prod.")
  data = solver.parse_data(puzzle.input_data)
  
  answer = fn(data)
  logging.info(f"Part {part} answer: {answer}")
  if part == 1:
    puzzle.answer_a = answer
  else:
    puzzle.answer_b = answer
    
def main(args):
  year = args.year
  day = args.day
  if day is None:
    raise AocException('Specify a day')
  print(f"Year: {year}, Day: {day:02}")
  p = Puzzle(year, day)
  slvr = load_solver(year, day)
  #print(p.examples)
  for part in [1, 2]:
    run_solver(slvr, p, part)

current_year = datetime.now().year
current_month = datetime.now().month
if current_month == 12 and datetime.now().day < 27:
  current_day = datetime.now().day
else:
  current_day = None

if __name__ == "__main__":
  parser = argparse.ArgumentParser()
  parser.add_argument("day", type=int, default=current_day, nargs='?')
  parser.add_argument("year", type=int, default=current_year, nargs='?')
  args = parser.parse_args()
  logging.basicConfig(level=logging.INFO)
  try:
    main(args)
  except AocException as e:
    logging.error(e)
    sys.exit(2)
  
