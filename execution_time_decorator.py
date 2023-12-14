import time

def measure_time(func):
   def wrapper(*args):
      start_time = time.time()
      func(*args)
      end_time = time.time()
      execution_time = end_time - start_time
      print(f"The {func.__name__} took {execution_time}")
   return wrapper
