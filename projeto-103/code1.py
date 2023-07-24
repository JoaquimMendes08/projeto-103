from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

import os
import shutil
import time 

pastaAtual = os.getcwd()



class FileHandler(FileSystemEventHandler):
    def on_created(self, event):
       print(f"Olá, {event.src_path} foi criado")

    def on_deleted(self, event):
        print(f"Alguém excluiu {event.src_path}")

    def on_modified(self, event):
        print(f"Olá, {event.src_path} foi modificado")  

fileHandler = FileHandler()
observer = Observer()

observer.schedule(fileHandler, pastaAtual, recursive = True)
observer.start()

while True:
    print("executando...")
    time.sleep(3)