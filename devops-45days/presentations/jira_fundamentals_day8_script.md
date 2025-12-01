# Jira Fundamentals - Day 8 Training Script
## Tool Administration: Project Management Made Simple

### Training Overview
**Duration:** Full Day (8 hours)  
**Target Audience:** DevOps professionals, project managers, team leads  
**Prerequisites:** Basic understanding of project management concepts  
**Training Period:** 23rd July - 19th September, 2025

---

## 🎯 Learning Objectives

By the end of this session, participants will be able to:

1. **Understand Jira Fundamentals**
   - Navigate the Jira interface confidently
   - Understand key terminology and concepts
   - Identify different project types and their use cases

2. **Create and Configure Projects**
   - Set up projects from scratch
   - Configure project settings and components
   - Organize projects using categories

3. **Master Board Configuration**
   - Configure Kanban boards for continuous workflow
   - Set up Scrum boards for sprint-based development
   - Customize columns, swimlanes, and filters

4. **Manage Users and Permissions**
   - Add and manage user accounts
   - Configure permission schemes
   - Set up groups and project roles

---

## 📋 Session 1: Introduction to Jira (90 minutes)

### What is Jira?

**Jira** is a powerful project management and issue tracking tool developed by Atlassian that helps teams plan, track, and manage their work efficiently from start to finish.

#### Key Concepts to Explain:

1. **The "Issue" Concept**
   - Everything in Jira is an "Issue" - the building block of all work
   - Types of issues:
     - 🐛 **Bug:** Something that's broken and needs fixing
     - ✨ **Feature:** New functionality to be developed
     - ✅ **Task:** General work that needs to be completed
     - 📖 **Story:** User requirement or feature from user perspective

2. **What Jira Does**
   - **Issue Tracking:** Monitor bugs, tasks, and user stories
   - **Project Management:** Plan and organize work effectively
   - **Team Collaboration:** Enable seamless teamwork
   - **Workflow Management:** Automate business processes
   - **Reporting:** Generate insights and analytics
   - **Integration:** Connect with development and business tools

3. **Why Teams Choose Jira**
   - **Flexibility:** Adapts to any workflow or methodology
   - **Scalability:** Works for small teams to large enterprises
   - **Customization:** Tailored to specific organizational needs
   - **Visibility:** Clear project status and progress tracking
   - **Collaboration:** Keeps everyone aligned and informed
   - **Reliability:** Trusted by millions of users worldwide

#### Real-World Example:
*"Imagine you're building a mobile app. You might have:*
- *Story: 'As a user, I want to login with my email'*
- *Task: 'Design the login screen'*
- *Bug: 'Login button doesn't work on iOS'*
- *Feature: 'Add social media login options'"*

### Jira Interface Overview

#### Main Navigation Areas:

1. **Top Navigation Bar**
   - **Jira Logo:** Home button
   - **Your Work:** Items assigned to you
   - **Projects:** All accessible projects
   - **Filters:** Saved searches and queries
   - **Dashboards:** Custom overview screens
   - **Apps:** Additional tools and integrations

2. **Project Sidebar**
   - **Backlog:** Planned work items
   - **Active Sprints:** Current sprint work
   - **Board:** Visual workflow representation
   - **Reports:** Analytics and insights
   - **Issues:** All project items
   - **Settings:** Project configuration

#### Pro Navigation Tips:
- **Keyboard Shortcuts:** Press "?" to see all available shortcuts
- **Quick Search:** Use "/" to quickly search for issues
- **Breadcrumbs:** Always visible at top to show current location
- **Recent Items:** Access recently viewed projects and issues

### Essential Jira Terminology

#### Core Concepts:
- **Issue:** Any piece of work - bug, task, story, or feature
- **Project:** Collection of issues for a specific goal or team
- **Workflow:** The path an issue takes from creation to completion
- **Board:** Visual representation of your team's work

#### People & Roles:
- **Assignee:** Person responsible for working on the issue
- **Reporter:** Person who created or reported the issue
- **Watcher:** Person who wants to be notified of changes
- **Project Lead:** Person responsible for the overall project

#### Agile Terms:
- **Backlog:** List of work items waiting to be done
- **Sprint:** Time-boxed period for completing work (usually 1-4 weeks)
- **Epic:** Large piece of work that can be broken into smaller stories
- **Story Points:** Estimation unit for measuring work complexity

#### Configuration Terms:
- **Scheme:** Configuration template (workflow, permission, etc.)
- **Component:** Subsection of a project (e.g., Frontend, Backend)
- **Version:** Release or milestone marker
- **Label:** Flexible tag for categorizing issues

#### Status Categories:
- 📝 **To Do:** Work not yet started
- ⚡ **In Progress:** Work currently being done
- ✅ **Done:** Work completed

---

## 📋 Session 2: Project Types and Templates (60 minutes)

### Understanding Project Types

Different teams work differently, so Jira offers various project types to match your team's workflow, methodology, and specific needs.

#### 1. Scrum Project 🏃‍♂️
**Best for:** Teams using Scrum methodology

**Features:**
- Sprint planning and management
- Backlog prioritization
- Burndown charts and reports
- Story point estimation
- Sprint reviews and retrospectives

**Perfect for:** Development teams, Product teams

#### 2. Kanban Project 📊
**Best for:** Continuous flow of work

**Features:**
- Visual workflow management
- Work-in-progress limits
- Continuous delivery
- Flexible prioritization
- Cumulative flow diagrams

**Perfect for:** Support teams, Operations teams

#### 3. Bug Tracking Project 🐛
**Best for:** Issue and bug management

**Features:**
- Bug reporting and tracking
- Issue prioritization
- Resolution workflows
- Quality assurance
- Customer support integration

**Perfect for:** QA teams, Support teams

#### 4. Business Project 📈
**Best for:** Non-technical teams

**Features:**
- Task management
- Process workflows
- Team collaboration
- Simple reporting
- Goal tracking

**Perfect for:** Marketing, HR, Finance teams

### Quick Decision Guide

**Choose Scrum if:**
- You work in fixed-length sprints
- You need backlog management
- You do sprint planning meetings
- You want burndown charts

**Choose Kanban if:**
- Work flows continuously
- Priorities change frequently
- You want to limit work-in-progress
- You need flexible workflows

### Project Templates and Workflows

#### What are Templates?
Templates are pre-configured project setups that include:
- **Issue Types:** Bug, Story, Task, Epic, etc.
- **Workflows:** Status transitions and rules
- **Screens:** Fields shown when creating/editing
- **Permissions:** Who can do what
- **Notifications:** Email and alert settings
- **Board Configuration:** Columns and swimlanes

#### Understanding Workflows
A workflow defines the path an issue takes from creation to completion:

```
📝 To Do → ⚡ In Progress → ✅ Done
```

Each transition can have:
- **Conditions:** Who can perform the transition
- **Validators:** Required fields or checks
- **Post-functions:** Automatic actions after transition

---

## 🛠️ Session 3: Hands-On Project Creation (90 minutes)

### Pre-Creation Planning

Before creating a project, consider:

#### Project Information Needed:
- **Project Name:** Clear, descriptive name
- **Project Key:** Short abbreviation (3-10 characters)
- **Project Type:** Based on your workflow
- **Template:** Starting configuration
- **Lead:** Project administrator
- **Description:** Project purpose and scope

#### Pre-Creation Checklist:
- **Project Purpose:** What will this project track?
- **Team Members:** Who needs access?
- **Workflow Type:** Scrum, Kanban, or other?
- **Issue Types:** What work will you track?
- **Permissions:** Who can do what?
- **Integration Needs:** Other tools to connect?

### Step-by-Step Project Creation

#### Step 1: Access Project Creation
- Navigate to **Projects → Create Project**
- Or use the "+" button in the top navigation

#### Step 2: Choose Project Type
- Select from Scrum, Kanban, Bug Tracking, or Business project
- Consider your team's methodology and needs

#### Step 3: Select Template
- Choose a template that matches your workflow
- Start with basic template if unsure

#### Step 4: Configure Details
- Enter project name and key
- Add description
- Choose project lead
- Set access settings

#### Step 5: Review and Create
- Double-check all settings
- Click "Create" to generate your new project

#### Step 6: Initial Configuration
- Set up boards
- Add team members
- Customize workflows as needed

### Project Key Best Practices

#### ✅ Good Project Keys:
- **WEBAPP** - Web Application
- **MOBILE** - Mobile App Project
- **SUPPORT** - Customer Support
- **INFRA** - Infrastructure Team

#### ❌ Avoid These:
- **PROJ1** - Too generic
- **TEST** - Confusing purpose
- **ABC** - No meaning
- **VERYLONGPROJECTKEY** - Too long

### Project Settings and Configuration

#### Essential Settings:

**Project Details:**
- Name & Description: Clear project identity
- Project Lead: Primary administrator
- Default Assignee: Who gets unassigned issues
- Avatar: Visual project identifier

**Access Control:**
- Access Level: Open, restricted, or private
- Permission Scheme: Who can do what
- Issue Security: Sensitive issue handling

#### Components and Versions

**Components (Project Subsections):**
- **Frontend:** UI/UX related work
- **Backend:** Server-side development
- **Database:** Data layer issues
- **Documentation:** User guides, specifications

**Versions (Release Tracking):**
- **v1.0:** Initial release
- **v1.1:** Bug fix release
- **v2.0:** Major feature release
- **Future:** Planned features

#### Configuration Best Practices:

**✅ Do This:**
- Start with simple configurations
- Involve team in decision making
- Document configuration choices
- Test changes in a safe environment
- Train team on new configurations

**❌ Avoid This:**
- Over-complicating initial setup
- Making changes without team input
- Frequent configuration changes
- Ignoring user feedback
- Not backing up configurations

---

## 📊 Session 4: Board Configuration (120 minutes)

### Introduction to Jira Boards

Boards are visual representations of your team's work that help you:
- Track progress visually
- Identify bottlenecks quickly
- Manage workflow efficiently
- Enable team collaboration

#### Board Components:
- **Columns:** Represent workflow stages (To Do, In Progress, Done)
- **Cards:** Individual issues displayed as moveable items
- **Swimlanes:** Horizontal groupings (by assignee, priority, etc.)

### Configuring Kanban Boards

#### Step-by-Step Kanban Configuration:

1. **Create or Access Board**
   - Go to your project → Boards → Create Board
   - Select existing Kanban board

2. **Configure Columns**
   - Board Settings → Columns
   - Add, remove, or modify columns to match workflow

3. **Set Column Constraints**
   - Configure minimum/maximum limits for each column
   - Control work-in-progress (WIP)

4. **Configure Swimlanes**
   - Set up horizontal groupings
   - Options: assignee, priority, epic, custom fields

5. **Set Up Filters**
   - Define which issues appear on board
   - Use JQL (Jira Query Language)

6. **Customize Card Layout**
   - Choose which fields to display on issue cards
   - Quick information access

#### Common Column Setups:
- **Basic:** To Do → In Progress → Done
- **Development:** Backlog → Development → Testing → Done
- **Support:** New → Investigating → Waiting → Resolved
- **Marketing:** Ideas → Planning → Creating → Review → Published

#### Swimlane Options:
- **Assignee:** Group by person responsible
- **Priority:** High, Medium, Low priority lanes
- **Epic:** Group by larger work items
- **Component:** Frontend, Backend, etc.
- **Issue Type:** Stories, Bugs, Tasks
- **Custom Field:** Team, Client, etc.

#### Work-in-Progress (WIP) Limits

**Why Use WIP Limits?**
- Prevent team overload
- Identify bottlenecks quickly
- Improve focus and quality
- Encourage collaboration
- Reduce context switching

**Setting WIP Limits:**
- **Start Conservative:** Begin with lower limits
- **Team Size Based:** Usually 1-2 items per person
- **Column Specific:** Different limits per column
- **Monitor & Adjust:** Refine based on experience

### Configuring Scrum Boards

#### Scrum Board Features:
- **Backlog Management:** Prioritized list of work
- **Sprint Planning:** Drag issues into sprints
- **Sprint Board:** Active sprint visualization
- **Burndown Charts:** Progress tracking
- **Story Points:** Effort estimation
- **Sprint Reports:** Detailed analytics
- **Velocity Tracking:** Team performance metrics

#### Board Views:

**Backlog View:**
- Product backlog prioritization
- Sprint planning interface
- Story point estimation
- Epic and version management

**Active Sprint View:**
- Current sprint progress
- Drag-and-drop status updates
- Sprint burndown chart
- Team workload visibility

#### Scrum Board Configuration Steps:

1. **Create Scrum Board**
   - Project → Boards → Create Board → Choose Scrum template

2. **Configure Columns**
   - Set up workflow columns (To Do, In Progress, Done)
   - Map to statuses

3. **Set Up Estimation**
   - Configure story points or time-based estimation
   - For sprint planning

4. **Configure Sprints**
   - Set default sprint duration
   - Configure sprint settings

5. **Customize Card Fields**
   - Choose which fields to display on issue cards
   - (assignee, story points, etc.)

6. **Set Up Reports**
   - Configure burndown charts
   - Other sprint reports

#### Sprint Planning Configuration:

**Estimation Setup:**
- **Story Points:** Fibonacci sequence (1,2,3,5,8,13)
- **Time Tracking:** Hours or days
- **T-Shirt Sizes:** XS, S, M, L, XL
- **Custom Scale:** Define your own values

**Sprint Settings:**
- **Duration:** 1-4 weeks (2 weeks common)
- **Start Day:** Monday, Tuesday, etc.
- **Working Days:** Exclude weekends/holidays
- **Capacity:** Team velocity planning

#### Scrum Board Best Practices:

**✅ Do This:**
- Keep sprint duration consistent
- Involve team in estimation
- Review velocity regularly
- Use burndown charts for daily standups
- Maintain a well-groomed backlog

**❌ Avoid This:**
- Changing sprint scope mid-sprint
- Ignoring velocity trends
- Over-committing in sprint planning
- Skipping retrospectives
- Not updating story points

---

## 👥 Session 5: User Management and Permissions (90 minutes)

### User Management Overview

Proper user management ensures:
- Right people have access to right projects
- Appropriate permissions for each role
- Security and organized workflows
- Effective collaboration

#### User Types in Jira:

**Licensed Users:**
- **Jira Software Users:** Full access to software features
- **Jira Core Users:** Basic project management
- **Jira Service Management:** Service desk access

**Special User Types:**
- **Administrators:** System-wide control
- **Project Admins:** Project-level control
- **Customers:** Limited portal access

#### User Management Levels:

**Global Level:**
- System administration
- User account creation
- Global permissions
- License management

**Project Level:**
- Project access control
- Role assignments
- Project-specific permissions
- Team member management

### Adding and Managing Users

#### Adding Users Process:

1. **Access User Management**
   - Settings → User Management

2. **Create User**
   - Click "Create User" button

3. **Enter Details**
   - Email, full name, username

4. **Set Password**
   - Temporary or permanent

5. **Assign Groups**
   - Add to relevant groups

6. **Send Invitation**
   - Email notification to user

#### Managing Existing Users:
- **Edit Profile:** Update user information
- **Reset Password:** Help with login issues
- **Deactivate User:** Temporarily disable access
- **Change Groups:** Modify permissions
- **View Activity:** Monitor user actions
- **Delete User:** Permanent removal (use carefully!)

### Permissions and Security

#### Understanding Jira Permissions

Jira uses a multi-layered permission system:

1. **Global Permissions:** System-wide access control
2. **Project Permissions:** Project-specific access
3. **Issue Security:** Individual issue access

#### Permission Types:

| Permission | Description | Typical Users | Risk Level |
|------------|-------------|---------------|------------|
| Browse Projects | View project and its issues | All team members | Low |
| Create Issues | Add new issues to project | Team members, stakeholders | Low |
| Edit Issues | Modify issue details | Assignees, project members | Medium |
| Delete Issues | Permanently remove issues | Project leads, admins | High |
| Administer Projects | Manage project settings | Project administrators | High |

#### Groups and Roles:

**Groups (Global):**
- **jira-administrators:** Full system access
- **jira-software-users:** Software license holders
- **jira-core-users:** Basic license holders
- **developers:** Custom development team
- **managers:** Custom management group

**Project Roles:**
- **Administrators:** Project management
- **Developers:** Development team
- **Users:** General project access
- **Viewers:** Read-only access
- **Custom Roles:** Specific to needs

#### Security Best Practices:
- **Least Privilege:** Grant minimum necessary permissions
- **Regular Audits:** Review permissions quarterly
- **Group Management:** Use groups instead of individual permissions
- **Role Clarity:** Clearly define what each role can do
- **Documentation:** Document permission decisions and changes
- **Testing:** Test permission changes in safe environment

---

## 🎯 Session 6: Hands-On Exercise - Complete Project Setup (90 minutes)

### Exercise Scenario

**Scenario:** You're setting up a Jira project for a new mobile app development team. The team consists of 2 developers, 1 designer, 1 QA tester, and 1 project manager. They want to use Scrum methodology with 2-week sprints.

### Part 1: Project Creation (15 minutes)

#### Tasks:
1. **Create Project:**
   - Name: "Mobile App Development"
   - Key: "MOBILE"
   - Type: Scrum
   - Template: Scrum template

2. **Configure Project Details:**
   - Add project description
   - Set project avatar
   - Configure default assignee

3. **Set Up Components:**
   - Frontend (iOS/Android)
   - Backend (API)
   - Design (UI/UX)
   - Testing (QA)

### Part 2: Board Configuration (15 minutes)

#### Tasks:
1. **Configure Scrum Board:**
   - Set up columns: To Do, In Progress, Review, Done
   - Map columns to workflow statuses
   - Configure card layout (show assignee, story points)

2. **Set Up Estimation:**
   - Enable story points
   - Use Fibonacci sequence (1,2,3,5,8,13)
   - Configure sprint duration (2 weeks)

3. **Create Sample Issues:**
   - 2 Epics (User Authentication, Core Features)
   - 5 User Stories
   - 3 Tasks
   - 2 Bugs

### Part 3: User Management (10 minutes)

#### Tasks:
1. **Create User Groups:**
   - mobile-developers
   - mobile-designers
   - mobile-qa
   - mobile-managers

2. **Add Team Members:**
   - Create 5 test users
   - Assign to appropriate groups
   - Set project roles

3. **Configure Permissions:**
   - Developers: Create, Edit, Assign issues
   - QA: Create, Edit issues, Resolve
   - Manager: All permissions
   - Designer: Create, Edit issues

### Part 4: Testing & Validation (10 minutes)

#### Tasks:
1. **Test Board Functionality:**
   - Move issues between columns
   - Create and start a sprint
   - View burndown chart

2. **Validate Permissions:**
   - Test different user access levels
   - Verify group memberships
   - Check project visibility

3. **Review Configuration:**
   - Verify all components are set up
   - Check board configuration
   - Confirm user assignments

### Success Criteria:

**✅ Project Setup Complete:**
- Project created with correct details
- Components configured
- Sample issues created
- Project accessible to team

**✅ Team Ready to Work:**
- Board configured for Scrum workflow
- Users added with correct permissions
- Sprint can be created and started
- Issues can be moved through workflow

### Exercise Tips:
- **Work in Pairs:** Collaborate with a partner for better learning
- **Ask Questions:** Don't hesitate to ask for help
- **Take Notes:** Document any challenges or insights
- **Experiment:** Try different configurations to see what works
- **Share Results:** Compare your setup with others

---

## 📚 Session 7: Best Practices and Troubleshooting (45 minutes)

### Configuration Best Practices

#### Project Organization:
- **Start Simple:** Begin with basic configurations and add complexity gradually
- **User Input:** Ask teams how they naturally group their work
- **Consistency:** Use consistent naming conventions across categories
- **Documentation:** Document the purpose and scope of each category
- **Training:** Help users understand the category structure

#### Board Configuration:
- **Start Simple:** Begin with basic columns and add complexity gradually
- **Team Input:** Involve the team in board design decisions
- **Regular Review:** Periodically assess and adjust board configuration
- **Test Changes:** Make incremental changes and monitor impact
- **Document Decisions:** Keep track of why certain configurations were chosen

#### User Management:
- **Principle of Least Privilege:** Give users minimum necessary access
- **Regular Audits:** Review user access periodically
- **Deactivate vs Delete:** Deactivate users who might return
- **Group Management:** Use groups instead of individual permissions
- **Onboarding Process:** Standardize new user setup

### Common Issues and Solutions

#### Issue: Users Can't See Project
**Solution:**
- Check project permissions
- Verify user group membership
- Confirm project access level

#### Issue: Board Not Showing Issues
**Solution:**
- Check board filter (JQL)
- Verify issue status mapping
- Confirm user has browse permission

#### Issue: Can't Move Issues on Board
**Solution:**
- Check workflow transitions
- Verify user has transition permission
- Confirm issue status mapping

#### Issue: Sprint Planning Not Working
**Solution:**
- Verify estimation is configured
- Check backlog permissions
- Confirm sprint settings

---

## 🎉 Session 8: Summary and Next Steps (30 minutes)

### What You've Accomplished Today

**Skills Mastered:**
- **Jira Fundamentals:** Interface, terminology, concepts
- **Project Types:** Scrum, Kanban, Bug Tracking, Business
- **Project Creation:** Setup, configuration, organization
- **Board Configuration:** Kanban and Scrum board setup
- **User Management:** Adding users, groups, permissions
- **Security:** Permission schemes, access control

**Practical Experience:**
- **Created:** Complete project from scratch
- **Configured:** Scrum board with proper workflow
- **Organized:** Components and project structure
- **Managed:** Users, groups, and permissions
- **Tested:** End-to-end functionality
- **Validated:** Security and access controls

### Key Takeaways

- **Start Simple:** Begin with basic configurations and add complexity gradually
- **User-Centric:** Always consider the end-user experience in your configurations
- **Security First:** Implement proper permissions and access controls from the start
- **Iterate and Improve:** Regularly review and refine your Jira setup
- **Documentation:** Keep track of configurations and decisions for future reference
- **Team Collaboration:** Involve your team in Jira setup and configuration decisions

### Coming Up: Days 9 & 10

**Day 9: Advanced Jira Administration**
- Custom workflows and automation
- Advanced reporting and dashboards
- Jira integrations and apps
- Performance optimization
- Backup and maintenance

**Day 10: Enterprise Jira & Best Practices**
- Scaling Jira for large organizations
- Advanced security configurations
- Compliance and governance
- Troubleshooting common issues
- Migration and upgrade strategies

### Action Items

1. **Continue Learning:** Practice with your own projects and explore advanced features
2. **Share Knowledge:** Help colleagues and team members with Jira setup and best practices
3. **Apply Skills:** Implement what you've learned in real projects and workflows

---

## 📖 Additional Resources

### Documentation Links:
- [Atlassian Jira Documentation](https://confluence.atlassian.com/jira)
- [Jira Administrator's Guide](https://confluence.atlassian.com/adminjiraserver)
- [Agile Project Management](https://www.atlassian.com/agile)

### Training Materials:
- Atlassian University courses
- Community forums and discussions
- Video tutorials and webinars

### Practice Environments:
- Atlassian Cloud free tier
- Local Jira instance for testing
- Sandbox environments

---

**Prepared by:** Rashi Rana (Corporate Trainer)  
**Training Period:** 23rd July - 19th September, 2025  
**Contact:** [Training Support Information]

---

*This script provides a comprehensive foundation for delivering effective Jira fundamentals training. Adapt the content, timing, and exercises based on your specific audience and organizational needs.*
