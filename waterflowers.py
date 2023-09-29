# Mrs. Simpson waters her geraniums once every 3 days, and she waters her other house plants once a week.
# How often does Mrs. Simpson water all the plants on the same day?

# Geraniums are watered once every 3 days i.e. if watered on Monday, then watered again on Thursday.
# Other plants are watered only once a week.
# We have to determine how many days it takes for the watering days to be the same day.
# Best way to do this is to first wait for the day to match, then count the number of days until the next matching day. Otherwise, we get 
# different answers for different geranium watering days. 


# ask for the first day that geraniums are watered.

spelling_indicator1 = 0
while spelling_indicator1 == 0:
    germ_first = input('What is the first day that the geraniums are watered (enter at least first 2 letters)? ').lower()
    # grab the first 2 letters of answer
    germ = germ_first[0:2]
    if germ not in ['su','mo','tu','we','th','fr', 'sa']:
        spelling_indicator1 = 0
        print('Spelling error, try again.')
    else:
        spelling_indicator1 = 2
    
# ask for the day of the week the other flowers are watered

spelling_indicator2 = 0
while spelling_indicator2 == 0:
    # grab the day of week that other flowers are watered
    others_first = input('What is day that other flowers are watered (enter at least first 2 letters)? ').lower()
    #grab the first 2 letters of answer
    others = others_first[0:2]
    if others not in ['su','mo','tu','we','th','fr', 'sa']:
        spelling_indicator2 = 0
        print('Spelling error, try again.')
    else:
        spelling_indicator2 = 2


no_of_days = 0
match_counter = 0

while match_counter < 2:
    
    if germ == others:
        match_counter = match_counter + 1
        if match_counter != 2:
            no_of_days = 0
        if match_counter == 2:
            break
    if germ == 'su':
        germ = 'we'
    elif germ == 'mo':
        germ = 'th'
    elif germ == 'tu':
        germ = 'fr'
    elif germ == 'we':
        germ = 'sa'
    elif germ == 'th':
        germ = 'su'
    elif germ == 'fr':
        germ = 'mo'
    elif germ == 'sa':
        germ = 'tu'

    no_of_days = no_of_days + 3

print('The number of days between matching watering days is: ', no_of_days)
    