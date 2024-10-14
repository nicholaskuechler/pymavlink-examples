import time
from pymavlink import mavutil


# create a serial connection from raspberry pi to cube orange
master = mavutil.mavlink_connection("/dev/serial0", baud=921600)
master.wait_heartbeat()


# print messages received up to message_limit count
message_limit = 100
counter = 0
while True:
    try:
        print(master.recv_match().to_dict())
        counter += 1
    except:
        pass
    if counter > message_limit:
        break
    time.sleep(0.1)


# arm
master.arducopter_arm()
print("Waiting for the vehicle to arm")
master.motors_armed_wait()
print('Armed!')
