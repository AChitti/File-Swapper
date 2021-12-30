import os
import shutil

source = input("enter source folder name:- ")
destination = input('enter destination folder name:- ')

#source = source + '/'
#destination = destination + '/'

#source="C:/Users/pchit/Desktop/Pieton/Project 98/folder1/file1.txt"
#destination="C:/Users/pchit/Desktop/Pieton/Project 98/folder2/file2.txt"





shutil.copyfile(source, destination)
    