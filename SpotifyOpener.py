import Leap
import sys
import os
import time


class Listener(Leap.Listener):
    def on_connect(self, controller):
        print "Connected"

    def on_frame(self, controller):
        frame = controller.frame()

        if len(frame.hands) > 0:
            filepath = "C:\Users\Anthony\Desktop\Spotify - Shortcut.lnk"
            os.startfile(filepath)

def main():

    controller = Leap.Controller()
    listener = Listener() 

    controller.add_listener(listener)

    # Keep this process running until Enter is pressed
    print "Press Enter to quit..."

    try:
        sys.stdin.readline()
    except KeyboardInterrupt:
        pass

if __name__ == "__main__":
    main()

