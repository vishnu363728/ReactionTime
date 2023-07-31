# ReactionTime

# Physics 4AL Experiment Setup with Arduino and Python

This guide outlines the setup for a physics experiment that involves using an Arduino board and Python code. The experiment measures reaction times by detecting when a button is pressed in response to a sound signal. Below are the step-by-step instructions and some code details for the experiment.

## Instructions:

1. **Download Arduino Code:**
   - Download the `arduinoComponents.ino` file and import it into the Arduino IDE.
   - Upload the code to your Arduino board.

2. **Set Up Python Environment:**
   - Download Python on your computer if you don't already have it installed.
   - Download the `.py` file that will run the Python component of the experiment.

3. **Install PySerial:**
   - Open your terminal or command prompt and type the following command to install the `pyserial` library:
   
```
pip install pyserial
```


4. **Navigate to File Location:**
- Open your terminal or command prompt and navigate to the location where you saved the Python file. For example, if the file is in the "Downloads" folder, use the following command:

```
cd Downloads
```


5. **Run Python Program:**
- In the terminal, type the following command to run the Python program that interfaces with the Arduino:
  
```
python pythonComponent.py
```


6. **Start the Experiment:**
- When you hear the sound, press the button on the circuit in response. Do not hold the button or press it between sounds.
- The program will display the reaction time in milliseconds, for example: "Recording 1 reaction time: 233.69073867797852 ms".

7. **Collect Samples:**
- Continue pressing the button and collecting samples until you have as many as you need.
- To stop the experiment, press `Ctrl-C` in the terminal.

8. **View and Save Results:**
- After stopping the experiment, the values will be displayed in the terminal like this:

```
Here are the values:
233.691
213.779
226.378
208.988
```

- Copy and paste these values into a `.txt` file for further analysis or record-keeping.
## Code Overview:

The experiment involves two programs that interface with each other via the Arduino. The Arduino program is written in C and sends a message when the button is pressed to the Python program. The Python program handles sound generation, timing, and data collection.

**The Arduino Code:**
- Written in C and uploaded to the Arduino board using the Arduino IDE.
- It detects the status of the button and sends a character 'A' through the Arduino's serial port when the button is pressed.

**The Python Code:**
- It first detects the operating system (Windows or Mac/Linux) and uses the appropriate module (e.g., `winsound` for Windows) to sound a beep.
- Generates a random sleep time between beeps using the `random` module.
- Runs an infinite loop that waits for a response from the Arduino's serial port (using `pyserial`) after playing a beep.
- Calculates and displays the reaction time when the 'A' character is received.
- Keeps track of the number of samples taken and stops after reaching the desired count.
- Reacts to `Ctrl-C` to stop the infinite loop and displays the collected values for easy copy-and-paste.




