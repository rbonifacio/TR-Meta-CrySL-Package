import os
import re

config = raw_input('Configuration: ') 
path   = raw_input('Input directory: ')

regex1 = "Findings in Java Class: ([\w\.]+)"
regex2 = "ConstraintError violating CrySL rule for ([\w\.]+)"
regex3 = "First parameter \(with value \"([-\w\/\.]+)\"\) should be any of (([\w\/]+)?{[-\w\.,\ \/\t]+})"
regex4 = "([\w]+ parameter) \(with value ([a-zA-Z0-9]+)\)(.*)"

if(os.path.isdir(path)):
    out    = open(config + ".csv", "w")
    total = 0
    m1 = ""
    for f in os.listdir(path):
        if f.endswith(".apk-out.txt"):
           aFile = open(path + "/" + f, 'r')
           lines = aFile.readlines()
           for i in range(len(lines)):
               s0 = lines[i].lstrip()
               if(s0.startswith("Findings in Java Class:")):
                   m1 = re.search(regex1, s0)
                   i += 1
               s1 = lines[i].lstrip()
               if(s1.startswith("ConstraintError violating")):
                   total += 1
                   m2 = re.search(regex2, s1)
                   if m2:
                       i += 1
                       s2 = lines[i].lstrip() 
                       m3 = re.search(regex3, s2)
                       m4 = re.search(regex4, s2) 
                       if m3:
                           out.write(config + ";" + os.path.basename(aFile.name)[:-12] + ";" + m1.group(1) + ";" + m2.group(1) + ";" + m3.group(1) + ";" +  m3.group(2) + ";" + s2)
                           out.write("\n")
                       elif m4:
                           out.write(config + ";" + os.path.basename(aFile.name)[:-12] + ";" + m1.group(1) + ";" + m2.group(1) + ";" + m4.group(1) + ";" +  m4.group(2) + ";" + s2)
                           out.write("\n")
                       else:
                           print(s2)
                   else:
                       print(s1)                            
            
    print(total)
    out.close()          
else:
    raise Exception(path + " is not a directory")
