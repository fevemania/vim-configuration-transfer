import os
import sys
import subprocess
from shutil import copyfile
 
def check_module_exists(module_name):
    result = subprocess.run(['pip3','list'], stdout=subprocess.PIPE)
    #print(type(result.stdout)) # the return value is byte object 
    if module_name not in result.stdout.decode('utf-8'):  # so we should decode it to extract proper string
        subprocess.run(['pip3', 'install', module_name])

# check_file_exist, if exist throw except_action, else do copy file action
def check_file_exist(filepath, action, filename, new_path):
    if os.path.isfile(filepath):
        print(filepath, 'already exist, please check it')
    else:
        action(filename, new_path)

def check_dir_exist(dirpath, action, current_path, new_path):
    if os.path.isdir(dirpath):
        print(dirpath, 'already exist, please check it')
    else:
        action(current_path, new_path)

def rename(current_path, new_path):
    os.rename(current_path, new_path)

if __name__ == '__main__':
    # Step1. pip3 install GitPython, if not exist.
    check_module_exists('GitPython')
    
    home_dir = os.path.expanduser('~')
    current_path = os.getcwd()
    
    # Step2. mv vim_config .vim
    dot_vim_path = home_dir + '/.vim'
    check_dir_exist(dot_vim_path, os.rename, current_path, dot_vim_path) 
    
    # Step3. cp .vim/.vimrc ~
    vimrc_path = home_dir + '/.vimrc'
    check_file_exist(vimrc_path, copyfile, '.vimrc', vimrc_path) 
    
    # Step4. cp copy.py ~ (for auto_copy .vimrc to .vim whenever change)
    copy_py_file = home_dir + '/copy.py'
    check_file_exist(copy_py_file, copyfile, 'copy.py', copy_py_file)
    
    # Step5. download for Vundle
    subprocess.run(['python3', 'auto_download.py']) 
  
   

    


