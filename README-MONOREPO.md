# AI Software Factory - 3 SaaS Apps Monorepo

**Status**: 🚀 **In Development** - Parallel build of 3 complete SaaS applications

**Repository**: [roel-karstens/ai_fullstack_starter](https://github.com/roel-karstens/ai_fullstack_starter)

---

## 📦 Monorepo Structure

```
ai_fullstack_starter/
├── .github/
│   ├── agents/           ← Shared: Product, Developer, Architect, Reviewer, Security, Database
│   ├── skills/           ← Shared: Product discovery, testing, verification, security, etc.
│   ├── prompts/          ← Shared: start-project, start-feature, implement-feature, etc.
│   ├── workflows/        ← Shared: test.yml, lint.yml, build.yml, deploy-staging.yml, promote-production.yml
│   └── instructions/     ← Shared: backend, frontend, database, tests standards
│
├── docs/
│   ├── factory/          ← Shared: Factory principles, workflow, quality gates, etc.
│   └── product/          ← Shared product docs (can be per-app or shared)
│
├── apps/
│   ├── project-manager/          ← Original: Project management CRUD app
│   ├── therapy-assistant/        ← 🚀 NEW: AI Therapy Assistant for solo practitioners
│   ├── contract-analyzer/        ← 🚀 NEW: AI Contract analysis platform for lawyers
│   └── energy-platform/          ← 🚀 NEW: Energy consulting platform
│
└── scripts/              ← Shared deployment, setup scripts
```

---

## 🎯 The 3 Apps

### App 1: **AI Therapy Assistant** 🧠
**For**: Solo therapists, therapists in small practices  
**Problem Solved**: Admin overhead, time spent on documentation  
**Core Features**:
- Session note taking → AI auto-summarization via Claude
- Client management (sessions, histories, progress tracking)
- Dashboard with analytics (client mood trends, treatment progress)
- Optional: AI chatbot for clients (between-session support)
- Crisis detection and alerts

**Tech Stack**:
- **Frontend**: React + TypeScript (session recorder, dashboard, client portal)
- **Backend**: FastAPI + Python (LLM integration, session management)
- **Database**: Supabase PostgreSQL (therapists, clients, sessions, notes)
- **AI**: Claude API (session summarization, pattern detection)

**Timeline**: 1-2 weeks (MVP) → 2-3 weeks (complete)

**Status**: 🚀 Ready to build

---

### App 2: **AI Contract Analyzer** ⚖️
**For**: Solo lawyers, legal consultants, contract reviewers  
**Problem Solved**: Reading contracts takes forever, easy to miss risks  
**Core Features**:
- Upload contract → AI extracts key terms (parties, dates, amounts, obligations)
- Risk flagging (unusual payment terms, vague clauses, missing safeguards)
- Template library (standard contract clauses for comparison)
- Side-by-side contract comparison
- Analytics: contract patterns, common risks, processing time

**Tech Stack**:
- **Frontend**: React + TypeScript (document viewer, comparison tool, analytics)
- **Backend**: FastAPI + Python (document parsing, LLM analysis)
- **Database**: Supabase PostgreSQL (contracts, templates, extractions, comparisons)
- **AI**: Claude API (term extraction, risk analysis, recommendations)

**Timeline**: 1-2 weeks (MVP) → 2-3 weeks (complete)

**Status**: 🚀 Ready to build

---

### App 3: **Energy Consulting Platform** ⚡
**For**: Energy consultants, facilities managers  
**Problem Solved**: Manual analysis of utility bills and facility data  
**Core Features**:
- Client management (buildings, utility accounts, energy profiles)
- Upload utility bills → AI analyzes consumption patterns
- Optimization recommendations (HVAC, lighting, insulation, renewable energy)
- ROI projections and savings calculations
- Progress tracking (before/after energy consumption)
- Client reports (PDF generation with recommendations)

**Tech Stack**:
- **Frontend**: React + TypeScript (dashboard, report builder, analytics)
- **Backend**: FastAPI + Python (bill parsing, LLM recommendations, calculations)
- **Database**: Supabase PostgreSQL (clients, buildings, utilities, analyses, recommendations)
- **AI**: Claude API (bill analysis, optimization recommendations)

**Timeline**: 1-2 weeks (MVP) → 2-3 weeks (complete)

**Status**: 🚀 Ready to build

---

## 🏗️ Shared Factory Components

All 3 apps inherit the **AI Software Factory** from the root:

**Agents** (6 total):
- Product Agent - Requirements discovery
- Developer Agent - Implementation
- Architect Agent - Design
- Code Reviewer Agent - Quality review
- Security Reviewer Agent - Security audit
- Database Agent - Schema design

**Skills** (13 total):
- Product Discovery, Testing, Verification, Security Review
- Frontend Design, Supabase Database, Deployment, etc.

**Prompts** (8 total):
- start-project, start-feature, implement-feature, verify-and-ship, review, security-review, database-change, test-and-review

**Quality Gates** (9 mandatory approval points):
1. Product approval (requirements clear)
2. Architecture approval (design feasible)
3. CI/CD validation (tests, lint, build pass)
4. Code review (quality & compliance)
5. Security audit (risks assessed)
6. Merge to main (automatic when gates pass)
7. Staging validation (manual testing)
8. Production promotion (manual approval)
9. Monitoring (24h observation)

**CI/CD Workflows** (5 workflows):
- `test.yml` - Run pytest + vitest
- `lint.yml` - Ruff + Pyright + ESLint + TypeScript
- `build.yml` - Frontend (Vite) + Backend build
- `deploy-staging.yml` - Auto-deploy to staging
- `promote-production.yml` - Manual production approval

---

## 🚀 Build Timeline

### Phase 1: **Foundation** (This week)
- ✅ Monorepo structure created
- ✅ All 3 apps scaffolded with factory template
- ⏳ **This week**: Product discovery for each app → requirement documents

### Phase 2: **Architecture** (Next week)
- Design database schemas for each app
- Design API endpoints for each app
- Design frontend pages and components
- Create LLM prompts for each app's AI features

### Phase 3: **Implementation** (Weeks 2-3)
- **Parallel**: Build all 3 apps simultaneously
- Each follows factory workflow (implement → test → verify → code review → security audit → deploy)

### Phase 4: **Polish** (Week 4)
- Refinements based on testing
- Documentation and case studies
- Performance optimization

### Phase 5: **Done** (Week 4 end)
- All 3 apps live in production
- Complete case study documentation
- Ready to monetize

**Total Timeline**: 3-4 weeks

---

## 📊 Development Progress

| App | Discovery | Architecture | Implementation | Testing | Production |
|-----|-----------|--------------|-----------------|---------|------------|
| Project Manager | ✅ Done | ✅ Done | ✅ Done | ✅ Done | ✅ Live |
| Therapy Assistant | ⏳ Starting | ⏰ Pending | ⏰ Pending | ⏰ Pending | ⏰ Pending |
| Contract Analyzer | ⏳ Starting | ⏰ Pending | ⏰ Pending | ⏰ Pending | ⏰ Pending |
| Energy Platform | ⏳ Starting | ⏰ Pending | ⏰ Pending | ⏰ Pending | ⏰ Pending |

---

## 🎯 Next Steps

### Immediate (Today)
1. **Product Discovery** (Parallel)
   - Use `product` agent for each app
   - Define requirements, user journeys, acceptance criteria
   - Create GitHub issues for each app with requirement documents

2. **Push to GitHub**
   - Commit monorepo structure
   - Push new branch with all 3 apps

### This Week
1. **Architecture Design** (Parallel)
   - Architect designs database schemas
   - Architect designs API contracts
   - Database agent reviews schemas

2. **Create Requirement Documents**
   - Product journeys
   - Acceptance criteria
   - Feature maps for each app

### Next Week
1. **Implementation** (Parallel)
   - Developer builds all 3 apps simultaneously
   - Each app follows factory workflow
   - Daily commits

2. **Testing & Verification**
   - Unit tests
   - Integration tests
   - Running system verification (EVIDENCE collection)

### Week 3-4
1. **Polish & Production**
   - Code review and security audit
   - Deploy to staging
   - Manual validation
   - Production deployment
   - Monitoring

---

## 📖 How to Navigate

### For App 1 (Project Manager)
- **Status**: Existing app, fully functional
- **Location**: `/apps/project-manager/`
- **Documentation**: `/apps/project-manager/docs/product/`
- **Ready to extend** with new features

### For App 2 (Therapy Assistant)
- **Status**: Scaffolded, requirements starting
- **Location**: `/apps/therapy-assistant/`
- **Documentation**: `/apps/therapy-assistant/docs/product/`
- **Next**: Product discovery → Architecture → Implementation

### For App 3 (Contract Analyzer)
- **Status**: Scaffolded, requirements starting
- **Location**: `/apps/contract-analyzer/`
- **Documentation**: `/apps/contract-analyzer/docs/product/`
- **Next**: Product discovery → Architecture → Implementation

### For App 4 (Energy Platform)
- **Status**: Scaffolded, requirements starting
- **Location**: `/apps/energy-platform/`
- **Documentation**: `/apps/energy-platform/docs/product/`
- **Next**: Product discovery → Architecture → Implementation

---

## 🔧 Shared Factory

### Location
- Agents: `.github/agents/`
- Skills: `.github/skills/`
- Prompts: `.github/prompts/`
- Workflows: `.github/workflows/`
- Documentation: `docs/factory/`

### How Each App Uses the Factory
Every app inherits:
1. **Quality gates** (9 mandatory checkpoints)
2. **CI/CD workflows** (test → lint → build → deploy)
3. **Development agents** (Product, Developer, Architect, Reviewer, Security, Database)
4. **Skills** (discovery, testing, verification, security)
5. **Coding standards** (backend, frontend, database, tests instructions)

Each app modifies:
- `apps/[app]/docs/product/` (product-specific docs)
- `apps/[app]/frontend/` (domain-specific components)
- `apps/[app]/backend/` (domain-specific services)
- `apps/[app]/supabase/` (domain-specific schema)

The factory stays consistent across all apps.

---

## 🎓 Using the Factory for Each App

### Start a New Feature for Any App

```bash
# Go to the app directory
cd apps/therapy-assistant

# Use the start-feature prompt from root
# (References factory agents, skills, prompts)
```

Each feature in each app:
1. **Discover** → Use Product Agent → Create requirement
2. **Design** → Use Architect Agent → Design solution
3. **Build** → Use Developer Agent → Implement
4. **Review** → Use Code Reviewer + Security Reviewer → Approve
5. **Test** → CI/CD validates (test, lint, build)
6. **Deploy** → Staging (automatic) → Production (manual)

---

## 💡 Key Decisions

**Monorepo Over Multiple Repos**:
- Shared factory stays in sync
- Easier to copy patterns between apps
- Single CI/CD pipeline (can be customized per app)
- One GitHub issue tracker for all

**Parallel Development**:
- Each app is independent (can work on them in any order)
- Use factory's quality gates to ensure consistency
- Developers can work on different apps simultaneously

**AI Integration**:
- All 3 apps use LLMs (Claude API)
- Each app has domain-specific prompts
- Security: API keys in `.env` (never committed)

---

## 📞 Questions?

- **What's the factory?** → See `docs/factory/factory-principles.md`
- **How to build a feature?** → See `.github/prompts/start-feature.prompt.md`
- **How to structure an app?** → See `.github/prompts/start-project.prompt.md`
- **What are quality gates?** → See `docs/factory/quality-gates.md`

---

## 🚀 Status

**Overall**: 📊 Monorepo set up, ready for parallel development

**Next Action**: Product discovery for all 3 new apps

---

**Last Updated**: October 8, 2026  
**Repository**: [roel-karstens/ai_fullstack_starter](https://github.com/roel-karstens/ai_fullstack_starter)  
**Branch**: main  
