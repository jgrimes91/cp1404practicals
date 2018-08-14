OUTPUT_FILE = "output_name.txt"
out_file = open(OUTPUT_FILE, 'w')

username = input("What is your name?")
print(username, file=out_file)

out_file.close()