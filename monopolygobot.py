import pyautogui
import keyboard
import time


goButtonPath = 'Buttons/GoButton.png'
collectButtonPath = 'Buttons/CollectButton.png'
shutdownButtonPath = 'Buttons/ShutDownButton.png'
heistButtonPath = 'Buttons/HeistButton.png'
megaHeistButtonPath = 'Buttons/MegaHeistButton.png'
shutdown2ButtonPath = 'Buttons/ShutDown2Button.png'
closeButtonPath = 'Buttons/CloseButton.png'
okayButtonPath = 'Buttons/OkayButton.png'
close2ButtonPath = 'Buttons/Close2Button.png'
close3ButtonPath = 'Buttons/Close3Button.png'
onItButtonPath = 'Buttons/OnItButton.png'
jailButtonPath = 'Buttons/JailButton.png'

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
            shutdownButtonLocation = pyautogui.locateOnScreen(shutdownButtonPath, confidence=0.5)
            if shutdownButtonLocation:
                print("I've found the go button! :)")
                pyautogui.click(pyautogui.center(shutdownButtonLocation))
            else:
                print("I couldn't find the go button! :(")
        except pyautogui.ImageNotFoundException:
            print("I've raised an execption")
        
        # SHUTDOWN2 BUTTON   
        try:
            shutdown2ButtonLocation = pyautogui.locateOnScreen(shutdown2ButtonPath, confidence=0.5)
            if shutdown2ButtonLocation:
                print("I've found the go button! :)")
                pyautogui.click(pyautogui.center(shutdown2ButtonLocation))
            else:
                print("I couldn't find the go button! :(")
        except pyautogui.ImageNotFoundException:
            print("I've raised an execption")

        # HEIST BUTTON   
        try:
            heistButtonLocation = pyautogui.locateOnScreen(heistButtonPath, confidence=0.8)
            if heistButtonLocation:
                print("I've found the go button! :)")
                pyautogui.click(pyautogui.center(heistButtonLocation))
            else:
                print("I couldn't find the go button! :(")
        except pyautogui.ImageNotFoundException:
            print("I've raised an execption")

        # MEGA HEIST BUTTON   
        try:
            megaHeistButtonLocation = pyautogui.locateOnScreen(megaHeistButtonPath, confidence=0.9)
            if megaHeistButtonLocation:
                print("I've found the go button! :)")
                pyautogui.click(pyautogui.center(megaHeistButtonLocation))
            else:
                print("I couldn't find the go button! :(")
        except pyautogui.ImageNotFoundException:
            print("I've raised an execption")

        # CLOSE BUTTON   
        try:
            closeButtonLocation = pyautogui.locateOnScreen(closeButtonPath, confidence=0.9)
            if closeButtonLocation:
                print("I've found the go button! :)")
                pyautogui.click(pyautogui.center(closeButtonLocation))
            else:
                print("I couldn't find the go button! :(")
        except pyautogui.ImageNotFoundException:
            print("I've raised an execption")

        # OKAY BUTTON   
        try:
            okayButtonLocation = pyautogui.locateOnScreen(okayButtonPath, confidence=0.9)
            if okayButtonLocation:
                print("I've found the go button! :)")
                pyautogui.click(pyautogui.center(okayButtonLocation))
            else:
                print("I couldn't find the go button! :(")
        except pyautogui.ImageNotFoundException:
            print("I've raised an execption")

        # CLOSE 2 BUTTON   
        try:
            close2ButtonLocation = pyautogui.locateOnScreen(close2ButtonPath, confidence=0.9)
            if close2ButtonLocation:
                print("I've found the go button! :)")
                pyautogui.click(pyautogui.center(close2ButtonLocation))
            else:
                print("I couldn't find the go button! :(")
        except pyautogui.ImageNotFoundException:
            print("I've raised an execption")

        # CLOSE 3 BUTTON   
        try:
            close3ButtonLocation = pyautogui.locateOnScreen(close3ButtonPath, confidence=0.9)
            if close3ButtonLocation:
                print("I've found the go button! :)")
                pyautogui.click(pyautogui.center(close3ButtonLocation))
            else:
                print("I couldn't find the go button! :(")
        except pyautogui.ImageNotFoundException:
            print("I've raised an execption")

        # OKAY BUTTON   
        try:
            onItButtonLocation = pyautogui.locateOnScreen(onItButtonPath, confidence=0.9)
            if onItButtonLocation:
                print("I've found the go button! :)")
                pyautogui.click(pyautogui.center(onItButtonLocation))
            else:
                print("I couldn't find the go button! :(")
        except pyautogui.ImageNotFoundException:
            print("I've raised an execption")

        # JAIL BUTTON   
        try:
            jailButtonLocation = pyautogui.locateOnScreen(jailButtonPath, confidence=0.9)
            if jailButtonLocation:
                print("I've found the go button! :)")
                pyautogui.click(pyautogui.center(jailButtonLocation))
            else:
                print("I couldn't find the go button! :(")
        except pyautogui.ImageNotFoundException:
            print("I've raised an execption")

        # Check if Enter key is pressed to stop
        if keyboard.is_pressed('enter'):  
            print("Stopping actions.")
            break  # Break out of the loop to stop actions


print("Press Space To Start The Bot!")
keyboard.wait('space')
StartBot()