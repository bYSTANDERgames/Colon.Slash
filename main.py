import time
extensions = [":/extension_web_browser"]

print("""
   ___       _               __  _           _     
  / __\ ___ | | ___  _ __   / _\| | __ _ ___| |__  
 / /   / _ \| |/ _ \| '_ \  \ \ | |/ _` / __| '_ \ 
/ /___| (_) | | (_) | | | |__\ \| | (_| \__ \ | | |
\____/ \___/|_|\___/|_| |_(_)__/|_|\__,_|___/_| |_|

                                                   """) 

line1 = input(">> ")
line2 = input(">> ")
line3 = input(">> ")
line4 = input(">> ")

#line1 commands
if line1 == ":/":
    print("line1:Started File!")
elif line1 == "::/":
    print("line1:File Stopped!")
    exit()
elif line1 == "help":
    print("https://github.com/bYSTANDERgames/Colon.Slash/blob/main/README.md")

#line1 error checking
elif line1 == "::/file/write":
    print("line1.error(file has not started yet!)")
elif line1 == "::/file/write/name/line1/content/line3":
    print("line1.error(file has not started yet!)")
elif line1 == "::/file/write/name/line1/content/line4":
    print("line1.error(file has not started yet!)")
elif line1 == "::/file/write/name/line2/content/line3":
    print("line1.error(file has not started yet!)")
elif line1 == "::/file/write/name/line2/content/line4":
    print("line1.error(file has not started yet!)")
elif line1 == "::/file/write/name/line3/content/line2":
    print("line1.error(file has not started yet!)")
elif line1 == "::/file/write/name/line4/content/line2":
    print("line1.error(file has not started yet!)")
elif line1 == "::/file/write/name/line1/content/line2":
   print("line1.error(file has not started yet!)")
elif line1 == "::/file/write/name/line2/content/line1":
   print("line1.error(file has not started yet!)")

#line2 commands
if line2 == "::/":
    print("line1.File Stopped!")
    exit()

elif line2 == "::/file/read/name/line3":
    f = open(line3, "r")
    print(f.read())
elif line2 == "::/file/read/name/line4":
    f = open(line4, "r")
    print(f.read())

#error checking read
elif line2 == "::/file/read/name/line1":
    print("line2.error(cannot read file with name of start)")
elif line2 == "::/file/read/name/line2":
    print("line2.error(cannot read file with name of line2)")

elif line2 == "::/file/write/runtime":
    name = input("line2:Input File Name : ")
    content = input("line2:Input File Content : ")
    print("Made File")
    f = open(name, "w")
    f.write(content)
    f.close()
elif line2 == "::/file/write/name/line3/content/line4":
    print("Made File")
    f = open(line3, "w")
    f.write(line4)
    f.close()
elif line2 == "::/file/write/content/line3/name/line4":
    print("Made File")
    f = open(line4, "w")
    f.write(line3)
    f.close()
elif line2 == "::/file/write/name/line4/content/line3":
    print("Made File")
    f = open(line4, "w")
    f.write(line3)
    f.close()

line2argsforline3 = ["::/file/write/name/line1/content/line3", "::/file/write/name/line1/content/line4", "::/file/write/name/line2/content/line3", "::/file/write/name/line2/content/line4", "::/file/write/name/line3/content/line2", "::/file/write/name/line4/content/line2", "::/file/write/name/line1/content/line2", "::/file/write/name/line2/content/line1", "::/file/read/name/line3", "::/create/variable/name/line4/value/line3", "::/create/variable/name/line3/value/line4"]
line2argsforline4 = ["::/file/write/name/line1/content/line3", "::/file/write/name/line1/content/line4", "::/file/write/name/line2/content/line3", "::/file/write/name/line2/content/line4", "::/file/write/name/line3/content/line2", "::/file/write/name/line4/content/line2", "::/file/write/name/line1/content/line2", "::/file/write/name/line2/content/line1", "::/file/read/name/line4", "::/create/variable/name/line4/value/line3", "::/create/variable/name/line3/value/line4"]
line2args = ["::/file/write/runtime", "::/file/write/content/line3/name/line4"]

#error checking line2
if line2 == "::/file/write/name/line1/content/line3":
    print("line2.error(cannot name file to start!)")
elif line2 == "::/file/write/name/line1/content/line4":
    print("line2.error(cannot name file to start!)")
elif line2 == "::/file/write/name/line2/content/line3":
    print("line2.error(cannot name file to line2!)")
elif line2 == "::/file/write/name/line2/content/line4":
    print("line2.error(cannot name file to line2)")
elif line2 == "::/file/write/name/line3/content/line2":
    print("line2.error(cannot make content of file to line2)")
elif line2 == "::/file/write/name/line4/content/line2":
    print("line2.error(cannot make content of file to line2)")
elif line2 == "::/file/write/name/line1/content/line2":
    print("line2.error(cannot make content of file to line2)")
    print("line2.error(cannot name file to start!)")
elif line2 == "::/file/write/name/line2/content/line1":
    print("line2.error(cannot make content of file to start!)")
    print("line2.error(cannot name file to line2!)")
elif line2 == " ":
    print("line2.did_not_execute")

#line2 deleting files
elif line2 == "::/file/delete":
    import os
    file_path = input("File Path : ")
    if os.path.isfile(file_path):
        os.remove(file_path)
    print(f"{file_path} has been deleted")
    if file_path == " ":
        print("nothing to delete")

#line2 adding variable and then adding to file
elif line2 == "::/create/variable/name/line3/value/line4":
    print("Made File")
    line4_w = (f"{line3} = {line4}")
    f = open(line3, "w")
    f.write(line4_w)
    f.close()

elif line2 == "::/create/variable/name/line4/value/line3":
    print("Made File")
    line3_w = (f"{line4} = {line3}")
    f = open(line4, "w")
    f.write(line3_w)
    f.close()

#line2 adding variable error checking
elif line2 == "::/create/variable/name/line1/value/line3":
    print("line2.error(cannot make variable with name line1)")
elif line2 == "::/create/variable/name/line1/value/line4":
    print("line2.error(cannot make variable with name line1)")
elif line2 == "::/create/variable/name/line1/value/line2":
    print("line2.error(cannot make variable with name line1)")
    print("line2.error(cannot make variable value with value line2)")
elif line2 == "::/create/variable/name/line1/value/line1":
    print("line2.error(cannot make variable with name line1)")

elif line2 == "::/create/variable/name/line3/value/line1":
    print("line2.error(cannot make variable value with value line1)")
elif line2 == "::/create/variable/name/line4/value/line1":
    print("line2.error(cannot make variable value with value line1)")
elif line2 == "::/create/variable/name/line2/value/line1":
    print("line2.error(cannot make variable value with value line1)")
    print("line2.error(cannot make variable with name line2)")

elif line2 == "::/create/variable/name/line2/value/line3":
    print("line2.error(cannot make variable with name line2)")
elif line2 == "::/create/variable/name/line2/value/line4":
    print("line2.error(cannot make variable with name line2)")
elif line2 == "::/create/variable/name/line2/value/line2":
    print("line2.error(cannot make variable with name line2)")
    print("line2.error(cannot make variable value with value line2)")

#global adding variable error checking
elif line2 == "::/create/variable/name/line3/value/line4" and line3 == " ":
    print("line2.error(nothing in line3!)")
elif line2 == "::/create/variable/name/line3/value/line4" and line4 == " ":
    print("line2.error(nothing in line4!)")
elif line2 == "::/create/variable/name/line4/value/line3" and line3 == " ":
    print("line2.error(nothing in line3!)")
elif line2 == "::/create/variable/name/line4/value/line3" and line4 == " ":
    print("line2.error(nothing in line4!)")

#line2 arithmatic 
elif line2 == "::/arithmetic/+":
    number1 = input(int("Number 1 : "))
    number2 = input(int("Number 2 : "))
    print(number1+number2)
elif line2 == "::/arithmetic/-":
    number1 = input(int("Number 1 : "))
    number2 = input(int("Number 2 : "))
    print(number1-number2)
elif line2 == "::/arithmetic//":
    number1 = input(int("Number 1 : "))
    number2 = input(int("Number 2 : "))
    print(number1/number2)
elif line2 == "::/arithmetic/*":
    number1 = input(int("Number 1 : "))
    number2 = input(int("Number 2 : "))
    print(number1*number2)
elif line2 == "::/arithmetic/%":
    number1 = input(int("Number 1 : "))
    number2 = input(int("Number 2 : "))
    print(number1%number2)
elif line2 == "::/arithmetic/**":
    number1 = input(int("Number 1 : "))
    number2 = input(int("Number 2 : "))
    print(number1**number2)
elif line2 == "::/arithmetic///":
    number1 = input(int("Number 1 : "))
    number2 = input(int("Number 2 : "))
    print(number1//number2)

elif line2 == "::/arithmetic/+/number1/line3/number2/line4":
    print(int(line3) + int(line4))
elif line2 == "::/arithmetic/-/number1/line3/number2/line4":
    print(int(line3) - int(line4))
elif line2 == "::/arithmetic///number1/line3/number2/line4":
    print(int(line3) / int(line4))
elif line2 == "::/arithmetic/*/number1/line3/number2/line4":
    print(int(line3) * int(line4))
elif line2 == "::/arithmetic/%/number1/line3/number2/line4":
    print(int(line3) % int(line4))
elif line2 == "::/arithmetic/**/number1/line3/number2/line4":
    print(int(line3) ** int(line4))
elif line2 == "::/arithmetic////number1/line3/number2/line4":
    print(int(line3) // int(line4))

elif line2 == "::/arithmetic/+/number1/line4/number2/line3":
    print(int(line3) + int(line4))
elif line2 == "::/arithmetic/-/number1/line4/number2/line3":
    print(int(line3) - int(line4))
elif line2 == "::/arithmetic///number1/line4/number2/line3":
    print(int(line3) / int(line4))
elif line2 == "::/arithmetic/*/number1/line4/number2/line3":
    print(int(line3) * int(line4))
elif line2 == "::/arithmetic/%/number1/line4/number2/line3":
    print(int(line3) % int(line4))
elif line2 == "::/arithmetic/**/number1/line4/number2/line3":
    print(int(line3) ** int(line4))
elif line2 == "::/arithmetic////number1/line4/number2/line3":
    print(int(line3) // int(line4))

elif line2 == "::/arithmetic/+/number1/line3/number2/line4" and line3 == " ":
    print("line2.error(nothing in line3!)")
elif line2 == "::/arithmetic/+/number1/line3/number2/line4" and line4 == " ":
    print("line2.error(nothing in line4!)")

elif line2 == "::/arithmetic/-/number1/line3/number2/line4" and line3 == " ":
    print("line2.error(nothing in line3!)")
elif line2 == "::/arithmetic/-/number1/line3/number2/line4" and line4 == " ":
    print("line2.error(nothing in line4!)")

elif line2 == "::/arithmetic///number1/line3/number2/line4" and line3 == " ":
    print("line2.error(nothing in line3!)")
elif line2 == "::/arithmetic///number1/line3/number2/line4" and line4 == " ":
    print("line2.error(nothing in line4!)")

elif line2 == "::/arithmetic/*/number1/line3/number2/line4" and line3 == " ":
    print("line2.error(nothing in line3!)")
elif line2 == "::/arithmetic/*/number1/line3/number2/line4" and line4 == " ":
    print("line2.error(nothing in line4!)")

elif line2 == "::/arithmetic/%/number1/line3/number2/line4" and line3 == " ":
    print("line2.error(nothing in line3!)")
elif line2 == "::/arithmetic/%/number1/line3/number2/line4" and line4 == " ":
    print("line2.error(nothing in line4!)")

elif line2 == "::/arithmetic/**/number1/line3/number2/line4" and line3 == " ":
    print("line2.error(nothing in line3!)")
elif line2 == "::/arithmetic/**/number1/line3/number2/line4" and line4 == " ":
    print("line2.error(nothing in line4!)")

elif line2 == "::/arithmetic////number1/line3/number2/line4" and line3 == " ":
    print("line2.error(nothing in line3!)")
elif line2 == "::/arithmetic////number1/line3/number2/line4" and line4 == " ":
    print("line2.error(nothing in line4!)")

#line2 get input on runtime
elif line2 == "::/create/input":
    input1_r = input(">> ")

inputline2 = ["::/create/input/str", "::/create/input/int", "::/create/input"]
input1_r = ""

#web_browser extension
if line2 == "::/extension/webbrowser/open/content/line3" and line1 == ":/extension_web_browser":
    import webbrowser
    webbrowser.open(line3)
if line2 == "::/extension/webbrowser/open/content/line4" and line1 == ":/extension_web_browser":
    import webbrowser
    webbrowser.open(line4)

#checking error
if line2 == "::/extension/webbrowser/open/content/line1" and line1 == ":/extension_web_browser":
    print("line2.error(cant open url line1)")
if line2 == "::/extension/webbrowser/open/content/line2" and line1 == ":/extension_web_browser":
    print("line2.error(cant open url line2)")

if line2 == "::/extension/webbrowser/open/content/line3" and line1 != ":/extension_web_browser":
    print("line2.error(import web_browser extension)")
if line2 == "::/extension/webbrowser/open/content/line4" and line1 != ":/extension_web_browser":
    print("line2.error(import web_browser extension)")

#check_spec extension
if line2 == "::/extension/check_spec" and line1 == ":/extension_check_spec":
    import platform,socket,re,uuid,json,logging

    def getSystemInfo():
        try:
            info={}
            info['platform']=platform.system()
            info['platform-release']=platform.release()
            info['platform-version']=platform.version()
            info['architecture']=platform.machine()
            info['hostname']=socket.gethostname()
            info['ip-address']=socket.gethostbyname(socket.gethostname())
            info['mac-address']=':'.join(re.findall('..', '%012x' % uuid.getnode()))
            info['processor']=platform.processor()
            return json.dumps(info)
        except Exception as e:
            logging.exception(e)

json.loads(getSystemInfo())

#line3 commands
if line3 not in line2argsforline3 and line3 == "::/file/read/name/line4":
    f = open(line4, "r")
    print(f.read())
if line3 not in line2argsforline3 and line3 == "::/file/read/name/line2":
    f = open(line2, "r")
    print(f.read())
    
#error checking read
if line3 not in line2argsforline3 and line3 == "::/file/read/name/line1":
    print("line3.error(cannot read file with name of start!)")
elif line3 not in line2argsforline3 and line3 == "::/file/read/name/line3":
    print("line3.error(cannot read file with name of line3!)")
elif line3 == "::/":
    print("line3:File Stopped!")
    exit()

#file/write errors
elif line3 not in line2argsforline3 and line3 == "::/file/write/runtime":
    print("line3.error(you can only execute this command on line2!)")

elif line3 not in line2argsforline3 and line3 == "::/file/write/name/line1/content/line3":
    print("line3.error(you can only execute this command on line2!)")
elif line3 not in line2argsforline3 and line3 == "::/file/write/name/line1/content/line4":
    print("line3.error(you can only execute this command on line2!)")
elif line3 not in line2argsforline3 and line3 == "::/file/write/name/line2/content/line3":
    print("line3.error(you can only execute this command on line2!)")
elif line3 not in line2argsforline3 and line3 == "::/file/write/name/line2/content/line4":
    print("line3.error(you can only execute this command on line2!)")
elif line3 not in line2argsforline3 and line3 == "::/file/write/name/line3/content/line2":
    print("line3.error(you can only execute this command on line2!)")
elif line3 not in line2argsforline3 and line3 == "::/file/write/name/line4/content/line2":
    print("line3.error(you can only execute this command on line2!)")
elif line3 not in line2argsforline3 and line3 == "::/file/write/name/line1/content/line2":
    print("line3.error(you can only execute this command on line2!)")
elif line3 == "::/file/write/name/line2/content/line1":
    print("line3.error(you can only execute this command on line2!)")
elif line3 == " ":
    print("line3.did_not_execute")
elif line3 == "::/file/delete":
    print("line3.error(you can only execute this command on line2!)")

#line3 if commands on input
elif line3 == "::/if/input/content/line4/then/alert" and line2 in inputline2:
    if input1_r == line4:
        print("Alert!")
elif line3 == "::/if/input/content/line4/then/wow" and line2 in inputline2:
    if input1_r == line4:
        print("Wow!")
elif line3 == "::/if/input/content/line4/then/calm" and line2 in inputline2:
    if input1_r == line4:
        print("~Calm~")
elif line3 == "::/if/input/content/line4/then/datetimenowanddatetime" and line2 in inputline2:
    from datetime import datetime

    # datetime object containing current date and time
    now = datetime.now()
    
    print("now =", now)

    # dd/mm/YY H:M:S
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    print("date and time =", dt_string)

elif line3 == "::/if/input/content/line4/then/datetimenow" and line2 in inputline2:
    from datetime import datetime

    # datetime object containing current date and time
    now = datetime.now()
    
    print("now =", now)

if line3 == "::/if/input/content/line4/then/datetime" and line2 in inputline2:
    from datetime import datetime

    # dd/mm/YY H:M:S
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    print("date and time =", dt_string)

elif line3 == "::/if/input/content/line4/then/print/line5" and line2 in inputline2:
    if input1_r == line4:
        print("line3.error(cannot print)")

#line4 commands
if line4 not in line2argsforline4 and line4 == "::/file/read/name/line3":
    f = open(line4, "r")
    print(f.read())
if line4 not in line2argsforline4 and line4 == "::/file/read/name/line2":
    f = open(line2, "r")
    print(f.read())
    
#error checking read
if line4 not in line2argsforline4 and line4 == "::/file/read/name/line1":
    print("line4.error(cannot read file with name of start!)")
elif line4 not in line2argsforline4 and line4 == "::/file/read/name/line4":
    print("line4.error(cannot read file with name of line4!)")
elif line4 == "::/":
    print("line4:File Stopped!")
    exit()

#file/write errors
elif line4 not in line2argsforline4 and line4 == "::/file/write/runtime":
    print("line4.error(you can only execute this command on line2!)")

elif line4 not in line2argsforline4 and line4 == "::/file/write/name/line1/content/line3":
    print("line4.error(you can only execute this command on line2!)")
elif line4 not in line2argsforline4 and line4 == "::/file/write/name/line1/content/line4":
    print("line4.error(you can only execute this command on line2!)")
elif line4 not in line2argsforline4 and line4 == "::/file/write/name/line2/content/line3":
    print("line4.error(you can only execute this command on line2!)")
elif line4 not in line2argsforline4 and line4 == "::/file/write/name/line2/content/line4":
    print("line4.error(you can only execute this command on line2!)")
elif line4 not in line2argsforline4 and line4 == "::/file/write/name/line3/content/line2":
    print("line4.error(you can only execute this command on line2!)")
elif line4 not in line2argsforline4 and line4 == "::/file/write/name/line4/content/line2":
    print("line4.error(you can only execute this command on line2!)")
elif line4 not in line2argsforline4 and line4 == "::/file/write/name/line1/content/line2":
    print("line4.error(you can only execute this command on line2!)")
elif line4 == "::/file/write/name/line2/content/line1":
    print("line4.error(you can only execute this command on line2!)")
elif line4 == " ":
    print("line4.did_not_execute")
elif line4 == "::/file/delete":
    print("line4.error(you can only execute this command on line2!)")

