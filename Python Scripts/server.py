
from opcua import Server
from random import randint
import datetime
import time

server = Server()

url = "opc.tcp://localhost:4840"
server.set_endpoint(url)

name = "OPCUA_SIMULATION_SERVER"
addspace = server.register_namespace(name)

node = server.get_objects_node()

Param = node.add_object(addspace, "Parameters")

Temp = Param.add_variable(addspace, "Temperature", 0)
Press = Param.add_variable(addspace, "Pressure", 0)
Time = Param.add_variable(addspace, "Time", 0)

Temp.set_writable()
Press.set_writable()
Time.set_writable()

server.start()
print("Server started at {}".format(url))

while True:
    SetTemp = randint(10, 50)
    SetPress = randint(200, 999)
    SetTime = datetime.datetime.now()

    print(SetTemp, SetPress, SetTime)

    Temp.set_value(SetTemp)
    Press.set_value(SetPress)
    Time.set_value(SetTime)

    time.sleep(2)