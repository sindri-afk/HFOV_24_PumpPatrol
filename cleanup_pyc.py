import os
import shutil

def delete_pycache_files(root_dir):
    for dirpath, dirnames, filenames in os.walk(root_dir):
        # Delete __pycache__ directories
        if "__pycache__" in dirnames:
            pycache_path = os.path.join(dirpath, "__pycache__")
            shutil.rmtree(pycache_path)
            print(f"Deleted: {pycache_path}")
        
        # Delete .pyc files
        for filename in filenames:
            if filename.endswith(".pyc"):
                pyc_file_path = os.path.join(dirpath, filename)
                os.remove(pyc_file_path)
                print(f"Deleted: {pyc_file_path}")

if __name__ == "__main__":
    project_root = os.path.dirname(os.path.abspath(__file__))
    delete_pycache_files(project_root)
    print("Cleanup complete.")