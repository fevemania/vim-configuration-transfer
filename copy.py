import shutil
import os
 
def copyFile(src, dest):
    try:
        shutil.copy(src, dest)
    # eg. src and dest are the same file
    except shutil.Error as e:
        print('Error: %s' % e)
    # eg. source or destination doesn't exist
    except IOError as e:
        print('Error: %s' % e.strerror)

if __name__ == '__main__':
    home = os.getcwd()
    if home == os.path.expanduser('~'):
        source = os.path.join(home, '.vimrc')
        target = os.path.join(home, '.vim/.vimrc')
        copyFile(source, target)
