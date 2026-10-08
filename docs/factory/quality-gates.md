# AI Software Factory: Quality Gates

**Version**: 1.0  
**Last Updated**: October 8, 2026

Quality gates are mandatory approval points. Agents do NOT bypass gates. If a gate requires approval, work pauses until a human decides.

---

## Gate 1: Product Approval

**When**: After product discovery, before architecture  
**Who Approves**: Product stakeholder (user/manager) or Product agent after stakeholder consultation  
**Time**: Same day  

### Checklist

- [ ] **Problem is clear** — Anyone reading it understands what we're solving
- [ ] **User is specific** — Not "users" or "people", but "project managers" or "account admins"
- [ ] **User journey documented** — Happy path AND error cases defined
- [ ] **Acceptance criteria testable** — Each criterion can be verified (not vague)
- [ ] **Non-goals explicit** — Scope creep is prevented
- [ ] **Constraints identified** — Technical, business, and compliance constraints documented
- [ ] **Risks surfaced** — Known risks and uncertain assumptions listed
- [ ] **Stakeholder approved** — Product owner/manager has reviewed and approved

### What Blocks a Gate

❌ **Vague acceptance criteria**
- "Users can search" → ✅ "Users can type in search box and see matching projects"

❌ **Missing user information**
- "Someone should be able to..." → ✅ "Project managers should be able to..."

❌ **Unconstrained scope**
- "Add reporting" → ✅ "Add export projects to CSV" (specific)

❌ **Unstated non-goals**
- "Export" without clarifying "not in real-time" or "not scheduled"

### How to Unblock

1. **Product agent asks clarifying questions** (don't guess)
2. **Stakeholder provides answers**
3. **Requirement is refined**
4. **Retry gate**

### Decision: APPROVED / CHANGES REQUESTED / REJECTED

**APPROVED**: Move to Phase 2 (Architecture)  
**CHANGES REQUESTED**: Refine requirement, retry gate  
**REJECTED**: Archive issue, document why

---

## Gate 2: Architecture Approval

**When**: After architecture design, before implementation  
**Who Approves**: Architect agent (you can override)  
**Time**: 1 day  

### Checklist

- [ ] **Solution is feasible** — Can it actually be built with our stack?
- [ ] **Fits existing architecture** — Doesn't violate established patterns
- [ ] **Reuses existing code** — Leverages existing components/services (where possible)
- [ ] **No unnecessary complexity** — Simplest appropriate solution
- [ ] **Trade-offs documented** — What we're choosing and why
- [ ] **Risks identified** — What could go wrong?
- [ ] **Performance acceptable** — Will it be fast enough?
- [ ] **Scalability considered** — Will it handle growth?
- [ ] **Security implications clear** — Are there auth/authz/data concerns?
- [ ] **API contract defined** — Request/response shapes clear
- [ ] **Database schema (if needed)** — New tables/columns planned
- [ ] **Estimate provided** — Rough effort (hours/days)
- [ ] **Team alignment** — Architect approves or has concerns noted

### What Blocks a Gate

❌ **Violates existing architecture**
- "Let's add a message queue" when our system is request-response
- "Let's use a new framework" when we're standardized on React/FastAPI

❌ **Over-engineered**
- "Build a plugin system" for a single export feature
- "Add microservices" for a monolithic app

❌ **Insufficient design**
- "Just implement it" without defining API contracts
- "We'll figure out the schema" during coding

❌ **Security concerns unaddressed**
- "Handle user authentication later"
- "We'll add encryption if needed"

❌ **Performance not considered**
- "It will probably be fast enough"
- No estimate of data volume or query complexity

### How to Unblock

1. **Architect refines design** (ask clarifying questions)
2. **Address concerns** (simplify, add security checks, estimate better)
3. **Get security agent review** (if relevant)
4. **Retry gate**

### Decision: APPROVED / CHANGES REQUESTED / REJECTED

**APPROVED**: Move to Phase 3 (Implementation)  
**CHANGES REQUESTED**: Refine architecture, retry gate  
**REJECTED**: Archive issue, explore alternative approaches

---

## Gate 3: CI/CD Validation

**When**: Before code review  
**Who Approves**: Automated (GitHub Actions)  
**Time**: Automatic (5-10 minutes)  

### Checks

**Frontend**
- [ ] ESLint passes (no linting errors)
- [ ] TypeScript strict mode passes (no type errors)
- [ ] Vitest passes (all tests pass)
- [ ] Vite build succeeds (production build works)
- [ ] No type regressions (compared to main)

**Backend**
- [ ] Ruff passes (no linting errors)
- [ ] Pyright passes (no type errors in strict mode)
- [ ] pytest passes (all tests pass)
- [ ] Build succeeds (can import and run)
- [ ] No dependency conflicts

**Database**
- [ ] Migrations valid SQL
- [ ] Migrations are idempotent (can run twice)

### What Blocks a Gate

❌ **Test failures** → All tests must pass
❌ **Linting errors** → Code must be formatted
❌ **Type errors** → No `any` types allowed
❌ **Build failure** → Code must compile/build successfully
❌ **Coverage regression** → Test coverage must not decrease

### How to Unblock

1. **Developer fixes failing tests**
2. **Developer fixes linting errors**
3. **Developer fixes type errors**
4. **Push to branch**
5. **CI/CD reruns automatically**

### Decision: PASSED / FAILED

**PASSED**: Proceed to code review  
**FAILED**: Fix issues and retry

---

## Gate 4: Code Review

**When**: After CI/CD passes, before security review  
**Who Approves**: Code reviewer (human)  
**Time**: Same day to 1 day  

### Checklist

- [ ] **Requirement compliance** — Does it meet all acceptance criteria?
- [ ] **Requirement completeness** — Are all acceptance criteria covered?
- [ ] **Architecture compliance** — Does it follow the approved design?
- [ ] **Pattern adherence** — Does it reuse existing patterns or unnecessarily deviate?
- [ ] **Code quality** — Is the code readable and maintainable?
- [ ] **Type safety** — No `any` types; all types appropriate?
- [ ] **Error handling** — Error cases handled (not just happy path)?
- [ ] **Logging** — Logging present without exposing sensitive data?
- [ ] **Comments** — Complex logic explained; obvious code not over-commented?
- [ ] **Test coverage** — Do tests cover acceptance criteria?
- [ ] **Test quality** — Do tests actually verify behavior (not just mock)?
- [ ] **No regressions** — Existing tests still pass?
- [ ] **Migrations correct** — (If DB changes) Migrations are safe and reversible?
- [ ] **Documentation updated** — README, API docs, environment variables?
- [ ] **Unnecessary complexity** — Is there obvious simplification?
- [ ] **Performance** — Any obvious performance issues?

### What Blocks a Gate

❌ **Doesn't meet acceptance criteria** → Fix or clarify criteria  
❌ **Violates approved architecture** → Refactor to match  
❌ **Poor code quality** → Refactor for readability  
❌ **Insufficient test coverage** → Add tests  
❌ **Unhandled error cases** → Add error handling  
❌ **Type errors** → Fix typing  
❌ **Unexplained complexity** → Simplify or document  

### How to Unblock

1. **Reviewer provides feedback** (specific, actionable)
2. **Developer makes requested changes**
3. **Push to branch**
4. **Reviewer reviews changes**
5. **Retry gate**

### Decision: APPROVED / CHANGES REQUESTED / REJECTED

**APPROVED**: Proceed to security review  
**CHANGES REQUESTED**: Developer refines, retry gate  
**REJECTED**: Requires significant rework; discuss alternatives

---

## Gate 5: Security Audit

**When**: After code review passes, before merge  
**Who Approves**: Security agent (human)  
**Time**: Same day  

### Checklist

- [ ] **Authentication enforced** — Is the endpoint protected by JWT token?
- [ ] **Authorization correct** — Does user A see user B's data?
- [ ] **RLS applied** — (For data endpoints) Are Row Level Security policies enforced?
- [ ] **Input validation** — Are all inputs validated and sanitized?
- [ ] **Injection protection** — No SQL injection, XSS, or other injection risks?
- [ ] **Sensitive data handling** — Passwords, tokens, keys never logged or exposed?
- [ ] **Encryption** — Is data encrypted at rest and in transit (where needed)?
- [ ] **Error messages** — Do error responses leak information?
- [ ] **Dependencies safe** — No known vulnerabilities in added packages?
- [ ] **Secret management** — Credentials in environment variables, not hardcoded?
- [ ] **CORS configured** — Cross-origin requests properly restricted?
- [ ] **Rate limiting** — (For APIs) Is rate limiting configured?
- [ ] **Logging secure** — Sensitive data not logged?
- [ ] **HTTPS in production** — (For web apps) Will run over HTTPS?

### What Blocks a Gate

❌ **No authentication** → "Endpoint has no auth; anyone can call it"  
❌ **Authorization bypassed** → "User A can see User B's private data"  
❌ **RLS missing** → "Endpoint doesn't filter by user"  
❌ **SQL injection risk** → "User input used in SQL without sanitization"  
❌ **Secrets exposed** → "API key hardcoded in source"  
❌ **Unencrypted sensitive data** → "Passwords stored in plain text"  
❌ **Information leakage** → "Error message reveals database structure"  
❌ **Vulnerable dependency** → "New package has known CVE"  

### How to Unblock

1. **Security agent identifies issues** (specific, actionable)
2. **Developer fixes security issues** (not workarounds, real fixes)
3. **Security agent reviews fixes**
4. **Retry gate**

### Decision: APPROVED / CHANGES REQUESTED / REJECTED

**APPROVED**: Ready for merge  
**CHANGES REQUESTED**: Developer fixes security issues, retry gate  
**REJECTED**: Security risk too high; requires significant redesign

---

## Gate 6: Merge to Main

**When**: After code review and security audit approved  
**Who Approves**: Developer (with CI/CD)  
**Time**: Automatic  

### Process

```bash
# All gates must pass
✅ Code review: APPROVED
✅ Security audit: APPROVED
✅ CI/CD: PASSED

# Developer merges via GitHub
# or from terminal:
git merge --squash feature-branch
git push origin main

# Automatically triggers CI/CD
```

### Automatic Actions

1. **Final CI/CD run**
   - Lint + type-check
   - Tests
   - Build

2. **Staging deployment** (if CI passes)
   - Frontend → staging environment
   - Backend → staging environment
   - Database → staging database

### Exit: Staging Live

Feature is now running in staging environment, ready for validation.

---

## Gate 7: Staging Validation

**When**: After feature deployed to staging  
**Who Approves**: You (human)  
**Time**: 1-2 hours  

### Checklist

- [ ] **Feature works** — Can I use the feature end-to-end?
- [ ] **Acceptance criteria met** — Does it do what was promised?
- [ ] **Error cases handled** — What if something goes wrong? Are errors clear?
- [ ] **Performance acceptable** — Is it fast enough? Does it feel responsive?
- [ ] **No regressions** — Did I break any existing features?
- [ ] **UI/UX correct** — Does it look right? Is it usable?
- [ ] **Cross-browser** — Works on Chrome, Firefox, Safari?
- [ ] **Mobile-friendly** — Works on phone and tablet?
- [ ] **Data integrity** — Is data saved correctly? Can I see it in database?
- [ ] **Logging helpful** — Can I find issues in logs?
- [ ] **Documentation accurate** — Do docs match actual behavior?

### What Blocks a Gate

❌ **Feature doesn't work** → Breaks user journey  
❌ **Acceptance criteria unmet** → Doesn't match requirement  
❌ **Severe bug** → Feature is unusable  
❌ **Major regression** → Broke existing feature  
❌ **Performance issue** → Too slow to be usable  
❌ **Data loss** → Feature corrupts or loses data  
❌ **Security issue** → Found security problem in staging  

### How to Unblock

1. **Test in staging** and document findings
2. **If bug found:**
   - Escalate to developer (don't approve)
   - Developer fixes in new PR
   - Retry gate from code review
3. **If validation fails:**
   - Document why (be specific)
   - Escalate to Product/Architect
   - May need requirement or architecture change

### Decision: APPROVED / CHANGES NEEDED / REJECTED

**APPROVED**: Ready for production  
**CHANGES NEEDED**: Bug found; developer fixes and retries from code review  
**REJECTED**: Fundamental issue; requires rework

---

## Gate 8: Production Promotion

**When**: After staging validation approved  
**Who Approves**: You (human)  
**Time**: Same day or next business day  

### Pre-Flight Checklist

- [ ] **Staging validation: APPROVED**
- [ ] **Code review: APPROVED**
- [ ] **Security audit: APPROVED**
- [ ] **CI/CD: PASSED**
- [ ] **Release notes: READY**
- [ ] **Rollback plan: READY**
- [ ] **On-call team: NOTIFIED**
- [ ] **Monitoring: CONFIGURED**

### Release Notes Required

```markdown
# Release v1.5.0: [Feature Name]

## What Changed
[User-facing description]

## How to Use
[Steps for users to find/use feature]

## Technical Details
[Backend changes, database changes, API changes]

## Known Limitations
[What we didn't include; what still needs work]

## Rollback Plan
[How to undo if needed]
```

### Rollback Plan Required

```markdown
# Rollback Steps

If critical issue found:
1. Trigger rollback CI/CD job
2. Verify production reverted
3. Investigate issue
4. Report to team
```

### Approval Decision

```
✅ All gates passed?              YES / NO
✅ Staging validation approved?   YES / NO
✅ Release notes complete?        YES / NO
✅ Rollback plan ready?          YES / NO
✅ Team ready?                   YES / NO

APPROVE PRODUCTION PROMOTION?    YES / NO
```

### Decision: APPROVED / HOLD / REJECTED

**APPROVED**: Deploy to production  
**HOLD**: Not ready; wait for clarity  
**REJECTED**: Don't deploy; escalate concerns

---

## Gate 9: Post-Launch Monitoring

**When**: First 24 hours after production deployment  
**Who Monitors**: On-call developer + automated alerts  
**Time**: Continuous monitoring  

### Alerts Configured

- [ ] Error rate spike (>5% 500 errors)
- [ ] Response time spike (>2x baseline)
- [ ] Database connection errors
- [ ] Memory/CPU usage spike
- [ ] Failed deployments

### Monitoring Checklist

- [ ] Check logs for errors (first 1 hour)
- [ ] Check metrics (latency, error rate, throughput)
- [ ] Spot-check feature (can I use it?)
- [ ] Check user reports (Slack, email, support)
- [ ] Document status in incident channel

### When to Rollback

**Rollback immediately if:**
- Data loss or corruption
- Security issue discovered
- Feature completely broken (>50% users affected)
- Database unreachable
- Payment processing failed

**Escalate if:**
- Mild performance degradation (users can still use)
- Minor bugs (obvious workarounds)
- Documentation issues
- Non-critical feature broken

### Decision: STABLE / DEGRADED / ROLLBACK

**STABLE**: Monitor for 24 more hours  
**DEGRADED**: Acknowledge issue, fix while live or rollback  
**ROLLBACK**: Trigger rollback, investigate offline

---

## When Gates Can Be Overridden

Gates can ONLY be overridden by the appropriate human decision-maker with explicit documentation:

### Can Override Product Gate

**Who**: Stakeholder / Product Manager  
**Reason**: "We don't have time for full discovery; shipping best-guess anyway"  
**Risk**: Feature might not solve real problem; rework likely  
**Documentation**: "Product gate overridden by [Name] on [Date] because [reason]"

### Can Override Architecture Gate

**Who**: Architect / Engineering Manager  
**Reason**: "Simple MVP; fine to ship without full architecture review"  
**Risk**: Feature might not fit long-term architecture; refactor later  
**Documentation**: "Architecture gate overridden by [Name] on [Date] because [reason]"

### Can Override Code Review

**Who**: Tech Lead / Engineering Manager  
**Reason**: "Critical hotfix; shipping without full review"  
**Risk**: Code quality lower; bugs more likely  
**Documentation**: "Code review gate overridden by [Name] on [Date] because [reason]"

### Can Override Security Audit

**Who**: Security Officer / CISO  
**Reason**: "Accepting known risk; shipping anyway"  
**Risk**: Security vulnerability in production  
**Documentation**: "Security gate overridden by [Name] on [Date] because [reason]. Risk: [X]. Mitigation: [Y]"

### Can NEVER Override

- [ ] Staging validation (you must test in staging)
- [ ] CI/CD pass (must build and tests pass)
- [ ] Production promotion approval (must explicitly approve)

---

## Gate Dashboard

Track status of each gate in a simple format:

```markdown
# Feature: Export Projects to CSV

| Gate | Status | Date | Notes |
|------|--------|------|-------|
| 1. Product | ✅ APPROVED | Oct 8 | Stakeholder reviewed |
| 2. Architecture | ✅ APPROVED | Oct 8 | Fits existing patterns |
| 3. CI/CD | ✅ PASSED | Oct 9 | All tests pass |
| 4. Code Review | ✅ APPROVED | Oct 9 | Ready for production |
| 5. Security | ✅ APPROVED | Oct 9 | No auth/authz issues |
| 6. Merge | ✅ COMPLETE | Oct 9 | Merged to main |
| 7. Staging | ✅ VALIDATED | Oct 9 | Tested and working |
| 8. Production | ✅ APPROVED | Oct 9 | Deployed to production |
| 9. Monitoring | ✅ STABLE | Oct 10 | No errors for 24h |

**Overall**: ✅ SHIPPED
```

---

## Summary

Gate -> Responsible -> Blocks If -> Unblocks By -> Timeline
1. Product | Stakeholder | Vague requirement | Clear requirement | Same day
2. Architecture | Architect | Infeasible/complex | Better design | 1 day
3. CI/CD | Automated | Failed test/lint | Fix code | Immediate
4. Code Review | Reviewer | Violates standards | Refactor code | Same day
5. Security | Security | Auth/authz missing | Add security checks | Same day
6. Merge | CI/CD | Any gate fails | All gates pass | Automatic
7. Staging | You | Broken/regressed | Fix in new PR | 1-2 hours
8. Production | You | Concerns raised | Resolve before promotion | Manual
9. Monitoring | On-call | Critical issue | Rollback or hotfix | Continuous

**NO SKIPPING GATES.**
