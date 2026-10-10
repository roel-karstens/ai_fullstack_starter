# 🏭 AI Software Factory

A production-grade full-stack SaaS factory with **4 complete applications**, built with React + FastAPI + PostgreSQL and optimized for GitHub Copilot development.

---

## 📚 Documentation Map

Start here based on your role:

| I want to... | Read this |
|---|---|
| **Understand the factory structure** | [docs/README-MONOREPO.md](docs/README-MONOREPO.md) |
| **Run the apps locally** | [docs/APPS-RUNNING-LOCALLY.md](docs/APPS-RUNNING-LOCALLY.md) |
| **Develop with AI agents** | [docs/AGENTS.md](docs/AGENTS.md) |
| **Learn factory principles** | [docs/factory/factory-principles.md](docs/factory/factory-principles.md) |
| **See architecture decisions** | [docs/factory/FACTORY-STATUS.md](docs/factory/FACTORY-STATUS.md) |
| **Get started with a new feature** | [.github/prompts/implement-feature.prompt.md](.github/prompts/implement-feature.prompt.md) |

---

## 🎯 The Factory at a Glance

**4 Complete SaaS Applications** (shared infrastructure, independent codebases):

| App | Purpose | Status |
|---|---|---|
| **🧠 Therapy Assistant** | AI session documentation for therapists | ⏳ In Development |
| **⚖️ Contract Analyzer** | AI contract analysis for lawyers | ⏳ In Development |
| **⚡ Energy Platform** | AI energy optimization for consultants | ⏳ In Development |
| **🔌 ChargePark** | EV charging decision support (Netherlands) | ⏳ In Development |

**Plus**: Original **Project Manager** demo app ✅ Live

---

## 🚀 Quick Start

### 1. Explore the Structure
```bash
ls -la apps/                    # 4 production apps
ls -la .github/                 # Shared agents, skills, prompts
ls -la docs/factory/            # Factory principles & workflow
```

### 2. Run an App Locally
```bash
cd apps/therapy-assistant/frontend
npm install
npm run dev              # Runs on http://localhost:5173/
```

### 3. Build a Feature
Use the factory workflow:
1. Read [.github/prompts/start-feature.prompt.md](.github/prompts/start-feature.prompt.md)
2. Follow the workflow with Copilot agents
3. Use [.github/prompts/implement-feature.prompt.md](.github/prompts/implement-feature.prompt.md) to code
4. Verify with [.github/skills/verification/SKILL.md](.github/skills/verification/SKILL.md)
5. Review with [.github/prompts/verify-and-ship.prompt.md](.github/prompts/verify-and-ship.prompt.md)

---

## 📁 Repository Structure

```
ai_fullstack_starter/
├── apps/                           ← 4 production SaaS apps
│   ├── project-manager/           ← Demo: Project CRUD
│   ├── therapy-assistant/         ← AI therapist assistant
│   ├── contract-analyzer/         ← AI legal contract analysis
│   ├── energy-platform/           ← AI energy optimization
│   └── chargepark/                ← EV charging decision support
│
├── .github/                        ← Shared factory components
│   ├── agents/                    ← Product, Architect, Developer, Reviewer
│   ├── skills/                    ← Testing, verification, security, etc.
│   ├── prompts/                   ← Workflow templates
│   ├── instructions/              ← Code standards (frontend, backend, tests)
│   └── workflows/                 ← GitHub Actions CI/CD
│
├── docs/
│   ├── factory/                   ← Factory principles, workflow, quality gates
│   ├── architecture.md            ← System design
│   ├── security.md                ← Security practices
│   ├── database.md                ← Database design patterns
│   └── TECHNICAL_AUDIT.md         ← Code quality audit
│
├── README.md                       ← This file (primary entry point)
├── README-MONOREPO.md             ← Detailed monorepo guide
├── APPS-RUNNING-LOCALLY.md        ← Local development setup
├── AGENTS.md                       ← AI agent guidelines
└── scripts/                        ← Shared utilities
```

---

## 🏗️ Architecture

```
┌─────────────────────────────────────┐
│      React Frontend (Vite)          │
│  - TypeScript + Tailwind            │
│  - Authentication UI                │
└──────────────┬──────────────────────┘
               │ HTTP (REST API)
               ↓
┌─────────────────────────────────────┐
│   FastAPI Backend (Python)          │
│  - Business Logic                   │
│  - API Endpoints                    │
│  - Authorization                    │
└──────────────┬──────────────────────┘
               │ SQL
               ↓
┌─────────────────────────────────────┐
│ Supabase PostgreSQL + Auth + RLS    │
│  - User Authentication              │
│  - Row Level Security               │
│  - Data Persistence                 │
└─────────────────────────────────────┘
```

**Critical Rule**: Frontend never accesses private keys or database directly. All access through authenticated FastAPI.

---

## ✨ Key Features

- **Production-Grade**: All apps follow SOLID principles, strict typing, comprehensive tests
- **AI-Ready**: Optimized for GitHub Copilot with custom agents, skills, and prompts
- **Monorepo**: 4 apps share factory infrastructure but maintain independent codebases
- **Security**: JWT auth, Row Level Security, no secrets in code
- **Verification-First**: Every feature change includes evidence of working on the real running system
- **Scalable**: Each app can deploy independently to production

---

## 📖 Next Steps

### For First-Time Users
1. Read [README-MONOREPO.md](README-MONOREPO.md) for the complete overview
2. Run a local app with [APPS-RUNNING-LOCALLY.md](APPS-RUNNING-LOCALLY.md)
3. Explore the code in one app directory to see the patterns

### For Copilot Development
1. Read [AGENTS.md](AGENTS.md) to understand the AI development workflow
2. Check [.github/copilot-instructions.md](.github/copilot-instructions.md) for Copilot guidance
3. Use [.github/prompts/](./github/prompts/) templates for common tasks

### For New Features
1. Start with [.github/prompts/start-feature.prompt.md](.github/prompts/start-feature.prompt.md) to define requirements
2. Build with [.github/prompts/implement-feature.prompt.md](.github/prompts/implement-feature.prompt.md) 
3. Verify with [.github/skills/verification/SKILL.md](.github/skills/verification/SKILL.md)
4. Ship with [.github/prompts/verify-and-ship.prompt.md](.github/prompts/verify-and-ship.prompt.md)

---

## 🔗 Related Documentation

- **Factory Workflow**: [docs/factory/factory-workflow.md](docs/factory/factory-workflow.md)
- **Quality Gates**: [docs/factory/quality-gates.md](docs/factory/quality-gates.md)
- **Feature Map**: [docs/factory/feature-map.md](docs/factory/feature-map.md)
- **Integration Summary**: [docs/chargepark-integration.md](docs/chargepark-integration.md)
- **Technical Audit**: [docs/TECHNICAL_AUDIT.md](docs/TECHNICAL_AUDIT.md)
- **Verification Report**: [docs/VERIFICATION_REPORT.md](docs/VERIFICATION_REPORT.md)

---

## 🎯 Principles

### Development
- **Minimal changes**: Solve the problem, no speculative abstractions
- **Reuse patterns**: Follow existing conventions in each app
- **Strict typing**: TypeScript and Python type hints on everything
- **Comprehensive tests**: Unit, integration, and runtime verification

### Security
- **No secrets in code**: Use `.env.example` for documentation
- **Server-side auth**: Validate JWT on every protected endpoint
- **RLS everywhere**: Row Level Security on all user data tables
- **Input validation**: Pydantic on all requests

### Verification
- **"It compiles" is not proof**: Run the app and test the actual feature
- **Evidence first**: Collect curl responses, database queries, screenshots
- **Before claiming done**: Verify on the real running system
- **Document the proof**: Include verification output in pull requests

---

## 📞 Support

- **Questions about the factory?** → Read [docs/factory/](docs/factory/)
- **How do I...?** → Check [docs/development.md](docs/development.md)
- **Security concern?** → See [docs/security.md](docs/security.md)
- **Architecture question?** → Review [docs/architecture.md](docs/architecture.md)

---

**Built with ❤️ for AI-assisted development**
