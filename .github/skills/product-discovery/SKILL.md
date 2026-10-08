# Product Discovery Skill

This skill teaches how to understand problems, define user needs, and extract clear requirements before building.

---

## When to Use This Skill

Use this skill when:
- Starting work on a new feature
- Requirements are unclear or ambiguous
- Need to understand user problems deeply
- Translating feature requests into actionable requirements
- Validating assumptions before expensive architecture/engineering

**Do NOT use when:**
- Requirement is already crystal clear
- Just refactoring or bug fixing
- Making pure implementation decisions

---

## Core Philosophy

**Validate First, Build Second**

The most expensive mistake is building the wrong thing. Validation is cheaper than rework.

**Know Why Before How**

Understand the problem and user needs before designing solutions. Why beats How.

**Ask More, Assume Less**

Assumptions are dangerous. Questions uncover truth.

---

## Discovery Process

### Phase 1: Surface the Problem (15-30 minutes)

**Goal**: Understand what problem we're solving

**Questions to ask:**

1. **"What problem are we solving?"**
   - Listen for the actual problem, not the proposed solution
   - User says: "We need a dashboard"
   - You ask: "What decisions would you make with a dashboard?"
   - Actual problem: "I spend 3 hours manually checking status of each project"

2. **"Who has this problem?"**
   - Get specific: not "users", but "project managers", "account admins", etc.
   - Different user types may have different problems
   - Example: "Project managers need at-a-glance status; individual contributors don't care"

3. **"How severe is the problem?"**
   - Cost in time, money, or frustration?
   - Example: "It costs $500/month in lost productivity to manually status-check"
   - Helps prioritize features

4. **"Why now?"**
   - What changed? Why is this suddenly important?
   - Example: "We hired 10 new account managers; manual checking doesn't scale"

5. **"What have they tried before?"**
   - Existing solutions or workarounds?
   - Spreadsheets, external tools, manual processes?
   - Example: "We've tried Slack updates, but they're unreliable"

### Phase 2: Understand the User (30-45 minutes)

**Goal**: Know who we're building for

**Questions to ask:**

1. **"Who specifically will use this feature?"**
   - Get specific job titles and scenarios
   - Example: "Project managers checking status in weekly standups"
   - NOT: "Everyone will use it"

2. **"What is their typical workflow?"**
   - When do they use the system?
   - What do they do before/after?
   - Example:
     - Before: Manual check of 20 projects via email
     - During: Login, view status, gather information
     - After: Prepare report for executives

3. **"What are their constraints?"**
   - Time available? Device used? Network quality?
   - Expertise level? Accessibility needs?
   - Example: "They're busy people; need <5 minute check"

4. **"What does success look like for them?"**
   - How would they know if the feature works?
   - Example: "I can see all 20 projects at once, understand status, in <2 minutes"

5. **"What frustrates them about current state?"**
   - Pain points reveal priorities
   - Example: "No central view; have to check email, Jira, Slack separately"

### Phase 3: Define the User Journey (30-45 minutes)

**Goal**: Map out step-by-step what the user does

**Create a flowchart:**

```
Happy Path:
1. User needs to know project status
2. User logs into system
3. User navigates to status dashboard
4. User sees all projects with status
5. User understands priorities at a glance
6. User has information needed for meeting

Error Cases:
- User has no projects → Show empty state
- Page takes too long → Show spinner, explain wait
- User loses internet → Show error, suggest retry
- User doesn't understand a status → Show help tooltip
```

**Document:**
- Starting point (what triggers this journey)
- Happy path (step-by-step)
- Error cases (what could go wrong)
- End state (what has the user achieved)
- Time budget (how long should it take)

### Phase 4: Extract Acceptance Criteria (30-45 minutes)

**Goal**: Define testable requirements

**Key: Criteria must be TESTABLE**

❌ Not testable:
- "Dashboard looks good"
- "Users can see their projects"
- "Performance is acceptable"

✅ Testable:
- "Dashboard shows all projects owned by user within 5 seconds"
- "Each project shows: name, due date, status color (green/yellow/red)"
- "Unauthorized users get 401 error"

**Structure:**

```markdown
## Must Have (Feature is incomplete without these)
- [ ] User can navigate to dashboard
- [ ] Dashboard shows all projects owned by user
- [ ] Each project shows: Name, Due Date, Status
- [ ] Status shows as color: Green=On Track, Yellow=At Risk, Red=Blocked
- [ ] Dashboard loads within 5 seconds
- [ ] Works on desktop and mobile

## Should Have (Nice to have; can defer)
- [ ] User can customize columns
- [ ] User can sort projects

## Nice to Have (Extra polish; can ship v2)
- [ ] Real-time updates when status changes
- [ ] Export dashboard as PDF
```

### Phase 5: Identify Constraints (15-30 minutes)

**Goal**: Understand what limits us

**Categories of constraints:**

**Technical:**
- "Must work with existing database"
- "No new backend infrastructure"
- "Must support 10,000+ projects"

**Business:**
- "Ship within 2 weeks"
- "Cannot cost more than $500/month in infrastructure"
- "Cannot distract from existing features"

**Compliance/Security:**
- "Must comply with GDPR"
- "Cannot expose other users' projects"
- "Cannot log sensitive data"

**User/UX:**
- "Must work on mobile (3G connection)"
- "Must be accessible (WCAG AA)"
- "Requires <2 minutes training"

### Phase 6: Document Non-Goals (15 minutes)

**Goal**: Prevent scope creep

**Explicitly state what you're NOT doing:**

- "We are NOT implementing real-time updates (V1)"
- "We are NOT exporting to PDF (V1)"
- "We are NOT supporting team managers (individual managers only, V1)"
- "We are NOT integrating with external tools (V1)"

**Why:** Prevents the "but you should also..." conversations. Clear boundaries protect scope.

### Phase 7: Surface Risks & Assumptions (15-30 minutes)

**Goal**: Identify what's uncertain

**Risks:**
- "Large CSV generation might timeout"
- "Users might expect real-time updates"
- "Authorization logic might be complex"

**Assumptions:**
- "We assume users have 1 browser tab open"
- "We assume projects are already tagged with status"
- "We assume user can interpret color codes"

**Document both.** Risks get mitigated in architecture. Assumptions get validated during implementation.

---

## Discovery Conversation Template

Use this structure to guide discovery:

```markdown
# Feature Discovery: [Feature Name]

## Problem
[What problem are we solving? Why now? Who has it?]

## Target User
[Specific user persona]
- Role: [Job title]
- Context: [When/where/why they'd use this]
- Constraints: [Time pressure, device, expertise]

## User Journeys

### Journey 1: [Happy Path]
1. [User action]
2. [System response]
3. [User action]
...
Result: [User achieves goal]

### Journey 2: [Error Case]
1. [User action]
2. [Error occurs]
3. [System shows recovery]
Result: [User can proceed or understand issue]

## Acceptance Criteria

### Must Have
- [ ] [Testable criterion 1]
- [ ] [Testable criterion 2]

### Should Have
- [ ] [Testable criterion 3]

### Non-Goals
- [Not doing X]
- [Not doing Y]

## Constraints
- Technical: [X]
- Business: [Y]
- Compliance: [Z]

## Risks & Assumptions
- Risk: [X] → Mitigation: [Y]
- Assumption: [Z] → Validation: [How we'll verify]

## Next Steps
1. [Stakeholder review]
2. [Architecture feasibility check]
3. [Implementation]
```

---

## Common Discovery Mistakes to Avoid

### ❌ Mistake 1: Accepting the Solution Instead of Understanding the Problem

**Bad conversation:**
- User: "We need a dashboard"
- You: "OK, I'll build a dashboard"

**Better conversation:**
- User: "We need a dashboard"
- You: "What problem does a dashboard solve?"
- User: "I need to know the status of all projects"
- You: "How do you check status now?"
- User: "I check email, Jira, and ask people individually"
- You: "What would be ideal?"
- User: "One place to see all project status"

**Result:** The solution is "status view", but it might not be a full dashboard. Might be a list, or a sidebar widget.

### ❌ Mistake 2: Assuming You Know the Problem

**Bad:**
- "They definitely want real-time updates"
- "This is obviously for mobile"
- "They need the full data export"

**Better:**
- "Do you need real-time updates or is hourly fine?"
- "How often do you need this while on the go?"
- "Which specific data do you need to export?"

### ❌ Mistake 3: Vague Acceptance Criteria

**Bad:**
- "Dashboard looks good"
- "Performance is acceptable"
- "Easy to use"

**Better:**
- "Dashboard shows all projects within 5 seconds"
- "Response time <1 second for loading additional projects"
- "First-time user completes task in <2 minutes without help"

### ❌ Mistake 4: Forgetting Edge Cases

**Bad:**
- Only define happy path
- Ignore errors: "Assume data is always correct"
- Ignore empty state: "Assume users have data"

**Better:**
- Define happy path + 3-5 error cases
- "What if CSV is empty?"
- "What if user loses internet mid-export?"
- "What if user has 0 projects?"

### ❌ Mistake 5: Not Documenting Non-Goals

**Bad:**
- Build feature, discover later that client wanted something else
- Scope expands during implementation

**Better:**
- Document non-goals up front
- "We are NOT [X] in this version"
- Protects scope

### ❌ Mistake 6: Missing Constraints

**Bad:**
- "We'll make it work" (later: security issues, performance problems)
- "We'll figure out the database" (later: schema redesign)

**Better:**
- Identify constraints early
- "Must work with existing PostgreSQL"
- "Must support 10,000+ projects"
- "Must be GDPR compliant"

---

## Discovery Output Checklist

A discovery is complete when you have:

✅ **Clear problem statement** — Not a solution, but a problem  
✅ **Specific user** — Not "users" but actual persona  
✅ **User journey** — Happy path + error cases  
✅ **Testable acceptance criteria** — Each can be verified  
✅ **Non-goals** — Scope boundaries  
✅ **Constraints** — Technical, business, compliance, UX  
✅ **Risks documented** — Known uncertainties  
✅ **Assumptions explicit** — Things we're betting on  
✅ **Stakeholder review** — Key people have reviewed  
✅ **Clarity** — Any developer could read this and understand what to build  

---

## Examples: Good vs. Bad Discovery

### Example 1: Export Feature

**Bad Discovery:**
```
"Feature: Export"
"We need to export data"
```
→ What data? To what format? Why? When? Who?

**Good Discovery:**
```markdown
# Feature: Export Projects to CSV

## Problem
Project managers need to share project data in Excel.
Currently they copy-paste manually; error-prone and time-consuming.

## Target Users
Project managers (need to share data with executives)

## User Journey
1. Manager opens Projects page
2. Clicks "Export" button
3. CSV downloads
4. Manager opens in Excel
5. Manager shares with executives

## Acceptance Criteria
- [ ] Clicking export generates CSV
- [ ] CSV includes: Name, Description, Due Date, Status
- [ ] Only user's own projects included
- [ ] Downloaded as "projects-YYYY-MM-DD.csv"
- [ ] Works on desktop and mobile

## Non-Goals
- NOT real-time updates
- NOT scheduled exports
- NOT importing CSV back into system

## Constraints
- Must work with existing RLS (security)
- Must complete within 5 seconds
```

### Example 2: Dashboard Feature

**Bad Discovery:**
```
"Users want a dashboard"
"Make it pretty"
```

**Good Discovery:**
```markdown
# Feature: Project Status Dashboard

## Problem
Project managers check project status in weekly standups.
Currently they manually check each project one-by-one via email.
Takes 30+ minutes for 20 projects.

## Target Users
Project managers in weekly standup meetings (time pressure, need quick overview)

## User Journey: Get Status Overview
1. Manager opens dashboard
2. Sees all their projects in one view
3. Each project shows status color (green/yellow/red)
4. Can quickly identify projects at risk
5. Has information for standup (5-minute task)

## User Journey: Drill Into Project
1. Manager sees red project
2. Clicks project name
3. Sees project details and history
4. Understands why it's at risk

## Acceptance Criteria
- [ ] Dashboard shows all projects owned by user
- [ ] Each project shows: Name, Due Date, Status Color
- [ ] Status is accurate (updates when project status changes)
- [ ] Loading time <5 seconds
- [ ] Works on desktop and mobile
- [ ] User can understand status colors without training
- [ ] Clicking project shows details

## Non-Goals
- NOT real-time updates (hourly refresh is fine)
- NOT supporting team managers (individual managers only)
- NOT exporting dashboard

## Constraints
- Must work with existing database
- Must respect RLS (users only see own projects)
- Must support 10,000+ projects efficiently
- Must be WCAG AA accessible
```

---

## Quick Discovery Checklist

When you're unsure if discovery is done, ask:

1. **Can a developer read this and build it without asking questions?**
   - YES → Ready
   - NO → More discovery needed

2. **Does it answer: Why? Who? When? Where? What?**
   - YES → Ready
   - NO → More discovery needed

3. **Are acceptance criteria testable?**
   - YES → Ready
   - NO → Rewrite criteria more specifically

4. **Are non-goals explicit?**
   - YES → Ready
   - NO → Document what you're NOT doing

5. **Have stakeholders reviewed and approved?**
   - YES → Ready
   - NO → Get approval before proceeding

If any answer is NO, do more discovery.

---

## When Discovery is NOT Needed

✅ **Bug fixes:** Already know the problem  
✅ **Refactoring:** Implementation detail, not a feature  
✅ **Minor UI tweaks:** Clear what needs to change  
✅ **Performance optimization:** Known constraint to address  

❌ **New features:** Always do discovery  
❌ **User-facing changes:** Do discovery to validate  
❌ **Integrations:** Discovery to understand requirements  
❌ **Policy/process changes:** Discovery to understand impact  

---

## Tools for Discovery

**Conversations:**
- 1-on-1 with stakeholder
- Group discussion with users
- Phone call, Slack, email thread

**Documents:**
- Google Docs / Notion for collaborative editing
- Requirement templates (from this skill)
- User journey diagrams (draw.io, Miro, paper)

**Validation:**
- Prototype/mockup to confirm understanding
- User interviews to validate assumptions
- Analytics to confirm problem severity

---

## Sign-Off

Discovery is ready for architecture when:

```markdown
# Discovery Sign-Off

Product Agent: ✅ Discovery complete
Stakeholder:   ✅ Requirement approved
Assumptions:   ✅ Documented
Non-Goals:     ✅ Clear
Acceptance:    ✅ Testable

Ready for → Architecture Phase
```
