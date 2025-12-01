# Day 12 Git Fundamentals - Group Activities
## 5 Groups × 6 Members Each - Collaborative Learning

---

## 🎯 Activity Overview
Each group will create a **private repository** and work through progressive Git scenarios that simulate real-world development workflows. These activities are designed to reinforce the Day 12 concepts through hands-on practice.

---

## 📋 Pre-Activity Setup (5 minutes)

### Group Formation & Repository Setup
1. **Group Leaders**: Each group selects one member as the "Repository Owner"
2. **Repository Creation**: Repository Owner creates a private GitHub repository named: `devops-git-lab-group[X]` (where X = group number)
3. **Team Invitation**: Repository Owner invites all 5 team members as collaborators
4. **Role Assignment**: 
   - 1 Repository Owner (manages main branch)
   - 2 Feature Developers (work on features)
   - 2 Code Reviewers (review and merge)
   - 1 Release Manager (handles tags and releases)

---

## 🚀 Activity 1: Git Basics Relay (15 minutes)
**Objective**: Master fundamental Git commands through team collaboration

### Scenario
Your team is starting a new project called "DevOps Task Manager" - a simple task management application.

### Instructions
**Round 1: Repository Initialization (Repository Owner)**
```bash
# Clone the empty repository
git clone https://github.com/[username]/devops-git-lab-group[X].git
cd devops-git-lab-group[X]

# Create initial project structure
mkdir src tests docs
echo "# DevOps Task Manager" > README.md
echo "A collaborative task management application built by Group [X]" >> README.md
echo "" >> README.md
echo "## Team Members" >> README.md
echo "- [List all 6 team member names]" >> README.md

# Create .gitignore
cat > .gitignore << EOF
node_modules/
.env
*.log
.DS_Store
dist/
EOF

# Initial commit
git add .
git commit -m "feat: initial project setup with team structure"
git push origin main
```

**Round 2: Feature Development (Feature Developers - 2 members)**

*Developer 1:*
```bash
# Pull latest changes
git pull origin main

# Create task management core
echo "class TaskManager {
    constructor() {
        this.tasks = [];
    }
    
    addTask(task) {
        this.tasks.push({
            id: Date.now(),
            title: task,
            completed: false,
            createdBy: 'Group[X]'
        });
    }
}" > src/taskManager.js

git add src/taskManager.js
git commit -m "feat: add TaskManager class with addTask method"
git push origin main
```

*Developer 2:*
```bash
# Pull latest changes (including Developer 1's work)
git pull origin main

# Add more functionality
echo "
    completeTask(id) {
        const task = this.tasks.find(t => t.id === id);
        if (task) {
            task.completed = true;
            return true;
        }
        return false;
    }
    
    getTasks() {
        return this.tasks;
    }
}" >> src/taskManager.js

git add src/taskManager.js
git commit -m "feat: add completeTask and getTasks methods"
git push origin main
```

**Round 3: Documentation & Testing (Code Reviewers - 2 members)**

*Reviewer 1:*
```bash
git pull origin main

# Add documentation
echo "# API Documentation

## TaskManager Class

### Methods

#### addTask(task)
- **Description**: Adds a new task to the task list
- **Parameters**: 
  - task (string): The task description
- **Returns**: void

#### completeTask(id)
- **Description**: Marks a task as completed
- **Parameters**: 
  - id (number): The task ID
- **Returns**: boolean - true if successful, false if task not found

#### getTasks()
- **Description**: Returns all tasks
- **Returns**: Array of task objects
" > docs/API.md

git add docs/API.md
git commit -m "docs: add API documentation for TaskManager"
git push origin main
```

*Reviewer 2:*
```bash
git pull origin main

# Add basic tests
echo "// Basic tests for TaskManager
const TaskManager = require('../src/taskManager');

// Test 1: Create TaskManager instance
const tm = new TaskManager();
console.log('✓ TaskManager instance created');

// Test 2: Add task
tm.addTask('Learn Git fundamentals');
console.log('✓ Task added successfully');

// Test 3: Get tasks
const tasks = tm.getTasks();
console.log('✓ Tasks retrieved:', tasks.length, 'task(s)');

// Test 4: Complete task
const success = tm.completeTask(tasks[0].id);
console.log('✓ Task completion:', success ? 'SUCCESS' : 'FAILED');

console.log('All tests completed by Group [X]!');
" > tests/taskManager.test.js

git add tests/taskManager.test.js
git commit -m "test: add basic tests for TaskManager functionality"
git push origin main
```

**Round 4: Release Management (Release Manager)**
```bash
git pull origin main

# Create version file
echo "1.0.0" > VERSION
git add VERSION
git commit -m "chore: add version file for release 1.0.0"

# Create release tag
git tag -a v1.0.0 -m "Release v1.0.0: Basic TaskManager with add, complete, and get functionality"
git push origin main
git push origin v1.0.0

# View project history
git log --oneline --graph
```

### 🎯 Learning Check Questions:
1. What's the difference between `git add .` and `git add filename`?
2. Why do we use `git pull` before making changes?
3. What information does `git log --oneline` show us?
4. What's the purpose of the .gitignore file?

---

## 🌿 Activity 2: Branching Challenge (20 minutes)
**Objective**: Master Git branching and merging through parallel development

### Scenario
Your TaskManager needs new features, but you want to develop them safely without breaking the main code.

### Instructions

**Phase 1: Feature Branch Creation (All members create branches)**

*Each member creates their own feature branch:*
- Member 1: `feature/user-authentication`
- Member 2: `feature/task-categories`
- Member 3: `feature/due-dates`
- Member 4: `feature/task-priority`
- Member 5: `feature/search-functionality`
- Member 6: `feature/export-tasks`

```bash
# Each member does this with their assigned feature
git checkout main
git pull origin main
git checkout -b feature/[your-assigned-feature]

# Check which branch you're on
git branch
```

**Phase 2: Parallel Development (10 minutes)**

*Member 1 (User Authentication):*
```bash
echo "class UserAuth {
    constructor() {
        this.users = [];
        this.currentUser = null;
    }
    
    register(username, email) {
        const user = {
            id: Date.now(),
            username,
            email,
            createdAt: new Date()
        };
        this.users.push(user);
        return user;
    }
    
    login(username) {
        const user = this.users.find(u => u.username === username);
        if (user) {
            this.currentUser = user;
            return true;
        }
        return false;
    }
}" > src/userAuth.js

git add src/userAuth.js
git commit -m "feat: add user authentication system"
git push origin feature/user-authentication
```

*Member 2 (Task Categories):*
```bash
# Modify taskManager.js to add categories
echo "
    addTaskWithCategory(task, category = 'general') {
        this.tasks.push({
            id: Date.now(),
            title: task,
            category: category,
            completed: false,
            createdBy: 'Group[X]'
        });
    }
    
    getTasksByCategory(category) {
        return this.tasks.filter(task => task.category === category);
    }
    
    getCategories() {
        return [...new Set(this.tasks.map(task => task.category))];
    }
" >> src/taskManager.js

git add src/taskManager.js
git commit -m "feat: add task categorization functionality"
git push origin feature/task-categories
```

*Member 3 (Due Dates):*
```bash
echo "
    addTaskWithDueDate(task, dueDate) {
        this.tasks.push({
            id: Date.now(),
            title: task,
            dueDate: new Date(dueDate),
            completed: false,
            createdBy: 'Group[X]'
        });
    }
    
    getOverdueTasks() {
        const now = new Date();
        return this.tasks.filter(task => 
            !task.completed && 
            task.dueDate && 
            task.dueDate < now
        );
    }
    
    getTasksDueToday() {
        const today = new Date().toDateString();
        return this.tasks.filter(task => 
            task.dueDate && 
            task.dueDate.toDateString() === today
        );
    }
" >> src/taskManager.js

git add src/taskManager.js
git commit -m "feat: add due date functionality for tasks"
git push origin feature/due-dates
```

*Member 4 (Task Priority):*
```bash
echo "
    addTaskWithPriority(task, priority = 'medium') {
        this.tasks.push({
            id: Date.now(),
            title: task,
            priority: priority, // high, medium, low
            completed: false,
            createdBy: 'Group[X]'
        });
    }
    
    getTasksByPriority(priority) {
        return this.tasks.filter(task => task.priority === priority);
    }
    
    getHighPriorityTasks() {
        return this.tasks.filter(task => 
            task.priority === 'high' && !task.completed
        );
    }
" >> src/taskManager.js

git add src/taskManager.js
git commit -m "feat: add task priority system"
git push origin feature/task-priority
```

*Member 5 (Search Functionality):*
```bash
echo "
    searchTasks(query) {
        const lowercaseQuery = query.toLowerCase();
        return this.tasks.filter(task => 
            task.title.toLowerCase().includes(lowercaseQuery)
        );
    }
    
    searchTasksByStatus(completed) {
        return this.tasks.filter(task => task.completed === completed);
    }
    
    getTaskStats() {
        return {
            total: this.tasks.length,
            completed: this.tasks.filter(t => t.completed).length,
            pending: this.tasks.filter(t => !t.completed).length
        };
    }
" >> src/taskManager.js

git add src/taskManager.js
git commit -m "feat: add search and statistics functionality"
git push origin feature/search-functionality
```

*Member 6 (Export Tasks):*
```bash
echo "
    exportToJSON() {
        return JSON.stringify(this.tasks, null, 2);
    }
    
    exportToCSV() {
        const headers = 'ID,Title,Completed,CreatedBy,CreatedAt\\n';
        const rows = this.tasks.map(task => 
            \`\${task.id},\"\${task.title}\",\${task.completed},\${task.createdBy},\${new Date()}\`
        ).join('\\n');
        return headers + rows;
    }
    
    importFromJSON(jsonData) {
        try {
            const importedTasks = JSON.parse(jsonData);
            this.tasks = [...this.tasks, ...importedTasks];
            return true;
        } catch (error) {
            return false;
        }
    }
" >> src/taskManager.js

git add src/taskManager.js
git commit -m "feat: add export/import functionality for tasks"
git push origin feature/export-tasks
```

**Phase 3: Merge Strategy Discussion (5 minutes)**
Before merging, the team discusses:
1. Which features should be merged first?
2. Which features might conflict with each other?
3. How should we handle conflicts?

**Phase 4: Controlled Merging (5 minutes)**
Repository Owner coordinates the merging:

```bash
# Merge features one by one
git checkout main
git pull origin main

# Merge first feature (usually the least likely to conflict)
git merge feature/user-authentication
git push origin main

# Continue with other features, handling conflicts as they arise
git merge feature/task-categories
# If conflicts occur, resolve them and commit
git push origin main

# Continue with remaining features...
```

### 🎯 Learning Check Questions:
1. What command shows you which branch you're currently on?
2. What happens when you try to merge branches that modify the same file?
3. Why is it important to pull from main before creating a new branch?
4. What's the difference between `git merge` and `git rebase`?

---

## ⚔️ Activity 3: Conflict Resolution Simulation (15 minutes)
**Objective**: Practice handling merge conflicts in a controlled environment

### Scenario
Two team members accidentally worked on the same file simultaneously. Let's learn to resolve conflicts!

### Instructions

**Phase 1: Create Intentional Conflict**

*Member A:*
```bash
git checkout main
git pull origin main
git checkout -b conflict-branch-a

# Modify README.md
echo "# DevOps Task Manager
A collaborative task management application built by Group [X]

## Features
- ✅ Add tasks
- ✅ Complete tasks  
- ✅ User authentication
- ✅ Task categories

## Team Members
- [List all 6 team member names]

## Version: 1.1.0 - Enhanced Features
" > README.md

git add README.md
git commit -m "docs: update README with new features list"
git push origin conflict-branch-a
```

*Member B (simultaneously):*
```bash
git checkout main
git pull origin main
git checkout -b conflict-branch-b

# Modify the same README.md differently
echo "# DevOps Task Manager
A collaborative task management application built by Group [X]

## Overview
This application helps teams manage tasks efficiently with modern features.

## Core Functionality
- Task creation and management
- User authentication system
- Advanced search capabilities
- Export/Import features

## Team Members
- [List all 6 team member names]

## Version: 1.1.0 - Major Update
" > README.md

git add README.md
git commit -m "docs: restructure README with better organization"
git push origin conflict-branch-b
```

**Phase 2: Attempt Merge (Repository Owner)**
```bash
git checkout main
git merge conflict-branch-a  # This will work fine
git push origin main

git merge conflict-branch-b  # This will create a conflict!
```

**Phase 3: Resolve Conflict (Whole Team)**
```bash
# View the conflict
git status
cat README.md

# The file will show conflict markers like:
# <<<<<<< HEAD
# Content from branch A
# =======
# Content from branch B
# >>>>>>> conflict-branch-b

# Team discusses and decides on the best resolution
# Edit README.md to combine the best of both versions
echo "# DevOps Task Manager
A collaborative task management application built by Group [X]

## Overview
This application helps teams manage tasks efficiently with modern features.

## Features
- ✅ Add tasks
- ✅ Complete tasks  
- ✅ User authentication
- ✅ Task categories
- ✅ Advanced search capabilities
- ✅ Export/Import features

## Team Members
- [List all 6 team member names]

## Version: 1.1.0 - Enhanced Features & Major Update
" > README.md

# Stage the resolved file
git add README.md

# Complete the merge
git commit -m "merge: resolve README conflict by combining both versions"
git push origin main

# Clean up branches
git branch -d conflict-branch-a
git branch -d conflict-branch-b
git push origin --delete conflict-branch-a
git push origin --delete conflict-branch-b
```

### 🎯 Learning Check Questions:
1. What do the conflict markers `<<<<<<<`, `=======`, and `>>>>>>>` mean?
2. How do you abort a merge if you're not ready to resolve conflicts?
3. What's the difference between `git merge --abort` and `git reset --hard`?
4. Why is communication important when resolving conflicts?

---

## 📊 Activity 4: Git History Detective (10 minutes)
**Objective**: Master Git log and history analysis commands

### Instructions

**Phase 1: History Analysis Challenge**
Each team member runs different git log commands and shares findings:

```bash
# Member 1: Basic history
git log --oneline
# Question: How many commits has our project had?

# Member 2: Graphical history
git log --graph --oneline --all
# Question: Can you identify where branches were created and merged?

# Member 3: Detailed history
git log --stat
# Question: Which files have been modified the most?

# Member 4: Author analysis
git log --pretty=format:"%h - %an, %ar : %s"
# Question: Who has made the most commits?

# Member 5: File-specific history
git log --oneline -- src/taskManager.js
# Question: How has the main file evolved?

# Member 6: Recent changes
git log --since="1 hour ago" --pretty=format:"%h %s"
# Question: What work was done in the last hour?
```

**Phase 2: Git Blame Investigation**
```bash
# Investigate who wrote what
git blame src/taskManager.js
git blame README.md

# Find when a specific line was added
git log -S "addTask" --oneline
```

**Phase 3: Diff Analysis**
```bash
# Compare current state with previous version
git diff HEAD~1

# Compare two specific commits
git diff v1.0.0 HEAD

# Compare branches (if any exist)
git diff main feature/branch-name
```

### 🎯 Learning Check Questions:
1. What's the difference between `git log` and `git log --oneline`?
2. How can you find out who last modified a specific line in a file?
3. What does `git diff HEAD~1` show you?
4. How would you find all commits that mention "bug" in the commit message?

---

## 🏆 Final Challenge: Team Showcase (10 minutes)
**Objective**: Demonstrate mastery of Day 12 concepts

### Instructions

**Phase 1: Project Summary**
Each group creates a final project summary:

```bash
# Create project summary
echo "# DevOps Task Manager - Final Report
## Group [X] - Git Fundamentals Mastery

### Project Statistics
- Total Commits: $(git rev-list --count HEAD)
- Contributors: 6 team members
- Branches Created: [count from your work]
- Conflicts Resolved: [number you resolved]
- Tags Created: $(git tag | wc -l)

### Features Implemented
$(ls src/ | sed 's/^/- /')

### Git Skills Demonstrated
- ✅ Repository initialization and configuration
- ✅ Basic Git workflow (add, commit, push, pull)
- ✅ Branch creation and management
- ✅ Merge conflict resolution
- ✅ Collaborative development
- ✅ Git history analysis
- ✅ Tagging and releases

### Team Collaboration Highlights
- Successfully collaborated on $(git rev-list --count HEAD) commits
- Resolved merge conflicts as a team
- Implemented parallel feature development
- Maintained clean project history

### Next Steps
- Implement advanced Git workflows (Day 13)
- Set up CI/CD integration (Day 14)
- Explore Git hooks and automation

---
Generated on: $(date)
Repository: $(git remote get-url origin)
" > PROJECT_SUMMARY.md

git add PROJECT_SUMMARY.md
git commit -m "docs: add final project summary and team achievements"
git push origin main

# Create final release tag
git tag -a v1.1.0 -m "Release v1.1.0: Complete Day 12 Git Fundamentals training with team collaboration"
git push origin v1.1.0
```

**Phase 2: Team Presentation (2 minutes per group)**
Each group presents:
1. **Biggest Challenge**: What was the most difficult part?
2. **Key Learning**: What's the most important thing you learned?
3. **Team Collaboration**: How did Git help your team work together?
4. **Git Command MVP**: Which Git command was most useful?

---

## 📋 Assessment Checklist

### Individual Skills ✅
- [ ] Can initialize a Git repository
- [ ] Understands the staging area concept
- [ ] Can create meaningful commit messages
- [ ] Knows how to create and switch branches
- [ ] Can resolve basic merge conflicts
- [ ] Understands git log and history commands

### Team Collaboration Skills ✅
- [ ] Successfully collaborated on shared repository
- [ ] Coordinated parallel development
- [ ] Resolved conflicts through communication
- [ ] Maintained clean project history
- [ ] Used proper Git workflow practices

### Repository Quality ✅
- [ ] Clean commit history
- [ ] Proper .gitignore file
- [ ] Meaningful branch names
- [ ] Good documentation
- [ ] Proper tagging strategy

---

## 🎯 Homework Assignment

**Individual Practice** (Complete before Day 13):
1. Create a personal repository for a small project
2. Practice all commands learned today
3. Create at least 5 meaningful commits
4. Experiment with branching and merging
5. Write a reflection on what you learned

**Group Follow-up** (Optional):
- Continue developing the TaskManager project
- Add more features using proper Git workflow
- Prepare for Day 13 advanced Git topics

---

## 💡 Instructor Notes

### Time Management:
- **Activity 1**: 15 minutes (focus on basic commands)
- **Activity 2**: 20 minutes (emphasize branching)
- **Activity 3**: 15 minutes (conflict resolution is crucial)
- **Activity 4**: 10 minutes (history analysis)
- **Final Challenge**: 10 minutes (consolidation)
- **Total**: 70 minutes + discussion time

### Common Issues to Watch For:
1. **Authentication Problems**: Help with SSH keys/HTTPS tokens
2. **Merge Conflicts**: Guide teams through first conflict resolution
3. **Branch Confusion**: Ensure everyone knows which branch they're on
4. **Commit Message Quality**: Encourage meaningful messages
5. **Collaboration Coordination**: Help teams communicate effectively

### Success Indicators:
- All team members can perform basic Git operations
- Teams successfully resolve at least one merge conflict
- Repository history shows good collaboration patterns
- Students can explain the difference between working directory, staging area, and repository

### Extension Activities (if time permits):
- Explore Git aliases and configuration
- Practice with .gitignore patterns
- Experiment with git stash
- Try different merge strategies

---

*This activity set is designed to be progressive, building from basic concepts to collaborative workflows. Each activity reinforces the Day 12 learning objectives while providing hands-on experience with real-world Git scenarios.*
