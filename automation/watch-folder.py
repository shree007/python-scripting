
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time

class FolderWatcher(FileSystemEventHandler):
    def on_modified(self, event):
        if not event.is_directory:
            print(f"📝 Modified: {event.src_path}")

    def on_created(self, event):
        if not event.is_directory:
            print(f"✅ Created: {event.src_path}")

    def on_deleted(self, event):
        if not event.is_directory:
            print(f"❌ Deleted: {event.src_path}")


if __name__ == '__main__':
    folder_to_watch = "."
    event_handler = FolderWatcher()
    observer = Observer()
    observer.schedule(event_handler, folder_to_watch, recursive=True)

    observer.start()
    print(f"👀 Watching folder: {folder_to_watch}")

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()