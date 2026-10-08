-- Contract Analyzer Database Schema with Row Level Security

-- Enable UUID extension
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

-- Contracts table
CREATE TABLE contracts (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    lawyer_id UUID NOT NULL REFERENCES auth.users(id) ON DELETE CASCADE,
    title VARCHAR(255) NOT NULL,
    file_name VARCHAR(255) NOT NULL,
    file_url TEXT NOT NULL,
    parties TEXT[] DEFAULT ARRAY[]::TEXT[],
    key_dates JSONB DEFAULT '{}'::JSONB,
    obligations TEXT[] DEFAULT ARRAY[]::TEXT[],
    risk_score INTEGER DEFAULT 0,
    analysis_status VARCHAR(50) DEFAULT 'pending',
    created_at TIMESTAMP WITH TIME ZONE DEFAULT now(),
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT now()
);

-- Risk flags table
CREATE TABLE risk_flags (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    contract_id UUID NOT NULL REFERENCES contracts(id) ON DELETE CASCADE,
    lawyer_id UUID NOT NULL REFERENCES auth.users(id) ON DELETE CASCADE,
    severity VARCHAR(50) NOT NULL,
    title VARCHAR(255) NOT NULL,
    description TEXT NOT NULL,
    recommendation TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT now(),
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT now()
);

-- Analysis results table
CREATE TABLE analyses (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    contract_id UUID NOT NULL UNIQUE REFERENCES contracts(id) ON DELETE CASCADE,
    lawyer_id UUID NOT NULL REFERENCES auth.users(id) ON DELETE CASCADE,
    extracted_terms JSONB DEFAULT '{}'::JSONB,
    safe_clauses TEXT[] DEFAULT ARRAY[]::TEXT[],
    comparison_result JSONB DEFAULT '{}'::JSONB,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT now(),
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT now()
);

-- Enable RLS on contracts
ALTER TABLE contracts ENABLE ROW LEVEL SECURITY;

CREATE POLICY contracts_select_own ON contracts
    FOR SELECT USING (auth.uid() = lawyer_id);

CREATE POLICY contracts_insert_own ON contracts
    FOR INSERT WITH CHECK (auth.uid() = lawyer_id);

CREATE POLICY contracts_update_own ON contracts
    FOR UPDATE USING (auth.uid() = lawyer_id);

CREATE POLICY contracts_delete_own ON contracts
    FOR DELETE USING (auth.uid() = lawyer_id);

-- Enable RLS on risk_flags
ALTER TABLE risk_flags ENABLE ROW LEVEL SECURITY;

CREATE POLICY risk_flags_select_own ON risk_flags
    FOR SELECT USING (auth.uid() = lawyer_id);

CREATE POLICY risk_flags_insert_own ON risk_flags
    FOR INSERT WITH CHECK (auth.uid() = lawyer_id);

CREATE POLICY risk_flags_update_own ON risk_flags
    FOR UPDATE USING (auth.uid() = lawyer_id);

CREATE POLICY risk_flags_delete_own ON risk_flags
    FOR DELETE USING (auth.uid() = lawyer_id);

-- Enable RLS on analyses
ALTER TABLE analyses ENABLE ROW LEVEL SECURITY;

CREATE POLICY analyses_select_own ON analyses
    FOR SELECT USING (auth.uid() = lawyer_id);

CREATE POLICY analyses_insert_own ON analyses
    FOR INSERT WITH CHECK (auth.uid() = lawyer_id);

CREATE POLICY analyses_update_own ON analyses
    FOR UPDATE USING (auth.uid() = lawyer_id);

CREATE POLICY analyses_delete_own ON analyses
    FOR DELETE USING (auth.uid() = lawyer_id);

-- Create indexes
CREATE INDEX idx_contracts_lawyer_id ON contracts(lawyer_id);
CREATE INDEX idx_risk_flags_contract_id ON risk_flags(contract_id);
CREATE INDEX idx_risk_flags_lawyer_id ON risk_flags(lawyer_id);
CREATE INDEX idx_analyses_contract_id ON analyses(contract_id);
CREATE INDEX idx_analyses_lawyer_id ON analyses(lawyer_id);
