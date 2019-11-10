import subprocess
import sys

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    

def inside_venv():
    return sys.base_prefix != sys.prefix
    
    
def pythanos():
    if not inside_venv():
        # Check if you are inside a virtual environment
        print(bcolors.WARNING, "Warning! You are outside a virtual environment. This will erase all system wide packages!", bcolors.ENDC)
        sys.exit(1)
    else:
        curr_packages = subprocess.getoutput('pip freeze').split('\n')
        
    print("Found {} installed packages in the current virtual environment".format(len(curr_packages)))

    # TODO - add an argument to get the packages before removing them
    # TODO - ask for confirmation
    
    c = input('Confirmation for Thanos to fuck this world up!')

    if c == 'y':

        print ("Pythanos snaps...")
        
        for package in curr_packages:
            print("Removing {}".format(package))
            command = 'pip uninstall {} -y'.format(package)
            print(subprocess.getoutput(command))
      
if __name__ == '__main__':
    pythanos()
