import os

class Entry:
    def __init__(self, filename, isDir):
        self.Filename = filename
        self.IsDir = isDir
        self.Files = []


def CrawlDir(dir, entriesOut):
    for filename in os.listdir(dir): 
        p = os.path.join(dir, filename)
        if os.path.isfile(p):
            entry = Entry(filename, False)
            entriesOut.append(entry)
        else:
            entry = Entry(filename, True)
            CrawlDir(p, entry.Files)
            entriesOut.append(entry)

def PrintEntryTree(entry, indentCount=0, indentMap={}):
    if indentCount == 0:
        print(entry.Filename)
    fileCount = len(entry.Files)
    index = 1
    indentMap[indentCount] = True
    for e in entry.Files:
        notLast = index < fileCount
        if not notLast:
            indentMap[indentCount] = False
        indent = ""
        for i in range(indentCount):
            if indentMap[i]:
                indent += '│   '
            else:
                indent += '    '
        string = f"{indent}{'├' if notLast else '└'}{'───' if indentCount else ''}{e.Filename}"
        print(string)
        
        if e.IsDir:
            PrintEntryTree(e, indentCount + 1, indentMap)
        index += 1