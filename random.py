import random

def random_generator(min_value, max_value):
  """Generates a random number between min_value and max_value, inclusive."""
  return random.randint(min_value, max_value)

if __name__ == "__main__":
  print(random_generator(1, 10))
