import csv

time = []
altitude = []
latitude = []
longitude = []
density = []

filename = "/Users/shannu/Desktop/AI L3.csv"
with open(filename) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            #this is the first line. It describes the data
            header = row
            line_count += 1
        else:
            #fill our lists (remember to convert string to float)
            time.append(row[0])
            altitude.append(float(row[7]))
            density.append(float(row[15]))

### Add code below this point.

#PROBLEM-1

'''Add a for loop that prints all of the altitude density data in the following format:
    Altitude: nnn.nnn km, density: nnn.nnn #/cm3
where n's are place holders for the actual values. 
Use the .format() function when printing to do this.'''

print(len(altitude)) #length is 181

for i in range(len(altitude)):  #len function gives the length,Here length of altitude = density

    print("Altitude: {:.3f},density: {:.3f} #/cm3".format(altitude[i], density[i]))

