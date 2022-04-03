import random
import sys

def main():
    print("Welcome to the useful keyboard shortcut quiz (including some extra mouse click commands)!\n")
    name = str(input("Mortal! What is your name? "))
    print("Okay, \"{0}\", if that is your real name...\n".format(name))
    instruction()
    print("There is a total of *77* different questions...")
    while True:
        try:
            quest = int(input("Input how many questions you want to be asked: "))
        except ValueError:
            print("What the heck did you even type? Invalid input. Try again.\n")
            continue
        if quest < 1:
            print("Are you okay? You want to give up before you even start? Okay... Coward.")
            results(0, 0, 0)
            continue
        elif quest > 77:
            print("Calm down. There's not even that many questions... Try again.\n")
            continue
        else:
            break

    print("ARE YOU READY? SHOW ME YOUR KNOWLEDGE!!!\n")
    score = 0
    combo = 0
    keylist = random.sample(range(77), quest)
    questnum = 1
    for key in keylist:
        score, combo = quiz(key, quest, score, questnum, combo)
        questnum+=1
    results(score, quest, combo)

def instruction():
    print("READ CAREFULLY. INSTRUCTIONS:")
    print("\t1) You will answer by typing out the abbreviation of the keyboard shortcuts in small case letters.")
    print("\t2) You do not need to type in the \'+\' symbol in between your answer. Just space it.")
    print("\t\tExample:")
    print("\t\t\tQ1. Copy?")
    print("\t\t\t-> [ctrl c]")
    print("\t3) You can input [quit] or [exit] during the quiz to stop at anytime")
    print("\t4) You can input [reset] during the quiz to stop at anytime")
    print("\t5) The allowed keywords are as follows:")
    keywords()

def keywords():
    print("\t\tControl key = [ctrl]")
    print("\t\tShift key = [shift]")
    print("\t\tAlternate key = [alt]")
    print("\t\tWindows key = [win]")
    print("\t\tSpace key = [space]")
    print("\t\tDelete key = [del]")
    print("\t\tHome key = [home]")
    print("\t\tEnd key = [end]")
    print("\t\tPage up key = [pgup]")
    print("\t\tPage down key = [pgdown]")
    print("\t\tEscape key = [esc]")
    print("\t\tTab key = [tab]")
    print("\t\tFunction keys = [f1] through [f12]")
    print("\t\tNumber keys = [0] through [9]")
    print("\t\tLetter keys = [a] through [z]")
    print("\t\tHyphen key = [-]")
    print("\t\tPlus(Equals) key = [+] or [=]")
    print("\t\tArrow keys = [left], [down], [up], [right]")
    print("\t\tMiddle Mouse button = [m3]")
    print("\n\tNOTE: If at anytime you need to bring up this list, type \'keywords\' during the quiz. You also are NOT to input the [ ] brackets in your answer.\n")

def quiz(key, quest, score, index, combo):
    content = sheet(key)
    while True:
        print("Q{0}. {1}".format(index, content))
        answer = str(input("-> "))
        if answer == 'keywords':
            keywords()
            continue
        elif answer == 'quit' or answer == 'exit':
            sys.exit(0)
        elif answer == 'reset':
            print("\n\nThere is a total of *77* different questions...")
            while True:
                try:
                    quest = int(input("Input how many questions you want to be asked: "))
                except ValueError:
                    print("What the heck did you even type? Invalid input. Try again.\n")
                    continue
                if quest < 1:
                    print("Are you okay? You want to give up before you even start? Okay... Coward.")
                    results(0, 0, 0)
                    continue
                elif quest > 77:
                    print("Calm down. There's not even that many questions... Try again.\n")
                    continue
                else:
                    break

            print("ARE YOU READY? SHOW ME YOUR KNOWLEDGE!!!\n")
            score = 0
            combo = 0
            keylist = random.sample(range(77), quest)
            questnum = 1
            for key in keylist:
                score, combo = quiz(key, quest, score, questnum, combo)
                questnum+=1
            results(score, quest, combo)

        else:
            break
    
    correct = rightwrong(answer, key)
    if correct == True and combo==0:
        print("Correct!")
        print("+1 score\n")
        combo+=1
        return score+1, combo
    elif correct == True and combo==1:
        print("Nice!")
        print("+1 score\n")
        combo+=1
        return score+1, combo
    elif correct == True and combo==2:
        print("Would ya look at that?")
        print("+1 score\n")
        combo+=1
        return score+1, combo
    elif correct == True and combo==3:
        print("OH SNAP!")
        combo+=1
        print("= COMBO x {0} =\n".format(combo-1))
        return score+1, combo
    elif correct == True and combo==4:
        print("HEATIN' UP~")
        combo+=1
        print("= COMBO x {0} =\n".format(combo-1))
        return score+1, combo
    elif correct == True and combo==5:
        print("You're getting good at this.")
        combo+=1
        print("= COMBO x {0} =\n".format(combo-1))
        return score+1, combo
    elif correct == True and combo==6:
        print("Keep it up!")
        combo+=1
        print("= COMBO x {0} =\n".format(combo-1))
        return score+1, combo
    elif correct == True and combo==7:
        print("HOLY")
        combo+=1
        print("= COMBO x {0} =\n".format(combo-1))
        return score+1, combo
    elif correct == True and combo==8:
        print("You've done this before, haven't you?")
        combo+=1
        print("= COMBO x {0} =\n".format(combo-1))
        return score+1, combo
    elif correct == True and combo==9:
        print("Woww!")
        combo+=1
        print("= COMBO x {0} =\n".format(combo-1))
        return score+1, combo
    elif correct == True and combo==10:
        print("Amazing!!")
        combo+=1
        print("= COMBO x {0}! =\n".format(combo-1))
        return score+1, combo
    elif correct == True and combo==11:
        print("Marvelousss~")
        combo+=1
        print("= COMBO x {0}! =\n".format(combo-1))
        return score+1, combo
    elif correct == True and combo==12:
        print("Incredible!")
        combo+=1
        print("= COMBO x {0}! =\n".format(combo-1))
        return score+1, combo
    elif correct == True and combo==13:
        print("MLG! MLG!")
        combo+=1
        print("= COMBO x {0}! =\n".format(combo-1))
        return score+1, combo
    elif correct == True and combo==14:
        print("You deserve to be sponsored.")
        combo+=1
        print("= COMBO x {0}! =\n".format(combo-1))
        return score+1, combo
    elif correct == True and combo==15:
        print("HAPPY FEET")
        combo+=1
        print("= COMBO x {0}! =\n".format(combo-1))
        return score+1, combo
    elif correct == True and combo==16:
        print("WOMBO COMBO")
        combo+=1
        print("= COMBO x {0}! =\n".format(combo-1))
        return score+1, combo
    elif correct == True and combo==17:
        print("THAT AIN'T FALCO")
        combo+=1
        print("= COMBO x {0}! =\n".format(combo-1))
        return score+1, combo
    elif correct == True and combo==18:
        print("Oh.")
        combo+=1
        print("= COMBO x {0}! =\n".format(combo-1))
        return score+1, combo
    elif correct == True and combo==19:
        print("OHHHHHHHHHHHHHH")
        combo+=1
        print("= COMBO x {0}! =\n".format(combo-1))
        return score+1, combo
    elif correct == True and combo==20:
        print("OH MY GOD!")
        combo+=1
        print("= COMBO x {0}!! =\n".format(combo-1))
        return score+1, combo
    elif correct == True and combo==21:
        print("You're a legend.")
        combo+=1
        print("= COMBO x {0}!! =\n".format(combo-1))
        return score+1, combo
    elif correct == True and combo==22:
        print("CAN YOU KEEP IT UP?")
        combo+=1
        print("= COMBO x {0}!! =\n".format(combo-1))
        return score+1, combo
    elif correct == True and combo==23:
        print("DON'T STOP!")
        combo+=1
        print("= COMBO x {0}!! =\n".format(combo-1))
        return score+1, combo
    elif correct == True and combo==24:
        print("BELIEEEEEVIN!")
        combo+=1
        print("= COMBO x {0}!! =\n".format(combo-1))
        return score+1, combo
    elif correct == True and combo==25:
        print("Wonderful.")
        combo+=1
        print("= COMBO x {0}!! =\n".format(combo-1))
        return score+1, combo
    elif correct == True and combo==26:
        print("HYPE")
        combo+=1
        print("= COMBO x {0}!! =\n".format(combo-1))
        return score+1, combo
    elif correct == True and combo==27:
        print("Pog")
        combo+=1
        print("= COMBO x {0}!! =\n".format(combo-1))
        return score+1, combo
    elif correct == True and combo==28:
        print("Did you make this quiz?")
        combo+=1
        print("= COMBO x {0}!! =\n".format(combo-1))
        return score+1, combo
    elif correct == True and combo==29:
        print("You made this quiz didn't you?")
        combo+=1
        print("= COMBO x {0}!! =\n".format(combo-1))
        return score+1, combo
    elif correct == True and combo==30:
        print("Phenomenal.")
        combo+=1
        print("= COMBO x {0}!!! =\n".format(combo-1))
        return score+1, combo
    elif correct == True and combo==31:
        print("I KNEW IT.")
        combo+=1
        print("= COMBO x {0}!!! =\n".format(combo-1))
        return score+1, combo
    elif correct == True and combo==32:
        print("YOU'RE CHEATING")
        combo+=1
        print("= COMBO x {0}!!! =\n".format(combo-1))
        return score+1, combo
    elif correct == True and combo==33:
        print("HAX")
        combo+=1
        print("= COMBO x {0}!!! =\n".format(combo-1))
        return score+1, combo
    elif correct == True and combo==34:
        print("VAC")
        combo+=1
        print("= COMBO x {0}!!! =\n".format(combo-1))
        return score+1, combo
    elif correct == True and combo==35:
        print("YOU'RE A WIZARD")
        combo+=1
        print("= COMBO x {0}!!! =\n".format(combo-1))
        return score+1, combo
    elif correct == True and combo==36:
        print("Oustanding.")
        combo+=1
        print("= COMBO x {0}!!! =\n".format(combo-1))
        return score+1, combo
    elif correct == True and combo==37:
        print("To the MOOOOOOON")
        combo+=1
        print("= COMBO x {0}!!! =\n".format(combo-1))
        return score+1, combo
    elif correct == True and combo==38:
        print("How is this possible?")
        combo+=1
        print("= COMBO x {0}!!! =\n".format(combo-1))
        return score+1, combo
    elif correct == True and combo==39:
        print("CAN YOU BE STOPPED?")
        combo+=1
        print("= COMBO x {0}!!! =\n".format(combo-1))
        return score+1, combo
    elif correct == True and combo==40:
        print("You show potential")
        combo+=1
        print("$ COMBO x {0}!!!! $\n".format(combo-1))
        return score+1, combo
    elif correct == True and combo==41:
        print("You are gifted.")
        combo+=1
        print("$ COMBO x {0}!!!! $\n".format(combo-1))
        return score+1, combo
    elif correct == True and combo==42:
        print("Teach me your ways.")
        combo+=1
        print("$ COMBO x {0}!!!! $\n".format(combo-1))
        return score+1, combo
    elif correct == True and combo==43:
        print("Unbelievable.")
        combo+=1
        print("$ COMBO x {0}!!!! $\n".format(combo-1))
        return score+1, combo
    elif correct == True and combo==44:
        print("Can you keep this up?")
        combo+=1
        print("$ COMBO x {0}!!!! $\n".format(combo-1))
        return score+1, combo
    elif correct == True and combo==45:
        print("Almost to 50x combo!")
        combo+=1
        print("$ COMBO x {0}!!!! $\n".format(combo-1))
        return score+1, combo
    elif correct == True and combo==46:
        print("Can you do it?")
        combo+=1
        print("$ COMBO x {0}!!!! $\n".format(combo-1))
        return score+1, combo
    elif correct == True and combo==47:
        print("Almost there!")
        combo+=1
        print("$ COMBO x {0}!!!! $\n".format(combo-1))
        return score+1, combo
    elif correct == True and combo==48:
        print("So close!")
        combo+=1
        print("$ COMBO x {0}!!!! $\n".format(combo-1))
        return score+1, combo
    elif correct == True and combo==49:
        print("One more combo!!")
        combo+=1
        print("$ COMBO x {0}!!!! $\n".format(combo-1))
        return score+1, combo
    elif correct == True and combo==50:
        print("CONGRATULATIONS.")
        combo+=1
        print("<< COMBO x [{0}] >>\n".format(combo-1))
        return score+1, combo
    elif correct == True and 60>=combo>=50:
        print("//IN THE ZONE//")
        combo+=1
        print("<< COMBO x [{0}] >>\n".format(combo-1))
        return score+1, combo
    elif correct == True and 70>=combo>60:
        print("You're about to transcend to where no mortal has gone before.")
        combo+=1
        print("<< | C O M B O | x [{0}] >>\n".format(combo-1))
        return score+1, combo
    elif correct == True and 77>combo>70:
        print("//DANGER//DANGER//DANGER//")
        combo+=1
        print("<< | C O M B O | x [{0}] >>\n".format(combo-1))
        return score+1, combo
    elif correct == True and combo==77:
        print("MAXMIMUM COMBO ACHIEVED. YOU HAVE SURPASSED YOUR STATUS AS A MORTAL.")
        combo+=1
        print(" <<< ( C O M B O ) x **{9999}** >>>\n")
        print("")
        return score+1, combo
    elif correct == False and 0<=combo<10:
        print("You got that wrong...")
        wrong(key)
        combo = 0
        print("* COMBO WAS RESET *\n")
        return score, combo
    elif correct == False and 10<=combo<20:
        print("Better luck next time...")
        wrong(key)
        combo = 0
        print("* COMBO WAS RESET *\n")
        return score, combo
    elif correct == False and 20<=combo<30:
        print("OH NO!")
        wrong(key)
        combo = 0
        print("* COMBO WAS RESET *\n")
        return score, combo
    elif correct == False and 30<=combo<40:
        print("GAH YOU HAD IT!")
        wrong(key)
        combo = 0
        print("* COMBO WAS RESET *\n")
        return score, combo
    elif correct == False and 40<=combo<50:
        print("YOU CAME ALL THIS WAY TO END UP LIKE THIS?")
        wrong(key)
        combo = 0
        print("* COMBO WAS RESET *\n")
        return score, combo
    elif correct == False and 50<=combo<60:
        print("Rage quit?")
        wrong(key)
        combo = 0
        print("* COMBO WAS RESET *\n")
        return score, combo
    elif correct == False and 60<=combo<70:
        print("I knew you couldn't do it.")
        wrong(key)
        combo = 0
        print("* COMBO WAS RESET *\n")
        return score, combo
    elif correct == False and combo==70:
        print("In the End - Linkin Park")
        wrong(key)
        combo = 0
        print("* COMBO WAS RESET *\n")
        return score, combo
    elif correct == False and combo==71:
        print("Not today.")
        wrong(key)
        combo = 0
        print("* COMBO WAS RESET *\n")
        return score, combo
    elif correct == False and combo==72:
        print(".....")
        wrong(key)
        combo = 0
        print("* COMBO WAS RESET *\n")
        return score, combo
    elif correct == False and combo==73:
        print("Hello? r u ok?")
        wrong(key)
        combo = 0
        print("* COMBO WAS RESET *\n")
        return score, combo
    elif correct == False and combo==74:
        print("THAT CHOKE....")
        wrong(key)
        combo = 0
        print("* COMBO WAS RESET *\n")
        return score, combo
    elif correct == False and combo==75:
        print("You will always be the second place silver medalist.")
        wrong(key)
        combo = 0
        print("* COMBO WAS RESET *\n")
        return score, combo
    elif correct == False and combo==76:
        print("Failure: When your best just isn't good enough.")
        wrong(key)
        combo = 0
        print("* COMBO WAS RESET *\n")
        return score, combo

def wrong(key):
    print(">>> Correct answer was: {0} <<<\n".format(answersheet(key)))

def rightwrong(answer, key):
    if answer in answersheet(key):
        return True
    else:
        return False

def sheet(key):
    question = {
        0: "Copy?",
        1: "Paste?",
        2: "Cut?",
        3: "Undo?",
        4: "Exit current window/program?",
        5: "Start menu?",
        6: "Switch between windows/programs?",
        7: "What can I hold on the keyboard for deleting text word by word with the Backspace key or the Del key?",
        8: "Delete file permanently without placing it in the Recycle Bin?",
        9: "Bold font?",
        10: "Underline font?",
        11: "Italicize font?",
        12: "Which function key displays Help?",
        13: "What can I hold on the keyboard to navigate through text word by word with the arrow keys?",
        14: "Task Manager?",
        15: "Open new tab?",
        16: "Close current tab/explorer window?",
        17: "Open previously closed tab?",
        18: "What can I hold on the keyboard for opening up the file properties window with the mouse or the Enter key?",
        19: "Open My Computer explorer window?",
        20: "What can I hold on the keyboard for selecting all files, texts, and tabs from where you click with the mouse?",
        21: "Zoom in?",
        22: "Zoom out?",
        23: "Select all?",
        24: "What can I hold on the keyboard for selecting specific files from where you click with the mouse?",
        25: "What can I hold on the keyboard for copy/pasting a file by drag/dropping with the mouse?",
        26: "Which function key refreshes a page?",
        27: "Find specific text?",
        28: "Which function key is the equivalent of the Find command?",
        29: "Which function key checks the spelling and grammar of a word document or a powerpoint?",
        30: "Which function key starts the presentation from the beginning in a powerpoint?",
        31: "Which function key makes the window into fullscreen?",
        32: "Which function key highlights the URL of the current browser window?",
        33: "Highlight the URL of the current browser window? (EXCLUDING the function keys)",
        34: "Cycle to the tab to the right of the current tab?",
        35: "Cycle to the tab to the left of the current tab?",
        36: "Open a new window?",
        37: "Open a new incognito window?",
        38: "Quit the browser entirely?",
        39: "Bookmark?",
        40: "What can I hold on the KEYBOARD for opening a link in a NEW TAB with the mouse?",
        41: "What can I click on the MOUSE for opening a link in a new tab?",
        42: "Browser history?",
        43: "Switch to the last tab?",
        44: "Switch to the first tab?",
        45: "Switch to the second tab?",
        46: "Switch to the third tab?",
        47: "Switch to the fourth tab?",
        48: "Switch to the fifth tab?",
        49: "Switch to the sixth tab?",
        50: "Switch to the seventh tab?",
        51: "Switch to the eighth tab?",
        52: "What can I hold on the keyboard for opening a link in a NEW WINDOW with the mouse?",
        53: "Copy/paste the current line of text into the next line without selecting?",
        54: "Minimize all windows and display the desktop?",
        55: "Browser downloads?",
        56: "Left alignment?",
        57: "Right alignment?",
        58: "Center alignment?",
        59: "Save?",
        60: "Print?",
        61: "Return everything on the page to normal zoom?",
        62: "Scroll down on a webpage?",
        63: "Go to the very bottom of a webpage?",
        64: "Go to the very top of a webpage?",
        65: "What can I hold on the keyboard for zooming in with the mouse wheel?",
        66: "What can I hold on the keyboard for zooming out with the mouse wheel?",
        67: "Refresh a webpage or window?",
        68: "Scroll up on a webpage?",
        69: "Move the text cursor to the end of the line of text?",
        70: "Move the text cursor to the beginning of the line of text?",
        71: "Maximize current window to fit the screen?",
        72: "Restore down/minimize current window size?",
        73: "Set the current window to fit the left half of the screen?",
        74: "Set the current window to fit the right half of the screen?",
        75: "Open the \'Run\' window?",
        76: "Redo?"
    }
    return question.get(key)

def answersheet(key):
    shortcut = {
        0: ['ctrl c'],
        1: ['ctrl v'],
        2: ['ctrl x'],
        3: ['ctrl z'],
        4: ['alt f4'],
        5: ['win', 'ctrl esc'],
        6: ['alt tab'],
        7: ['ctrl'],
        8: ['shift del'],
        9: ['ctrl b'],
        10: ['ctrl u'],
        11: ['ctrl i'],
        12: ['f1'],
        13: ['ctrl'],
        14: ['ctrl shift esc', 'shift ctrl esc'],
        15: ['ctrl t'],
        16: ['ctrl w'],
        17: ['ctrl shift t', 'shift ctrl t'],
        18: ['alt'],
        19: ['win e'],
        20: ['shift'],
        21: ['ctrl =', 'ctrl +'],
        22: ['ctrl -'],
        23: ['ctrl a'],
        24: ['ctrl'],
        25: ['ctrl'],
        26: ['f5'],
        27: ['ctrl f'],
        28: ['f3'],
        29: ['f7'],
        30: ['f5'],
        31: ['f11'],
        32: ['f6'],
        33: ['ctrl l', 'alt d'],
        34: ['ctrl tab'],
        35: ['ctrl shift tab', 'shift ctrl tab'],
        36: ['ctrl n'],
        37: ['ctrl shift n', 'shift ctrl n'],
        38: ['ctrl shift q', 'shift ctrl q'],
        39: ['ctrl d'],
        40: ['ctrl'],
        41: ['m3'],
        42: ['ctrl h'],
        43: ['ctrl 9'],
        44: ['ctrl 1'],
        45: ['ctrl 2'],
        46: ['ctrl 3'],
        47: ['ctrl 4'],
        48: ['ctrl 5'],
        49: ['ctrl 6'],
        50: ['ctrl 7'],
        51: ['ctrl 8'],
        52: ['shift'],
        53: ['ctrl d'],
        54: ['win d', 'win m'],
        55: ['ctrl j'],
        56: ['ctrl l'],
        57: ['ctrl r'],
        58: ['ctrl e'],
        59: ['ctrl s'],
        60: ['ctrl p'],
        61: ['ctrl 0'],
        62: ['space', 'pgdown', 'down'],
        63: ['end'],
        64: ['home'],
        65: ['ctrl'],
        66: ['ctrl'],
        67: ['ctrl r', 'f5'],
        68: ['shift space', 'pgup', 'up'],
        69: ['end'],
        70: ['home'],
        71: ['win up'],
        72: ['win down'],
        73: ['win left'],
        74: ['win right'],
        75: ['win r'],
        76: ['ctrl y']
    }
    return shortcut.get(key)

def results(score, quest, combo):
    try:
        percentage = score/quest*100
    except ZeroDivisionError:
        percentage = 0
    print("\nYou got {0} questions out of {1} questions right".format(score, quest))
    print("giving you a score of {0:.2f}%".format(percentage))
    
    if percentage == 100 and combo == 77:
        print("\nYOU'VE PROVEN YOURSELF WORTHY MORTAL. YOU HAVE BESTED THIS QUIZ AND BESTED ME.")
        print("Take a screenshot of this because you've earned this. CONGRATULATIONS!")
        print("\n\t<[Achievement Unlocked: THE REAL PERFECT SCORE]>")
    elif percentage == 100 and combo < 77:
        print("So you got a 100. BIG WHOOP. YOU ARE STILL A MERE MORTAL. You show potential, but this is not the real perfect score.")
        print("BE A MAN and CHALLENGE yourself to the IRONMAN MODE with ALL 77 QUESTIONS.")
        print("\n\t<[Achievement Unlocked: The Fake Perfect Score]>")
    elif 90<=percentage<100:
        print("\nPretty decent. NOT GOOD ENOUGH HOWEVER. FOOLISH MORTAL.")
        print("\n\t<[Achievement Unlocked: Mediocre]>")
    elif 80<=percentage<90:
        print("\nYOU HAVE A LONG WAYS TO GO MORTAL. KEEP TRYING.")
        print("\n\t<[Achievement Unlocked: The Average User]>")
    elif 70<=percentage<80:
        print("\nARE YOU KIDDING ME? MY GRANDMOTHER CAN DO BETTER.")
        print("\n\t<[Achievement Unlocked: Keep Trying, Kid]>")
    elif 60<=percentage<70:
        print("\nARE YOU EVEN TRYING? YOU DON'T KNOW SH!T.")
        print("\n\t<[Achievement Unlocked: Crash Test Dummy]>")
    elif 50<=percentage<60:
        print("\nYou are the reason the world population is half braindead.")
        print("\n\t<[Achievement Unlocked: Potato]>")
    elif 40<=percentage<50:
        print("\nHAVE YOU EVEN USED A COMPUTER BEFORE? A CAVEMAN HAS BETTER KNOWLEDGE THAN YOU.")
        print("\n\t<[Achievement Unlocked: Primitive Pleb]>")
    elif 30<=percentage<40:
        print("\nYou were probably dropped on the head when you were born.")
        print("\n\t<[Achievement Unlocked: Born This Way]>")
    elif 20<=percentage<30:
        print("\nImagine the world's dumbest person. Now imagine him with a concussion. You're dumber than that.")
        print("\n\t<[Achievement Unlocked: Despair]>")
    elif 10<=percentage<20:
        print("\nDon't talk to me ever again. I'll catch stupidity.")
        print("\n\t<[Achievement Unlocked: ._.]>")
    elif 0<percentage<10:
        print("\nThis score is so low, you obviously HAD to have been trolling. Well, congrats. You proved that your brain is as useful as your feces.")
        print("\n\t<[Achievement Unlocked: F*cking Troller Doge]>")
    elif percentage == 0:
        print("\nIf I was locked in a room with Bin Ladin, Hitler, and you, and had a gun with only 2 bullets, I'd shoot you twice.")
        print("\n\t<[Achievement Unlocked: The Ultimate Failure]>")
    print("\n**BONUS** COMBO ACHIEVEMENTS:")
    if 0<=combo<50:
        print("\n\t[None]")
    elif 50<=combo<60:
        print("\n\t<[Achievement Unlocked: 50x combo!]>")
    elif 60<=combo<70:
        print("\n\t<[Achievement Unlocked: 50x combo!]>")
        print("\n\t<[Achievement Unlocked: The Zone]>")
    elif combo == 70:
        print("\n\t<[Achievement Unlocked: 50x combo!]>")
        print("\n\t<[Achievement Unlocked: The Zone]>")
        print("\n\t<[SECRET Unlocked: MY MIDDLE SCHOOL JAM!]>")
    elif 70<=combo<77:
        print("\n\t<[Achievement Unlocked: 50x combo!]>")
        print("\n\t<[Achievement Unlocked: The Zone]>")
        print("\n\t<[Achievement Unlocked: The Dream is Still Just a Dream]>")
    elif combo == 77:
        print("\n\t<[Achievement Unlocked: 50x combo!]>")
        print("\n\t<[Achievement Unlocked: The Zone]>")
        print("\n\t<[Achievement Unlocked: Broken Boundaries]>")

    again = str(input("\n\nWanna go again (y/n)? "))
    if again == 'y':
        print()
        print()
        print()
        main()
    elif again == 'n':
        sys.exit(0)

main()
