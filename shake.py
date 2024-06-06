import cyberpi
from cypi import write_csv, get_time

# Define your column headers
data = [
    ["Label", "Shake_Value"],
]

label = "running"
num_of_samples = 50

while len(data) < num_of_samples:
    val = cyberpi.get_shakeval()
    data.append([label, val])
    cyberpi.console.println(label + " " + str(val))

filename = get_time() + "_" + "data10.csv"
write_csv(data, filename)
cyberpi.console.println("Data saved.")