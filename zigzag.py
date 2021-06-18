import time , sys
indent = 10 # how many spaces to indent
indentIncreasing = True #Whether the indentation is increasing or not.
try:
    while True:
        print(' ' * indent, end='')
        print('llllllll')
        time.sleep(.002)
        if indentIncreasing:
            indent += 1
            if indent == 50:
                indentIncreasing = False
        else:
            indent -= 1
            # decrease the number of spaces
            if indent == 0:
                #change direction
                indentIncreasing = True
except KeyboardInterrupt :
    sys.exit()

