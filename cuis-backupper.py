import subprocess
import time
import os
import datetime

def take_input():
    CUIS_PATH = raw_input("Enter cuis directory (default: .): ") or "./"
    SAVING_INTERVAL_IN_SECONDS = int(raw_input("Enter interval in seconds to backup (default: 60): ") or 60)
    OUTPUT_DIR_BASE_PATH = raw_input("Enter output directory (default: /tmp): ") or "/tmp"
    return CUIS_PATH, SAVING_INTERVAL_IN_SECONDS, OUTPUT_DIR_BASE_PATH

def generate_zip(cuis_path, output_dir, file_name):
    cmd = "ls -- {}/CuisUniversity* | zip \"{}/{}\" -@ > /dev/null".format(cuis_path, output_dir, file_name)
    subprocess.call(cmd, shell=True)

def create_folder_if_does_not_exist(directory, folder_name):
    absolute_path_to_output = directory + "/" + folder_name
    if os.path.isdir(absolute_path_to_output):
        print("Folder exists. (path: {})".format(absolute_path_to_output))
    else:
        print("Creating folder at path: {}".format(absolute_path_to_output))
        os.mkdir(absolute_path_to_output)

def log_args():
    print("----------ARGS----------")
    print("CUIS_PATH: {}".format(CUIS_PATH))
    print("OUTPUT_DIR_PATH: {}".format(OUTPUT_DIR_BASE_PATH))
    print("SAVING_INTERVAL: {} secs.".format(SAVING_INTERVAL_IN_SECONDS))
    print("------------------------")


CUIS_PATH, SAVING_INTERVAL_IN_SECONDS, OUTPUT_DIR_BASE_PATH = take_input()
log_args()

OUTPUT_FOLDER_NAME = "backup-cuis-" + datetime.datetime.now().strftime('%Y-%m-%d')
create_folder_if_does_not_exist(OUTPUT_DIR_BASE_PATH, OUTPUT_FOLDER_NAME)
OUTPUT_DIR_PATH = OUTPUT_DIR_BASE_PATH + "/" + OUTPUT_FOLDER_NAME

backup_count = 0
while True:

    file_name = datetime.datetime.now().strftime('%Y-%m-%d_%H.%M.%S')
    time_now = datetime.datetime.now().strftime('%H:%M:%S')
    generate_zip(CUIS_PATH, OUTPUT_DIR_PATH, file_name)
    print("[{}] Generated backup #{} with name {}".format(time_now, backup_count, file_name))
    
    backup_count += 1
    time.sleep(SAVING_INTERVAL_IN_SECONDS)

