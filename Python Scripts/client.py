from opcua import Client
import time

url = "opc.tcp://localhost:4840"

client = Client(url)

client.connect()
print("Client Connected")

while True:
    SetTemp = client.get_node("ns=2;i=2")
    SetPress = client.get_node("ns=2;i=3") #NS2|Numeric|3
    SetTime = client.get_node("ns=2;i=4")

    Temperature = SetTemp.get_value()
    Pressure = SetPress.get_value()
    Time = SetTime.get_value()

    print(Temperature,Pressure,Time)

    time.sleep(1)