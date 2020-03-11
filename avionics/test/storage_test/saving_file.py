print('Creating text file')
text = input("Enter data you would like to save: ")
Logfile = "data.txt"
file = open(Logfile, "w")
file.write(text)
#Wrote to text
file.close()
print('Data saved to text file')


#Open and read file'
file = open(Logfile, "r")
input_text = file.readline()
print('input text', input_text)
file.close()
