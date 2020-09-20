from Functions import *

while True:
    print("What files would you like to sort? Type Stop to exit.")
    print("Images, Documents, Speadsheets, Installers, Music, Videos, All")
    type = input().lower()
    if type == "stop":
        break
    print("What directory would you like to sort from?")
    startDir = input()
    print("What directory would you like to move sorted files to?")
    newDir = input()
    if type == "images":
        sortFiles.sortImages("", startDir, newDir)
    elif type == "documents":
        sortFiles.sortDocuments("", startDir, newDir)
    elif type == "spreadsheets":
        sortFiles.sortSpreadsheets("", startDir, newDir)
    elif type == "installers":
        sortFiles.sortInstallers("", startDir, newDir)
    elif type == "music":
        sortFiles.sortMusic("", startDir, newDir)
    elif type == "videos":
        sortFiles.sortVideos("", startDir, newDir)
    elif type == "all":
        sortFiles.sortImages("", startDir, newDir)
        sortFiles.sortDocuments("", startDir, newDir)
        sortFiles.sortInstallers("", startDir, newDir)
        sortFiles.sortMusic("", startDir, newDir)
        sortFiles.sortVideos("", startDir, newDir)
    else:
        print("Invalid input")


