import os
import sys
import threading
tqdm_enabled = False
try:
    from tqdm import tqdm
    tqdm_enabled = True
except ImportError:
    pass


def main():
    try:
        search_at = sys.argv[1]
        filename = sys.argv[2]
        if not tqdm_enabled:
            for root, dir, file in os.walk(search_at):
                for each in file:
                    if filename in each:
                        print("Filename: %s" % (root + "/" + each))
        if tqdm_enabled:
            for root, dir, file in tqdm(os.walk(search_at)):
                for each in file:
                    if filename in each:
                        print("Filename: %s" % (root + "/" + each))
    except:
        search_at = input("Start search at:")
        filename = input("Filename: ")
        if not tqdm_enabled:
            for root, dir, file in os.walk(search_at):
                for each in file:
                    if filename in each:
                        print("Filename: %s" % (root + "/" + each))
        if tqdm_enabled:
            for root, dir, file in tqdm(os.walk(search_at)):
                for each in file:
                    if filename in each:
                        print("Filename: %s" % (root + "/" + each))


main_thread = threading.Thread(target=main)
main_thread.start()

