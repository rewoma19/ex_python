EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2

print(EXPECTED_BAKE_TIME)

def bake_time_remaining(elapsed_bake_time):
  """Calculate the bake time remaining.

  :param elapsed_bake_time: int - baking time already elapsed.
  :return int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

  Function that takes the actual minutes the lasagna has been in the oven as an argument and returns how many minutes the lasagna still needs to bake based on the `EXPECTED_BAKE_TIME`.
  """
  return EXPECTED_BAKE_TIME - elapsed_bake_time

bake_time_remaining(30)
# 10

def preparation_time_in_minutes(number_of_layers):
  """Calculate the preparation time in minutes.

  :param number_of_layers int - number of layers to be added to the lasagna
  :return int - preparation time in minutes

  Function that takes the number_of_layers you want to add to the lasagna as an argument and returns how many minutes will be spent making them. Assume each layer takes 2 minutes to prepare.
  """
  return number_of_layers * PREPARATION_TIME

preparation_time_in_minutes(2)
# 4

def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
  """Calculate the total elapse time (prepping + baking) in minutes.

  :param number_of_layers int - number of layers added to the lasagna
  :param elapsed_bake_time - the number of minutes the lasagna has spent baking in the oven already
  :return int - total minutes spent in the kitchen cooking

  Function that returns the total minutes spent in the kitchen cooking - preparation time layering + time the lasagna has spent baking in the oven.
  """
  return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time

elapsed_time_in_minutes(3, 20)
# 26