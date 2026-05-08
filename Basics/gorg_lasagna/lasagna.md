## Task 1

### Define expected bake time in minutes as a constant

Define the **EXPECTED_BAKE_TIME** constant that represents how many minutes the lasagna should bake in the oven. According to your cookbook, the lasagna should be in the oven for 40 minutes:

    print(EXPECTED_BAKE_TIME)
    40

## Task 2

### Calculate remaining bake time in minutes

Complete the **bake_time_remaining()** function that takes the actual minutes the lasagna has been in the oven as an argument and returns how many minutes the lasagna still needs to bake based on the **EXPECTED_BAKE_TIME** constant.

    bake_time_remaining(30)
    10

## Task 3

### Calculate preparation time in minutes

Define the **preparation_time_in_minutes()** function that takes the **number_of_layers** you want to add to the lasagna as an argument and returns how many minutes you would spend making them. Assume each layer takes 2 minutes to prepare.

    def preparation_time_in_minutes(number_of_layers):

    preparation_time_in_minutes(2)
    4

## Task 4

### Calculate the total elapsed time (prepping + baking) in minutes

Define the **elapsed_time_in_minutes()** function that takes two parameters as arguments:

- **number_of_layers** (the number of layers added to the lasagna)

- **elapsed_bake_time** (the number of minutes the lasagna has spent baking in the oven already).

This function should return the total minutes you have been in the kitchen cooking — your preparation time layering + the time the lasagna has spent baking in the oven.

    def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):


    elapsed_time_in_minutes(3, 20)
    26

## Task 5

### Update the recipe with notes

Go back through the recipe, adding "notes" in the form of function docstrings.

    def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculate the elapsed cooking time.

    :param number_of_layers: int - the number of layers in the lasagna.
    :param elapsed_bake_time: int - time the lasagna has been baking in the oven.
    :return: int - total time elapsed (in minutes) preparing and baking.

    This function takes two integers representing the number of lasagna
    layers and the time already spent baking the lasagna. It calculates
    the total elapsed minutes spent cooking (preparing + baking).
    """
