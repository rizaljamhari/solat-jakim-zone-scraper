# import needed library
from bs4 import BeautifulSoup
import urllib.request
import csv

wiki = "http://api.kayrules.com/solatjakim/zones"
header = {'User-Agent': 'Mozilla/5.0'}
req = urllib.request.Request(wiki,headers=header)
page = urllib.request.urlopen(req)
soup = BeautifulSoup(page, "html.parser")

code = ""
location = ""
latitude = ""
longitude = ""
table = soup.find_all("tbody")
print (table)

f = open('locationcode.csv', 'w')

for x in range(0, len(table)):
    for row in table[x].findAll("tr"):
        cells = row.findAll("td")
        #For each "tr", assign each "td" to a variable.
        if len(cells) == 4:
            code = cells[0].find(text=True)
            location = cells[1].find(text=True)
            latitude = cells[2].find(text=True)
            longitude = cells[3].find(text=True)

            write_to_file = code + "," + location + "," + latitude + "," + longitude + "\n"
            print (write_to_file)
            f.write(write_to_file)
            # # open a csv file with append, so old data will not be erased
            # with open('locationcode.csv', 'a') as csv_file:
            #     writer = csv.writer(csv_file)
            #     writer.writerow([code, location, latitude, longitude])

f.close()
