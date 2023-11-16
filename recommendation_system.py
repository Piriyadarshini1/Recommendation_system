# ARTIFICIAL INTELLIGENCE
# TASK 3
# RECOMMENDATION SYSTEM
data={
    'Movies':{
        'The mummy':['Action','Adventure','Thriller'],
        'The Conjuring':['Horror','Mystery','Thriller'],
        'The Avator':['Action','Adventure','Fantasy'],
        'Home Alone':['Comedy','Drama'],
        'The lion king':['Fantasy',' Adventure',' musical'],
        'Guardians of the Galaxy':['Superhero', 'Action', 'Adventure','Comedy'],
        'Turning RED':['Family', 'Comedy', 'Animation'],
        'Free Guy':['Action' ,'Comedy'],
        'Ice age':['Animation', 'Fantasy', 'Adventure' ,'Kids'],
        'Avengers Infinity War':['Superhero', 'Action', 'Fantasy'],
        'The boogeyman':['Horror' ,'Thriller'],
        'A Haunting in venice':['Mystery' ,'Thriller'],
        'No one will save you':['Horror', 'Thriller', 'Science Fiction' ]
    },
    'Books':{
        'Jack Reacher':['Mystery','Thriller'],
        'Harry Potter':['Science Fiction','Adventure','Young Adult'],
        'Around the Globe':['Fantasy','Young Adult'],
        'Emily':['Non-Fiction','Self-Help'],
        'Goodnight Moon':['Picture Books'],
        'The Very Hungry Caterpillar':['Picture Books'],
        'Brown Bear, Brown Bear, What Do You See?'  :['Picture Books'],
        'Where the Wild Things Are':['Early Readers'],
        'Green Eggs and Ham':['Early Readers'],
        'Corduroy':['Early Readers'],
        'Matilda':['Intermediate Readers'],
        'Diary of a Wimpy Kid':['Intermediate Readers'],
        'Charlottes Web':['Intermediate Readers'],
        'Percy Jackson & The Olympians':['Young Adult'],
        'The Hunger Games':['Young Adult'],
        'The Magic School Bus': ['Non-Fiction and Educational'],
        'Encyclopedia Brown':['Non-Fiction and Educational'],
        'National Geographic Kids':['Non-Fiction and Educational']
    },
    'Items':{
        'Vision Pro':['Electronics','Gadgets'],
        'Sombrero':['Clothing','Fashion'],
        'Birch table':['Home Decor','Furniture'],
        'Football':['Sports','Outdoor'],
        'Cricket':['Sports','Outdoor'],
        'RC Zoom':['Toys','Kids'],
        'Kindle Paperwhite':['Electronics', 'E-Readers'],
        'Sun Hat':['Clothing',' Accessories'],
        'Bookshelf':['Home Decor','Furniture'],
        'Basketball':['Sports', 'Outdoor'],
        'Badminton Set':['Sports', 'Outdoor'],
        'LEGO Star Wars Millennium Falcon':['Toys', 'Building Sets'],
        'Smartphone':['Electronics', 'Mobile Devices'],
        'Sneakers':['Clothing', 'Footwear'],
        'Throw Pillows':['Home Decor', 'Furniture'],
        'Tennis Racket':['Sports','Outdoor'],
        'Dollhouse':[' Toys', 'Dolls' ' Accessories']
    }
}
def recommend_items(category, user_preferences):
  recommended_items=[]

  for item, attributes in data[category].items():
    if all(attribute in attributes for attribute in user_preferences):
      recommended_items.append(item)
  return recommended_items
def get_user_preferences():
  print("Enter your preferenes(comma-separated) for the selected category:")
  user_input=input().strip().split(',')
  return[preference.strip() for preference in user_input]

def recommend_category(category):
  print(f"\nRecommendations for {category}:")
  user_preferences = get_user_preferences()
  recommended_items= recommend_items(category, user_preferences)
  if recommended_items:
    print(f"\nRecommended {category} for preferences: {', '.join(user_preferences)}")
    for item in recommended_items:
      print(f"{category}:{item}")
  else:
    print(f"\nNo {category} found for the givenpreferences.")

while True:
  print("\nSelect a category: Movies, Books, Items(or 'exit' to quit)")
  selected_category=input().strip().capitalize()
  if selected_category=='Exit':
    break
  if selected_category in data:
    recommend_category(selected_category)
  else:
    print("\nInvalid category. PleaseSelect Movies,Books, or Items.")
