# Quick Start Guide: Using the AI Software Factory

**You are here**: Factory is complete and ready to use.

---

## 🚀 Get Started in 5 Minutes

### Step 1: Understand What You Have (5 minutes)

You now have a complete AI Software Factory with:
- **6 Agents** - Different roles (Product, Developer, Architect, Reviewer, Security, Database)
- **13 Skills** - Domain expertise (product discovery, testing, verification, etc.)
- **8 Prompts** - User workflows (start-project, start-feature, etc.)
- **9 Quality Gates** - Approval checkpoints (requirements, design, code quality, security, etc.)
- **5 CI/CD Workflows** - Automated validation (test, lint, build, deploy)

### Step 2: Read the Core Philosophy (20 minutes)

Start here: [`docs/factory/factory-principles.md`](./factory-principles.md)

Key concepts:
- **"Prove It Works"** - Evidence required on running system, not just tests
- **Quality Gates** - Mandatory approval points (no skipping)
- **Separation** - Agents ≠ Skills ≠ Prompts (clean architecture)

### Step 3: Understand the Workflow (30 minutes)

Next: [`docs/factory/factory-workflow.md`](./factory-workflow.md)

The complete 9-phase lifecycle:
```
IDEA
  → DISCOVERY (2-3 hours)
  → APPROVAL (1-2 hours)
  → DESIGN (1-2 hours)
  → APPROVAL
  → IMPLEMENTATION (varies)
  → TESTING
  → CODE REVIEW
  → SECURITY AUDIT
  → MERGE TO MAIN (automatic)
  → STAGING DEPLOYMENT (automatic)
  → YOU TEST STAGING (manual)
  → PRODUCTION PROMOTION (manual)
  → DONE ✅
```

### Step 4: Pick Your Path

Choose what you want to do:

---

## 📋 Path A: Create New Application

**Time**: 4-6 hours (one day)

**Use**: `.github/prompts/start-project.prompt.md`

**Steps**:
1. Copy factory repository
2. Run start-project prompt
3. Customize frontend/backend/database for your domain
4. Configure CI/CD with your deployment target
5. Deploy to staging
6. Begin building features

**When to use**: Starting completely new app from template

---

## ✨ Path B: Add Feature to Existing App

**Time**: 3-5 days per feature

**Use**: `.github/prompts/start-feature.prompt.md`

**Workflow**:
1. **DISCOVER** (2-3 hours) - Product Agent helps define what to build
2. **DESIGN** (1-2 hours) - Architect Agent designs how to build it
3. **BUILD** (1-3 days) - Developer Agent implements with verification
4. **REVIEW** (1-2 hours) - Code & Security reviewers approve
5. **DEPLOY** (automatic to staging)
6. **VALIDATE** (manual) - You test in staging
7. **PROMOTE** (manual) - Deploy to production

**When to use**: Adding features to your app

---

## 🔍 Path C: Understand Existing Project

**Time**: 1-2 hours

**Read these** (in order):
1. [`docs/factory/repository-assessment.md`](./repository-assessment.md) - What exists
2. [`docs/factory/quality-gates.md`](./quality-gates.md) - Approval points
3. [`docs/factory/feature-map.md`](./feature-map.md) - What features exist

**When to use**: Evaluating existing project or understanding what's already built

---

## 📚 Documentation Structure

```
docs/factory/
├── factory-principles.md      ← Start here (philosophy)
├── factory-workflow.md         ← 9-phase development cycle
├── quality-gates.md            ← 9 approval points
├── repository-assessment.md    ← Current state analysis
├── feature-map.md              ← Track all features
├── FACTORY-STATUS.md           ← Implementation report
└── SESSION-COMPLETION.md       ← This session summary

.github/
├── agents/
│   ├── product.agent.md        ← Discover requirements
│   ├── developer.agent.md      ← Implement features
│   ├── architect.agent.md      ← Design solutions
│   ├── code-reviewer.agent.md  ← Review quality
│   ├── security-reviewer.agent.md ← Audit risks
│   └── database.agent.md       ← Design schemas
│
├── skills/
│   ├── product-discovery/      ← How to discover requirements
│   ├── testing/                ← Testing patterns
│   ├── verification/           ← How to verify it works
│   ├── security-review/        ← Security audit process
│   └── ... 8 more skills
│
├── prompts/
│   ├── start-project.prompt.md      ← NEW APP (4-6 hours)
│   ├── start-feature.prompt.md      ← NEW FEATURE (3-5 days)
│   ├── implement-feature.prompt.md  ← Build approved feature
│   ├── verify-and-ship.prompt.md    ← Test before shipping
│   └── ... 3 more prompts
│
└── workflows/
    ├── test.yml                ← Run tests (GitHub Actions)
    ├── lint.yml                ← Check code quality
    ├── build.yml               ← Verify builds
    ├── deploy-staging.yml      ← Auto-deploy to staging
    └── promote-production.yml  ← Manual production approval
```

---

## 🎯 Decision Tree: What to Do Now?

```
Are you starting a NEW application?
  → YES: Use start-project.prompt.md
  → NO: Continue below

Do you have an existing feature to add?
  → YES: Use start-feature.prompt.md
  → NO: Continue below

Do you need to understand the existing project?
  → YES: Read factory-principles.md, then factory-workflow.md
  → NO: Read quality-gates.md for approval process

Need to understand CI/CD?
  → Read .github/workflows/ directory
  
Need to understand agents/skills?
  → Read .github/agents/ and .github/skills/ directories
```

---

## ⚡ Quick Commands

**Verify everything works**:
```bash
# Backend
cd backend
source venv/bin/activate
pytest                  # Run tests
ruff check app/        # Lint
pyright                # Type check

# Frontend
cd frontend
npm test               # Run tests
npm run lint           # Lint
npm run type-check     # Type check
npm run build          # Build for production
```

**See CI/CD status**:
- Go to GitHub → Actions tab
- See test.yml, lint.yml, build.yml results
- See deployment workflow status

**Deploy to staging**:
- Push to main branch
- GitHub automatically runs: test → lint → build
- If all pass: auto-deploy to staging
- Test in staging manually
- Then use promote-production.yml for production

---

## 📖 Reading Recommendations

### 30-Minute Overview (Get Started Fast)
1. This file (Quick Start Guide) - 10 min
2. `factory-principles.md` - 15 min
3. `quality-gates.md` (skim) - 5 min

### 2-Hour Deep Dive (Understand Everything)
1. `factory-principles.md` - 20 min
2. `factory-workflow.md` - 45 min
3. `quality-gates.md` - 30 min
4. `feature-map.md` - 15 min
5. Skim `.github/agents/` - 10 min

### 4-Hour Mastery (Ready to Build)
1-5. Above 2-hour dive
6. Read `.github/prompts/start-feature.prompt.md` - 30 min
7. Read `.github/agents/developer.agent.md` - 30 min
8. Read `.github/agents/product.agent.md` - 30 min
9. Read `.github/agents/architect.agent.md` - 30 min

---

## 🚦 Common Scenarios

### Scenario 1: "I want to build a new SaaS app"

```
Week 1:
  - Read factory-principles.md
  - Run start-project.prompt.md (4-6 hours)
  - Customize database schema
  - Update backend services
  - Update frontend components
  - Deploy to staging

Week 2+:
  - Start first feature with start-feature.prompt.md
  - Repeat: discover → design → implement → deploy
  - Build 2-3 features to get into rhythm
```

### Scenario 2: "I have an existing app and want to add a feature"

```
Today (1 hour):
  - Read factory-principles.md
  - Read factory-workflow.md
  
Tomorrow (3-5 days):
  - Run start-feature.prompt.md for your feature
  - Follow the workflow (discover → design → implement → test → review → deploy)
```

### Scenario 3: "I want to understand what was built"

```
Today (2 hours):
  - Read factory-principles.md (20 min)
  - Read quality-gates.md (30 min)
  - Skim .github/agents/ and .github/skills/ (1 hour)
  
Later (optional):
  - Read factory-workflow.md for complete workflow
  - Read repository-assessment.md to see what exists
```

### Scenario 4: "I want to add my own agents/skills"

```
First:
  - Read factory-principles.md (understand separation)
  - Read existing agents in .github/agents/
  - Read existing skills in .github/skills/

Then:
  - Create new agent based on existing template
  - Create new skill based on existing template
  - Test by using in prompts
```

---

## ✅ Pre-Flight Checklist

Before starting your first feature, verify:

- [ ] Read `factory-principles.md`
- [ ] Read `factory-workflow.md`
- [ ] Understand the 9 quality gates
- [ ] Know how to use the `start-feature.prompt.md`
- [ ] Understand that "it compiles" is NOT the same as "it works"
- [ ] Ready to collect evidence (curl responses, screenshots, database state)
- [ ] Know that production deployment requires manual approval (not automatic)

---

## 🎓 Learning Path

### Beginner (Just Getting Started)
- Read: Quick Start Guide (this file)
- Read: factory-principles.md
- Do: Run start-project.prompt.md
- Use: start-feature.prompt.md for first feature

### Intermediate (Building Features)
- Understand: All 9 quality gates (quality-gates.md)
- Study: Product Agent workflow (product.agent.md)
- Study: Developer Agent workflow (developer.agent.md)
- Use: All factory prompts and agents

### Advanced (Extending Factory)
- Understand: Why factory is structured this way
- Create: Custom agents for your domain
- Create: Custom skills for your patterns
- Mentor: Others using the factory

---

## 🆘 Getting Help

**If you don't know where to start**:
- Read: `factory-principles.md`
- Do: Pick "Path A" or "Path B" above

**If you need to understand architecture**:
- Read: `factory-workflow.md`

**If you need to understand approval process**:
- Read: `quality-gates.md`

**If you need to understand a specific role**:
- Look in: `.github/agents/` (find the agent)
- Read: That agent's documentation

**If you need domain-specific guidance**:
- Look in: `.github/skills/` (find the skill)
- Read: That skill's documentation

**If something doesn't work**:
- Check: Existing app still compiles/tests
- Fix: Any linting errors (`ruff check .`, `npm run lint`)
- Verify: CI/CD workflows pass

---

## 🎉 You're Ready!

The factory is complete and ready to use. Pick one:

1. **Build new app** → Use `start-project.prompt.md` (4-6 hours)
2. **Add new feature** → Use `start-feature.prompt.md` (3-5 days)
3. **Understand more** → Read `factory-principles.md` (20 minutes)

---

## 📞 Quick Reference

| Need | File |
|------|------|
| Philosophy | `factory-principles.md` |
| Complete Workflow | `factory-workflow.md` |
| Approval Points | `quality-gates.md` |
| Product Discovery | `.github/agents/product.agent.md` |
| Implementation | `.github/agents/developer.agent.md` |
| Code Review | `.github/agents/code-reviewer.agent.md` |
| Security Audit | `.github/agents/security-reviewer.agent.md` |
| Database Design | `.github/agents/database.agent.md` |
| Architecture | `.github/agents/architect.agent.md` |
| New App | `.github/prompts/start-project.prompt.md` |
| New Feature | `.github/prompts/start-feature.prompt.md` |
| Feature Tracking | `docs/factory/feature-map.md` |

---

**Good luck building amazing things!** 🚀

Remember: The factory makes you more disciplined, not faster. You'll ship fewer bugs and sleep better at night. That's the point.

Now go pick something to build! 💪
