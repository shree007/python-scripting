from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import os
import time

class FileWatcher(FileSystemEventHandler):
    def __init__(self, filename):
        self.filename = os.path.abspath(filename)
    def on_created(self, event):
        if event.src_path == self.filename:
            print(f"Created: {self.filename}")

    def on_modified(self, event):
        if event.src_path == self.filename:
            print(f"Modified: {self.filename}")
    
    def on_deleted(self, event):
        if event.src_path == self.filename:
            print(f"Deleted: {self.filename}")

    def on_moved(self, event):
        if event.src_path == self.filename:
            print(f"Renamed/Moved: {event.src_path} → {event.dest_path}")

if __name__ == "__main__":
    file_to_watch = os.path.abspath("watch-test.txt")
    directory_to_watch = os.path.dirname(file_to_watch)

    event_handler = FileWatcher(file_to_watch)
    observer = Observer()
    observer.schedule(event_handler, directory_to_watch, recursive=False)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
