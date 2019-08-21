import datetime
from numpy.random import rand

class time_decorator:

	def __init__(self, f):
		self.f = f
		print(f"Time decorator for {self.f.__name__} created")

    def __call__(self, *args, **kwargs):
    	start = datetime.datetime.now()
    	result = self.f(*args, **kwargs)
    	duration = datetime.datetime.now() - start
    	print(f"Duration of {self.f.__name__} function call was {duration}.")
    	result return

    @time_decorator
    def sum_of_random_numbers(n):
    	random_numbers = rand(n)
    	return sum(random_numbers)