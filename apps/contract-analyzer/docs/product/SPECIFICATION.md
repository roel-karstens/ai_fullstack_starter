# Contract Analyzer - Product Specification

**Status**: 🚀 MVP Phase  
**Target Users**: Solo lawyers, legal consultants, contract reviewers  
**Problem**: Reading & analyzing contracts is time-consuming; easy to miss risks  

---

## 🎯 Vision

An AI-powered platform that **instantly extracts key terms, flags risks, and recommends protections** in contracts, turning hours of review into minutes.

---

## 👥 User Personas

### Primary: **Marco, Solo Lawyer**
- Runs solo practice or small firm
- Reviews 5-10 contracts/week
- Spends 2-4 hours analyzing each contract
- Worried about missing liability clauses
- Needs efficiency to stay competitive
- Budget: $100-300/month

---

## 📋 Core Features (MVP)

### 1. Contract Upload & Analysis
- Upload PDF or text file
- AI extracts:
  - Parties involved
  - Key dates (start, end, renewal, termination)
  - Financial terms (amounts, payment schedule)
  - Obligations (what each party must do)
  - Liabilities & indemnification
  - Termination clauses
  - Dispute resolution

**Acceptance Criteria**:
- ✅ Upload any contract (PDF, Word, TXT)
- ✅ Extraction completes <2 minutes
- ✅ Extracted terms are 90%+ accurate
- ✅ Missing terms highlighted

---

### 2. Risk Flagging
- AI identifies potential risks:
  - **Red flags**: Unusual payment terms, indefinite liability, one-sided obligations
  - **Yellow flags**: Vague definitions, missing enforcement clauses, poor dispute language
  - **Green**: Standard safe language
- Severity score (1-10)
- Explanation for each flag

**Acceptance Criteria**:
- ✅ Common risks detected automatically
- ✅ Lawyer can review risk classifications
- ✅ Lawyer can override/add risks
- ✅ Risk summary exportable

---

### 3. Template Library
- Standard contract templates (NDA, Service Agreement, Purchase Agreement, Employment)
- Compare current contract to template
- Highlight deviations
- Suggest safer language

**Acceptance Criteria**:
- ✅ At least 5 template contracts
- ✅ Side-by-side comparison view
- ✅ Suggests "safer" clauses from templates
- ✅ Lawyer can create custom templates

---

### 4. Contract Comparison
- Compare 2+ versions of same contract
- Highlight changes
- AI explains significance of each change

**Acceptance Criteria**:
- ✅ Upload 2 contract versions
- ✅ Show differences in sidebar
- ✅ AI explains what changed and impact

---

### 5. Analytics Dashboard
- Contracts processed this month
- Risk distribution (% high/medium/low)
- Common risks across all contracts
- Processing time trends
- Client history (which clients' contracts reviewed)

**Acceptance Criteria**:
- ✅ Dashboard shows key metrics
- ✅ Searchable contract history
- ✅ Export analytics report

---

## 🔧 Technical Requirements

### Database Schema

**Tables**:
- `lawyers` (account info, templates)
- `contracts` (file, upload date, extracted data)
- `extracted_terms` (party, date, amount, obligation, etc.)
- `risk_flags` (severity, explanation, resolution)
- `templates` (template name, clauses, standard language)
- `comparisons` (v1 contract, v2 contract, differences)

---

### API Endpoints

**Contract Upload & Analysis**:
- `POST /api/v1/contracts` - Upload contract
- `GET /api/v1/contracts/{id}` - Get contract + extracted terms
- `GET /api/v1/contracts/{id}/risks` - Get risk flags
- `POST /api/v1/contracts/{id}/risks` - Add/edit risk

**Template Management**:
- `GET /api/v1/templates` - List templates
- `POST /api/v1/templates` - Create custom template
- `POST /api/v1/contracts/{id}/compare-template` - Compare to template

**Contract Comparison**:
- `POST /api/v1/comparisons` - Compare 2 contracts
- `GET /api/v1/comparisons/{id}` - Get differences

**Analytics**:
- `GET /api/v1/analytics` - Dashboard metrics

---

### AI/LLM Integration

**Claude Prompts**:

1. **Extract Key Terms**
   - Input: Contract text
   - Output: Structured JSON with parties, dates, amounts, obligations
   - Tone: Legal, precise

2. **Identify Risks**
   - Input: Contract text
   - Output: List of risks with severity, explanation, recommendation
   - Tone: Cautious, expert

3. **Compare Contracts**
   - Input: 2 contract versions
   - Output: List of changes with legal significance
   - Tone: Analytical

4. **Suggest Safer Language**
   - Input: Risky clause + template clauses
   - Output: Suggested alternative language
   - Tone: Professional, protective

---

## 📊 MVP Features

**Must-Have**:
1. Contract upload (PDF/text)
2. Term extraction (parties, dates, amounts, obligations)
3. Risk flagging (auto-detect common risks)
4. Risk management (lawyer reviews, adds, resolves risks)
5. Dashboard + contract history

**Nice-to-Have (v0.2)**:
6. Template library + comparison
7. Contract comparison (version diff)
8. PDF export with risk report
9. Email collaboration (share with other lawyers)

**Future (v1.0+)**:
10. OCR for scanned contracts
11. Signature management
12. E-signature integration
13. Contract renewal alerts
14. Clause library (AI-tagged clauses)

---

## 🎯 Acceptance Criteria for MVP

### Technical
- ✅ All tests pass
- ✅ Code quality checks pass
- ✅ Type safety verified
- ✅ No security issues
- ✅ No regressions

### Functional
- ✅ Can upload contract (PDF, text, Word)
- ✅ AI extracts terms within 2 minutes
- ✅ Extraction accuracy >90%
- ✅ Risk flags detected automatically
- ✅ Lawyer can manage risks
- ✅ Dashboard shows analytics
- ✅ Contract history searchable

### UX
- ✅ Upload workflow is intuitive
- ✅ Extracted terms clearly displayed
- ✅ Risk list prioritized by severity
- ✅ Dashboard at a glance

### Security
- ✅ Contracts encrypted at rest
- ✅ RLS prevents cross-user access
- ✅ No contract content in logs
- ✅ Secure upload/download

---

## 📈 Success Metrics

- Contracts uploaded per month
- Risk detection accuracy (lawyer feedback)
- Time saved per contract (estimated vs actual)
- User retention (target: <5% churn/month)

---

## 🚀 Timeline

**Week 1**: Requirements, architecture, schema  
**Week 2**: Implement upload + term extraction  
**Week 3**: Implement risk flagging + analytics  
**Week 4**: Polish, testing, deployment  

---

**Owner**: Roel Karstens  
**Created**: October 8, 2026  
**Status**: 🚀 Ready for development  
