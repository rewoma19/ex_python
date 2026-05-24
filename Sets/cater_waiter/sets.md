# Instructions

You and your business partners operate a small catering company. You've just agreed to run an event for a local cooking club that features "club favorite" dishes. The club is inexperienced in hosting large events, and needs help with organizing, shopping, prepping and serving. You've decided to write some small Python scripts to speed the whole planning process along.

## Task 1

### Clean up Dish Ingredients

The event recipes were added from various sources and their ingredients appear to have duplicate (or more) entries — you don't want to end up purchasing excess items! Before the shopping and cooking can commence, each dish's ingredient list needs to be "cleaned".

Implement the **clean_ingredients(<dish_name>, <dish_ingredients>)** function that takes the name of a dish and a **list** of ingredients. This function should return a tuple with the name of the dish as the first item, followed by the de-duped **set** of ingredients.

    >>> clean_ingredients('Punjabi-Style Chole', ['onions', 'tomatoes', 'ginger paste', 'garlic paste', 'ginger paste', 'vegetable oil', 'bay leaves', 'cloves', 'cardamom', 'cilantro', 'peppercorns', 'cumin powder', 'chickpeas', 'coriander powder', 'red chili powder', 'ground turmeric', 'garam masala', 'chickpeas', 'ginger', 'cilantro'])

    >>> ('Punjabi-Style Chole', {'garam masala', 'bay leaves', 'ground turmeric', 'ginger', 'garlic paste', 'peppercorns', 'ginger paste', 'red chili powder', 'cardamom', 'chickpeas', 'cumin powder', 'vegetable oil', 'tomatoes', 'coriander powder', 'onions', 'cilantro', 'cloves'})

## Task 2

### Cocktails and Mocktails

The event is going to include both cocktails and "mocktails" - mixed drinks without the alcohol. You need to ensure that "mocktail" drinks are truly non-alcoholic and the cocktails do indeed include alcohol.

Implement the **check_drinks(<drink_name>, <drink_ingredients>)** function that takes the name of a drink and a **list** of ingredients. The function should return the name of the drink followed by "Mocktail" if the drink has no alcoholic ingredients, and drink name followed by "Cocktail" if the drink includes alcohol. For the purposes of this exercise, cocktails will only include alcohols from the ALCOHOLS constant in **sets_categories_data.py**:

    >>> from sets_categories_data import ALCOHOLS

    >>> check_drinks('Honeydew Cucumber', ['honeydew', 'coconut water', 'mint leaves', 'lime juice', 'salt', 'english cucumber'])
    ...
    'Honeydew Cucumber Mocktail'

    >>> check_drinks('Shirley Tonic', ['cinnamon stick', 'scotch', 'whole cloves', 'ginger', 'pomegranate juice', 'sugar', 'club soda'])
    ...
    'Shirley Tonic Cocktail'
