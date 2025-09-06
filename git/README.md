# Practie 01
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
# Practie 02
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
## Local Area - untracked, unmodifed, modifed, staged
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
				- msg in cli diff og git
git commit -m "staged"
git diff --cached
git status

```
