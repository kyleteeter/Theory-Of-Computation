import re # module for processing regular expressions https://docs.python.org/3/library/re.html
import sys
import csv
if __name__ == '__main__':
  # Exit if command line args entered incorrectly
  if len(sys.argv) != 2:
    print("usage: extract_links.py [input_file]")
    sys.exit(0)

# Filename is 2nd command line arg
filename = sys.argv[1]

# TODO Read HTML
matches = []
with open(f"{filename}", "r", encoding='utf-8') as f:
  # TODO Set up regex
    for line in f:
      if 'http' in line:
        link_ex = (r"(http|https)\:\/\/[a-zA-Z0-9\-\.]+(?:(?!'|\").)*")
        link = re.findall(link_ex, line)
        print(link)
        if len(link) > 0:
          matches.append(link[0])
    f.close()
if matches:
  for match in matches:
    print(match)

# TODO Find links using regex, save in list called 'matches'
# (http).+[>]

# Check matches, print results
# TODO Read in links from answers.txt (hint...this is a CSV file), 
# save in list called 'answer_data'

answer_data = []
with open("answers.txt", "r") as csvfile:
  readCSV = csv.reader(csvfile, delimiter=",")
  for answers in readCSV:
    for index in answers:
      answer_data.append(index)
  csvfile.close()


# Compare answers with matches found using regex, print out any mismatches
# UNCOMMENT BELOW WHEN READY TO CHECK IF YOUR REGEX IS FINDING ALL THE LINKS
result = "All links matched!"
if len( matches ) != len( answer_data ):
  result = "Your regex found %i matches. There should be %i matches" %(len( matches ), len( answer_data ) )
else:
  for i in range( len(answer_data) ):
    if( matches[i] != answer_data[i] ):
      result = "Mismatched link. Got %s but expected %s" % ( matches[i], answer_data[i] )
      break
print( result )