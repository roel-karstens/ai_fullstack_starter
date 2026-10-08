# Feature Map

**Purpose**: Document all user-facing features and the tests that verify them.

Use this to:
- Understand what your app can do
- Identify test coverage per feature
- Verify nothing is untested
- Track which features are complete

**Keep this in sync**: Whenever you add/remove a feature, update this map.

---

## Features

### Authentication

**User Can Sign Up**
- Frontend: AuthPage signup form
- Backend: POST /api/v1/auth/signup
- Tests:
  - test_auth_signup_success
  - test_auth_signup_validation (missing email, weak password)
  - test_auth_signup_duplicate_email
- Acceptance: User can create account with email/password, receives confirmation

**User Can Log In**
- Frontend: AuthPage login form
- Backend: POST /api/v1/auth/login
- Tests:
  - test_auth_login_success
  - test_auth_login_invalid_password
  - test_auth_login_missing_credentials
- Acceptance: User can log in with email/password, receives JWT token

**User Can Log Out**
- Frontend: Logout button in navbar
- Backend: Session invalidation
- Tests:
  - test_auth_logout
- Acceptance: User can log out, JWT token invalidated

**User Can Reset Password**
- Frontend: Password reset form
- Backend: POST /api/v1/auth/reset-password
- Tests:
  - test_auth_reset_password_flow
  - test_auth_reset_token_expires
- Acceptance: User can reset password via email link

---

### Projects (Example Feature)

**User Can Create Project**
- Frontend: ProjectForm component, CreateProjectPage
- Backend: POST /api/v1/projects
- Tests:
  - test_projects_create_success
  - test_projects_create_missing_fields
  - test_projects_create_unauthorized (no auth)
  - test_projects_create_validation
- Acceptance: User can create project with name and description, sees it in list

**User Can View Own Projects**
- Frontend: ProjectListPage
- Backend: GET /api/v1/projects
- Database: RLS policy ensures only owned projects returned
- Tests:
  - test_projects_list_success
  - test_projects_list_empty
  - test_projects_list_authorization (user can't see other users' projects)
- Acceptance: User sees their projects in a list, can't see other users' projects

**User Can Edit Own Project**
- Frontend: EditProjectPage
- Backend: PATCH /api/v1/projects/{id}
- Tests:
  - test_projects_update_success
  - test_projects_update_unauthorized
  - test_projects_update_validation
- Acceptance: User can edit project name/description, changes persist

**User Can Delete Own Project**
- Frontend: Delete button in project detail
- Backend: DELETE /api/v1/projects/{id}
- Tests:
  - test_projects_delete_success
  - test_projects_delete_unauthorized
  - test_projects_delete_already_deleted
- Acceptance: User can delete project, project disappears from list

**User Can Export Projects to CSV**
- Frontend: Export button in ProjectList
- Backend: GET /api/v1/projects/export
- Tests:
  - test_projects_export_csv_format
  - test_projects_export_authorization
  - test_projects_export_empty
  - test_projects_export_large
- Acceptance: User can export projects to CSV, file downloads, contains correct data

---

## Test Coverage Summary

| Feature | Unit | Integration | E2E | Coverage |
|---------|------|-------------|-----|----------|
| Sign Up | ✅ | ✅ | ⏳ | 90% |
| Log In | ✅ | ✅ | ⏳ | 85% |
| Log Out | ✅ | ✅ | ⏳ | 100% |
| Reset Password | ✅ | ⏳ | ❌ | 70% |
| Create Project | ✅ | ✅ | ✅ | 95% |
| View Projects | ✅ | ✅ | ✅ | 90% |
| Edit Project | ✅ | ✅ | ✅ | 85% |
| Delete Project | ✅ | ✅ | ✅ | 90% |
| Export to CSV | ✅ | ✅ | ⏳ | 80% |

**Legend:**
- ✅ Complete
- ⏳ In Progress / Partial
- ❌ Missing

---

## Critical Paths (Must Have Tests)

These user journeys must be fully tested:

### Path 1: User Signup → Create Project → Export
1. Sign up as new user ✅
2. Create project ✅
3. Export to CSV ✅

### Path 2: User Login → Edit Project
1. Log in as existing user ✅
2. View projects ✅
3. Edit project ✅

### Path 3: Authorization Checks
1. User A cannot see User B's projects ✅
2. User A cannot edit User B's projects ✅
3. User A cannot delete User B's projects ✅

---

## Recently Added / Changed

| Date | Feature | Change | Tests Updated |
|------|---------|--------|----------------|
| Oct 8 | Export to CSV | New | ✅ |
| Oct 5 | Edit Project | Enhanced validation | ✅ |
| Oct 1 | Delete Project | Added soft-delete option | ⏳ |

---

## Known Gaps

**Features missing tests:**
- [ ] Export file performance with 10,000+ projects
- [ ] Concurrent edits to same project
- [ ] Special characters in project names

**Features not yet implemented:**
- [ ] Search projects by name
- [ ] Filter projects by status
- [ ] Project sharing with team members
- [ ] Real-time collaboration

---

## Test Execution

### Run All Tests

**Backend:**
```bash
cd backend
pytest
```

**Frontend:**
```bash
cd frontend
npm run test
```

### Run Tests for Specific Feature

**Example: Projects**
```bash
cd backend
pytest -k "project"

cd frontend
npm run test -- ProjectList
```

### Run With Coverage

**Backend:**
```bash
pytest --cov=app --cov-report=html
# Open htmlcov/index.html
```

**Frontend:**
```bash
npm run test -- --coverage
# See coverage in terminal
```

---

## Maintenance

**When adding a new feature:**
1. Add feature to Feature Map
2. Add test cases to the feature entry
3. Update Test Coverage Summary
4. Run full test suite
5. Verify coverage maintained/improved

**When deleting a feature:**
1. Remove feature entry
2. Delete corresponding tests
3. Update Feature Map
4. Commit: "Remove [feature] and tests"

**Weekly:**
- Verify Feature Map matches actual app
- Run full test suite
- Check for untested features
- Update coverage metrics

---

## Statistics

**Total Features:** 9  
**Total Test Cases:** 42  
**Average Coverage:** 87%  
**Status:** 🟢 Healthy  

**Trends:**
- Coverage improving (was 82% last month)
- All critical paths have >85% coverage
- No regression in test count

---

## Integration with Verification Skill

When verifying a feature works:

1. **Find feature in Feature Map**
2. **Identify its test cases**
3. **Run those tests locally**
4. **Verify in running app** (DRIVE phase)
5. **Collect proof** (EVIDENCE phase)
6. **Update map if new tests added**

Example:
```
Feature: User Can Export to CSV
Tests: test_projects_export_csv_format, test_projects_export_authorization
Running tests: ✅ All pass
Verification: ✅ Tested in staging, CSV format correct, only owns projects included
Evidence: curl response, CSV file contents, database query
Status: ✅ VERIFIED
```

---

## Approval Checklist

Before marking feature as "done":

- [ ] Feature documented in Feature Map
- [ ] All acceptance criteria listed
- [ ] All test cases documented
- [ ] Tests written and passing
- [ ] Coverage >80%
- [ ] Verified on running system (EVIDENCE collected)
- [ ] No regressions
- [ ] Documentation updated

---

**Last Updated**: [Date]  
**Updated By**: [Name]  
**Next Review**: [Date]  
