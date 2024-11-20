# Create a sentence by concatenating multiple strings,
# then replace a word in the sentence with another word
# methods to use replace() and print()

name = "Princess "
maiden_name = "Machuma"
full_name = name + maiden_name
print(full_name)
married_name = name + maiden_name.replace("Machuma", "Alpha")
print(F"Your married name is " + married_name)
