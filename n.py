 logo():
	print("""%s
               ______      _    _ _____ __  __ 
              |  ____/\   | |  | |_   _|  \/  |
              | |__ /  \  | |__| | | | | \  / |
              |  __/ /\ \ |  __  | | | | |\/| |
              | | / ____ \| |  | |_| |_| |  | |
              |_|/_/    \_\_|  |_|_____|_|  |_|
"""%(O))

def reg():
    os.system('clear')
    logo()
    print ('')
    print ('                     Checking Approval')
    time.sleep(1) 
    try:
        to = open('/sdcard/Android/.bs7nt.txt', 'r').read()
    except (KeyError, IOError):
        reg2()
    r = requests.get('https://pastebin.com/AkKJ257v').text
    if to in r:
        time.sleep(2)
        bsn_menu()
    else:
        os.system('clear')
        logo()
        print('')
        print ('               \tApproved Not Detected')
        print ('')
        print("            \033[1;97mTHIS TOOL IS PAID YOU NEED TO GET APPROVED FIRST")
        print ('               \033[1;97mYOUR KEY : ' + to)
        print("               COPY AND SEND KEY TO ADMIN")
        name = input("               YOUR NAME : ")
        input('\033[1;97m               PRESS ENTER  TO SEND TOKEN')
        time.sleep(3.5)
        tks = 'Dear%20Admin,%20Please%20Approved%20My%20Key%20To%20Premium%20%20Thanks%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20My%20Name%20:%20'+name+'%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20
        reg()

def reg2():
    os.system('clear')
    logo()
    print('')
    print ('\tApproval Not Detected')
    print('')
    id = uuid.uuid4().hex[:50]
    print("            \033[1;97mTHIS TOOL IS PAID YOU NEED TO GET APPROVED FIRST")
    print ('               \033[1;97mYOUR KEY : ' + id)
    print("               COPY AND SEND KEY TO ADMIN")
    name = input("               YOUR NAME : ")
    input('\033[1;97m               PRESS ENTER  TO SEND TOKEN')
    time.sleep(3.5)
    tks = 'Dear%20Admin,%20Please%20Approved%20My%20Key%20To%20Premium%20%20Thanks%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20My%20Name%20:%20'+name+'%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20My%20%20Key%20%20:%20'+id
    sav.write(id)
    sav.close()
    reg()
