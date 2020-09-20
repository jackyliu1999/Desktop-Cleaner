import os
import sys
import shutil

class sortFiles():
    def sortImages(self, path, moveDirectory):
        listDir = []  # List for
        for file in os.listdir(path):
            listDir.append(file)
        for item in listDir:
            if item.endswith(".png") or item.endswith(".jpg") or item.endswith(".jpeg") or item.endswith(".gif"):
                newpath = moveDirectory + "/images"
                if not os.path.exists(newpath):
                    os.makedirs(newpath)
                itemPath = path + "/" + item
                shutil.move(itemPath, newpath)

    def sortDocuments(self, path, moveDirectory):
        listDir = []  # List for
        for file in os.listdir(path):
            listDir.append(file)
        for item in listDir:
            if item.endswith(".docx") or item.endswith(".txt") or item.endswith(".rtf") or item.endswith(".pdf"):
                newpath = moveDirectory + "/Documents"
                if not os.path.exists(newpath):
                    os.makedirs(newpath)
                itemPath = path + "/" + item
                shutil.move(itemPath, newpath)

    def sortSpreadsheets(self, path, moveDirectory):
        listDir = []  # List for
        for file in os.listdir(path):
            listDir.append(file)
        for item in listDir:
            if item.endswith(".xlsx") or item.endswith(".csv"):
                newpath = moveDirectory + "/Spreadsheets"
                if not os.path.exists(newpath):
                    os.makedirs(newpath)
                itemPath = path + "/" + item
                shutil.move(itemPath, newpath)

    def sortInstallers(self, path, moveDirectory):
        listDir = []  # List for
        for file in os.listdir(path):
            listDir.append(file)
        for item in listDir:
            if item.endswith(".exe"):
                newpath = moveDirectory + "/Installers"
                if not os.path.exists(newpath):
                    os.makedirs(newpath)
                itemPath = path + "/" + item
                shutil.move(itemPath, newpath)

    def sortMusic(self, path, moveDirectory):
        listDir = []  # List for
        for file in os.listdir(path):
            listDir.append(file)
        for item in listDir:
            if item.endswith(".mp3") or item.endswith(".wav"):
                newpath = moveDirectory + "/Music"
                if not os.path.exists(newpath):
                    os.makedirs(newpath)
                itemPath = path + "/" + item
                shutil.move(itemPath, newpath)

    def sortVideos(self, path, moveDirectory):
        listDir = []  # List for
        for file in os.listdir(path):
            listDir.append(file)
        for item in listDir:
            if item.endswith(".avi") or item.endswith(".flv") or item.endswith(".mp4") or item.endswith(".wmv") or item.endswith(".mpg"):
                newpath = moveDirectory + "/Videos"
                if not os.path.exists(newpath):
                    os.makedirs(newpath)
                itemPath = path + "/" + item
                shutil.move(itemPath, newpath)