import re

templates = ["It was about (Number) (Measure of time) ago when I arrived at the hospital in a (Mode of Transportation). The hospital is a/an (Adjective) place, there are a lot of (Adjective2) (Noun) here. There are nurses here who have (Color) (Part of the Body ). If someone wants to come into my room I told them that they have to (Verb) first. I’ve decorated my room with (Number2) (Noun2). Today I talked to a doctor and they were wearing a (Noun3) on their ( Part of the Body 2). I heard that all doctors (Verb) (Noun4) every day for breakfast. The most ( Adjective3) thing about being in the hospital is the (Silly Word ) (Noun) !",
"This weekend I am going camping with ( Proper Noun (Person’s Name)). I packed my lantern, sleeping bag, and (Noun). I am so (Adjective (Feeling)) to (Verb) in a tent. I am (Adjective (Feeling) 2) we might see a(n) (Animal), I hear they’re kind of dangerous. While we’re camping, we are going to hike, fish, and (Verb2). I have heard that the (Color) lake is great for ( Verb (ending in ing) ). Then we will (Adverb (ending in ly)) hike through the forest for (Number) (Measure of Time). If I see a (Color) (Animal) while hiking, I am going to bring it home as a pet! At night we will tell (Number) (Silly Word) stories and roast (Noun2) around the campfire!!", 
"Dear (Proper Noun (Person’s Name) ), I am writing to you from a (Adjective) castle in an enchanted forest. I found myself here one day after going for a ride on a (Color) (Animal) in (Place). There are (Adjective2) (Magical Creature (Plural)) and (Adjective3) (Magical Creature (Plural)2) here! In the ( Room in a House) there is a pool full of (Noun). I fall asleep each night on a (Noun2) of (Noun(Plural)3) and dream of (Adjective4) ( Noun (Plural)4). It feels as though I have lived here for (Number) ( Measure of time). I hope one day you can visit, although the only way to get here now is (Verb (ending in ing)) on a (Adjective5) (Noun5)!!"]

replacement_words = []
chosen_template = ""

def extract_key_words(template: str):
	temp = []
	results = []
	for i, char in enumerate(template):
		if char == '(':
			temp.append(i)
		elif char == ')':
			start = temp.pop()
			if len(temp) == 0 and i - start + 1 > 3:
				results.append(template[start + 1: i])
	return results
	
def result_with_ending(changeable: str):
	regex_start = r"[^(]+"
	start_part = re.search(regex_start, changeable).group().strip()
	end_regex = r" ([a-zA-Z]+)\)"
	end_part = re.search(end_regex, changeable).group(1).strip()
	return f"{start_part} + {end_part}"
	
def number_extract(number_to_be: float):
	return float(number_to_be)
	
		
def which_to_use(word: str):
	vowels = ["a","e","i","o","u"]
	if word[0].lower() in vowels:
		return "an"
	else:
		return "a"

def is_digit_in_value(input_value):
	#value = any(digit.isdigit() for digit in input_value)
	return bool(re.search(r'\d', input_value))
	
def create_input_right(word: str):
	result = word
	if '(' in word and "ending in" in word:
		result = result_with_ending(word)
	result = re.sub(r'\d', '', result)
	input_value = input(f"Input {which_to_use(word)} {result}: ")
	check_input_value(word, input_value)
	return input_value
	
def is_float(string):
    if string.replace(".", "").isnumeric():
        return True
    else:
        return False	
		
def is_value_number(input_value: str):
	if is_float(input_value):
		return True
	return input_value.isdigit()
	
def check_input_value(word: str, input_value: str):
	if len(input_value) == 0:
		raise ValueError("Input should not be empty!!!")
	elif "number" in word and not is_value_number(input_value):
		raise ValueError("Input should be only numbers!!!")
	elif "ending in ing" in word and not input_value.endswith("ing"):
		raise ValueError("Input should end with 'ing'!!!")
	elif "ending in ly" in word and not input_value.endswith("ly"):
		raise ValueError("Input should end with 'ly'!!!") 
	elif "plural" in word and not input_value.endswith("s"):
		raise ValueError("Input should be plural and end with 's'!!!") 
	elif "measure of time" in word and is_digit_in_value(input_value):
		raise ValueError("'{}' should not contain number!!!".format(input_value)) 
	elif not "number" in word and is_digit_in_value(input_value):
		raise ValueError("'{}' should not contain numbers!!!".format(input_value))
	
while True:
	try:
		template = int(input("Please, type number of story you want to interact with:\n1. Hospital affaire\n2. Weekend Camping\n3. Life in Castle\nYour choice: "))
		if template in range(1, 4):
			chosen_template = templates[template - 1]
			break
		else:
			print("Please enter only a valid number!!!")
	except ValueError:
		print("Please enter only a valid number!!!")
words = extract_key_words(chosen_template)
count = 0
while count < len(words):
	try:
		word = words[count].lower().strip()
		input_value = create_input_right(word)
		replacement_words.append((f"({words[count]})", input_value))
		count = count + 1
	except ValueError as ve:
		print("Wrong value.", ve)

for item in replacement_words:
	chosen_template = chosen_template.replace(item[0], item[1], 1)
print(chosen_template)
