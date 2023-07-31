import serial
import time
import struct
arduino = serial.Serial(port = 'COM3', timeout=0)
time.sleep(2)
import platform
import os
import random 

def play_system_beep():
    if platform.system() == 'Windows':
        import winsound
        winsound.Beep(1000, 200)  # Frequency of 1000 Hz for 500 milliseconds
    elif platform.system() == 'Darwin' or platform.system() == 'Linux':
        os.system("echo -e '\a'")  # ASCII bell character for macOS and Linux
    else:
        print("Sorry, system beep is not supported on this platform.")

def random_sleep(min_duration, max_duration):
    return random.uniform(min_duration, max_duration)

# def beep_with_spacing(num_beeps, min_interval, max_interval):
    # beep_count = 0
    # retarr =  []
    # baseline = arduino.read(8)
    # while beep_count < num_beeps:
        # #arduino.write(str.encode('1'))
        # play_system_beep()

        # current_start_time_milliseconds = int(time.time() * 1000)

        # print(f"Current start time in milliseconds: {current_start_time_milliseconds}")

        # looping = True
        # while(looping):
            # x = arduino.read(8)
            # print(x)
            # if x >100:
                # looping = False
        # retarr.append(x)
        # print("reaction time was: ", x)
        # interval = random_sleep(min_interval, max_interval)
        # time.sleep(interval)
        # beep_count += 1
        # print("The current beep count is: ",beep_count)
        

# Play 200 beeps with intervals between 1 and 3 seconds
num_beeps = 200
min_interval = 1.5  # seconds
max_interval = 3  # seconds

#beep_with_spacing(num_beeps,min_interval,max_interval)

counter = 1
prev = 0
recording_arr = []
try:
    while True:
        if prev == 0: 
            arduino.reset_input_buffer()

            time.sleep(random_sleep(min_interval, max_interval))
            #_ = arduino.read(arduino.in_waiting)  # Clear any data in the buffer
            starting_point = time.time()
            play_system_beep()
            prev = 1

        if arduino.in_waiting > 0 and prev==1:
            received_data = arduino.read(1).decode('utf-8')
            if 'A' in received_data and prev == 1:
                prev = 0
                arduino.reset_input_buffer()

                current_time = time.time()
                elapsed_time_milliseconds = (current_time - starting_point) * 1000
                print(f"Recording {counter} reaction time: {elapsed_time_milliseconds} ms")
                recording_arr.append(elapsed_time_milliseconds)
                counter+=1
                continue
except KeyboardInterrupt:
    print("Here are the values: ")
    for element in recording_arr:
        print(round(element,3))

    
