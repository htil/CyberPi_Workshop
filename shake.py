import cyberpi
from cypi import write_csv, get_time

# Define your column headers
data = [
    ["Index", "Label", "Shake_Value"],
]

label = "sitting"
num_of_samples = 50
index = 0
cyberpi.console.println("Starting program.")
while len(data) < num_of_samples:
    val = cyberpi.get_shakeval()
    data.append([index, label, val])
    cyberpi.console.println(label + " " + str(val))
    index += 1

filename = "shake.csv"
write_csv(data, filename)
cyberpi.console.println("Data saved.")