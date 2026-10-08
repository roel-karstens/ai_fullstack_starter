# Energy Platform - Product Specification

**Status**: 🚀 MVP Phase  
**Target Users**: Energy consultants, facilities managers, sustainability advisors  
**Problem**: Analyzing energy consumption manually is tedious; clients need clear recommendations  

---

## 🎯 Vision

An AI-powered platform that **automatically analyzes utility bills, identifies savings opportunities, and calculates ROI**, turning raw data into actionable recommendations.

---

## 👥 User Personas

### Primary: **Lisa, Energy Consultant**
- Advises small businesses on energy efficiency
- Analyzes 10+ buildings/month
- Spends 3-4 hours per building analyzing bills
- Needs to quantify savings potential for clients
- Budget: $80-200/month

---

## 📋 Core Features (MVP)

### 1. Client & Building Management
- Create client profiles
- Add multiple buildings per client
- Building profile: size, type, location, year built, occupancy
- Upload utility bills (electric, gas, water)

**Acceptance Criteria**:
- ✅ Create client + buildings
- ✅ Upload utility bills (PDF, CSV, manual entry)
- ✅ Parse bill data (consumption, costs, rates)
- ✅ Historical tracking (12+ months)

---

### 2. Consumption Analysis
- AI analyzes consumption patterns:
  - Peak vs off-peak usage
  - Seasonal variations
  - Anomalies (unusual spikes)
  - Usage per square foot (benchmarking)
- Compare to regional/national benchmarks
- Identify inefficiencies

**Acceptance Criteria**:
- ✅ Consumption charts show trends
- ✅ Seasonal patterns identified
- ✅ Benchmark comparison
- ✅ Anomaly detection (alerts on unusual usage)

---

### 3. AI Optimization Recommendations
- AI analyzes building profile + consumption patterns
- Recommends improvements:
  - **HVAC**: Thermostat optimization, scheduling, maintenance
  - **Lighting**: LED conversion, occupancy sensors
  - **Building envelope**: Insulation, weatherstripping, window upgrades
  - **Renewable**: Solar feasibility, payback period
  - **Water**: Fixture upgrades, leak detection
- Prioritized by impact & cost

**Acceptance Criteria**:
- ✅ AI generates personalized recommendations
- ✅ Each recommendation includes:
  - Estimated savings (kWh/year, $)
  - Implementation cost
  - Payback period
  - Risk level (proven vs experimental)
- ✅ Recommendations prioritized by ROI

---

### 4. ROI & Savings Calculator
- Calculate:
  - Annual savings potential
  - Implementation costs
  - Payback period
  - 5-year & 10-year projections
  - Incentives/rebates available
- Interactive: adjust assumptions, recalculate

**Acceptance Criteria**:
- ✅ Savings calculator transparent (shows assumptions)
- ✅ Conservative estimates (under-promise, over-deliver)
- ✅ Payback period clearly stated
- ✅ Incentive lookup (local rebates)

---

### 5. Client Reports
- Generate professional PDF report:
  - Executive summary
  - Current energy spend + benchmarks
  - Consumption analysis (charts)
  - Top recommendations (prioritized)
  - ROI projections (5-year, 10-year)
  - Implementation roadmap
  - Next steps

**Acceptance Criteria**:
- ✅ PDF report professional & clear
- ✅ Charts are easy to understand
- ✅ Recommendations ranked by ROI
- ✅ Implemention timeline included

---

### 6. Progress Tracking
- Track implementation of recommendations
- Monitor savings after implementation
- Compare actual vs projected
- Track multiple buildings simultaneously

**Acceptance Criteria**:
- ✅ Consultant can mark recommendations as implemented
- ✅ Updated bill data compared to baseline
- ✅ Actual savings vs projected displayed
- ✅ Multi-building dashboard

---

## 🔧 Technical Requirements

### Database Schema

**Tables**:
- `consultants` (account info, preferences)
- `clients` (name, contact, industry, location)
- `buildings` (address, size, type, year_built, occupancy)
- `utility_bills` (date, type, consumption, cost)
- `consumption_analysis` (building, analysis data, benchmarks)
- `recommendations` (building, type, savings, cost, payback, status)
- `reports` (building, timestamp, generated_by, data)
- `actual_results` (recommendation, post-implementation consumption, actual_savings)

---

### API Endpoints

**Client & Building Management**:
- `POST /api/v1/clients` - Create client
- `GET /api/v1/clients` - List clients
- `POST /api/v1/buildings` - Add building
- `GET /api/v1/buildings/{id}` - Building details

**Utility Data**:
- `POST /api/v1/buildings/{id}/utility-bills` - Upload bill
- `GET /api/v1/buildings/{id}/utility-bills` - Bill history
- `POST /api/v1/buildings/{id}/parse-bill` - Parse PDF bill

**Analysis & Recommendations**:
- `POST /api/v1/buildings/{id}/analyze` - Trigger AI analysis
- `GET /api/v1/buildings/{id}/consumption-analysis` - Get consumption data
- `GET /api/v1/buildings/{id}/recommendations` - Get recommendations
- `PATCH /api/v1/recommendations/{id}` - Update recommendation (mark implemented)

**Reports**:
- `POST /api/v1/buildings/{id}/generate-report` - Generate PDF report
- `GET /api/v1/reports` - Report history
- `GET /api/v1/reports/{id}` - Get report

**Analytics**:
- `GET /api/v1/analytics` - Dashboard metrics
- `GET /api/v1/buildings/{id}/savings-tracking` - Actual vs projected

---

### AI/LLM Integration

**Claude Prompts**:

1. **Consumption Analysis**
   - Input: Bill history, building profile
   - Output: Pattern analysis, inefficiencies identified, benchmarking
   - Tone: Technical but accessible

2. **Optimization Recommendations**
   - Input: Building profile + consumption patterns
   - Output: Prioritized recommendations with savings estimates
   - Tone: Professional, optimistic but realistic

3. **ROI Calculations**
   - Input: Recommendation + local costs + incentives
   - Output: Implementation cost, annual savings, payback period
   - Tone: Conservative, show assumptions

4. **Report Generation**
   - Input: All analysis data
   - Output: Executive summary, findings, recommendations, next steps
   - Tone: Professional, persuasive for clients

---

## 📊 MVP Features

**Must-Have**:
1. Client + building management
2. Utility bill upload & parsing
3. Consumption analysis (trends, benchmarks)
4. AI recommendations (HVAC, lighting, insulation, renewables)
5. ROI calculator
6. PDF report generation
7. Dashboard + analytics

**Nice-to-Have (v0.2)**:
8. Progress tracking (post-implementation monitoring)
9. Actual savings verification
10. Incentive/rebate lookup
11. Multi-consultant teams

**Future (v1.0+)**:
12. Integration with utility APIs (automate bill collection)
13. IoT sensor data integration
14. Advanced modeling (weather-normalized consumption)
15. Contractor marketplace (find installers)

---

## 🎯 Acceptance Criteria for MVP

### Technical
- ✅ All tests pass
- ✅ Code quality checks pass
- ✅ Type safety verified
- ✅ No security issues
- ✅ PDF generation works reliably

### Functional
- ✅ Can create client + buildings
- ✅ Can upload utility bills (PDF, CSV, manual)
- ✅ Bill parsing 95%+ accurate
- ✅ AI generates meaningful recommendations
- ✅ ROI calculator accurate
- ✅ PDF report professional & complete
- ✅ Dashboard shows key metrics

### UX
- ✅ Upload workflow intuitive
- ✅ Analysis results clearly displayed
- ✅ Recommendations ranked by ROI
- ✅ Report looks professional

### Security
- ✅ Consultant can only see own clients
- ✅ Client data encrypted
- ✅ No sensitive data in logs
- ✅ Secure file upload/download

---

## 📈 Success Metrics

- Buildings analyzed per month
- Average savings projected per building
- Report generation time <2 minutes
- User retention (target: <10% churn/month)
- Consultant satisfaction with recommendations

---

## 🚀 Timeline

**Week 1**: Requirements, architecture, schema  
**Week 2**: Implement client mgmt + bill parsing  
**Week 3**: Implement analysis + recommendations  
**Week 4**: Report generation, polish, deployment  

---

**Owner**: Roel Karstens  
**Created**: October 8, 2026  
**Status**: 🚀 Ready for development  
