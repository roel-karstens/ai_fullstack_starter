# Start a New Feature

Use this prompt to discover and prepare a new feature for implementation.

## Input

**You have:**
- A feature idea or user request
- (Optional) Initial stakeholder discussion

**Example:**
"Users want to export projects to CSV"

## Workflow

### Step 1: Activate Product Agent

Ask the Product Agent to conduct discovery using the [Product Discovery Skill](./../skills/product-discovery/SKILL.md).

**You say to Product Agent:**
```
Help me discover this feature:
[Feature request or idea]

Use the Product Discovery Skill to:
1. Understand the problem (not just the solution)
2. Identify the target user
3. Map user journeys (happy path + errors)
4. Extract testable acceptance criteria
5. Document constraints
6. Surface risks and assumptions
7. Produce a complete requirement document
```

### Step 2: Validate Requirement Document

Product Agent delivers a complete requirement covering:
- Clear problem statement
- Specific user persona
- User journeys
- Testable acceptance criteria
- Non-goals (scope boundaries)
- Constraints (technical, business, compliance)
- Risks and assumptions

**You review:**
- Does this match what I was asking for?
- Are acceptance criteria clear and testable?
- Are non-goals preventing scope creep?
- Can a developer read this and understand what to build?

**If NO:** Send back to Product Agent for refinement

**If YES:** Proceed to Gate 1

### Step 3: Get Stakeholder Approval (Gate 1)

Review the requirement with relevant stakeholders:
- Product owner
- Subject matter expert
- Manager (if timeline/priority critical)

**Get explicit approval:**
```
✅ Requirement is clear
✅ Acceptance criteria are testable
✅ Non-goals make sense
✅ Constraints are understood
✅ Stakeholder approves this feature
```

**If approval not obtained:** Refine and retry

**If approval obtained:** Create GitHub issue

### Step 4: Create GitHub Issue

Create a new GitHub issue with:

**Title:** `[Feature] [Short description]`

**Body:**
```markdown
# [Feature Name]

## Problem
[From requirement document]

## Target User
[From requirement document]

## User Journeys
[From requirement document]

## Acceptance Criteria
[From requirement document]

## Non-Goals
[From requirement document]

## Constraints
[From requirement document]

## Risks & Assumptions
[From requirement document]

## Related Issues
[Links to related issues if any]

## Timeline
[When is this needed?]

## Priority
[ ] Critical
[ ] High
[ ] Medium
[ ] Low
```

**Label the issue:** 
- `type: feature` (or `type: bug`, etc.)
- `status: ready` (ready for architecture review)
- `priority: high/medium/low`

### Step 5: Proceed to Architecture

Once GitHub issue is created with `status: ready` label:

**Ask Architect Agent** to review feasibility and design a solution:

```
Here's an approved feature ready for architecture review:
[Link to GitHub issue]

Use the Factory Workflow (Phase 2: Architecture Design) to:
1. Review the requirement for clarity
2. Analyze existing architecture
3. Propose an implementation approach
4. Document affected components
5. Identify trade-offs
6. Surface security considerations
7. Produce an architecture proposal

Deliver in GitHub issue comments or separate document.
```

---

## Output

A GitHub issue ready for architecture review:

```
✅ Feature discovery complete
✅ Requirement clear and testable
✅ Acceptance criteria specific
✅ Non-goals documented
✅ Stakeholder approved
✅ Issue labeled "status: ready"
✅ Ready for Architect Agent

Next: Architecture Design Phase
```

---

## When Discovery Might Fail

**Scenario:** Requirement is too vague

**Solution:** 
1. Product Agent asks more clarifying questions
2. Refine requirement until testable
3. Retry stakeholder approval

**Scenario:** Stakeholder approves requirement but then changes mind during implementation

**Prevention:**
- Get explicit written approval before proceeding
- Document decision in GitHub issue
- Note any assumptions stakeholders approved

**Scenario:** Requirement violates existing constraints

**Solution:**
- Architect identifies constraint violation (Phase 2)
- Escalate back to Product/stakeholder
- Either refine requirement or challenge constraint
- (Constraints usually win unless justified to override)

---

## Timeline

**Typical duration:** 4-8 hours
- Discovery: 2-3 hours (conversations, documentation)
- Stakeholder review: 1-2 hours (depends on availability)
- Issue creation: 15 minutes
- Total: Same day to next day

**Variables:**
- Complexity of feature (simple: 2-4 hours, complex: 8+ hours)
- Stakeholder availability (if delayed, whole process delays)
- Clarity of initial request (clear requests: faster, vague requests: slower)

---

## Checklist

Before moving to Architecture Phase:

- [ ] Problem clearly stated (not solution-focused)
- [ ] User is specific (persona, not "users")
- [ ] User journeys documented (happy path + errors)
- [ ] Acceptance criteria are testable (not vague)
- [ ] Non-goals are explicit (scope boundaries)
- [ ] Constraints documented (technical, business, compliance)
- [ ] Risks and assumptions surfaced
- [ ] Stakeholder has approved
- [ ] GitHub issue created
- [ ] Issue labeled "status: ready"

---

## Success Criteria

This prompt succeeds when:

✅ Requirement is clear to any developer  
✅ Acceptance criteria are testable  
✅ Stakeholder is aligned  
✅ GitHub issue is documented  
✅ Ready for architecture review  

You should feel confident that:
- You've understood the real problem (not just the stated solution)
- You've defined what success looks like
- You've prevented scope creep with non-goals
- You've surfaced constraints and risks
- Stakeholders are committed

---

## Next Step

Once complete, use: **Implement Feature** prompt

Or invite: **Architect Agent** to begin Phase 2 (Architecture Design)
