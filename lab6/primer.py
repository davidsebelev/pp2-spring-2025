import os 
from datetime import datetime#added to use frotimestamp 
#module allows to interact with file system

#print(os.getcwd()) #get_current_working_directory
#os.mkdir("boba")#making directory
#os.rmdir("boba")#deleting directory 
#os.chdir("lab6")#chosing directory that we need 
#os.rename("text.txt","bibo.txt")#renaming file to another that we want to
#print(os.stat("labwork.py"))#showing all stat of file 
#if we want to take some direct stat we need to write something like this os.stat("name_of_file".st_size)
#i picked stat size but you can choose everything
#to make stat for human do this
#mod_time = os.stat("labwork.py").st_mtime
#print(datetime.fromtimestamp(mod_time))
#in the 14 and 15 strings you can see how make in people language your dates
#print(os.listdir())

os.chdir("/Users/david/Desktop/")
#going through all files directories ant path
#for dirpath , dirnames , filenames in os.walk("/Users/david/Desktop/"):
    #print("Current Path:", dirpath)
    #print("Directiries:", dirnames)
    #print("Files:", filenames)
print(os.environ.get("HOME"))#getting home dirrectory
#all enviroment variables
print(os.path.basename("tmp/tes.txt"))#printing basename in path
print(os.path.dirname("tmp/text.name"))#printing dirname from path
print(os.path.split("tmp/text.txt"))#printing all splited
print(os.path.exists("tmp/text.txt"))#checking exist or not?
print(os.path.isdir("tmp/text.txt"))#dir or not?
print(os.path.isfile("temp/text.txt"))#file or nah?
