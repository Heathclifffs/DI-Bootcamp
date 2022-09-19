
# --------------------------------------------------------------Exercise 6 : Magicians

# 1.Using this list of magician’s names. magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel']
magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel']
# 2.Pass the list to a function called show_magicians(), which prints the name of each magician in the list.
def show_magicians(names):
    for i in names:
        print(i)
# 3. Write a function called make_great() that modifies the list of magicians by adding the phrase "the Great" to each magician’s name.
def make_great(names):
    for i,name in enumerate(names):
        names[i] = name + " the Great"
# 4.Call the function make_great().
make_great(magician_names)
# 5.Call the function show_magicians() to see that the list has actually been modified.
show_magicians(magician_names)
