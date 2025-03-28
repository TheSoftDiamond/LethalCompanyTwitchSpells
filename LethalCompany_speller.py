import concurrent.futures, keyboard, time
import pydirectinput, pyautogui
import TwitchPlays_Connection
from TwitchPlays_KeyCodes import *
import psutil
import ctypes
import settings

# Load configurations from the settings file
TWITCH_CHANNEL = settings.TWITCH_CHANNEL
STREAMING_ON_TWITCH = settings.STREAMING_ON_TWITCH
YOUTUBE_CHANNEL_ID = settings.YOUTUBE_CHANNEL_ID 
YOUTUBE_STREAM_URL = settings.YOUTUBE_STREAM_URL
MESSAGE_RATE = settings.MESSAGE_RATE
MAX_QUEUE_LENGTH = settings.MAX_QUEUE_LENGTH
MAX_WORKERS = settings.MAX_WORKERS
disableSameUser = settings.disableSameUser
printProgress = settings.printProgress
announceWin = settings.announceWin
full_dictionary = settings.full_dictionary
cooldown = settings.cooldown

# These are used to keep track of the messages and tasks
last_time = time.time()
message_queue = []
thread_pool = concurrent.futures.ThreadPoolExecutor(max_workers=MAX_WORKERS)
active_tasks = []
pyautogui.FAILSAFE = False

# These are used to keep track of the progress of the word
word_progress = {word: '' for word in full_dictionary}
word_lengths = {word: len(word) for word in full_dictionary}
last_spawn_time = {word: int(cooldown) for word in full_dictionary}
last_user = None

if STREAMING_ON_TWITCH:
    t = TwitchPlays_Connection.Twitch()
    t.twitch_connect(TWITCH_CHANNEL)
else:
    t = TwitchPlays_Connection.YouTube()
    t.youtube_connect(YOUTUBE_CHANNEL_ID, YOUTUBE_STREAM_URL)

def get_active_exe_name():
    user32 = ctypes.windll.user32
    kernel32 = ctypes.windll.kernel32

    # Get the handle of the foreground window
    hwnd = user32.GetForegroundWindow()

    # Get the process ID of the foreground window
    pid = ctypes.c_ulong()
    user32.GetWindowThreadProcessId(hwnd, ctypes.byref(pid))

    # Get the process name from the process ID
    process = psutil.Process(pid.value)
    exe_name = process.name()

    return exe_name

def check_name(name, names_list):
    for n in names_list:
        if n.lower() == name.lower():
            return True
    return False

def handle_message(message):
    global word_progress, last_user, last_spawn_time
    try:
        themessage = message['message'].lower()
        theusername = message['username'].lower()
        
        if check_name(theusername, settings.BannedUsers):
            return
        
        if themessage.startswith('!'):
            return
        
        print("Got this message from " + theusername + ": " + themessage)

        # Only process single-character messages
        if len(themessage) == 1:
            # if disableSameUser is enabled, prevent the same user from playing twice in a row
            if disableSameUser and theusername == last_user:
                print(f"User {theusername} is not allowed to play twice in a row.")
                return

            new_word_progress = {}
            word_completed = False
            
            for word, current_progress in word_progress.items():
                progress_length = len(current_progress)
                word_length = word_lengths[word]
                
                if progress_length < word_length and word[progress_length] == themessage:
                    new_progress = current_progress + themessage
                    new_word_progress[word] = new_progress
                    print(f"Progressing: {new_progress} in word {word}")
                    
                    # Check if the word has been completed
                    if progress_length + 1 == word_length:
                        if announceWin: # Announce the user who completed the word
                            print(f"Word '{word}' completed by {theusername}")
                            print(f"{theusername} completed the word '{word}'!")
                        word_completed = True
                        break
                else:
                    new_word_progress[word] = ""  # Reset progress for invalid inputs
            
            if word_completed:
                active_exe_name = get_active_exe_name()
                current_time = time.time()
                if active_exe_name in settings.ApprovedExeProcesses:
                    if current_time - last_spawn_time[word] >= cooldown:
                        last_spawn_time[word] = current_time

                        # THIS IS WHERE THE MAGIC HAPPENS
                        if word == "random":
                            print("Attempted to spawn enemy")
                            HoldKey(LEFT_ALT)
                            HoldKey(NUMPAD_9)
                            ReleaseKey(NUMPAD_9)
                            ReleaseKey(LEFT_ALT)

                        if word == "baboonhawk":
                            print("Attempted to spawn enemy")
                            HoldKey(LEFT_ALT)
                            HoldKey(NUMPAD_8)
                            ReleaseKey(NUMPAD_8)
                            ReleaseKey(LEFT_ALT)

                        if word == "barber":
                            print("Attempted to spawn enemy")
                            HoldKey(LEFT_ALT)
                            HoldKey(NUMPAD_7)
                            ReleaseKey(NUMPAD_7)
                            ReleaseKey(LEFT_ALT)

                        if word == "hygrodere":
                            print("Attempted to spawn enemy")
                            HoldKey(LEFT_ALT)
                            HoldKey(NUMPAD_6)
                            ReleaseKey(NUMPAD_6)
                            ReleaseKey(LEFT_ALT)

                        if word == "bracken":
                            print("Attempted to spawn enemy")
                            HoldKey(LEFT_ALT)
                            HoldKey(NUMPAD_5)
                            ReleaseKey(NUMPAD_5)
                            ReleaseKey(LEFT_ALT)
                        
                        if word == "spider":
                            print("Attempted to spawn enemy")
                            HoldKey(LEFT_ALT)
                            HoldKey(NUMPAD_4)
                            ReleaseKey(NUMPAD_4)
                            ReleaseKey(LEFT_ALT)

                        if word == "butler":
                            print("Attempted to spawn enemy")
                            HoldKey(LEFT_ALT)
                            HoldKey(NUMPAD_3)
                            ReleaseKey(NUMPAD_3)
                            ReleaseKey(LEFT_ALT)

                        if word == "coilhead":
                            print("Attempted to spawn enemy")
                            HoldKey(LEFT_ALT)
                            HoldKey(NUMPAD_2)
                            ReleaseKey(NUMPAD_2)
                            ReleaseKey(LEFT_ALT)

                        if word == "leviathan":
                            print("Attempted to spawn enemy")
                            HoldKey(LEFT_ALT)
                            HoldKey(NUMPAD_1)
                            ReleaseKey(NUMPAD_1)
                            ReleaseKey(LEFT_ALT)

                        if word == "eyelessdog":
                            print("Attempted to spawn enemy")
                            HoldKey(LEFT_ALT)
                            HoldKey(NUMPAD_0)
                            ReleaseKey(NUMPAD_0)
                            ReleaseKey(LEFT_ALT)

                        if word == "forestgiant":
                            print("Attempted to spawn enemy")
                            HoldKey(LEFT_ALT)
                            HoldKey(F8)
                            ReleaseKey(F8)
                            ReleaseKey(LEFT_ALT)

                        if word == "ghostgirl":
                            print("Attempted to spawn enemy")
                            HoldKey(LEFT_ALT)
                            HoldKey(F9)
                            ReleaseKey(F9)
                            ReleaseKey(LEFT_ALT)

                        if word == "hoardingbug":
                            print("Attempted to spawn enemy")
                            HoldKey(LEFT_ALT)
                            HoldKey(F10)
                            ReleaseKey(F10)
                            ReleaseKey(LEFT_ALT)

                        if word == "jester":
                            print("Attempted to spawn enemy")
                            HoldKey(LEFT_ALT)
                            HoldKey(NUMPAD_MINUS)
                            ReleaseKey(NUMPAD_MINUS)
                            ReleaseKey(LEFT_ALT)
                        
                        if word == "kidnapperfox":
                            print("Attempted to spawn enemy")
                            HoldKey(LEFT_ALT)
                            HoldKey(NUMPAD_PLUS)
                            ReleaseKey(NUMPAD_PLUS)
                            ReleaseKey(LEFT_ALT)

                        if word == "maneater":
                            print("Attempted to spawn enemy")
                            HoldKey(LEFT_ALT)
                            HoldKey(NUMPAD_ENTER)
                            ReleaseKey(NUMPAD_ENTER)
                            ReleaseKey(LEFT_ALT)
                        
                        if word == "manticoil":
                            print("Attempted to spawn enemy")
                            HoldKey(LEFT_ALT)
                            HoldKey(NUMPAD_PERIOD)
                            ReleaseKey(NUMPAD_PERIOD)
                            ReleaseKey(LEFT_ALT)
                        
                        if word == "masked":
                            print("Attempted to spawn enemy")
                            HoldKey(LEFT_ALT)
                            HoldKey(F1)
                            ReleaseKey(F1)
                            ReleaseKey(LEFT_ALT)
                        
                        if word == "nutcracker":
                            print("Attempted to spawn enemy")
                            HoldKey(LEFT_ALT)
                            HoldKey(F2)
                            ReleaseKey(F2)
                            ReleaseKey(LEFT_ALT)

                        if word == "oldbird":
                            print("Attempted to spawn enemy")
                            HoldKey(LEFT_ALT)
                            HoldKey(F3)
                            ReleaseKey(F3)
                            ReleaseKey(LEFT_ALT)

                        if word == "snareflea":
                            print("Attempted to spawn enemy")
                            HoldKey(LEFT_ALT)
                            HoldKey(F4)
                            ReleaseKey(F4)
                            ReleaseKey(LEFT_ALT)

                        if word == "sporelizard":
                            print("Attempted to spawn enemy")
                            HoldKey(LEFT_ALT)
                            HoldKey(F5)
                            ReleaseKey(F5)
                            ReleaseKey(LEFT_ALT)

                        if word == "thumper":
                            print("Attempted to spawn enemy")
                            HoldKey(LEFT_ALT)
                            HoldKey(F6)
                            ReleaseKey(F6)
                            ReleaseKey(LEFT_ALT)
                        
                        if word == "tulipsnake":
                            print("Attempted to spawn enemy")
                            HoldKey(LEFT_ALT)
                            HoldKey(F7)
                            ReleaseKey(F7)
                            ReleaseKey(LEFT_ALT)
                    
                    else:
                        print("ON COOLDOWN")
      
                word_progress = {word: '' for word in full_dictionary}
                last_user = None
                print("Game reset. Word progress initialized.")
            else:
                word_progress = new_word_progress
                last_user = theusername

            if printProgress:
                print(f"Current word progress: {word_progress}")

    except Exception as e:
        print(f"Error in handle_message: {e}")

while True:
    active_tasks = [t for t in active_tasks if not t.done()]

    # Check for new messages
    new_messages = t.twitch_receive_messages()
    if new_messages:
        message_queue += new_messages  # New messages are added to the back of the queue
        message_queue = message_queue[-MAX_QUEUE_LENGTH:]  # Shorten the queue to only the most recent X messages

    messages_to_handle = []
    if not message_queue:
        # No messages in the queue
        last_time = time.time()
    else:
        # Determine how many messages we should handle now
        r = 1 if MESSAGE_RATE == 0 else (time.time() - last_time) / MESSAGE_RATE
        n = int(r * len(message_queue))
        if n > 0:
            # Pop the messages we want off the front of the queue
            messages_to_handle = message_queue[0:n]
            del message_queue[0:n]
            last_time = time.time()

    # If user presses Shift+Backspace, automatically end the program
    if keyboard.is_pressed('shift+backspace'):
        exit()

    if not messages_to_handle:
        continue
    else:
        for message in messages_to_handle:
            if len(active_tasks) <= MAX_WORKERS:
                active_tasks.append(thread_pool.submit(handle_message, message))
            else:
                print(f'WARNING: active tasks ({len(active_tasks)}) exceeds number of workers ({MAX_WORKERS}). ({len(message_queue)} messages in the queue)')
 
