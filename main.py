import threading
from brain import pi_ai_talking
#from integrate_image import describe_image
from listen import listen
from DLG import *
def comain():
    output_text = ""
    while True:
        with open("input.txt", "r") as input_text:
            current_text = input_text.read()
        if current_text!= output_text:
            output_text = current_text
            text = output_text.lower()
            pi_ai_talking(text)
            #describe_image(text)

            if "ok bye" in text:
                print("sure sir , we will meet again")
                break
            else:
                 pass
        else:
            pass
def main():

    output_text = ""
    while True:
        with open("input.txt", "r") as input_text:
            current_text = input_text.read()
        if current_text!= output_text:
            output_text = current_text
            wake_cmd = output_text.lower()
            if wake_cmd in wake_key_word:
                comain()



        else:
              pass


def jarvis():
    t0 = threading.Thread(target=listen)
    t1 = threading.Thread(target=main)
    t0.start()
    t1.start()
    t0.join()
    t1.join()

jarvis()
    

