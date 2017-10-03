s = "EBG KVVV vf n fvzcyr yrggre fhofgvghgvba pvcure gung ercynprf n yrggre jvgu gur yrggre KVVV yrggref nsgre vg va gur nycunorg. EBG KVVV vf na rknzcyr bs gur Pnrfne pvcure, qrirybcrq va napvrag Ebzr. Synt vf SYNTFjmtkOWFNZdjkkNH. Vafreg na haqrefpber vzzrqvngryl nsgre SYNT."
sl = list(s)

def change(c):
    if c == "S" or c == "s":
        return chr(ord(c) + (ord("f") - ord("s")))
    elif c == "F" or c == "f":
        return chr(ord(c) + (ord("s") - ord("f")))
    elif c == "N" or c == "n":
        return chr(ord(c) + (ord("a") - ord("n")))
    elif c == "A" or c == "a":
        return chr(ord(c) + (ord("n") - ord("a")))
    elif c == "T" or c == "t":
        return chr(ord(c) + (ord("g") - ord("t")))
    elif c == "G" or c == "g":
        return chr(ord(c) + (ord("t") - ord("g")))
    elif c == "R" or c == "r":
        return chr(ord(c) + (ord("e") - ord("r")))
    elif c == "E" or c == "e":
        return chr(ord(c) + (ord("r") - ord("e")))
    elif c == "C" or c == "c":
        return chr(ord(c) + (ord("p") - ord("c")))
    elif c == "P" or c == "p":
        return chr(ord(c) + (ord("c") - ord("p")))
    elif c == "O" or c == "o":
        return chr(ord(c) + (ord("b") - ord("o")))
    elif c == "B" or c == "b":
        return chr(ord(c) + (ord("o") - ord("b")))
    elif c == "U" or c == "u":
        return chr(ord(c) + (ord("h") - ord("u")))
    elif c == "H" or c == "h":
        return chr(ord(c) + (ord("u") - ord("h"))) 
    elif c == "Y" or c == "y":
        return chr(ord(c) + (ord("l") - ord("y")))
    elif c == "L" or c == "l":
        return chr(ord(c) + (ord("y") - ord("l"))) 
    elif c == "I" or c == "i":
        return chr(ord(c) + (ord("v") - ord("i")))         
    elif c == "V" or c == "v":
        return chr(ord(c) + (ord("i") - ord("v")))

    elif c == "J" or c == "j":
        return chr(ord(c) + (ord("w") - ord("j")))
    elif c == "Z" or c == "z":
        return chr(ord(c) + (ord("m") - ord("z")))
    elif c == "K" or c == "k":
        return chr(ord(c) + (ord("x") - ord("k")))
    elif c == "Q" or c == "q":
        return chr(ord(c) + (ord("d") - ord("q"))) 

    elif c == "W" or c == "w":
        return chr(ord(c) + (ord("j") - ord("w")))
    elif c == "M" or c == "m":
        return chr(ord(c) + (ord("z") - ord("m")))
    elif c == "X" or c == "x":
        return chr(ord(c) + (ord("k") - ord("x")))
    elif c == "D" or c == "d":
        return chr(ord(c) + (ord("q") - ord("d"))) 
        
    elif c == " " or c == "." or c == ",":
        return c
    else : return "*"
#    else : return c
print(''.join(map(change,sl)))
