# File Integrity Check
    # Input - Folder path
    # Output - Files in the folder and their hashes
   

from pathlib import Path
import hashlib
import json

def file_integrity_check (folder_path):

    #file_hashes = {}
    current_hashes = calculate_hashes(folder_path)

    old_hashes = load_hashes()

    #establishing baseline
    if old_hashes is None:
        print(" No previous hash file found. Creating baseline.")
    else:
        compare_hashes(old_hashes, current_hashes)

    save_hashes(current_hashes)

def calculate_hashes(folder_path):
    
    file_hashes ={}
    for file_path in folder_path.iterdir():
        if file_path.is_file():
            with open(file_path, "rb") as f:
                digest = hashlib.file_digest(f, "sha256")
            file_hashes[str(file_path)] = digest.hexdigest()
            
    return file_hashes

def load_hashes():
    if not Path("hashes.json").is_file():
        return None
    else:
        with open("hashes.json", "r") as f:
            old_hashes = json.load(f)
        return old_hashes

def compare_hashes(old_hashes, current_hashes):
    for key in current_hashes:
        if key in old_hashes:
            if current_hashes[key] != old_hashes[key]:
                print(f"{key} was modified")
        elif key not in old_hashes:
            print(f"{key} is a new file")

    for i in old_hashes:
        if i not in current_hashes:
            print(f"{i} was deleted")
    
def save_hashes(current_hashes):
    
    # ## display results
    # for file_path, file_hash in file_hashes.items():
    #     print(f"{file_path.name:<30}: {file_hash}")          
     #store results
    with open("hashes.json", "w") as f:
        json.dump(current_hashes, f, indent=4)
        
def main():
    print("Please input the folder path: ")
    folder_path = Path(input())
    
    file_integrity_check(folder_path)

if __name__ == "__main__":
    main()