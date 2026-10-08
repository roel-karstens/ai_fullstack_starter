-- Therapy Assistant Initial Schema
-- Tables: therapists, clients, sessions, ai_summaries, tasks, messages, mood_tracking

-- Therapists table (extends auth.users)
CREATE TABLE IF NOT EXISTS public.therapists (
  id UUID PRIMARY KEY REFERENCES auth.users(id) ON DELETE CASCADE,
  name TEXT NOT NULL,
  email TEXT NOT NULL UNIQUE,
  phone TEXT,
  license_number TEXT,
  specialization TEXT,
  bio TEXT,
  created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Clients table
CREATE TABLE IF NOT EXISTS public.clients (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  therapist_id UUID NOT NULL REFERENCES public.therapists(id) ON DELETE CASCADE,
  name TEXT NOT NULL,
  email TEXT,
  phone TEXT,
  date_of_birth DATE,
  presenting_issues TEXT,
  notes TEXT,
  status TEXT DEFAULT 'active' CHECK (status IN ('active', 'inactive', 'discharged')),
  created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Sessions table
CREATE TABLE IF NOT EXISTS public.sessions (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  therapist_id UUID NOT NULL REFERENCES public.therapists(id) ON DELETE CASCADE,
  client_id UUID NOT NULL REFERENCES public.clients(id) ON DELETE CASCADE,
  session_date TIMESTAMP WITH TIME ZONE NOT NULL,
  duration_minutes INTEGER,
  notes TEXT,
  mood_before INTEGER CHECK (mood_before >= 1 AND mood_before <= 10),
  mood_after INTEGER CHECK (mood_after >= 1 AND mood_after <= 10),
  created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- AI Summaries table
CREATE TABLE IF NOT EXISTS public.ai_summaries (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  session_id UUID NOT NULL UNIQUE REFERENCES public.sessions(id) ON DELETE CASCADE,
  summary TEXT,
  key_topics TEXT[],
  goals TEXT[],
  action_items TEXT[],
  recommended_focus TEXT,
  created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Tasks (homework) table
CREATE TABLE IF NOT EXISTS public.tasks (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  therapist_id UUID NOT NULL REFERENCES public.therapists(id) ON DELETE CASCADE,
  client_id UUID NOT NULL REFERENCES public.clients(id) ON DELETE CASCADE,
  title TEXT NOT NULL,
  description TEXT,
  due_date DATE,
  status TEXT DEFAULT 'pending' CHECK (status IN ('pending', 'completed', 'skipped')),
  created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Messages table (therapist-client)
CREATE TABLE IF NOT EXISTS public.messages (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  sender_id UUID NOT NULL REFERENCES auth.users(id) ON DELETE CASCADE,
  recipient_id UUID NOT NULL REFERENCES auth.users(id) ON DELETE CASCADE,
  content TEXT NOT NULL,
  is_from_ai BOOLEAN DEFAULT FALSE,
  message_type TEXT DEFAULT 'text' CHECK (message_type IN ('text', 'ai_response')),
  created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Mood tracking table
CREATE TABLE IF NOT EXISTS public.mood_tracking (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  client_id UUID NOT NULL REFERENCES public.clients(id) ON DELETE CASCADE,
  mood_score INTEGER CHECK (mood_score >= 1 AND mood_score <= 10),
  anxiety_score INTEGER CHECK (anxiety_score >= 1 AND anxiety_score <= 10),
  sleep_quality INTEGER CHECK (sleep_quality >= 1 AND sleep_quality <= 10),
  stress_level INTEGER CHECK (stress_level >= 1 AND stress_level <= 10),
  notes TEXT,
  tracked_date DATE NOT NULL,
  created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Indexes
CREATE INDEX idx_clients_therapist_id ON public.clients(therapist_id);
CREATE INDEX idx_sessions_therapist_id ON public.sessions(therapist_id);
CREATE INDEX idx_sessions_client_id ON public.sessions(client_id);
CREATE INDEX idx_tasks_therapist_id ON public.tasks(therapist_id);
CREATE INDEX idx_tasks_client_id ON public.tasks(client_id);
CREATE INDEX idx_mood_tracking_client_id ON public.mood_tracking(client_id);
CREATE INDEX idx_mood_tracking_date ON public.mood_tracking(tracked_date);

-- Row Level Security (RLS)
ALTER TABLE public.therapists ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.clients ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.sessions ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.ai_summaries ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.tasks ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.messages ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.mood_tracking ENABLE ROW LEVEL SECURITY;

-- RLS Policies - Therapists can see their own profile
CREATE POLICY "Therapists can view their own profile" 
  ON public.therapists FOR SELECT 
  USING (auth.uid() = id);

-- RLS Policies - Therapists can see their own clients
CREATE POLICY "Therapists can view their clients" 
  ON public.clients FOR SELECT 
  USING (therapist_id = auth.uid());

CREATE POLICY "Therapists can insert their own clients" 
  ON public.clients FOR INSERT 
  WITH CHECK (therapist_id = auth.uid());

CREATE POLICY "Therapists can update their own clients" 
  ON public.clients FOR UPDATE 
  USING (therapist_id = auth.uid());

-- RLS Policies - Therapists can see their sessions
CREATE POLICY "Therapists can view their sessions" 
  ON public.sessions FOR SELECT 
  USING (therapist_id = auth.uid());

CREATE POLICY "Therapists can insert their sessions" 
  ON public.sessions FOR INSERT 
  WITH CHECK (therapist_id = auth.uid());

CREATE POLICY "Therapists can update their sessions" 
  ON public.sessions FOR UPDATE 
  USING (therapist_id = auth.uid());

-- RLS Policies - AI Summaries follow sessions
CREATE POLICY "Therapists can view AI summaries for their sessions" 
  ON public.ai_summaries FOR SELECT 
  USING (session_id IN (SELECT id FROM sessions WHERE therapist_id = auth.uid()));

CREATE POLICY "Therapists can insert AI summaries for their sessions" 
  ON public.ai_summaries FOR INSERT 
  WITH CHECK (session_id IN (SELECT id FROM sessions WHERE therapist_id = auth.uid()));

-- RLS Policies - Tasks
CREATE POLICY "Therapists can view their tasks" 
  ON public.tasks FOR SELECT 
  USING (therapist_id = auth.uid());

CREATE POLICY "Therapists can manage their tasks" 
  ON public.tasks FOR INSERT 
  WITH CHECK (therapist_id = auth.uid());

CREATE POLICY "Therapists can update their tasks" 
  ON public.tasks FOR UPDATE 
  USING (therapist_id = auth.uid());

-- RLS Policies - Messages
CREATE POLICY "Users can view messages they sent or received" 
  ON public.messages FOR SELECT 
  USING (sender_id = auth.uid() OR recipient_id = auth.uid());

CREATE POLICY "Users can send messages" 
  ON public.messages FOR INSERT 
  WITH CHECK (sender_id = auth.uid());

-- RLS Policies - Mood Tracking
CREATE POLICY "Therapists can view mood tracking for their clients" 
  ON public.mood_tracking FOR SELECT 
  USING (client_id IN (SELECT id FROM clients WHERE therapist_id = auth.uid()));

CREATE POLICY "Clients can insert their own mood tracking" 
  ON public.mood_tracking FOR INSERT 
  WITH CHECK (client_id IN (SELECT id FROM clients WHERE therapist_id = auth.uid()));

CREATE POLICY "Clients can update their own mood tracking" 
  ON public.mood_tracking FOR UPDATE 
  USING (client_id IN (SELECT id FROM clients WHERE therapist_id = auth.uid()));
