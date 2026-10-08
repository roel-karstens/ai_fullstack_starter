# AI Software Factory: Operating Principles

**Version**: 1.0  
**Last Updated**: October 8, 2026

---

## Core Philosophy

The AI Software Factory is designed to build **production-quality software rapidly and reliably** using GitHub Copilot.

### Core Tenets

**1. Prove It Works**

"It compiles" is NOT evidence that software works.

Every feature, fix, and change must be demonstrated to work on the actual running system with concrete evidence:

- API responses (status codes, response shapes)
- Database state changes (rows inserted, policies enforced)
- User flows (screenshots, browser verification)
- Error cases (authorization rejected, validation failed)

Evidence beats speculation. Screenshots beat code reviews. Working systems beat passing tests.

**2. Build for Humans First, Then for Machines**

This factory exists to make human developers faster and better, not to maximize machine autonomy.

- Machines should validate (lint, type-check, test) automatically
- Machines should suggest and implement following patterns
- Humans should review for correctness and intent
- Humans should approve high-stakes decisions (architecture, deployment)

**3. Consistency Over Cleverness**

Reusable, predictable software beats novel, clever software.

- Follow established patterns (don't silently redesign)
- Reuse components, services, and functions (don't duplicate)
- Use boring technology (prefer proven over cutting-edge)
- Make code easy for humans to understand (not optimal for machines)

**4. Separation of Concerns**

Each actor has a clear role; responsibilities don't overlap:

- **Product**: Defines problems, user journeys, acceptance criteria
- **Architect**: Validates feasibility, designs components, documents trade-offs
- **Developer**: Implements faithfully, writes tests, verifies functionality
- **Reviewer**: Checks compliance with requirements, architecture, standards
- **Security**: Audits for risks, validates controls
- **Tester**: Validates against acceptance criteria

Agents work sequentially, not in parallel. Product defines what; Architect designs how; Developer implements; Reviewer validates.

**5. Quality Over Speed**

Speed without quality is rework; quality with speed is efficiency.

- Take time to understand requirements (prevents building wrong thing)
- Follow patterns (faster to implement, easier to maintain)
- Test thoroughly (less time debugging)
- Verify on real system (catches issues early)

Fast > Good is a false choice. Good is Fastest.

**6. Transparency Over Autonomy**

Visibility beats darkness.

- Document assumptions and decisions
- Surface uncertainties early
- Show evidence for claims
- Be explicit about what was/wasn't done

If an agent is uncertain, say so. Don't guess. Escalate.

**7. Pragmatism Over Perfection**

Shipping working software beats perfect software that never ships.

- 80% solution that ships > 100% solution in progress
- Pragmatic test coverage > perfectionist coverage
- Ship, then iterate
- BUT: Never ship broken, insecure, or untested

---

## The Factory's Scope

### What the Factory Builds

✅ **Web applications** with:
- React + TypeScript frontend
- FastAPI + Python backend
- Supabase PostgreSQL database
- Supabase email/password authentication
- User-owned data with Row Level Security

✅ **Examples:**
- Project management apps
- Content management systems
- Inventory management
- Team collaboration tools
- SaaS platforms with multiple users

### What the Factory Does NOT Build

❌ **Mobile applications** (native iOS/Android)  
❌ **Hardware integrations**  
❌ **Real-time collaborative editing** (not without WebSockets, which we can add)  
❌ **Complex video processing**  
❌ **Machine learning model training** (predictions from pre-trained models OK)  

### What IS Configurable

**Per-application:**
- Product domain (project management vs. inventory vs. content)
- Business rules
- Data model
- User roles and permissions
- Styling/branding
- Deployment target (as long as it supports Node.js + Python + PostgreSQL)

**NOT configurable without factory changes:**
- Frontend framework (React)
- Backend framework (FastAPI)
- Database (PostgreSQL)
- Authentication mechanism (Supabase)

---

## Key Concepts

### Agents vs. Skills vs. Prompts

**Agents = WHO (Role & Responsibility)**

Agents are roles defined by:
- What decisions they can make
- What decisions require approval
- Their expertise domain
- Their relationship to other agents

**Initial Agents:**
- Product → defines problems and requirements
- Architect → designs solutions
- Developer → implements solutions
- Reviewer → validates compliance
- Security → audits for risks

**Skills = HOW (Reusable Procedures)**

Skills are domain-specific knowledge:
- How to discover product requirements
- How to design APIs
- How to design databases
- How to test features
- How to verify features work
- How to conduct security reviews

**Prompts = WHAT (Workflows)**

Prompts initiate repeatable workflows:
- "start-project" → launch a new application
- "start-feature" → discover a new feature
- "implement-feature" → build an approved feature
- "review-feature" → validate implementation
- "verify-project" → demonstrate system works

### Quality Gates

**Quality gates are mandatory approval points** where a human must review and approve before proceeding.

Gates prevent:
- Building the wrong thing (Product gate)
- Building it wrong (Architect gate)
- Shipping untested code (Test gate)
- Shipping insecure code (Security gate)
- Shipping non-compliant code (Review gate)

Agents do NOT bypass gates. If a gate requires approval, agents wait for human decision.

---

## Development Model

### Phase 1: Product Discovery

**Goal**: Understand the problem

**Who**: Product Agent + Stakeholders

**Inputs**: 
- User problem statement
- Business context

**Outputs**:
- Clear problem definition
- Target user personas
- User journeys
- Acceptance criteria
- Non-goals

**Quality Gate**: Product review
- Problem is clear
- Acceptance criteria are testable
- Non-goals are explicit
- Stakeholders approve

### Phase 2: Architecture Design

**Goal**: Design a solution

**Who**: Architect Agent + Security Agent

**Inputs**:
- Product requirement
- Architectural constraints

**Outputs**:
- Architecture proposal
- Component design
- API contracts
- Database schema
- Security considerations

**Quality Gate**: Architecture review
- Solution is feasible
- Fits existing architecture
- No major security issues
- No unnecessary complexity

### Phase 3: Implementation

**Goal**: Build the feature

**Who**: Developer Agent

**Inputs**:
- Approved architecture
- Product requirement

**Outputs**:
- Code following patterns
- Tests covering acceptance criteria
- Database migrations (if needed)
- Verification evidence

**Quality Gates**:
- All tests pass
- Linting/type-checking pass
- Feature verified on running system

### Phase 4: Review

**Goal**: Validate implementation

**Who**: Code Reviewer

**Inputs**:
- Pull request
- Verification evidence

**Outputs**:
- Approved or rejected
- Code review comments

**Quality Gate**: Code review
- Implements requirements correctly
- Follows established patterns
- Test coverage is adequate
- No security issues
- No regressions

### Phase 5: Security Audit

**Goal**: Check for security issues

**Who**: Security Agent

**Inputs**:
- Implementation
- Security requirements

**Outputs**:
- Security audit or approval

**Quality Gate**: Security review
- No sensitive data exposed
- Authentication/authorization correct
- Input validation present
- Error handling appropriate

### Phase 6: Deployment

**Goal**: Release to users

**Who**: Deployment Agent + Human Approval

**Inputs**:
- Reviewed and approved code
- Staging test results

**Outputs**:
- Production deployment
- Release notes

**Quality Gate**: Manual promotion
- Staging environment passed all tests
- Human reviewed staging
- Stakeholders approved release
- Deployment plan reviewed

---

## Artifacts & Documentation

### Requirement Document

**Owner**: Product Agent

Created during product discovery. Documents:
- Problem statement
- User journeys
- Acceptance criteria
- Non-goals
- Constraints

**Used by**: Architect, Developer, Reviewer

### Architecture Design Document

**Owner**: Architect Agent

Created during architecture phase. Documents:
- Component changes
- API contracts
- Database schema changes
- Security implications
- Trade-offs considered

**Used by**: Developer, Reviewer, Security Agent

### Implementation Evidence

**Owner**: Developer Agent

Created during implementation. Documents:
- What changed
- How to verify it works
- Test results
- Verification screenshots/output
- Database state changes

**Used by**: Reviewer, Security Agent, Tester

### Pull Request

**Owner**: Developer Agent

Brings everything together:
- Clear description of changes
- Link to requirement
- Link to architecture design
- Test results
- Verification evidence
- Migration notes (if database changes)

### Release Notes

**Owner**: Deployment Agent

Describes:
- What changed for users
- Known issues
- Breaking changes (if any)
- How to migrate (if applicable)

---

## Success Metrics

### Factory Effectiveness

**Shipping Velocity**
- How many features per sprint?
- How long from idea to production?

**Quality**
- Defect rate (bugs reported by users)
- Test coverage
- Type error density

**Productivity**
- Engineer time spent on productive work vs. debugging
- Time spent in code review
- Rework rate (features that need changes)

**User Satisfaction**
- Do features work as intended?
- User adoption rate
- Feature satisfaction scores

### Code Quality

**Maintainability**
- Cyclomatic complexity (is code simple?)
- Code duplication (are we reusing or repeating?)
- Test coverage (can we refactor safely?)

**Performance**
- API response times
- Frontend load times
- Database query performance

**Security**
- Vulnerabilities per release
- Failed security audits
- Unauthorized access attempts

---

## Principles in Practice

### Principle: "Prove It Works"

**In Practice:**

❌ **Bad:**
- "I implemented the API" (no evidence)
- "Tests pass" (which tests? did you run them?)
- "No type errors" (running TypeScript in your head?)

✅ **Good:**
- "Here's the curl request, status code, and response body"
- "Screenshot of browser showing feature working"
- "Database query showing new row with correct data"
- "Test output showing 23 tests passed, 0 failed"

### Principle: "Consistency Over Cleverness"

**In Practice:**

❌ **Bad:**
- "I refactored the auth system to be more elegant"
- "I added a cache layer for performance"
- "I rewrote the API using a different pattern"

✅ **Good:**
- "I followed the existing pattern from ProjectService"
- "I reused the ErrorAlert component"
- "I kept auth the same as existing endpoints"

### Principle: "Separation of Concerns"

**In Practice:**

❌ **Bad:**
- Product Agent designing API endpoints
- Developer Agent making architecture decisions
- Architect Agent implementing code

✅ **Good:**
- Product Agent defines what (acceptance criteria)
- Architect Agent designs how (component structure)
- Developer Agent implements (following architecture)
- Reviewer Agent validates (compliance with design)

### Principle: "Transparency Over Autonomy"

**In Practice:**

❌ **Bad:**
- Agent silently redesigns a component
- Agent guesses at unclear requirements
- Agent commits code with untested assumptions

✅ **Good:**
- Agent documents assumptions in PR
- Agent escalates unclear requirements to Product
- Agent surfaces risks in implementation notes
- Agent shows verification evidence in PR

---

## Common Questions

**Q: Can an agent skip a quality gate?**  
A: No. Quality gates exist to prevent bad decisions. If an agent thinks a gate is wrong, escalate to a human, don't bypass it.

**Q: How long should each phase take?**  
A: It depends. A small feature: hours. A medium feature: days. A large feature: weeks. The factory optimizes for correctness, not speed.

**Q: Can we deploy directly to production?**  
A: No. In this factory, code always goes to staging first, gets human validation, then is promoted to production.

**Q: What if an agent disagrees with a decision?**  
A: Agents should document their concern and escalate to a human. The human makes the final call.

**Q: Should we use a new technology?**  
A: Discuss with Architect. If it's a major change, it may require Architect approval. If it's a small library, get Product input (cost) and Architect input (fit).

---

## Graduation Path

### v1: Foundation (Now)
- Basic agents (product, architect, developer, reviewer, security)
- Basic skills (discovery, design, implementation, testing, verification)
- Manual CI/CD (on PR)
- Manual promotion to staging/production

### v1.1: Automation
- GitHub Actions for lint/test/build
- Automated staging deployment
- Automated security scanning
- Feature Map integration

### v2: Intelligence
- Agents can propose tests and verification strategy
- Agents can suggest architecture improvements
- Agents can audit pull requests autonomously
- Cost tracking (estimate and actual)

### v3: Maturity
- Production deployment automation (with approval)
- Performance monitoring integration
- Dependency scanning and auto-updates
- Metrics dashboard
- Integration with issue tracking

---

## Final Note

This factory is designed for **truth over speed**. We build working software verified on real systems, not theoretical systems that might work. 

Every feature proves itself before shipping. Every change is reversible. Every decision is documented.

The factory's job is to make this process fast without sacrificing correctness.
