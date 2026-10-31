from tools import get_current_time,roll_dice,generate_password,read_text_file

print(get_current_time())
print(roll_dice())
print(generate_password())

text = read_text_file("data/notes.txt")

print(text)
