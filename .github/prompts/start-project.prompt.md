# Start a New Project

Use this prompt to initialize a new application using the AI Software Factory.

---

## What This Creates

A production-ready full-stack web application with:
- React 18 + TypeScript frontend (Vite)
- FastAPI + Python backend
- Supabase PostgreSQL + authentication
- User-owned data with Row Level Security
- Full CRUD example feature
- Complete test coverage
- Ready for GitHub Copilot development

---

## Prerequisites

Before starting:

- [ ] GitHub account
- [ ] Supabase account (free tier available at supabase.com)
- [ ] Node.js 18+ installed locally
- [ ] Python 3.12+ installed locally
- [ ] Clear application idea (product domain)

---

## Workflow

### Step 1: Plan Your Application

**You define:**

**Product:**
- What problem does this app solve?
- Who is the target user?
- What is the core feature?
- What data model (entities/relationships)?

**Example:**
```
Product: Task Management App for Teams
Problem: Teams lose track of tasks across projects
User: Team lead managing 10 team members
Core Feature: Create tasks, assign to people, track status
Data Model: Teams → Projects → Tasks → Assigned users
```

**Technology:**
- Will you keep the default stack? (React/FastAPI/Supabase)
- Or customize any part? (Optional; requires more setup)

**Deployment:**
- Where will this run? (Vercel for frontend, suggested)
- What's your domain? (Optional; can use default first)

### Step 2: Fork the Factory Template

Clone the factory repository to start your project:

```bash
# Clone the factory
git clone https://github.com/yourusername/AI_FactorY.git my-app
cd my-app

# Create a new GitHub repository for your app
# (Keep factory as upstream to receive improvements)
git remote set-url origin https://github.com/yourusername/my-app.git

# Optional: Keep factory as upstream to sync improvements
git remote add factory https://github.com/yourusername/AI_FactorY.git
```

### Step 3: Customize for Your Domain

Update repository files to reflect your application:

**README.md:**
```markdown
# My App Name

[Your description]

## Features
- [Feature 1]
- [Feature 2]

## Getting Started
...
```

**Frontend (.env.example):**
```
VITE_APP_NAME=My App Name
VITE_API_URL=http://localhost:8000
```

**Backend (app/main.py):**
```python
app.title = "My App API"
app.description = "API for My App"
```

### Step 4: Set Up Supabase Project

1. Go to supabase.com
2. Create new project (free tier)
3. Get your credentials:
   - `SUPABASE_URL`
   - `SUPABASE_ANON_KEY`
   - `SUPABASE_SERVICE_ROLE_KEY`

4. Enable Row Level Security (RLS)
5. Add users (create test accounts)

### Step 5: Configure Environment Variables

**Backend (.env):**
```
SUPABASE_URL=your_supabase_url
SUPABASE_ANON_KEY=your_anon_key
SUPABASE_SERVICE_ROLE_KEY=your_service_role_key
```

**Frontend (.env.local):**
```
VITE_SUPABASE_URL=your_supabase_url
VITE_SUPABASE_ANON_KEY=your_anon_key
VITE_API_URL=http://localhost:8000
```

### Step 6: Set Up Database Schema

1. Replace the example `projects` table with your domain model
2. Create migrations in `supabase/migrations/`
3. Define RLS policies for your data

**Example: Task Management App**

Replace `projects` table with:
```sql
-- Teams
CREATE TABLE teams (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    name TEXT NOT NULL,
    owner_id UUID NOT NULL REFERENCES auth.users(id),
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW()
);

-- Tasks
CREATE TABLE tasks (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    team_id UUID NOT NULL REFERENCES teams(id),
    title TEXT NOT NULL,
    assigned_to UUID REFERENCES auth.users(id),
    status TEXT DEFAULT 'todo', -- todo, in_progress, done
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW()
);

-- Enable RLS
ALTER TABLE teams ENABLE ROW LEVEL SECURITY;
ALTER TABLE tasks ENABLE ROW LEVEL SECURITY;

-- RLS Policies
CREATE POLICY "Users can see teams they own"
    ON teams FOR SELECT
    USING (owner_id = auth.uid());

CREATE POLICY "Users can see tasks in their teams"
    ON tasks FOR SELECT
    USING (team_id IN (
        SELECT id FROM teams WHERE owner_id = auth.uid()
    ));
```

### Step 7: Update Backend Services

Replace the `ProjectService` with your domain services:

**Example: TaskService**
```python
# app/services/task.py

class TaskService:
    def __init__(self, db: Session):
        self.db = db
    
    async def get_tasks(self, user_id: UUID, team_id: UUID) -> list[TaskResponse]:
        """Get tasks in a team owned by user"""
        # Verify user owns team
        team = self.db.query(TeamModel).filter(
            TeamModel.id == team_id,
            TeamModel.owner_id == user_id,
        ).first()
        
        if not team:
            raise HTTPException(status_code=403)
        
        # Get tasks (RLS automatically applied)
        return self.db.query(TaskModel).filter(
            TaskModel.team_id == team_id
        ).all()
    
    async def create_task(self, req: CreateTaskRequest, user_id: UUID) -> TaskResponse:
        """Create task in a team owned by user"""
        # Verify team exists
        team = self.db.query(TeamModel).filter(
            TeamModel.id == req.team_id,
            TeamModel.owner_id == user_id,
        ).first()
        
        if not team:
            raise HTTPException(status_code=403)
        
        # Create task
        task = TaskModel(
            team_id=req.team_id,
            title=req.title,
            assigned_to=req.assigned_to,
        )
        self.db.add(task)
        self.db.commit()
        return task
```

### Step 8: Update Frontend Components

Replace ProjectList with your domain components:

**Example: TaskBoard**
```typescript
// src/pages/TasksPage.tsx

import { useEffect, useState } from 'react';
import { TaskList } from '../components/TaskList';
import { CreateTaskForm } from '../components/CreateTaskForm';

export const TasksPage: React.FC = () => {
  const [tasks, setTasks] = useState([]);
  const [loading, setLoading] = useState(true);
  
  useEffect(() => {
    fetchTasks();
  }, []);
  
  const fetchTasks = async () => {
    const response = await fetch('/api/v1/tasks');
    const data = await response.json();
    setTasks(data);
    setLoading(false);
  };
  
  if (loading) return <div>Loading...</div>;
  
  return (
    <div>
      <CreateTaskForm onTaskCreated={() => fetchTasks()} />
      <TaskList tasks={tasks} />
    </div>
  );
};
```

### Step 9: Set Up CI/CD

1. Create `.github/workflows/` directory (if not exists)
2. Add CI/CD workflows:
   - `test.yml` — Run tests on PR
   - `lint.yml` — Lint and type-check
   - `build.yml` — Build frontend/backend
   - `deploy-staging.yml` — Deploy to staging
   - `promote-production.yml` — Manual promotion to production

See [CI/CD Workflows](./../skills/ci-cd/workflows.md) for templates.

### Step 10: Verify Everything Works

**Start backend:**
```bash
cd backend
python -m venv venv
source venv/bin/activate
pip install -e ".[dev]"
python -m uvicorn app.main:app --reload
```

**Start frontend (new terminal):**
```bash
cd frontend
npm install
npm run dev
```

**Test:**
1. Navigate to http://localhost:5173
2. Sign up as a test user
3. Create a test entity (task, project, etc.)
4. Verify it appears in the list
5. Verify you can only see your own entities
5. Verify tests pass: `npm run test` and `pytest`

### Step 11: Document Your App

Update docs for your application:

**docs/product/README.md** — Product overview
**docs/product/features.md** — Feature list
**docs/architecture/README.md** — Architecture overview
**docs/architecture/data-model.md** — Your data model
**docs/api/README.md** — API documentation

### Step 12: Begin Development

Create your first feature using the [Start Feature](./../prompts/start-feature.prompt.md) prompt.

---

## Project Structure After Setup

```
my-app/
├── .github/
│   ├── workflows/           # CI/CD pipelines
│   ├── agents/             # Factory agents
│   ├── skills/             # Factory skills
│   └── prompts/            # Factory prompts
│
├── frontend/               # React app (update components/pages)
│   └── src/
│       ├── pages/          # Your pages (replace ProjectsPage)
│       ├── components/     # Your components
│       └── types/          # Your types
│
├── backend/                # FastAPI app (update services)
│   └── app/
│       ├── api/            # Your endpoints
│       ├── services/       # Your services
│       ├── models/         # Your database models
│       └── schemas/        # Your request/response schemas
│
├── supabase/               # Database (update schema)
│   └── migrations/         # Your schema migrations
│
└── docs/                   # Documentation (update for your app)
    ├── factory/            # Factory docs (keep as-is)
    ├── product/            # YOUR product docs
    ├── architecture/       # YOUR architecture docs
    └── api/                # YOUR API docs
```

---

## Key Files to Customize

| File | Changes |
|------|---------|
| README.md | Update app name and description |
| .github/workflows/* | Customize for your app (names, paths) |
| frontend/package.json | Update app name |
| backend/pyproject.toml | Update app name |
| supabase/migrations/*.sql | Replace projects table with your schema |
| docs/product/* | Create product-specific docs |
| docs/architecture/* | Document your architecture |

---

## Do NOT Change (Factory Core)

Keep these as-is to maintain factory benefits:

- `.github/agents/` (use existing agents)
- `.github/skills/` (use existing skills)
- `.github/prompts/` (use existing prompts)
- `.github/copilot-instructions.md` (base instructions)
- `docs/factory/` (factory documentation)

These are the factory; your customizations are separate.

---

## First Feature Workflow

Once project is set up:

1. **Use start-feature prompt** to discover first feature
2. **Product Agent** conducts discovery
3. **Get approval** (stakeholder)
4. **Architect Agent** designs solution
5. **Developer Agent** implements
6. **Test in staging**
7. **Deploy to production**

See [Factory Workflow](./../../docs/factory/factory-workflow.md) for full details.

---

## Deployment Setup (Optional)

### Vercel (Frontend)

```bash
# Push to GitHub
git push origin main

# Go to vercel.com, connect GitHub repository
# Vercel auto-deploys on every push to main
```

### Supabase (Backend + Database)

Already running in the cloud!

### Custom Backend Hosting (Optional)

If you want custom backend hosting (AWS, Google Cloud, etc.):

1. Create account
2. Set up PostgreSQL connection
3. Deploy FastAPI app
4. Configure environment variables
5. Update frontend API_URL

---

## Timeline

**Total setup time:** 2-4 hours
- Planning: 30 minutes
- Supabase setup: 30 minutes
- Code customization: 1-2 hours
- Testing: 30 minutes
- Deployment (optional): 1 hour

---

## Troubleshooting

**"Tests are failing"** → Check environment variables are set  
**"Frontend can't reach backend"** → Check VITE_API_URL in .env.local  
**"Authentication not working"** → Verify Supabase credentials  
**"Database table not found"** → Run migrations in Supabase  
**"RLS is blocking queries"** → Check RLS policies are correct  

See `docs/development.md` for more troubleshooting.

---

## Next Steps

1. ✅ Project set up and running locally
2. ✅ Database schema customized for your domain
3. ✅ Tests passing
4. ✅ CI/CD configured

**Now:** Start building features using the factory workflow!

Use the **start-feature** prompt for each new feature.

---

## Keep the Factory Updated

Over time, the factory will improve (new skills, better prompts, etc.).

**Keep improvements synced:**
```bash
# Pull latest factory improvements
git fetch factory
git merge factory/main

# Your app-specific changes stay separate
# Factory changes are backward compatible
```

---

## Support

**Questions about factory?** See `docs/factory/`  
**Questions about your app?** See `docs/`  
**Questions about development?** See `README.md` in frontend/backend/

Good luck building! 🚀
