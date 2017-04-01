from git import Repo
import os
from pathlib import Path 
from os.path import expanduser

def auto_download(filename):
    HOME = os.path.expanduser('~')
    bundle_dir = os.path.join(HOME, '.vim/bundle')
    if not os.path.exists(bundle_dir):
        os.makedirs(bundle_dir)

    vundle_path = Path(os.path.join(HOME, filename))

    # Check if Vundle.vim exist to avoid repeatly download 
    if vundle_path.is_dir():
    	print(dir_name, " is alreadly in ", vundle_path)
    else:
    	Repo.clone_from("https://github.com/VundleVim/Vundle.vim.git", vundle_path, branch="master")

if __name__ == "__main__":
	auto_download('Vundle.vim')
