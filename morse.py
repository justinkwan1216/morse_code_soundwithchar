import keyboard  # using module keyboard
import playsound
import winsound
import time
def check_word(array):
    if array==".-":
        return "a"
    elif array=="-...":
        return "b"
    elif array=="-.-.":
        return "c"
    elif array=="-..":
        return "d"
    elif array==".":
        return "e"
    elif array=="..-.":
        return "f"
    elif array=="--.":
        return "g"
    elif array=="....":
        return "h"
    elif array=="..":
        return "i"
    elif array==".---":
        return "j"
    elif array=="-.-":
        return "k"
    elif array==".-..":
        return "l"
    elif array=="--":
        return "m"
    elif array=="-.":
        return "n"
    elif array=="---":
        return "o"
    elif array==".--.":
        return "p"
    elif array=="--.-":
        return "q"
    elif array==".-.":
        return "r"
    elif array=="...":
        return "s"
    elif array=="-":
        return "t"
    elif array=="..-":
        return "u"
    elif array=="...-":
        return "v"
    elif array==".--":
        return "w"
    elif array=="-..-":
        return "x"
    elif array=="-.--":
        return "y"
    elif array=="--..":
        return "z"
    else:
        return 0
    
array=""
counter=0
while True:  # making a loop
    #print(array)
    try:  # used try so that if user pressed other than the given key error will not be shown
        if keyboard.is_pressed('0'):  # if key 'q' is pressed 
            array+="-"
            counter=0
            time.sleep(0.099)
            winsound.Beep(1000, 300)  # Beep at 1000 Hz for 100 ms
            #playsound.playsound('C:/Users/gifte/Downloads/Dat.mp3', duration="10")
        elif keyboard.is_pressed('.'):  # if key 'q' is pressed
            time.sleep(0.099)
            counter=0
            array+="."
            winsound.Beep(1000, 100)
            #playsound.playsound('C:/Users/gifte/Downloads/Dit.mp3', True)
        elif keyboard.is_pressed('1'):  # if key 'q' is pressed 
            array=""
        else:
            counter+=1
            if counter>=610:
                counter=0
                word=check_word(array)
                if word!=0:
                    print(word,end="")
                    array=""
                pass
        #print(counter)
    except:
        break  
