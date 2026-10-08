# AI Software Factory: Development Workflow

**Version**: 1.0  
**Last Updated**: October 8, 2026

This document describes the canonical development workflow for the AI Software Factory.

---

## The Complete Lifecycle

```
IDEA
  ↓
PRODUCT DISCOVERY
  ├─ Understand problem
  ├─ Define user journeys
  ├─ Write acceptance criteria
  ├─ Document constraints
  ↓
PRODUCT APPROVAL GATE
  ├─ Requirements clear?
  ├─ Acceptance criteria testable?
  ├─ Stakeholders approve?
  ↓
GITHUB ISSUE CREATION
  ├─ Create issue from requirement
  ├─ Add "ready" label
  ↓
ARCHITECTURE DESIGN
  ├─ Architect reviews requirement
  ├─ Architect proposes approach
  ├─ Architect documents trade-offs
  ├─ Security agent reviews risks
  ↓
ARCHITECTURE APPROVAL GATE
  ├─ Solution feasible?
  ├─ Fits existing architecture?
  ├─ Security concerns addressed?
  ├─ Team approves?
  ↓
IMPLEMENTATION
  ├─ Developer inspects existing code
  ├─ Developer follows patterns
  ├─ Developer writes tests
  ├─ Developer creates migrations (if needed)
  ├─ Developer verifies on running system
  ↓
CI/CD VALIDATION GATE
  ├─ Linting passes
  ├─ Type checking passes
  ├─ Tests pass
  ├─ Builds succeed
  ↓
CODE REVIEW
  ├─ Reviewer checks: requirement compliance
  ├─ Reviewer checks: architecture compliance
  ├─ Reviewer checks: code quality
  ├─ Reviewer checks: test coverage
  ├─ Reviewer checks: no security issues
  ↓
SECURITY AUDIT GATE
  ├─ Security review for risks
  ├─ Authentication/authorization correct?
  ├─ Sensitive data protected?
  ├─ Input validation present?
  ↓
PULL REQUEST APPROVAL GATE
  ├─ Code reviewer approves or rejects
  ├─ Security reviewer approves or rejects
  ↓
STAGING DEPLOYMENT
  ├─ Merge PR to main
  ├─ CI/CD automatically builds and deploys to staging
  ↓
STAGING VERIFICATION
  ├─ You test in staging environment
  ├─ All features work as expected?
  ├─ No regressions?
  ↓
PRODUCTION PROMOTION GATE
  ├─ Manual human approval to promote
  ├─ Create release notes
  ↓
PRODUCTION DEPLOYMENT
  ├─ Manual promotion to production
  ├─ Monitoring activated
  ↓
MONITORING & ROLLBACK
  ├─ Watch logs and metrics
  ├─ Respond to issues
  ├─ If critical: rollback to previous version
  ↓
DONE
```

---

## Phase 1: Product Discovery (You + Product Agent)

**Duration**: Hours to days  
**Goal**: Understand the problem, define the feature

### Entry

**Input**: Raw idea or feature request

"Users want to export projects to CSV"

### Process

#### Step 1: Problem Discovery

**Who**: You + Product Agent  
**Time**: 15-30 minutes

**Questions to answer:**
- What problem does this solve?
- Who needs this?
- How severe is the problem?
- Why now?
- What have users tried before?

**Example conversation:**
```
You: "Users want to export projects to CSV"

Product Agent: "Why do they want to export? What will they do with the CSV?"

You: "They want to share project data with their managers in Excel"

Product Agent: "Do they need just project names, or all project details?"

You: "Names, due dates, and status"

Product Agent: "Do they need this manually or on a schedule?"

You: "Manually, when they want to share"
```

#### Step 2: User Journey Mapping

**Who**: Product Agent  
**Time**: 15-30 minutes

**Deliverable:**

```markdown
## Happy Path
1. User clicks "Export" button on project list
2. System generates CSV file
3. Browser downloads projects.csv
4. User can open in Excel

## Edge Cases
- What if user has no projects? (Show message, disable button)
- What if CSV is very large? (Show progress, handle timeout)
- What about authorization? (Only their projects, not other users')
```

#### Step 3: Acceptance Criteria

**Who**: Product Agent (you provide details)  
**Time**: 30 minutes

**Deliverable:**

```markdown
## Acceptance Criteria

**Must Have:**
- [ ] Clicking "Export" generates CSV file with all user's projects
- [ ] CSV includes columns: Name, Description, Due Date, Status, Owner
- [ ] Only projects owned by current user are included
- [ ] File downloads with name "projects-YYYY-MM-DD.csv"
- [ ] CSV is generated within 5 seconds

**Should Have:**
- [ ] User can select which columns to export
- [ ] CSV file can be imported back into system

**Non-Goals:**
- We are NOT implementing scheduled exports (future feature)
- We are NOT exporting to other formats (just CSV)
- We are NOT adding export templates
```

#### Step 4: Constraints & Non-Goals

**Who**: Product Agent  
**Time**: 15 minutes

**Deliverable:**

```markdown
## Constraints
- Must work on mobile browsers
- CSV file size < 10MB (no massive exports)
- Export must respect RLS (users can only export their own data)

## Non-Goals
- NOT exporting related entities (comments, tasks)
- NOT real-time export (on-demand only)
- NOT archived/deleted projects in CSV
```

### Output: Requirement Document

Product Agent produces a complete requirement in this format:

```markdown
# Feature: Export Projects to CSV

## Problem
Project managers need to share project data with their executives in Excel.
Currently they manually copy-paste from our system into Excel, which is error-prone.

## Target Users
- Project Manager: Wants to export and share project list with stakeholders

## User Journeys

### Happy Path: Export Projects
1. Manager clicks "Export" button
2. System generates CSV file
3. File downloads to computer
4. Manager opens in Excel and sends to stakeholders

### Error Case: No Projects
1. Manager with no projects clicks "Export"
2. System shows message "No projects to export"
3. Button is disabled

### Error Case: Large Export
1. Manager with 10,000 projects clicks "Export"
2. System shows "Generating..." progress
3. After 30 seconds, CSV downloads
4. If timeout (>60s), show error and let user try again

## Acceptance Criteria

**Must Have:**
- [ ] Clicking "Export" button generates CSV file
- [ ] CSV includes columns: Project Name, Description, Due Date, Status
- [ ] Only projects owned by current user appear in CSV
- [ ] CSV filename is "projects-YYYY-MM-DD.csv"
- [ ] Generation completes within 5 seconds
- [ ] Authorization is enforced (RLS applies)
- [ ] Works on desktop and mobile browsers

**Should Have:**
- [ ] User can customize which columns to include
- [ ] CSV includes all project properties

**Non-Goals:**
- NOT exporting comments or tasks (separate feature)
- NOT scheduled/automatic exports
- NOT importing CSV back into system

## Constraints

**Technical:**
- Must work with existing Supabase PostgreSQL
- No new database tables (use existing projects table)
- CSV must be generated server-side (security)

**Business:**
- Timeline: Ship in next 2 weeks
- Priority: Medium

**Compliance:**
- Must respect Row Level Security (users can only export their own data)
- No sensitive data should be logged

## Risks & Questions

**Unclear:**
- [ ] Should archived projects be included? (Assume NO)
- [ ] Should "created by" be different from "owner"? (Assume same)

**Risks:**
- Very large CSVs could time out → Implement pagination
- Users might expect to import CSV back → Clearly this is export only

## Next Steps
1. ✅ Requirement approved by stakeholders
2. Send to Architect for feasibility assessment
3. Create GitHub issue
4. Implement
```

### Exit: Product Approval Gate

**Decision Point**: Is this requirement ready for architecture?

**Checklist:**
- [ ] Problem is clearly stated (not just "users want CSV")
- [ ] User journeys are documented (happy path + errors)
- [ ] Acceptance criteria are testable (not vague)
- [ ] Non-goals are explicit (prevents scope creep)
- [ ] Constraints are documented
- [ ] Risks are surfaced
- [ ] Stakeholders have approved

**If YES**: Create GitHub issue with requirement  
**If NO**: Refine requirement with Product Agent until ready

---

## Phase 2: Architecture Design (Architect + Security)

**Duration**: Hours to days  
**Goal**: Design a solution, validate feasibility

### Entry

**Input**: Approved requirement (GitHub issue with requirement document)

### Process

#### Step 1: Understand Requirement

**Who**: Architect Agent  
**Time**: 15 minutes

- Read requirement document
- Understand acceptance criteria
- Ask clarifying questions (if needed)

#### Step 2: Analyze Current Architecture

**Who**: Architect Agent  
**Time**: 30 minutes

**Questions:**
- What existing patterns can we follow?
- Are there similar features already implemented? (CSV download, API responses)
- What components are affected? (Frontend, backend, database)
- What data flows are involved?

**Example research:**
```
1. Is there already a CSV export somewhere? 
   → Check ProjectService, similar endpoints
2. How do we generate files?
   → Search for "download", "export", "file"
3. How do we handle authorization?
   → Look at get_authorized_project() pattern
4. How do we handle large data?
   → Check existing pagination patterns
```

#### Step 3: Propose Approach

**Who**: Architect Agent  
**Time**: 30 minutes

**Deliverable:**

```markdown
## Proposal: Export Projects to CSV

### Approach

**Frontend:**
- Add "Export" button to ProjectList component
- Call new `/api/v1/projects/export` endpoint
- Browser handles file download automatically

**Backend:**
- New endpoint: `GET /api/v1/projects/export?format=csv`
- Service generates CSV from user's projects
- Returns with `Content-Disposition: attachment` header
- Python library: `csv` module (built-in)

**Database:**
- NO schema changes
- Query existing projects table with user's RLS
- Leverage existing authorization

### Why This Approach
- Minimal changes (reuses existing patterns)
- Secure (RLS applies on backend)
- Simple (built-in Python csv module)
- Scalable (server-side generation)

### Affected Components
- Frontend: ProjectList component (add button)
- Backend: projects.py (new endpoint), project_service.py (new method)
- Database: no changes (use existing queries)

### Benefits
- Reuses existing patterns
- No new dependencies
- RLS automatically applied
- Straightforward implementation

### Trade-offs
- Server does CSV generation (not client-side)
  - Pro: Secure (users only see what they own)
  - Pro: Handles large datasets better
  - Con: Slightly more server load
- No streaming (whole CSV in memory)
  - Pro: Simple
  - Con: Large CSVs might be slow
  - Mitigation: Add pagination if needed later

### Risks
- Large CSV generation could timeout
  → Mitigate: Test with realistic data sizes, add pagination if needed
- Users might expect to re-import CSV
  → Mitigate: Document export-only in UI

### Security Considerations
- Endpoint must require authentication ✅ (use existing dependency)
- Must respect RLS ✅ (query uses user_id)
- No sensitive data in CSV ✅ (only project names/dates/status)
- No sensitive logging ✅ (don't log CSV content)

### Implementation Estimate
- Frontend: 1-2 hours (button + API call)
- Backend: 2-3 hours (endpoint + CSV generation)
- Testing: 2-3 hours
- Total: ~6 hours

### Next Steps
1. Security agent reviews for risks
2. Get approval from architect/product
3. Create implementation plan
4. Developer implements
```

#### Step 4: Security Review

**Who**: Security Agent  
**Time**: 15-30 minutes

**Questions:**
- Is authentication enforced? (Yes, endpoint requires auth)
- Is authorization correct? (Yes, RLS applied)
- Could user A see user B's projects? (No, RLS prevents it)
- Is sensitive data exposed? (No, only public project info)
- Are there injection risks? (No, using csv module properly)
- Should the CSV be encrypted? (No, users own this data)
- Should export be logged? (Yes, but don't log content)

**Result**: Security approval or concerns

### Exit: Architecture Approval Gate

**Decision Point**: Is this architecture approved?

**Checklist:**
- [ ] Approach is feasible
- [ ] Fits existing architecture
- [ ] Reuses existing patterns (where possible)
- [ ] No unnecessary complexity
- [ ] Security considerations addressed
- [ ] Non-functional requirements met (performance, scalability)
- [ ] Known risks documented
- [ ] Team approves

**If YES**: Update GitHub issue with architecture  
**If NO**: Refine architecture or reconsider approach

---

## Phase 3: Implementation (Developer)

**Duration**: Hours to days  
**Goal**: Write working, tested code

### Entry

**Input**: Approved architecture (GitHub issue with architecture design)

### Process

#### Step 1: Inspect

**Who**: Developer Agent  
**Time**: 30-45 minutes

**Activities:**
- Read approval documents
- Look at existing similar features
- Identify patterns to follow
- Find where to add code

**Example checklist:**
```
Frontend:
- [ ] Find ProjectList component
- [ ] Understand how buttons are added
- [ ] Find similar API calls to reuse
- [ ] Check what hooks are used

Backend:
- [ ] Find projects.py routes
- [ ] Look at ProjectService methods
- [ ] Check how authorization works
- [ ] Find existing GET endpoints to follow

Testing:
- [ ] Check existing tests in test_projects.py
- [ ] See how API tests are structured
```

#### Step 2: Plan

**Who**: Developer Agent  
**Time**: 15-30 minutes

**Deliverable:**

```markdown
## Implementation Plan

### Frontend Changes
1. Open src/components/ProjectList.tsx
2. Find button section
3. Add export button next to existing buttons
4. Import and use fetchProjectsCSV() hook
5. Handle loading/error states

### Backend Changes
1. Open app/api/projects.py
2. Add new route: GET /api/v1/projects/export
3. Open app/services/project.py
4. Add method: export_to_csv(user_id)
5. Use Python csv module to generate CSV

### Testing
1. Test endpoint requires authentication (missing token → 401)
2. Test user only gets their projects (User A can't see User B's)
3. Test CSV format (correct columns, correct data)
4. Test with various project data

### Verification
1. Start backend
2. Create test user + projects
3. Call /api/v1/projects/export with curl
4. Verify CSV downloads correctly
5. Check data integrity
```

#### Step 3: Implement

**Who**: Developer Agent  
**Time**: 2-4 hours

**Activities:**

**Frontend:**
```typescript
// src/components/ProjectList.tsx

// Add button
<button onClick={handleExport}>
  {exporting ? "Exporting..." : "Export CSV"}
</button>

// Call API
const handleExport = async () => {
  try {
    const response = await fetch('/api/v1/projects/export');
    const blob = await response.blob();
    const url = window.URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = `projects-${new Date().toISOString().split('T')[0]}.csv`;
    a.click();
  } catch (error) {
    setError('Failed to export');
  }
};
```

**Backend:**
```python
# app/api/projects.py

@router.get("/export", response_class=FileResponse)
async def export_projects(
    user_id: UUID = Depends(get_current_user_id),
    service: ProjectService = Depends(),
) -> FileResponse:
    csv_content = await service.export_to_csv(user_id)
    
    return FileResponse(
        path=csv_content,
        filename=f"projects-{date.today()}.csv",
        media_type="text/csv",
    )

# app/services/project.py

async def export_to_csv(self, user_id: UUID) -> str:
    projects = self.db.query(ProjectModel).filter(
        ProjectModel.owner_id == user_id
    ).all()
    
    import csv
    import tempfile
    
    with tempfile.NamedTemporaryFile(mode='w', suffix='.csv', delete=False) as f:
        writer = csv.writer(f)
        writer.writerow(['Name', 'Description', 'Due Date', 'Status'])
        for project in projects:
            writer.writerow([
                project.name,
                project.description or '',
                project.due_date or '',
                project.status or 'active',
            ])
        return f.name
```

#### Step 4: Write Tests

**Who**: Developer Agent  
**Time**: 1-2 hours

**Test cases:**

```python
# tests/test_projects.py

@pytest.mark.asyncio
async def test_export_requires_auth():
    """Unauthenticated request should return 401"""
    response = client.get("/api/v1/projects/export")
    assert response.status_code == 401

@pytest.mark.asyncio
async def test_export_csv_format(auth_headers, test_project):
    """CSV should have correct format"""
    response = client.get(
        "/api/v1/projects/export",
        headers=auth_headers
    )
    assert response.status_code == 200
    assert response.headers["content-type"] == "text/csv"
    
    # Verify CSV content
    lines = response.text.split('\n')
    assert "Name" in lines[0]
    assert test_project.name in response.text

@pytest.mark.asyncio
async def test_export_only_user_projects(auth_headers, other_user_project):
    """User should only see their own projects in export"""
    response = client.get(
        "/api/v1/projects/export",
        headers=auth_headers
    )
    assert other_user_project.name not in response.text
```

#### Step 5: Verify on Running System

**Who**: Developer Agent  
**Time**: 30-45 minutes

**Activities:**

1. **Start backend and frontend**
   ```bash
   cd backend
   python -m uvicorn app.main:app --reload
   
   cd frontend
   npm run dev
   ```

2. **Create test data**
   - Sign up as test user
   - Create 3-5 test projects

3. **Test export**
   ```bash
   # Get auth token
   TOKEN=$(python scripts/generate_test_token.py)
   
   # Call export endpoint
   curl -H "Authorization: Bearer $TOKEN" \
     http://localhost:8000/api/v1/projects/export > projects.csv
   
   # Verify file
   cat projects.csv
   # Expected output:
   # Name,Description,Due Date,Status
   # Project 1,Demo,2024-12-31,active
   # Project 2,Test,2025-01-15,active
   ```

4. **Test in browser**
   - Open http://localhost:5173
   - Click "Export" button
   - Verify CSV downloads
   - Verify filename correct
   - Open CSV in Excel/text editor
   - Verify data correct

5. **Document evidence**
   - Screenshot of browser export
   - Screenshot of CSV opened in Excel
   - Test output from running tests

### Exit: Implementation Complete

**Checklist:**
- [ ] Code follows established patterns
- [ ] All acceptance criteria met
- [ ] Tests written and passing
- [ ] Verified on running system
- [ ] No regressions to existing features
- [ ] Ready for pull request

---

## Phase 4: Code Review

**Duration**: 30 minutes to hours  
**Goal**: Validate compliance with requirements and standards

### Entry

**Input**: Pull request with implementation

### Process

**Reviewer checks:**

1. **Requirement Compliance**
   - Does it meet acceptance criteria? ✅
   - Does it handle non-goals correctly? ✅

2. **Architecture Compliance**
   - Does it follow approved design? ✅
   - Does it reuse existing patterns? ✅
   - Is it unnecessarily complex? ✅

3. **Code Quality**
   - Types correct (no `any`)? ✅
   - Error handling present? ✅
   - Logging appropriate? ✅
   - Code readable? ✅

4. **Test Coverage**
   - Happy path tested? ✅
   - Error cases tested? ✅
   - Authorization tested? ✅

5. **Security**
   - Authentication enforced? ✅
   - Authorization correct? ✅
   - Sensitive data protected? ✅
   - No obvious vulnerabilities? ✅

### Exit: Review Decision

**Options:**
- ✅ **APPROVED** → Proceed to security review
- 🔄 **CHANGES REQUESTED** → Developer refines
- ❌ **REJECTED** → Rework required

---

## Phase 5: Security Audit

**Duration**: 30 minutes to hours  
**Goal**: Validate security controls

### Entry

**Input**: Code review approved

### Process

**Security checks:**

1. **Authentication**
   - Is endpoint protected? ✅
   - Does it verify JWT token? ✅
   - Does it extract user_id correctly? ✅

2. **Authorization**
   - Does user A see user B's data? ❌ (No, RLS blocks it)
   - Are ownership checks present? ✅
   - Is RLS applied correctly? ✅

3. **Data Protection**
   - Is sensitive data encrypted? ✅ (CSV is user's own data)
   - Is PII handled correctly? ✅ (No leakage)
   - Is data logged safely? ✅ (No CSV content in logs)

4. **Input Validation**
   - Are parameters validated? ✅ (No user input to this endpoint)
   - Are there injection risks? ✅ (No, using csv module)

5. **Error Handling**
   - Do errors leak information? ✅ (Generic error messages)
   - Are stack traces hidden? ✅ (User only sees "Export failed")

### Exit: Security Decision

**Options:**
- ✅ **APPROVED** → Ready for merge
- 🔄 **CHANGES REQUESTED** → Developer fixes
- ❌ **REJECTED** → Security risk must be addressed

---

## Phase 6: Merge & Deploy to Staging

**Duration**: Minutes to 5 minutes  
**Goal**: Deploy to staging automatically

### Process

1. **All gates passed**
   - Code review: ✅ APPROVED
   - Security audit: ✅ APPROVED
   - CI/CD: ✅ PASSED (tests, lint, build)

2. **Merge PR**
   ```bash
   # GitHub UI: Click "Squash and merge"
   # or from terminal:
   git merge --squash feature/export-csv
   git push origin main
   ```

3. **CI/CD Triggered**
   - Runs lint + type-check
   - Runs tests
   - Builds frontend (Vite)
   - Builds backend (setup.py)

4. **Staging Deployment**
   - If CI passes, automatically deploy to staging
   - Frontend deployed to staging URL
   - Backend deployed to staging API

### Exit: Ready for Validation

**Output:**
- Staging environment has new feature
- Release notes drafted
- Ready for you to test

---

## Phase 7: Staging Validation

**Duration**: 30 minutes to hours  
**Goal**: Validate feature in realistic environment

### Entry

**Input**: Feature deployed to staging

### Process

**You test in staging:**

1. **Navigate to staging environment**
   - Frontend: https://staging.app.yourdomain.com
   - Backend: https://api-staging.app.yourdomain.com

2. **Reproduce acceptance criteria**
   - Sign in as test user
   - Create test projects
   - Click "Export" button
   - Download CSV
   - Verify columns and data

3. **Check error cases**
   - Sign out, try export (should get 401)
   - Try to export with no projects (should show message)
   - Try large export (should handle gracefully)

4. **Verify no regressions**
   - Existing features still work
   - Other project operations unaffected
   - UI loads correctly
   - No console errors (F12)

5. **Document approval**
   ```markdown
   # Staging Validation: Export CSV

   ✅ Feature works as expected
   ✅ CSV downloads correctly
   ✅ Format is correct (headers, columns)
   ✅ Only user's projects included
   ✅ Error handling works
   ✅ No regressions to existing features
   ✅ Tested on mobile and desktop
   
   **Approved for production**
   ```

### Exit: Promotion Gate

**Decision Point**: Is this ready for production?

**Options:**
- ✅ **APPROVED** → Promote to production
- 🔄 **CHANGES NEEDED** → Report issue, developer fixes
- ❌ **REJECTED** → Rollback, investigate, retry

---

## Phase 8: Production Promotion

**Duration**: Minutes  
**Goal**: Deploy to production with human approval

### Entry

**Input:** Staging validation approved

### Process

1. **Create release notes**
   ```markdown
   # Release v1.5.0: Export Projects to CSV
   
   ## New Features
   - Users can now export all projects to CSV
   - Exported file includes: Name, Description, Due Date, Status
   - File is automatically named with current date
   
   ## How to Use
   1. Go to Projects page
   2. Click "Export" button
   3. CSV downloads to your computer
   4. Open in Excel or your favorite spreadsheet app
   
   ## Technical Changes
   - New endpoint: GET /api/v1/projects/export
   - New service method: ProjectService.export_to_csv()
   
   ## Known Limitations
   - Export includes only your own projects
   - Export is on-demand (not scheduled)
   - Exports up to 10,000 rows
   
   ## Rollback Plan
   If issues found:
   git revert <commit-hash>
   git push origin main
   # Wait 5 minutes for redeploy
   ```

2. **Manual approval**
   ```
   ✅ Staging validation: APPROVED
   ✅ Security audit: APPROVED
   ✅ Code review: APPROVED
   ✅ Release notes ready: YES
   ✅ Rollback plan ready: YES
   
   PROCEED TO PRODUCTION: YES / NO
   ```

3. **Promote to production**
   ```bash
   # Tag release
   git tag -a v1.5.0 -m "Export CSV feature"
   git push origin v1.5.0
   
   # Deploy (manual trigger in CI/CD)
   # CI/CD runs same tests, builds, deploys to production
   # Frontend: https://app.yourdomain.com
   # Backend: https://api.app.yourdomain.com
   ```

### Exit: Live in Production

**Checklist:**
- [ ] Frontend updated
- [ ] Backend running
- [ ] Database in sync
- [ ] Monitoring active
- [ ] On-call alert ready

---

## Phase 9: Post-Launch Monitoring

**Duration**: First hour, then ongoing  
**Goal**: Catch and respond to issues

### First Hour

**Monitor:**
- Error logs (any 500 errors?)
- API latency (slower than staging?)
- User reports (any issues in Slack?)

**Be ready to:**
- Rollback if critical bug found
- Hotfix if minor issue found
- Communicate status if investigating

### Ongoing

**Monitor:**
- Feature adoption (are users using export?)
- Performance (is export fast enough?)
- Errors (any edge cases we missed?)
- User feedback (do they like it?)

### Exit: Feature Stable

Once monitoring shows:
- No errors for 24 hours
- Good performance metrics
- User feedback is positive
- Feature is stable

**Then: DONE** ✅

---

## Summary

| Phase | Duration | Who | Gate | Input | Output |
|-------|----------|-----|------|-------|--------|
| 1. Discovery | Hours | You + Product | Stakeholder approval | Idea | Requirement doc |
| 2. Architecture | Hours | Architect | Team approval | Requirement | Architecture doc |
| 3. Implementation | Hours/days | Developer | CI/CD pass | Architecture | Pull request |
| 4. Code Review | Hours | Reviewer | Review approval | PR | Code approved |
| 5. Security | Hours | Security | Security approval | PR | Security approved |
| 6. Merge & Deploy | Minutes | CI/CD | Auto | Merge | Staging live |
| 7. Validation | Hours | You | Manual approval | Staging | Promotion approved |
| 8. Production | Minutes | CI/CD | Manual promotion | Approval | Production live |
| 9. Monitoring | Days | You | Stability | Production | Feature stable |

**Total time:** 1-2 weeks for a medium feature (discovery → production)

---

## How to Start

To begin a new feature using this workflow:

1. **Have an idea** → Start Phase 1 (Product Discovery)
2. **Use prompt** → `start-feature.prompt.md` guides you through Phase 1
3. **Get approval** → Gate 1 (Product Approval)
4. **Invoke Architect** → Phase 2 (Architecture Design)
5. **Get approval** → Gate 2 (Architecture Approval)
6. **Invoke Developer** → Phase 3 (Implementation)
7. **Pull request** → Phases 4-6 (Review → Staging)
8. **Test staging** → Phase 7 (Staging Validation)
9. **Promote** → Phase 8 (Production)

Each phase has clear inputs, outputs, and quality gates. No skipping gates.
