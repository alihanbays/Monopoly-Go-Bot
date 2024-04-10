import pyautogui
import keyboard
import time


goButtonPath = 'Buttons/GoButton.png'
collectButtonPath = 'Buttons/CollectButton.png'
shutdownButtonPath = 'Buttons/ShutDownButton.png'
heistButtonPath = 'Buttons/HeistButton.png'

def StartBot():
    while True:

        # GO BUTTON
        try:
            goButtonLocation = pyautogui.locateOnScreen(goButtonPath, confidence=0.9)
            if goButtonLocation:
                print("I've found the go button! :)")
                pyautogui.click(pyautogui.center(goButtonLocation))
            else:
                print("I couldn't find the go button! :(")
        except pyautogui.ImageNotFoundException:
            print("I've raised an execption")

        # CONFIRM BUTTON
        try:
            collectButtonLocation = pyautogui.locateOnScreen(collectButtonPath, confidence=0.9)
            if collectButtonLocation:
                print("I've found the go button! :)")
                pyautogui.click(pyautogui.center(collectButtonLocation))
            else:
                print("I couldn't find the go button! :(")
        except pyautogui.ImageNotFoundException:
            print("I've raised an execption")

        # SHUTDOWN BUTTON   
        try:
            shutdownButtonLocation = pyautogui.locateOnScreen(shutdownButtonPath, confidence=0.9)
            if shutdownButtonLocation:
                print("I've found the go button! :)")
                pyautogui.click(pyautogui.center(shutdownButtonLocation))
            else:
                print("I couldn't find the go button! :(")
        except pyautogui.ImageNotFoundException:
            print("I've raised an execption")

        # HEIST BUTTON   
        try:
            heistButtonLocation = pyautogui.locateOnScreen(heistButtonPath, confidence=0.9)
            if heistButtonLocation:
                print("I've found the go button! :)")
                pyautogui.click(pyautogui.center(heistButtonLocation))
            else:
                print("I couldn't find the go button! :(")
        except pyautogui.ImageNotFoundException:
            print("I've raised an execption")


        # Check if Enter key is pressed to stop
        if keyboard.is_pressed('enter'):  
            print("Stopping actions.")
            break  # Break out of the loop to stop actions
        time.sleep(1)


print("Press Space To Start The Bot!")
keyboard.wait('space')
StartBot()