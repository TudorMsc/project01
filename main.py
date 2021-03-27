student@ACAD06 MINGW64 ~/Desktop
$ mkdir project

student@ACAD06 MINGW64 ~/Desktop
$ cd project

student@ACAD06 MINGW64 ~/Desktop/project
$ git init
Initialized empty Git repository in C:/Users/student/Desktop/project/.git/
t
student@ACAD06 MINGW64 ~/Desktop/project (master)
$ touch main.py

student@ACAD06 MINGW64 ~/Desktop/project (master)
$ ls
main.py

student@ACAD06 MINGW64 ~/Desktop/project (master)
$ git add main.py

student@ACAD06 MINGW64 ~/Desktop/project (master)
$ git status
On branch master

No commits yet

Changes to be committed:
  (use "git rm --cached <file>..." to unstage)

        new file:   main.py


student@ACAD06 MINGW64 ~/Desktop/project (master)
$ git commit -m "New commit"
[master (root-commit) b802136] New commit
 1 file changed, 0 insertions(+), 0 deletions(-)
 create mode 100644 main.py

student@ACAD06 MINGW64 ~/Desktop/project (master)
$ git status
On branch master
nothing to commit, working tree clean

student@ACAD06 MINGW64 ~/Desktop/project (master)
$

student@ACAD06 MINGW64 ~/Desktop/project (master)
$

student@ACAD06 MINGW64 ~/Desktop/project (master)
$ git remote add origin https://github.com/TudorMsc/TudorMsc.git

student@ACAD06 MINGW64 ~/Desktop/project (master)
$ git push -u origin main
error: src refspec main does not match any.
error: failed to push some refs to 'https://github.com/TudorMsc/TudorMsc.git'

student@ACAD06 MINGW64 ~/Desktop/project (master)
$ git push
fatal: The current branch master has no upstream branch.
To push the current branch and set the remote as upstream, use

    git push --set-upstream origin master


student@ACAD06 MINGW64 ~/Desktop/project (master)
$ ^C

student@ACAD06 MINGW64 ~/Desktop/project (master)
$ ^C

student@ACAD06 MINGW64 ~/Desktop/project (master)
$ git push --set-upstream origin master
Logon failed, use ctrl+c to cancel basic credential prompt.
Username for 'https://github.com': TudorMsc
Enumerating objects: 3, done.
Counting objects: 100% (3/3), done.
Writing objects: 100% (3/3), 208 bytes | 208.00 KiB/s, done.
Total 3 (delta 0), reused 0 (delta 0)
To https://github.com/TudorMsc/TudorMsc.git
 * [new branch]      master -> master
Branch 'master' set up to track remote branch 'master' from 'origin'.

student@ACAD06 MINGW64 ~/Desktop/project (master)
$ python
