# Day 12: Git & Version Control - DevOps Training

## 🎯 Learning Objectives
By the end of this session, you will:
- Understand what Version Control is and why it's essential
- Know why Git is the industry standard
- Install and configure Git on your system
- Master essential Git commands
- Understand branching strategies and workflows
- Practice hands-on Git operations

---

## 📋 Table of Contents
1. [What is Version Control?](#what-is-version-control)
2. [Why Do We Need SCM?](#why-do-we-need-scm)
3. [Why Git?](#why-git)
4. [Installing Git](#installing-git)
5. [Git Configuration](#git-configuration)
6. [Essential Git Commands](#essential-git-commands)
7. [Branching Strategies](#branching-strategies)
8. [Hands-on Labs](#hands-on-labs)
9. [Best Practices](#best-practices)

---

## What is Version Control?

### Definition
**Version Control System (VCS)** is a tool that helps manage changes to source code over time. It keeps track of every modification to the code in a special kind of database.

### Key Concepts
- **Repository (Repo)**: A storage location for your project
- **Commit**: A snapshot of your project at a specific point in time
- **Branch**: A parallel version of your repository
- **Merge**: Combining changes from different branches
- **Clone**: Creating a local copy of a remote repository

### Types of Version Control Systems

#### 1. Local Version Control
```
Version 1 ← Version 2 ← Version 3 ← Current
```
- Simple database that keeps all changes to files
- Example: RCS (Revision Control System)

#### 2. Centralized Version Control
```
Developer A ↗
              Central Server
Developer B ↙
```
- Single server contains all versioned files
- Examples: CVS, Subversion (SVN), Perforce

#### 3. Distributed Version Control
```
Developer A (Full History) ↔ Central Server ↔ Developer B (Full History)
```
- Every clone is a full backup of all data
- Examples: Git, Mercurial, Bazaar

---

## Why Do We Need SCM?

### 1. **Track Changes**
```bash
# Without VCS - Manual backup nightmare
project-v1.0/
project-v1.1-bug-fix/
project-v1.2-new-feature/
project-v1.3-final/
project-v1.4-really-final/
project-v1.5-final-final/
```

### 2. **Collaboration Issues**
```
❌ Without VCS:
- Email code files back and forth
- "Who has the latest version?"
- Overwriting each other's work
- No way to merge changes safely

✅ With VCS:
- Everyone works on same codebase
- Automatic conflict detection
- Safe merging of changes
- Complete change history
```

### 3. **Backup & Recovery**
- Distributed nature provides multiple backups
- Never lose work due to hardware failure
- Can recover any previous version

### 4. **Branching & Experimentation**
- Create branches for new features
- Experiment without affecting main code
- Easy to switch between different versions

### 5. **Accountability & Documentation**
- Who made what changes and when
- Why changes were made (commit messages)
- Code review process

---

## Why Git?

### Git vs Other VCS

| Feature | Git | SVN | CVS |
|---------|-----|-----|-----|
| **Distributed** | ✅ | ❌ | ❌ |
| **Offline Work** | ✅ | ❌ | ❌ |
| **Branching** | Fast & Easy | Slow | Limited |
| **Merging** | Intelligent | Basic | Basic |
| **Performance** | Fast | Slower | Slowest |
| **Data Integrity** | SHA-1 checksums | Limited | None |

### Git Advantages

#### 1. **Speed**
```bash
# Git operations are lightning fast
git status    # Instant
git log       # Instant
git branch    # Instant
git checkout  # Seconds
```

#### 2. **Distributed Architecture**
```
Remote Repository (GitHub/GitLab)
         ↕
Local Repository (Your Machine)
         ↕
Working Directory
```

#### 3. **Data Integrity**
- Every file and commit is checksummed
- Impossible to change file contents without Git knowing
- SHA-1 hash ensures data integrity

#### 4. **Branching Model**
```
main     ●─────●─────●─────●
              ↗       ↙
feature      ●───●───●
```

#### 5. **Industry Standard**
- Used by 90%+ of developers
- Supported by all major platforms
- Extensive tooling ecosystem

---

## Installing Git

### Linux Installation

#### Ubuntu/Debian
```bash
# Update package index
sudo apt update

# Install Git
sudo apt install git

# Verify installation
git --version
```

#### CentOS/RHEL/Fedora
```bash
# For CentOS/RHEL
sudo yum install git

# For Fedora
sudo dnf install git

# Verify installation
git --version
```

#### From Source (Latest Version)
```bash
# Install dependencies
sudo apt install make libssl-dev libghc-zlib-dev libcurl4-gnutls-dev libncurses5-dev libedit-dev

# Download and compile
wget https://github.com/git/git/archive/v2.42.0.tar.gz
tar -xzf v2.42.0.tar.gz
cd git-2.42.0
make configure
./configure --prefix=/usr/local
make all
sudo make install
```

### Windows Installation

#### Option 1: Git for Windows
1. Download from: https://git-scm.com/download/win
2. Run the installer
3. Choose options:
   - Use Git from Git Bash only (recommended for beginners)
   - Use Git from the Windows Command Prompt
   - Use Git and optional Unix tools from Command Prompt

#### Option 2: Using Package Managers
```powershell
# Using Chocolatey
choco install git

# Using Scoop
scoop install git

# Using Winget
winget install Git.Git
```

### macOS Installation

#### Option 1: Homebrew
```bash
# Install Homebrew if not installed
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Install Git
brew install git
```

#### Option 2: Xcode Command Line Tools
```bash
# This will prompt to install if not present
git --version
```

---

## Git Configuration

### Initial Setup
```bash
# Set your identity (required)
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"

# Set default branch name
git config --global init.defaultBranch main

# Set default editor
git config --global core.editor "code --wait"  # VS Code
git config --global core.editor "vim"          # Vim
git config --global core.editor "nano"         # Nano

# Enable colored output
git config --global color.ui auto

# Set line ending preferences
git config --global core.autocrlf true   # Windows
git config --global core.autocrlf input  # macOS/Linux
```

### Configuration Levels
```bash
# System level (all users)
git config --system

# Global level (current user)
git config --global

# Local level (current repository)
git config --local

# View all configurations
git config --list

# View specific configuration
git config user.name
git config user.email
```

### Useful Aliases
```bash
# Create shortcuts for common commands
git config --global alias.st status
git config --global alias.co checkout
git config --global alias.br branch
git config --global alias.ci commit
git config --global alias.unstage 'reset HEAD --'
git config --global alias.last 'log -1 HEAD'
git config --global alias.visual '!gitk'

# Advanced aliases
git config --global alias.lg "log --oneline --decorate --all --graph"
git config --global alias.s "status -s"
git config --global alias.ac "!git add -A && git commit"
```

---

## Essential Git Commands

### 1. git init
**Purpose**: Initialize a new Git repository

```bash
# Create a new directory and initialize Git
mkdir my-project
cd my-project
git init

# Initialize Git in existing directory
cd existing-project
git init

# Create bare repository (for servers)
git init --bare my-repo.git
```

**What happens:**
- Creates `.git` directory
- Sets up repository structure
- Creates initial branch (main/master)

### 2. git clone
**Purpose**: Create a local copy of a remote repository

```bash
# Clone a repository
git clone https://github.com/user/repo.git

# Clone to specific directory
git clone https://github.com/user/repo.git my-local-name

# Clone specific branch
git clone -b develop https://github.com/user/repo.git

# Shallow clone (recent history only)
git clone --depth 1 https://github.com/user/repo.git

# Clone with SSH
git clone git@github.com:user/repo.git
```

### 3. git status
**Purpose**: Show the working tree status

```bash
# Basic status
git status

# Short format
git status -s
git status --short

# Show ignored files
git status --ignored
```

**Status Indicators:**
```
?? - Untracked files
A  - Added to staging area
M  - Modified
D  - Deleted
R  - Renamed
C  - Copied
U  - Updated but unmerged
```

### 4. git add
**Purpose**: Add file contents to the staging area

```bash
# Add specific file
git add filename.txt

# Add multiple files
git add file1.txt file2.txt

# Add all files in directory
git add .

# Add all files in repository
git add -A
git add --all

# Add by pattern
git add *.txt
git add src/

# Interactive adding
git add -i

# Add patches interactively
git add -p
```

### 5. git commit
**Purpose**: Record changes to the repository

```bash
# Commit with message
git commit -m "Add user authentication feature"

# Commit with detailed message
git commit -m "Add user authentication" -m "- Implement login/logout functionality
- Add password hashing
- Create user session management"

# Add and commit in one step
git commit -am "Fix bug in user validation"

# Commit with editor for long message
git commit

# Amend last commit
git commit --amend

# Amend without changing message
git commit --amend --no-edit
```

**Good Commit Messages:**
```bash
# ✅ Good
git commit -m "Fix user login validation bug"
git commit -m "Add Docker configuration for development"
git commit -m "Update README with installation instructions"

# ❌ Bad
git commit -m "fix"
git commit -m "changes"
git commit -m "stuff"
```

### 6. git log
**Purpose**: Show commit logs

```bash
# Basic log
git log

# One line per commit
git log --oneline

# Show last n commits
git log -5

# Show commits with diff
git log -p

# Show commits for specific file
git log filename.txt

# Show commits by author
git log --author="John Doe"

# Show commits in date range
git log --since="2023-01-01" --until="2023-12-31"

# Graphical representation
git log --graph --oneline --decorate --all

# Custom format
git log --pretty=format:"%h - %an, %ar : %s"
```

### 7. git diff
**Purpose**: Show changes between commits, working tree, etc.

```bash
# Show unstaged changes
git diff

# Show staged changes
git diff --staged
git diff --cached

# Compare specific files
git diff filename.txt

# Compare branches
git diff main..feature-branch

# Compare commits
git diff HEAD~1 HEAD

# Show word-level differences
git diff --word-diff

# Show statistics
git diff --stat

# Compare with remote
git diff origin/main
```

---

## Branching Strategies

### Understanding Branches

```
main     ●─────●─────●─────●
              ↗       ↙
feature      ●───●───●
```

Branches allow you to:
- Work on features independently
- Experiment without affecting main code
- Collaborate without conflicts
- Maintain different versions

### git branch
**Purpose**: List, create, or delete branches

```bash
# List all branches
git branch

# List all branches (including remote)
git branch -a

# Create new branch
git branch feature-login

# Create branch from specific commit
git branch hotfix-123 abc1234

# Delete branch
git branch -d feature-login

# Force delete branch
git branch -D feature-login

# Rename current branch
git branch -m new-branch-name

# Show last commit on each branch
git branch -v
```

### git checkout
**Purpose**: Switch branches or restore working tree files

```bash
# Switch to existing branch
git checkout feature-login

# Create and switch to new branch
git checkout -b feature-signup

# Switch to previous branch
git checkout -

# Checkout specific commit (detached HEAD)
git checkout abc1234

# Checkout specific file from another branch
git checkout main -- filename.txt

# Discard changes in working directory
git checkout -- filename.txt
git checkout .
```

### Modern Alternative: git switch & git restore
```bash
# Switch branches (Git 2.23+)
git switch feature-login
git switch -c feature-signup  # create and switch

# Restore files (Git 2.23+)
git restore filename.txt      # discard changes
git restore --staged file.txt # unstage file
```

### git merge
**Purpose**: Join two or more development histories together

```bash
# Merge feature branch into current branch
git merge feature-login

# Merge with commit message
git merge feature-login -m "Merge login feature"

# No fast-forward merge (always create merge commit)
git merge --no-ff feature-login

# Abort merge in case of conflicts
git merge --abort

# Continue merge after resolving conflicts
git merge --continue
```

**Merge Types:**

#### Fast-Forward Merge
```
Before:
main     ●─────●
              ↘
feature        ●───●

After:
main     ●─────●───●───●
```

#### Three-Way Merge
```
Before:
main     ●─────●─────●
              ↗       ↘
feature      ●───●───● ●

After:
main     ●─────●─────●───●
              ↗           ↙
feature      ●───●───●───●
```

### git rebase
**Purpose**: Reapply commits on top of another base tip

```bash
# Rebase current branch onto main
git rebase main

# Interactive rebase (last 3 commits)
git rebase -i HEAD~3

# Rebase specific range
git rebase -i abc1234..def5678

# Continue rebase after resolving conflicts
git rebase --continue

# Skip current commit during rebase
git rebase --skip

# Abort rebase
git rebase --abort
```

**Rebase vs Merge:**

#### Before:
```
main     ●─────●─────●
              ↗
feature      ●───●───●
```

#### After Merge:
```
main     ●─────●─────●───●
              ↗           ↙
feature      ●───●───●───●
```

#### After Rebase:
```
main     ●─────●─────●───●───●───●
```

### Common Branching Strategies

#### 1. Git Flow
```
main        ●─────●─────●─────●
            ↑     ↑     ↑     ↑
develop     ●─●─●─●─●─●─●─●─●─●
            ↗ ↘ ↗ ↘ ↗ ↘
feature       ●─●   ●─●
hotfix          ●─●
release           ●─●─●
```

#### 2. GitHub Flow
```
main     ●─────●─────●─────●
              ↗ ↘   ↗ ↘
feature      ●───● ●───●
```

#### 3. GitLab Flow
```
main        ●─────●─────●─────●
            ↓     ↓     ↓     ↓
production  ●─────●─────●─────●
```

---

## Hands-on Labs

### Lab 1: Basic Git Workflow

```bash
# 1. Create and initialize repository
mkdir git-lab-1
cd git-lab-1
git init

# 2. Create initial file
echo "# My First Git Project" > README.md
echo "This is a sample project for learning Git." >> README.md

# 3. Check status and add file
git status
git add README.md
git status

# 4. Make first commit
git commit -m "Initial commit: Add README"

# 5. Make changes
echo "" >> README.md
echo "## Features" >> README.md
echo "- Version control with Git" >> README.md

# 6. View differences
git diff
git add README.md
git diff --staged

# 7. Commit changes
git commit -m "Add features section to README"

# 8. View history
git log --oneline
```

### Lab 2: Working with Branches

```bash
# 1. Create and switch to feature branch
git checkout -b feature-user-auth

# 2. Create new files
echo "class User:" > user.py
echo "    def __init__(self, username):" >> user.py
echo "        self.username = username" >> user.py

echo "def login(username, password):" > auth.py
echo "    # TODO: Implement login logic" >> auth.py
echo "    return True" >> auth.py

# 3. Add and commit
git add .
git commit -m "Add user authentication scaffolding"

# 4. Switch back to main
git checkout main

# 5. Make changes on main
echo "" >> README.md
echo "## Installation" >> README.md
echo "pip install -r requirements.txt" >> README.md

git add README.md
git commit -m "Add installation instructions"

# 6. View branch differences
git log --oneline --graph --all

# 7. Merge feature branch
git merge feature-user-auth

# 8. Clean up
git branch -d feature-user-auth
```

### Lab 3: Handling Merge Conflicts

```bash
# 1. Create conflicting branches
git checkout -b branch-a
echo "Hello from Branch A" > conflict.txt
git add conflict.txt
git commit -m "Add greeting from branch A"

git checkout main
git checkout -b branch-b
echo "Hello from Branch B" > conflict.txt
git add conflict.txt
git commit -m "Add greeting from branch B"

# 2. Try to merge (will cause conflict)
git checkout main
git merge branch-a  # This will work
git merge branch-b  # This will cause conflict

# 3. Resolve conflict
# Edit conflict.txt to resolve
echo "Hello from both branches!" > conflict.txt
git add conflict.txt
git commit -m "Resolve merge conflict"

# 4. Clean up
git branch -d branch-a branch-b
```

### Lab 4: Rebase Practice

```bash
# 1. Create feature branch
git checkout -b feature-database

# 2. Make several commits
echo "import sqlite3" > database.py
git add database.py
git commit -m "Add database module"

echo "def connect():" >> database.py
echo "    return sqlite3.connect('app.db')" >> database.py
git add database.py
git commit -m "Add database connection function"

echo "def create_tables():" >> database.py
echo "    # TODO: Create tables" >> database.py
git add database.py
git commit -m "Add table creation function"

# 3. Switch to main and make changes
git checkout main
echo "python>=3.8" > requirements.txt
git add requirements.txt
git commit -m "Add Python version requirement"

# 4. Rebase feature branch
git checkout feature-database
git rebase main

# 5. View clean history
git log --oneline --graph
```

---

## Best Practices

### 1. Commit Messages
```bash
# ✅ Good commit message format
git commit -m "Add user authentication middleware

- Implement JWT token validation
- Add role-based access control
- Update API documentation

Fixes #123"

# Follow conventional commits
git commit -m "feat: add user authentication"
git commit -m "fix: resolve login validation bug"
git commit -m "docs: update API documentation"
git commit -m "refactor: simplify database queries"
```

### 2. Branching Strategy
```bash
# Use descriptive branch names
git checkout -b feature/user-authentication
git checkout -b bugfix/login-validation
git checkout -b hotfix/security-patch
git checkout -b release/v1.2.0

# Keep branches focused and short-lived
# Merge or rebase regularly
# Delete merged branches
```

### 3. Repository Structure
```
project/
├── .gitignore          # Ignore unnecessary files
├── README.md           # Project documentation
├── CONTRIBUTING.md     # Contribution guidelines
├── LICENSE            # License information
├── requirements.txt   # Dependencies
├── src/              # Source code
├── tests/            # Test files
├── docs/             # Documentation
└── scripts/          # Build/deployment scripts
```

### 4. .gitignore Best Practices
```bash
# Create comprehensive .gitignore
cat > .gitignore << EOF
# OS generated files
.DS_Store
Thumbs.db

# IDE files
.vscode/
.idea/
*.swp
*.swo

# Language specific
__pycache__/
*.pyc
node_modules/
*.class
*.jar

# Build artifacts
dist/
build/
*.egg-info/

# Environment files
.env
.env.local

# Logs
*.log
logs/

# Database
*.db
*.sqlite

# Temporary files
*.tmp
*.temp
EOF
```

### 5. Security Considerations
```bash
# Never commit sensitive information
# Use environment variables for secrets
# Review commits before pushing
# Use signed commits for important repositories

# Set up commit signing
git config --global user.signingkey YOUR_GPG_KEY
git config --global commit.gpgsign true
```

### 6. Collaboration Workflow
```bash
# 1. Always pull before starting work
git pull origin main

# 2. Create feature branch
git checkout -b feature/new-feature

# 3. Make changes and commit regularly
git add .
git commit -m "Implement feature component"

# 4. Push branch and create pull request
git push origin feature/new-feature

# 5. After review and merge, clean up
git checkout main
git pull origin main
git branch -d feature/new-feature
```

---

## Common Git Scenarios & Solutions

### Undo Changes
```bash
# Undo unstaged changes
git checkout -- filename.txt
git restore filename.txt

# Undo staged changes
git reset HEAD filename.txt
git restore --staged filename.txt

# Undo last commit (keep changes)
git reset --soft HEAD~1

# Undo last commit (discard changes)
git reset --hard HEAD~1

# Undo specific commit
git revert abc1234
```

### Stashing Changes
```bash
# Stash current changes
git stash

# Stash with message
git stash save "Work in progress on feature X"

# List stashes
git stash list

# Apply latest stash
git stash apply

# Apply and remove stash
git stash pop

# Apply specific stash
git stash apply stash@{2}

# Drop stash
git stash drop stash@{1}
```

### Remote Repositories
```bash
# Add remote
git remote add origin https://github.com/user/repo.git

# List remotes
git remote -v

# Fetch from remote
git fetch origin

# Pull from remote
git pull origin main

# Push to remote
git push origin main

# Push new branch
git push -u origin feature-branch
```

---

## Troubleshooting Common Issues

### 1. Merge Conflicts
```bash
# When you see conflict markers:
<<<<<<< HEAD
Your changes
=======
Their changes
>>>>>>> branch-name

# Steps to resolve:
# 1. Edit file to resolve conflicts
# 2. Remove conflict markers
# 3. Add resolved file
git add conflicted-file.txt
# 4. Complete merge
git commit
```

### 2. Detached HEAD State
```bash
# If you're in detached HEAD:
# 1. Create branch from current state
git checkout -b recovery-branch

# 2. Or go back to main branch
git checkout main
```

### 3. Accidentally Committed to Wrong Branch
```bash
# Move commits to correct branch
git checkout correct-branch
git cherry-pick abc1234  # commit hash

# Remove from wrong branch
git checkout wrong-branch
git reset --hard HEAD~1
```

---

## Summary & Next Steps

### What We Covered Today
- ✅ Understanding Version Control and SCM importance
- ✅ Why Git is the industry standard
- ✅ Installing and configuring Git
- ✅ Essential Git commands (init, clone, status, add, commit, log, diff)
- ✅ Branching strategies (branch, checkout, merge, rebase)
- ✅ Hands-on practice with real scenarios
- ✅ Best practices and troubleshooting

### Key Takeaways
1. **Git is essential** for modern software development
2. **Commit early and often** with meaningful messages
3. **Use branches** for features and experiments
4. **Collaborate safely** with proper workflows
5. **Practice regularly** to build muscle memory

### Tomorrow's Preview: Day 13
- Advanced Git workflows
- Git hooks and automation
- Integration with CI/CD pipelines
- GitHub/GitLab workflows
- Code review processes

### Homework Assignment
1. Create a personal project repository
2. Practice all commands covered today
3. Create at least 3 branches and merge them
4. Set up your Git configuration properly
5. Create a meaningful .gitignore file

### Resources for Further Learning
- [Pro Git Book](https://git-scm.com/book) - Free online book
- [Git Documentation](https://git-scm.com/docs) - Official documentation
- [GitHub Learning Lab](https://lab.github.com/) - Interactive tutorials
- [Atlassian Git Tutorials](https://www.atlassian.com/git/tutorials) - Comprehensive guides

---

## Q&A Session

**Common Questions:**

**Q: When should I use merge vs rebase?**
A: Use merge for feature integration (preserves history), use rebase for cleaning up commit history before sharing.

**Q: How often should I commit?**
A: Commit whenever you complete a logical unit of work. Better to commit too often than too rarely.

**Q: What if I accidentally commit sensitive data?**
A: Use `git filter-branch` or BFG Repo-Cleaner to remove it from history, then force push.

**Q: Should I commit directly to main branch?**
A: No, always use feature branches and pull requests for better collaboration and code review.

---

*End of Day 12 Presentation*

**Remember**: Git mastery comes with practice. Start using it for all your projects, even small ones!
