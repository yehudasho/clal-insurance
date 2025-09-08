# Practice 01
- GIT - it is not just random 3 letters
- Created by Linus Torvalds in 2005 (the same person who created Linux)

## General TFS and TFVC
- TFS (Team Foundation Server)
Microsoft’s on-premises suite for:
Version control
Build automation
Bug tracking
Project management (work items, Agile boards, etc.)
- TFS supports two kinds of version control:
  - TFVC (centralized, older)
  - Git (distributed, modern)

TFS was later renamed to Azure DevOps Server.

- In short:
  - TFVC = just the centralized version control system.
  - TFS = the whole DevOps/ALM platform, which includes TFVC (or Git).
# Practice 02
## lab-01
- https://gitlab.com/sela-git-basic-workshop/lab-01
  
- Bonus: clone the repository of clal and do it via **Git Bash**
  - git clone https://github.com/yehudasho/clal-insurance.git

```
cd clal-insurance/
ls
echo "new line" >> test-file-01.txt
cat test-file-01.txt
ls
git add test-file-01.txt
git commit -m "new line"
git tag "tag-lab-01"
git tag
git status
```

- Go to https://github.com/yehudasho/clal-insurance/tags in order to see the tag
```
git tag "tag-lab-01"
git pull
git push
git push origin "tag-lab-01"
```
# Git Structure, Four Areas and Lifecycle
## Git Structure - untracked, unmodifed, modifed, staged
- The staged area in Git is also called the index or cache area
- It holds changes that you’ve marked to be included in the next commit, but haven’t committed yet
  
```
	# untracked - new file but not in git add yet
vi test-file-02.txt
git status
 				 - msg in cli is: Untracked files
cat test-file-02.txt

	# unmodifed
git add test-file-02.txt
git commit -m "commited"
				- you can combine commit and add with one command:
git commit -am  "am"
git status
				- is committed and unmodifed

	
	# modifed
echo "new line-02" >> test-file-02.txt
git status
				- msg in cli is:  modified:   test-file-02.txt
git commit -am  "am"
				- msg in cli is:  modified:   nothing to commit, working tree clean

	# staged
git status
git diff --cached
echo "new line-03" >> test-file-02.txt
git status
git add test-file-02.txt
git diff --cached
				- msg in cli is: diff of git
git commit -m "staged"
git diff --cached
				- msg in cli is: no diff of git
git status
```

## Four Areas - Working, Index, Repository and Stash
### Local Area or Working Area
```
mkdir course-name
cd course-name
ls -la
git init
ls -la                # you can see the ./git folder
ls -la ./git
cat ./git/config                                       - see the diff with remote server
cat ../devops-git-hungry-to-healthy/.git/config
Gitignore - go to gitignore.io site​
from site choose vsc and python - create file to add to .gitignore​
Paralell on .git folder
```
### Stage Area or Index Area
- The staged area in Git is also called the index or cache area
- It holds changes that you’ve marked to be included in the next commit, but haven’t committed yet

- More Example
```
git status
git diff --cached
echo "stage area example 01" >> README.md
git diff --cached
git status
git add .
git diff --cached
cat README.md
git status
git commit -m "nnn"
git diff --cached
git status

```
### Repository Area ( .git )
- Repository = permanent history of commits.
- Repository = All in the .git folder that stores all commits, branches, tags, and history

```
ls -la                # you can see the ./git folder
ls -la ./git
cat ./git/config                                       - see the diff with remote server
cat ../devops-git-hungry-to-healthy/.git/config
Gitignore - go to gitignore.io site​
from site choose vsc and python - create file to add to .gitignore​
Paralell on .git folder
```
### Stash Area 
Stash = temporary storage for unfinished work.
- Step-by-step example of using git stash while editing README.md,
  temporarily switching to work on index.html, and then 
  returning to your original work
- You're on main branch working on README.md,
  but suddenly you need to fix something in index.html first
- stash Area

```
ls -ltra
git status
cat README.md
echo "stash example" >> README.md
cat README.md
git status
git stash list
git stash push -m "contact switch to other task"
git stash list
git status
cat index.html 			# make sure that the content of index.html file already exist and commited
echo "<h1>Fixing index.html</h1>" >> index.html
cat index.html
git stash list
git add index.html
git commit -m "fix index file"
git status
git stash pop		# Now we can back to work on README.md task
git status
git add README.md
git commit -m "END task of readme file"
git stash list
git stash clear				# clear if needed
```
# Practice 03
## Git mv, log and rm commands
```
echo "mv-log-rm file line 01" >> mv-log-rm-file.txt
git add .
git commit -m "new"
ls
git status
cat mv-log-rm-file.txt
git mv mv-log-rm-file.txt mv-log-rm-file-01.txt
git status
git add .
git commit -m "new"
git status
git log						# See the SHA1
gitk
git log --oneline mv-log-rm-file-01
git log --graph --pretty='%Cred%h%Creset -%C(auto)%d%Creset %s %Cgreen(%cr) %C(bold blue)<%an>%Creset' --all
gitk

echo "mv-log-rm file line 02" >> mv-log-rm-file-01.txt
cat mv-log-rm-file-01.txt
git commit -am "am"
git status
git log mv-log-rm-file-01.txt

	# git diff <SHA 12345>  <SHA67899>
git diff 67c66 af8e1

		# add as alias
git config --global alias.lg "log --graph --pretty='%Cred%h%Creset -%C(auto)%d%Creset %s %Cgreen(%cr) %C(bold blue)<%an>%Creset' --all"
cat ~/.gitconfig

git rm -f mv-log-rm-file-01.txt
git ls-files
```

# Practice 04

## Branches - workfolw via visualizing-git 
- Make sure you are not lossing the head

- Go to http://git-school.github.io/visualizing-git
  
```
git commit "01"
git commit "02"
git commit "03"
git checkout -b "new-branch"
git commit "new-branch-01"
git commit "new-branch-02"
git checkout head~3
git checkout -b "feature-01"	
git commit "feature-01"
git commit "feature-02"
git commit "feature-03"
git checkout master 
git checkout -b "feature-02"
git commit "feature-02-01"
git commit "feature-02-02"
git commit "feature-02-03"
git commit "feature-02-04"

	# lossing the head				
git checkout head~6 
git commit "lossing the head"
git commit "lossing the head 02"
git checkout -b "loss-head-br"           # fix lossing the head
git branch
git checkout master
git branch -d "loss-head-br"             # delete branch
git branch
```

## Branches - workfolw via Visual Studio Code  or Git bash

```
git status
git branch
git branch --all
git branch -r
git checkout -b feature01
git branch
git branch --all
ls
ls -la
cat .gitignore
vi README.md
cat README.md
git add .
git commit -m "first commit in feature br"
echo "add second line in feature br" >> README.md
git diff --cached
git add .
git diff --cached
git commit -m "second commit in feature br"
git status
git branch
git branch --all
git pull
git push 					# the message is since we need to sync the branches
git push --set-upstream origin feature01
git push
```


# Practice 05
## Revert, Cherry-pick

### Git Revert
- Git revert is a Git command that cencel the changes by a specific commit
  by creating a new commit that is the inverse of that commit
- It does not delete history
- It does not remove the original commit instead,
  it cancels out its changes in a new commit

- Steps are:
  - Create file with 3 commit
  - Revert on revision by revert command
    
```
echo "line 01" >> revert.txt
git add .
git commit -m "line-01"
echo "line 02" >> revert.txt
git add .
git commit -m "line 02"
echo "line 03" >> revert.txt
git commit -m "line-03"
git add .
git commit -m "line-03"
echo "line 04" >> revert.txt
git commit -am "line 04"
echo "line 05" >> revert.txt
git commit -am "line 05"
git log --oneline revert.txt
	# Output
		fb6e4de (HEAD -> main) line 05
		041aab9 line 04
		02e8d93 line 03
		21d7822 line 02
		53ecf45 line 01
cat revert.txt
	# Output
		line 01
		line 02
		line 03
		line 04
		line 05
git revert HEAD
git log --oneline revert-01.txt
	# Output - creating a new commit
		589cc42 (HEAD -> main) Revert "line-05"
		fb6e4de line 05
		041aab9 line 04
		02e8d93 line 03
		21d7822 line 02
		53ecf45 line 01
cat revert.txt
	# Output
		line 01
		line 02
		line 03
		line 04
```
### Git Cherry-pick

- Git cherry-pick is a Git command that applies the changes from an existing commit (or commits) onto your current branch
Unlike git merge, it does not merge the whole branch.
- It only takes specific commit(s) and applies their changes on top of your current     branch.
- This creates a new commit with a new SHA on your current branch
  Steps are:
  - In branch main, Make three commits ( its means 3 line )
  - Create a new branch feature without the latest commits(HEAD 2, its means 1 line )
  - Cherry-pick a commit from main (pick HEAD 1 its means line 02)
  - Now feature has C1 plus C2
    
```
echo "line 01" >> cherry-pick.txt
git add .
git commit -m "line-01"
echo "line 02" >> cherry-pick.txt
git add .
git commit -m "line-02"
echo "line 03" >> cherry-pick.txt
git commit -m "line-03"
git add .
git commit -m "line-03"
git log --oneline cherry-pick.txt
	# Output
			db29065 (HEAD -> main) line-03
			02b9326 line-02
			bba4221 line-01

git checkout -b feature HEAD~2
git branch
git log --oneline cherry-pick.txt
	#	Output
		0c024d7 (HEAD -> feature) line-01

git cherry-pick main~1
git log --oneline cherry-pick.txt
	#	Output
		f88f488 (HEAD -> feature) line-02
		0c024d7 line-01
cat cherry-pick.txt
	# Output
		line 01
		line 02

```

# Practie 06
## Merge and Rebase

# Practie 07
## Git - Working via Visual Studio Code (VSC)

- Open the VSC
- Create a new clal.html file
- copy the contant of index.html file into clal.html
```
<!DOCTYPE html>
<html>
<head>
    <title>Hello World</title>
</head>
<body>
    <h1>Hello Clal! 🎉</h1>
    <p>Git - Working via Visual Studio Code .</p>
</body>
</html>
```
- Save the the file
- Commit the file
- Sync as with Remote Repository
- Right-click on index.html
- Choose **Open with Live Server**
  - A browser window will open automatically at
  - http://127.0.0.1:5500/index.html
### VSC - Additinal Example with calendar.html app
- Open the VSC
- On Git Bash terminal run the main.py app
```
py.exe main.py
```
- OPen the Browser and see the calendar app is running
- Go to templates -> calendar.html file and change the color
- Make sure the color is changed
  
# Practie 08
## Hooks

# Practie 09
## Cherry-Pick


