import sys
import os
import file_crawler as fc
import constants as c

def CrawlDirectory(dir=''):
    if dir == '':
        dir = os.getcwd()
    entryTree = fc.Entry(dir, True)
    entryTree.Filename = os.path.basename(dir)
    fc.CrawlDir(dir, entryTree.Files)
    fc.PrintEntryTree(entryTree)

argCount = len(sys.argv)
if (argCount < 2):
    CrawlDirectory()
    exit(0)

index = 1
for index in range(argCount):
    if (sys.argv[index] == '-h' or sys.argv[index] == "-help"):
        print(f"File Spider {c.VERSION}")
        print("\tCreated by MercuryDev\n")
        print("Description:")
        print("\tFile Spider generates a directory tree structure for a given directory and prints it\n")
        print(f"Usage: {sys.argv[0]} {'{flags}'}\n")
        print("Options:")
        for row in c.FLAGS:
            print("\t{: <20} - {: <}".format(*row))
        print()
        print("Examples:")
        print(f"\t{sys.argv[0]}")
        print(f"\t{sys.argv[0]} -h")
        print(f"\t{sys.argv[0]} -p C:/")
        exit(0)
    elif (sys.argv[index] == '-v' or sys.argv[index] == "--version"):
        print(f"FileSpider {c.VERSION}")
        exit(0)
    elif (sys.argv[index] == '-p' or sys.argv[index] == "--path"):
        if index + 1 < argCount:
            index += 1
            print(f"path: {sys.argv[index]}")
        else:
            print(f"Expected path: {sys.argv[0]} ... -p {'{dir_path}'}")
            exit(1)