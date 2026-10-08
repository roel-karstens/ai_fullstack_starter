-- Energy Platform Database Schema with Row Level Security

-- Enable UUID extension
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

-- Consultants table (energy consultants)
CREATE TABLE consultants (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    consultant_id UUID NOT NULL UNIQUE REFERENCES auth.users(id) ON DELETE CASCADE,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    company VARCHAR(255),
    phone VARCHAR(20),
    expertise TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT now(),
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT now()
);

-- Clients table (commercial properties)
CREATE TABLE clients (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    consultant_id UUID NOT NULL REFERENCES auth.users(id) ON DELETE CASCADE,
    name VARCHAR(255) NOT NULL,
    industry VARCHAR(255),
    contact_name VARCHAR(255),
    contact_email VARCHAR(255),
    contact_phone VARCHAR(20),
    address TEXT,
    city VARCHAR(255),
    state VARCHAR(50),
    postal_code VARCHAR(20),
    country VARCHAR(255),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT now(),
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT now()
);

-- Buildings table
CREATE TABLE buildings (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    consultant_id UUID NOT NULL REFERENCES auth.users(id) ON DELETE CASCADE,
    client_id UUID NOT NULL REFERENCES clients(id) ON DELETE CASCADE,
    name VARCHAR(255) NOT NULL,
    address TEXT NOT NULL,
    city VARCHAR(255),
    state VARCHAR(50),
    postal_code VARCHAR(20),
    country VARCHAR(255),
    building_type VARCHAR(100), -- warehouse, office, retail, etc.
    square_feet INTEGER,
    annual_energy_cost DECIMAL(12, 2),
    current_utilities JSONB DEFAULT '{}'::JSONB, -- gas, electric, water
    created_at TIMESTAMP WITH TIME ZONE DEFAULT now(),
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT now()
);

-- Recommendations table
CREATE TABLE recommendations (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    consultant_id UUID NOT NULL REFERENCES auth.users(id) ON DELETE CASCADE,
    building_id UUID NOT NULL REFERENCES buildings(id) ON DELETE CASCADE,
    category VARCHAR(100) NOT NULL, -- HVAC, Lighting, Insulation, Solar, Water
    title VARCHAR(255) NOT NULL,
    description TEXT,
    annual_savings DECIMAL(12, 2),
    implementation_cost DECIMAL(12, 2),
    payback_years DECIMAL(5, 2),
    priority VARCHAR(50), -- High, Medium, Low
    status VARCHAR(50) DEFAULT 'pending', -- pending, approved, implemented
    created_at TIMESTAMP WITH TIME ZONE DEFAULT now(),
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT now()
);

-- Analysis results table
CREATE TABLE analyses (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    consultant_id UUID NOT NULL REFERENCES auth.users(id) ON DELETE CASCADE,
    building_id UUID NOT NULL UNIQUE REFERENCES buildings(id) ON DELETE CASCADE,
    current_spend DECIMAL(12, 2),
    estimated_savings DECIMAL(12, 2),
    roi_percentage DECIMAL(5, 2),
    recommendation_count INTEGER DEFAULT 0,
    analysis_date TIMESTAMP WITH TIME ZONE DEFAULT now(),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT now(),
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT now()
);

-- Enable RLS on consultants
ALTER TABLE consultants ENABLE ROW LEVEL SECURITY;

CREATE POLICY consultants_select_own ON consultants
    FOR SELECT USING (auth.uid() = consultant_id);

CREATE POLICY consultants_insert_own ON consultants
    FOR INSERT WITH CHECK (auth.uid() = consultant_id);

CREATE POLICY consultants_update_own ON consultants
    FOR UPDATE USING (auth.uid() = consultant_id);

CREATE POLICY consultants_delete_own ON consultants
    FOR DELETE USING (auth.uid() = consultant_id);

-- Enable RLS on clients
ALTER TABLE clients ENABLE ROW LEVEL SECURITY;

CREATE POLICY clients_select_own ON clients
    FOR SELECT USING (auth.uid() = consultant_id);

CREATE POLICY clients_insert_own ON clients
    FOR INSERT WITH CHECK (auth.uid() = consultant_id);

CREATE POLICY clients_update_own ON clients
    FOR UPDATE USING (auth.uid() = consultant_id);

CREATE POLICY clients_delete_own ON clients
    FOR DELETE USING (auth.uid() = consultant_id);

-- Enable RLS on buildings
ALTER TABLE buildings ENABLE ROW LEVEL SECURITY;

CREATE POLICY buildings_select_own ON buildings
    FOR SELECT USING (auth.uid() = consultant_id);

CREATE POLICY buildings_insert_own ON buildings
    FOR INSERT WITH CHECK (auth.uid() = consultant_id);

CREATE POLICY buildings_update_own ON buildings
    FOR UPDATE USING (auth.uid() = consultant_id);

CREATE POLICY buildings_delete_own ON buildings
    FOR DELETE USING (auth.uid() = consultant_id);

-- Enable RLS on recommendations
ALTER TABLE recommendations ENABLE ROW LEVEL SECURITY;

CREATE POLICY recommendations_select_own ON recommendations
    FOR SELECT USING (auth.uid() = consultant_id);

CREATE POLICY recommendations_insert_own ON recommendations
    FOR INSERT WITH CHECK (auth.uid() = consultant_id);

CREATE POLICY recommendations_update_own ON recommendations
    FOR UPDATE USING (auth.uid() = consultant_id);

CREATE POLICY recommendations_delete_own ON recommendations
    FOR DELETE USING (auth.uid() = consultant_id);

-- Enable RLS on analyses
ALTER TABLE analyses ENABLE ROW LEVEL SECURITY;

CREATE POLICY analyses_select_own ON analyses
    FOR SELECT USING (auth.uid() = consultant_id);

CREATE POLICY analyses_insert_own ON analyses
    FOR INSERT WITH CHECK (auth.uid() = consultant_id);

CREATE POLICY analyses_update_own ON analyses
    FOR UPDATE USING (auth.uid() = consultant_id);

CREATE POLICY analyses_delete_own ON analyses
    FOR DELETE USING (auth.uid() = consultant_id);

-- Create indexes
CREATE INDEX idx_consultants_consultant_id ON consultants(consultant_id);
CREATE INDEX idx_clients_consultant_id ON clients(consultant_id);
CREATE INDEX idx_buildings_consultant_id ON buildings(consultant_id);
CREATE INDEX idx_buildings_client_id ON buildings(client_id);
CREATE INDEX idx_recommendations_consultant_id ON recommendations(consultant_id);
CREATE INDEX idx_recommendations_building_id ON recommendations(building_id);
CREATE INDEX idx_analyses_consultant_id ON analyses(consultant_id);
CREATE INDEX idx_analyses_building_id ON analyses(building_id);
CREATE INDEX idx_projects_created_at ON public.projects(created_at DESC);
