message="Tuesday: 22C, Wednesday: 21C, Thursday: 26C "
import re
message = "Tuesday: 22C, Wednesday: 21C, Thursday: 26C "
temperatures = re.findall("\d{2}",message)
suma=0
for x in range(len(temperatures)):
    suma+=int(temperatures[x])
print(suma/len(temperatures))