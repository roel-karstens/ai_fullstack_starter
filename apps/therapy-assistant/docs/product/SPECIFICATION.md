# Therapy Assistant - Product Specification

**Status**: 🚀 MVP Phase  
**Target Users**: Solo therapists, psychologists, coaches  
**Problem**: Therapists spend too much time on documentation; risk of missing patient insights  

---

## 🎯 Vision

An AI-powered platform that **automatically handles session admin**, freeing therapists to focus on patient care while collecting data for better outcomes.

---

## 👥 User Personas

### Primary: **Sofia, Solo Therapist**
- Runs practice alone
- 20-30 clients/week
- Spends 2 hours/day on notes, follow-ups, admin
- Frustrated with manual documentation
- Values privacy and data security
- Budget: $50-200/month

---

## 📋 User Journeys

### Journey 1: Session Recording & Note Taking

```
1. Sofia starts a session
2. Opens app, clicks "Start Session"
3. Microphone captures session audio (optional)
4. Sofia takes notes manually OR AI listens
5. Session ends
6. AI summarizes:
   - Key topics discussed
   - Client goals/concerns
   - Recommended actions
   - Next session focus
7. Sofia reviews & edits summary
8. Saved to client file
```

**Acceptance Criteria**:
- ✅ Sofia can start/stop sessions
- ✅ Audio optional (some therapists prefer manual)
- ✅ AI generates summary in <30 seconds
- ✅ Sofia can edit/approve before saving
- ✅ Summary saved to client record

---

### Journey 2: Track Client Progress

```
1. Sofia views client dashboard
2. Sees mood/symptom trends over time
3. Charts show: anxiety, depression, sleep, stress
4. AI highlights patterns:
   - "Client's anxiety spikes before work meetings"
   - "Mood improves after exercises are done"
5. Sofia can export report for client
```

**Acceptance Criteria**:
- ✅ Client dashboard shows all sessions
- ✅ Mood/symptom tracking over weeks/months
- ✅ Charts show trends
- ✅ AI identifies patterns
- ✅ Client can view progress (with permission)

---

### Journey 3: Between-Session Support (Optional)

```
1. Sofia adds a between-session task:
   - "Practice mindfulness 10 min daily"
   - "Track anxiety triggers"
2. Client logs in to app
3. Sees task list
4. Can message AI assistant
5. AI provides:
   - Guided exercises (breathing, grounding)
   - Homework check-ins
   - Crisis detection (alerts therapist if severe)
6. Sofia sees client engagement metrics
```

**Acceptance Criteria**:
- ✅ Therapist can create homework assignments
- ✅ Client gets reminders
- ✅ Client can message AI assistant
- ✅ AI responds with evidence-based techniques
- ✅ Crisis keywords trigger alert to therapist
- ✅ Therapist sees engagement metrics

---

## ✨ Core Features (MVP)

### For Therapists

**1. Session Management**
- Start/end session
- Auto-record audio (optional)
- Manual notes during session
- Session timer

**2. AI Session Summary**
- Automatic summarization via Claude
- Key topics extracted
- Client goals/concerns identified
- Action items listed
- Recommended next session focus
- Therapist can edit before saving

**3. Client Dashboard**
- List of all clients
- Quick stats (# sessions, last visit, mood trend)
- Client profile (name, email, contact)
- Session history
- Progress notes

**4. Analytics Dashboard**
- Total sessions this month
- Client mood trends (chart)
- Common themes/patterns
- Time spent per client
- Upcoming appointments

**5. Simple Between-Sessions**
- Client task list
- Task reminder notifications
- Basic message to AI assistant
- Simple mood/anxiety tracking

### For Clients (Optional v1)

**1. Client Portal**
- View assigned tasks/homework
- Log mood and symptoms
- Message with therapist
- Message with AI assistant
- View progress charts (therapist decides what to show)

**2. Basic AI Chatbot**
- Guided breathing exercises
- Grounding techniques
- CBT worksheets
- Homework reminders
- Crisis detection (flags to therapist)

---

## 🔧 Technical Requirements

### Database Schema (Supabase PostgreSQL)

**Tables**:
- `therapists` (account info, preferences)
- `clients` (name, contact, intake info, therapy focus)
- `sessions` (date, duration, notes, mood tracking)
- `ai_summaries` (session ID, summary, key topics, action items)
- `tasks` (homework assignments, status)
- `messages` (therapist-client, client-AI)
- `mood_tracking` (daily mood/anxiety/sleep/stress)

**RLS Policies**:
- Therapist can only see their own clients
- Clients can only see their own data
- AI summaries linked to sessions

---

### API Endpoints

**Therapist Endpoints**:
- `POST /api/v1/sessions` - Start session
- `PATCH /api/v1/sessions/{id}` - End session, add notes
- `POST /api/v1/sessions/{id}/summarize` - Trigger AI summary
- `GET /api/v1/clients` - List therapist's clients
- `GET /api/v1/clients/{id}` - Client details + sessions
- `GET /api/v1/analytics` - Dashboard metrics
- `POST /api/v1/tasks` - Create homework task
- `GET /api/v1/messages` - Conversations with clients

**Client Endpoints**:
- `GET /api/v1/tasks` - Assigned homework
- `POST /api/v1/mood-tracking` - Log mood/symptoms
- `GET /api/v1/progress` - View progress charts
- `POST /api/v1/messages` - Message therapist
- `POST /api/v1/ai-chat` - Chat with AI

**LLM Endpoints**:
- `/api/v1/ai/summarize-session` - Claude API wrapper
- `/api/v1/ai/detect-crisis` - Crisis detection
- `/api/v1/ai/suggest-exercise` - Recommend coping technique

---

### AI/LLM Integration

**Claude Prompts**:

1. **Session Summarization**
   - Input: Session notes/transcript
   - Output: Summary, topics, goals, action items
   - Tone: Clinical, concise

2. **Pattern Detection**
   - Input: Session history (5-10 sessions)
   - Output: Identified patterns, suggested interventions
   - Tone: Evidence-based recommendations

3. **Crisis Detection**
   - Input: Message from client
   - Output: Risk level (low/medium/high), alert recommendation
   - Tone: Cautious, immediate escalation if high

4. **Exercise Suggestion**
   - Input: Client's reported issue (anxiety, insomnia, etc.)
   - Output: Guided exercise (breathing, grounding, CBT)
   - Tone: Warm, supportive, step-by-step

---

## 🎨 Frontend Components

**Therapist Dashboard**:
- Session timer widget
- Notes text area
- Client list sidebar
- Analytics charts
- Task management panel

**Client Portal** (Optional v1):
- Task checklist
- Mood tracking form
- Progress chart
- Message threads
- Exercise library

---

## 📊 Non-Functional Requirements

**Security**:
- All data encrypted in transit (HTTPS)
- Patient data at rest encryption
- HIPAA-ready (though MVP may not be fully compliant)
- Session recordings optional & encrypted
- No data shared with third parties

**Privacy**:
- Therapist controls what client can see
- Clear consent for AI processing
- Data retention policies

**Performance**:
- Session summary generated <30 seconds
- Dashboard loads <2 seconds
- Mobile-friendly UI

**Reliability**:
- 99.5% uptime
- Automatic backups
- Graceful error handling

---

## 🚀 MVP Features (v0.1)

### Absolute Must-Have:
1. ✅ Session management (start/end)
2. ✅ AI session summarization
3. ✅ Client list + dashboard
4. ✅ Simple analytics
5. ✅ Authentication

### Nice-to-Have (v0.2):
6. Session recording (audio optional)
7. Between-session tasks
8. Basic client portal
9. Simple AI chatbot

### Future (v1.0+):
10. Advanced analytics
11. Integration with calendar
12. Team features
13. Mobile app

---

## 🎯 Acceptance Criteria for MVP

### Technical
- ✅ All tests pass
- ✅ Code quality: ESLint + Ruff
- ✅ Type safety: TypeScript + Pyright
- ✅ Security: No secrets in code
- ✅ No regressions in existing features

### Functional
- ✅ Therapist can create session + get AI summary
- ✅ AI summary is clinically meaningful
- ✅ Client list shows all therapist's clients
- ✅ Analytics dashboard shows trends
- ✅ Session history is searchable
- ✅ Export session notes to PDF

### UX
- ✅ Dashboard intuitive (therapist understands immediately)
- ✅ Session workflow < 2 clicks to start
- ✅ Summary review < 1 minute
- ✅ No confusing error messages
- ✅ Mobile-friendly design

### Security
- ✅ RLS policies prevent cross-user access
- ✅ API validates authentication
- ✅ Session data encrypted
- ✅ No PII in logs
- ✅ API keys in `.env` only

---

## 📈 Success Metrics

**User Adoption**:
- Therapist creates account
- Therapist records 1st session
- Therapist gets AI summary
- Therapist rates summary quality (target: >4/5)

**Usage**:
- Sessions recorded per day (target: >50% of actual sessions)
- Summary quality rating (target: >4/5)
- Client engagement (if portal included)

**Business**:
- Cost per user (target: <$20/month)
- Churn rate (target: <5%/month)
- NPS score (target: >50)

---

## 🔐 Privacy & Compliance Considerations

**HIPAA** (US):
- Requires BAA (Business Associate Agreement)
- Encryption in transit + at rest
- Access logs
- Audit trails
- v1.0 goal: fully HIPAA compliant

**GDPR** (EU/Netherlands):
- Right to be forgotten
- Data portability
- Clear privacy policy
- Consent management
- v1.0 goal: fully GDPR compliant

**MVP Approach**:
- Focus on privacy-by-design
- Clear data retention policies
- Therapist controls all data sharing
- Prepare for compliance later

---

## 📅 Timeline

**Week 1**: Product discovery, architecture, database schema  
**Week 2**: Implement session management + AI summary  
**Week 3**: Implement analytics + client dashboard  
**Week 4**: Testing, polish, deployment  

---

## 🚀 Next Steps

1. **Interview real therapists** (Sofia persona)
   - Validate the problem
   - Refine feature requirements
   - Understand compliance needs

2. **Create detailed wireframes**
   - Therapist dashboard
   - Session workflow
   - Analytics views

3. **Design database schema**
   - Review with security-reviewer agent
   - Plan migrations

4. **Begin implementation**
   - Backend: Session endpoints + AI integration
   - Frontend: Dashboard + session timer
   - Database: Schema + RLS policies

---

**Owner**: Roel Karstens  
**Created**: October 8, 2026  
**Status**: 🚀 Ready for development  
