import os
import sys
from github import Github

def main(argv):
    startPath = os.getcwd()
    os.chdir(argv[0])
    try:
        projName = ''
        folderName = ''
        for item in argv[3:]:
            projName += ' ' + item
            folderName += '-' + item.lower()
        projName = projName[1:]
        folderName = folderName[1:]
        os.mkdir(folderName)
    except OSError:
        print('Error creating the directory %s.' % folderName)
    else:
        Github(argv[1], argv[2]).get_user().create_repo(folderName)
        os.chdir(folderName)
        os.system('echo "New repository for ' + projName + '" >> README.md')
        os.system('git init')
        os.system('git add -A')
        os.system('git commit -m "Initial commit, creation of basic README."')
        os.system('git remote add origin https://github.com/' + argv[1] + '/' + folderName)
        os.system('git push -u origin master')
        os.system(argv[1])
        os.system(argv[2])
    os.chdir(startPath)

if __name__ == '__main__':
    if (len(sys.argv) >= 5):
        main(sys.argv[1:])
    else:
        print('Usage of this program: python3 new_repo.py [Repository Directory] [Github Username] [Github Password] [Project Name]')
