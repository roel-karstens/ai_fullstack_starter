import { useState } from 'react';
import './App.css';

interface Client {
  id: string;
  name: string;
  presenting_issues: string;
  last_session?: string;
  status: 'active' | 'inactive' | 'discharged';
}

interface Session {
  id: string;
  client_id: string;
  client_name: string;
  session_date: string;
  duration: number;
  mood_before: number;
  mood_after: number;
}

interface AISummary {
  summary: string;
  key_topics: string[];
  goals: string[];
  action_items: string[];
  recommended_focus: string;
}

type Page = 'dashboard' | 'clients' | 'sessions' | 'analytics';

export function App() {
  const [currentPage, setCurrentPage] = useState<Page>('dashboard');
  const [selectedClient, setSelectedClient] = useState<Client | null>(null);
  const [selectedSession, setSelectedSession] = useState<Session | null>(null);

  // Mock data
  const mockClients: Client[] = [
    {
      id: '1',
      name: 'Sarah Mitchell',
      presenting_issues: 'Anxiety, work stress',
      last_session: '2026-10-05',
      status: 'active',
    },
    {
      id: '2',
      name: 'James Chen',
      presenting_issues: 'Depression, isolation',
      last_session: '2026-10-04',
      status: 'active',
    },
    {
      id: '3',
      name: 'Emma Rodriguez',
      presenting_issues: 'Relationship issues, grief',
      last_session: '2026-10-02',
      status: 'active',
    },
  ];

  const mockSessions: Session[] = [
    {
      id: '1',
      client_id: '1',
      client_name: 'Sarah Mitchell',
      session_date: '2026-10-05',
      duration: 60,
      mood_before: 5,
      mood_after: 7,
    },
    {
      id: '2',
      client_id: '2',
      client_name: 'James Chen',
      session_date: '2026-10-04',
      duration: 50,
      mood_before: 4,
      mood_after: 6,
    },
  ];

  const mockSummary: AISummary = {
    summary: 'Sarah discussed her anxiety around an upcoming presentation at work. She explored coping strategies including breathing exercises and cognitive reframing. Mood improved from 5 to 7 after the session.',
    key_topics: ['Work anxiety', 'Perfectionism', 'Coping strategies'],
    goals: ['Reduce anxiety before presentations', 'Develop grounding techniques'],
    action_items: ['Practice breathing exercises daily', 'Use cognitive reframing worksheet'],
    recommended_focus: 'Building confidence in public speaking situations',
  };

  const renderDashboard = () => (
    <div className="space-y-6">
      <div className="bg-white rounded-lg shadow p-6">
        <h2 className="text-2xl font-bold text-gray-900 mb-6">Therapist Dashboard</h2>

        <div className="grid grid-cols-1 md:grid-cols-3 gap-4 mb-6">
          <div className="bg-blue-50 p-4 rounded-lg">
            <div className="text-3xl font-bold text-blue-600">{mockClients.length}</div>
            <div className="text-sm text-gray-600">Active Clients</div>
          </div>
          <div className="bg-green-50 p-4 rounded-lg">
            <div className="text-3xl font-bold text-green-600">{mockSessions.length}</div>
            <div className="text-sm text-gray-600">Sessions This Week</div>
          </div>
          <div className="bg-purple-50 p-4 rounded-lg">
            <div className="text-3xl font-bold text-purple-600">85%</div>
            <div className="text-sm text-gray-600">Avg Mood Improvement</div>
          </div>
        </div>

        <div className="text-center text-gray-600 py-8">
          <p className="mb-4">Welcome to Therapy Assistant!</p>
          <p className="text-sm">Navigate through the menu to manage clients, sessions, and analytics.</p>
        </div>
      </div>
    </div>
  );

  const renderClients = () => (
    <div className="bg-white rounded-lg shadow p-6">
      <h2 className="text-2xl font-bold text-gray-900 mb-6">Client Management</h2>

      <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
        {mockClients.map((client) => (
          <div
            key={client.id}
            onClick={() => setSelectedClient(client)}
            className={`p-4 border-2 rounded-lg cursor-pointer transition ${
              selectedClient?.id === client.id
                ? 'border-blue-500 bg-blue-50'
                : 'border-gray-200 hover:border-blue-300'
            }`}
          >
            <h3 className="font-bold text-lg text-gray-900">{client.name}</h3>
            <p className="text-sm text-gray-600 mt-1">{client.presenting_issues}</p>
            <div className="flex justify-between items-center mt-3">
              <span
                className={`text-xs px-2 py-1 rounded ${
                  client.status === 'active'
                    ? 'bg-green-100 text-green-800'
                    : 'bg-gray-100 text-gray-800'
                }`}
              >
                {client.status}
              </span>
              <span className="text-xs text-gray-500">Last: {client.last_session}</span>
            </div>
          </div>
        ))}
      </div>

      {selectedClient && (
        <div className="mt-6 p-4 bg-gray-50 rounded-lg">
          <h3 className="font-bold text-lg text-gray-900 mb-3">{selectedClient.name} - Details</h3>
          <div className="space-y-2 text-sm text-gray-700">
            <p>
              <strong>Presenting Issues:</strong> {selectedClient.presenting_issues}
            </p>
            <p>
              <strong>Status:</strong> {selectedClient.status}
            </p>
            <p>
              <strong>Total Sessions:</strong> 12
            </p>
            <p>
              <strong>Next Appointment:</strong> 2026-10-12 at 2:00 PM
            </p>
          </div>
        </div>
      )}
    </div>
  );

  const renderSessions = () => (
    <div className="bg-white rounded-lg shadow p-6">
      <h2 className="text-2xl font-bold text-gray-900 mb-6">Session Management</h2>

      <div className="grid grid-cols-1 gap-4 mb-6">
        {mockSessions.map((session) => (
          <div
            key={session.id}
            onClick={() => setSelectedSession(session)}
            className={`p-4 border-2 rounded-lg cursor-pointer transition ${
              selectedSession?.id === session.id
                ? 'border-blue-500 bg-blue-50'
                : 'border-gray-200 hover:border-blue-300'
            }`}
          >
            <div className="flex justify-between items-center">
              <div>
                <h3 className="font-bold text-gray-900">{session.client_name}</h3>
                <p className="text-sm text-gray-600">{session.session_date} • {session.duration} min</p>
              </div>
              <div className="text-right">
                <div className="text-sm">
                  <span className="text-red-600">Mood: {session.mood_before}</span>
                  <span className="text-gray-400"> → </span>
                  <span className="text-green-600">{session.mood_after}</span>
                </div>
              </div>
            </div>
          </div>
        ))}
      </div>

      {selectedSession && (
        <div className="mt-6 p-4 bg-gradient-to-br from-blue-50 to-purple-50 rounded-lg">
          <h3 className="font-bold text-lg text-gray-900 mb-4">Session Summary - {selectedSession.client_name}</h3>

          <div className="space-y-4">
            <div>
              <h4 className="font-semibold text-gray-900 mb-2 flex items-center">
                <span className="text-2xl mr-2">✨</span> AI Summary
              </h4>
              <p className="text-gray-700 text-sm leading-relaxed">{mockSummary.summary}</p>
            </div>

            <div>
              <h4 className="font-semibold text-gray-900 mb-2">Key Topics</h4>
              <div className="flex flex-wrap gap-2">
                {mockSummary.key_topics.map((topic, idx) => (
                  <span key={idx} className="bg-blue-100 text-blue-800 text-xs px-2 py-1 rounded">
                    {topic}
                  </span>
                ))}
              </div>
            </div>

            <div>
              <h4 className="font-semibold text-gray-900 mb-2">Action Items</h4>
              <ul className="list-disc list-inside text-sm text-gray-700 space-y-1">
                {mockSummary.action_items.map((item, idx) => (
                  <li key={idx}>{item}</li>
                ))}
              </ul>
            </div>

            <div>
              <h4 className="font-semibold text-gray-900 mb-2">Next Focus</h4>
              <p className="text-sm text-gray-700">{mockSummary.recommended_focus}</p>
            </div>
          </div>
        </div>
      )}
    </div>
  );

  const renderAnalytics = () => (
    <div className="bg-white rounded-lg shadow p-6">
      <h2 className="text-2xl font-bold text-gray-900 mb-6">Client Analytics</h2>

      <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
        <div className="p-4 bg-gray-50 rounded-lg">
          <h3 className="font-semibold text-gray-900 mb-4">Mood Trends (Last 4 Weeks)</h3>
          <div className="space-y-3">
            {['Week 1', 'Week 2', 'Week 3', 'Week 4'].map((week, idx) => (
              <div key={idx}>
                <div className="flex justify-between text-sm mb-1">
                  <span className="text-gray-700">{week}</span>
                  <span className="font-semibold">{5 + idx}</span>
                </div>
                <div className="w-full bg-gray-200 rounded-full h-2">
                  <div
                    className="bg-green-500 h-2 rounded-full"
                    style={{ width: `${(5 + idx) * 10}%` }}
                  ></div>
                </div>
              </div>
            ))}
          </div>
        </div>

        <div className="p-4 bg-gray-50 rounded-lg">
          <h3 className="font-semibold text-gray-900 mb-4">Common Themes</h3>
          <div className="space-y-2">
            <div className="flex justify-between text-sm">
              <span className="text-gray-700">Anxiety</span>
              <span className="font-semibold text-blue-600">8 clients</span>
            </div>
            <div className="flex justify-between text-sm">
              <span className="text-gray-700">Depression</span>
              <span className="font-semibold text-purple-600">5 clients</span>
            </div>
            <div className="flex justify-between text-sm">
              <span className="text-gray-700">Relationships</span>
              <span className="font-semibold text-pink-600">4 clients</span>
            </div>
            <div className="flex justify-between text-sm">
              <span className="text-gray-700">Work Stress</span>
              <span className="font-semibold text-orange-600">6 clients</span>
            </div>
          </div>
        </div>
      </div>

      <div className="mt-6 p-4 bg-yellow-50 border border-yellow-200 rounded-lg">
        <h3 className="font-semibold text-yellow-900 mb-2">⚠️ Alerts</h3>
        <ul className="text-sm text-yellow-800 space-y-1">
          <li>• Sarah's anxiety scores trending up - consider intervention</li>
          <li>• James missed last two session reminders</li>
        </ul>
      </div>
    </div>
  );

  return (
    <div className="min-h-screen bg-gray-100">
      <nav className="bg-white shadow">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="flex justify-between items-center h-16">
            <h1 className="text-2xl font-bold text-blue-600">🧠 Therapy Assistant</h1>
            <div className="flex space-x-4">
              {(
                ['dashboard', 'clients', 'sessions', 'analytics'] as const
              ).map((page) => (
                <button
                  key={page}
                  onClick={() => setCurrentPage(page)}
                  className={`px-3 py-2 rounded-md text-sm font-medium transition ${
                    currentPage === page
                      ? 'bg-blue-100 text-blue-700'
                      : 'text-gray-700 hover:bg-gray-100'
                  }`}
                >
                  {page.charAt(0).toUpperCase() + page.slice(1)}
                </button>
              ))}
            </div>
          </div>
        </div>
      </nav>

      <main className="max-w-7xl mx-auto py-6 sm:px-6 lg:px-8">
        {currentPage === 'dashboard' && renderDashboard()}
        {currentPage === 'clients' && renderClients()}
        {currentPage === 'sessions' && renderSessions()}
        {currentPage === 'analytics' && renderAnalytics()}
      </main>
    </div>
  );
}
