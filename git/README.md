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
git status
```

  
