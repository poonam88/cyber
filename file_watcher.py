import time
import os

def tail_file(file_path, last_position=0):
    with open(file_path, "r") as f:
        f.seek(last_position)
        new_lines = f.readlines()
        new_position = f.tell()
    return new_lines, new_position
