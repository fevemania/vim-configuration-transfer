from git import Repo
import os
from pathlib import Path 
from os.path import expanduser

def auto_download(dir_name):
    HOME = os.path.expanduser('~')
    bundle_dir = os.path.join(HOME, '.vim/bundle')
    if not os.path.exists(bundle_dir):
        os.makedirs(bundle_dir)
    vundle_path = Path(os.path.join(HOME, dir_name))

    # Check if Vundle.vim exist to avoid repeatly download 
    if vundle_path.is_dir():
    	print(dir_name, " is alreadly in ", vundle_path)
    else:
    	Repo.clone_from("git@github.com:VundleVim/Vundle.vim.git", dir_name,branch="master")
if __name__ == "__main__":
	auto_download('.vim/bundle/Vundle.vim')