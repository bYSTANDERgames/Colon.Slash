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

else:
    print("line1.Command Not Recognised")

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

line2argsforline3 = ["::/file/write/name/line1/content/line3", "::/file/write/name/line1/content/line4", "::/file/write/name/line2/content/line3", "::/file/write/name/line2/content/line4", "::/file/write/name/line3/content/line2", "::/file/write/name/line4/content/line2", "::/file/write/name/line1/content/line2", "::/file/write/name/line2/content/line1", "::/file/read/name/line3",]
line2argsforline4 = ["::/file/write/name/line1/content/line3", "::/file/write/name/line1/content/line4", "::/file/write/name/line2/content/line3", "::/file/write/name/line2/content/line4", "::/file/write/name/line3/content/line2", "::/file/write/name/line4/content/line2", "::/file/write/name/line1/content/line2", "::/file/write/name/line2/content/line1", "::/file/read/name/line4"]
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