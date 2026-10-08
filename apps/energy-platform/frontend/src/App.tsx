import { useState } from 'react';
import './App.css';

interface Building {
  id: string;
  address: string;
  square_feet: string;
  type: 'office' | 'warehouse' | 'retail' | 'multi-family';
  annual_cost: string;
}

interface Client {
  id: string;
  name: string;
  industry: string;
  buildings: number;
}

interface Recommendation {
  id: string;
  category: 'HVAC' | 'Lighting' | 'Insulation' | 'Solar' | 'Water';
  title: string;
  savings_per_year: string;
  implementation_cost: string;
  payback_years: string;
  priority: 'high' | 'medium' | 'low';
}

interface AnalysisData {
  current_annual_spend: string;
  estimated_savings: string;
  roi_percent: string;
  payback_period_years: string;
  recommendations: Recommendation[];
}

type Page = 'clients' | 'buildings' | 'analysis';

export function App() {
  const [currentPage, setCurrentPage] = useState<Page>('clients');
  const [selectedClient, setSelectedClient] = useState<Client | null>(null);
  const [selectedBuilding, setSelectedBuilding] = useState<Building | null>(null);

  // Mock data
  const mockClients: Client[] = [
    {
      id: '1',
      name: 'Acme Manufacturing LLC',
      industry: 'Manufacturing',
      buildings: 3,
    },
    {
      id: '2',
      name: 'GreenRetail Inc.',
      industry: 'Retail',
      buildings: 2,
    },
    {
      id: '3',
      name: 'TechOffices Corp',
      industry: 'Technology',
      buildings: 1,
    },
  ];

  const mockBuildings: Building[] = [
    {
      id: '1',
      address: '123 Industrial Way, Chicago, IL',
      square_feet: '50,000',
      type: 'warehouse',
      annual_cost: '$85,000',
    },
    {
      id: '2',
      address: '456 Office Plaza, Chicago, IL',
      square_feet: '25,000',
      type: 'office',
      annual_cost: '$45,000',
    },
  ];

  const mockAnalysis: AnalysisData = {
    current_annual_spend: '$85,000',
    estimated_savings: '$28,900',
    roi_percent: '156%',
    payback_period_years: '0.9',
    recommendations: [
      {
        id: '1',
        category: 'HVAC',
        title: 'Smart Thermostat + Scheduling Optimization',
        savings_per_year: '$8,500',
        implementation_cost: '$3,500',
        payback_years: '0.4',
        priority: 'high',
      },
      {
        id: '2',
        category: 'Lighting',
        title: 'LED Conversion + Motion Sensors',
        savings_per_year: '$12,000',
        implementation_cost: '$8,000',
        payback_years: '0.7',
        priority: 'high',
      },
      {
        id: '3',
        category: 'Insulation',
        title: 'Roof & Wall Insulation Upgrade',
        savings_per_year: '$5,400',
        implementation_cost: '$15,000',
        payback_years: '2.8',
        priority: 'medium',
      },
      {
        id: '4',
        category: 'Solar',
        title: 'Solar Panel Installation (50kW)',
        savings_per_year: '$12,000',
        implementation_cost: '$150,000',
        payback_years: '8.2',
        priority: 'medium',
      },
      {
        id: '5',
        category: 'Water',
        title: 'Low-Flow Fixtures + Leak Detection',
        savings_per_year: '$2,000',
        implementation_cost: '$4,000',
        payback_years: '2.0',
        priority: 'low',
      },
    ],
  };

  const renderClients = () => (
    <div className="bg-white rounded-lg shadow p-6">
      <h2 className="text-2xl font-bold text-gray-900 mb-6">Client Portfolio</h2>

      <div className="space-y-3">
        {mockClients.map((client) => (
          <div
            key={client.id}
            onClick={() => {
              setSelectedClient(client);
              setCurrentPage('buildings');
            }}
            className="p-4 border-2 border-gray-200 rounded-lg hover:border-green-400 hover:bg-green-50 transition cursor-pointer"
          >
            <div className="flex justify-between items-center">
              <div>
                <h3 className="font-bold text-lg text-gray-900">{client.name}</h3>
                <p className="text-sm text-gray-600">{client.industry}</p>
              </div>
              <div className="text-right">
                <div className="text-2xl font-bold text-green-600">{client.buildings}</div>
                <p className="text-xs text-gray-600">Buildings</p>
              </div>
            </div>
          </div>
        ))}
      </div>

      <div className="mt-6 p-4 bg-green-50 border border-green-200 rounded-lg">
        <h3 className="font-semibold text-green-900 mb-2">💡 Quick Tips</h3>
        <ul className="text-sm text-green-800 space-y-1">
          <li>• Average payback period for efficiency projects: 2-3 years</li>
          <li>• Most buildings waste 15-30% of energy</li>
          <li>• LED + HVAC upgrades offer fastest ROI</li>
        </ul>
      </div>
    </div>
  );

  const renderBuildings = () => (
    <div className="bg-white rounded-lg shadow p-6">
      <div className="mb-6">
        <h2 className="text-2xl font-bold text-gray-900">{selectedClient?.name}</h2>
        <p className="text-sm text-gray-600">Buildings & Energy Usage</p>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-2 gap-4 mb-6">
        {mockBuildings.map((building) => (
          <div
            key={building.id}
            onClick={() => {
              setSelectedBuilding(building);
              setCurrentPage('analysis');
            }}
            className={`p-4 border-2 rounded-lg cursor-pointer transition ${
              selectedBuilding?.id === building.id
                ? 'border-green-500 bg-green-50'
                : 'border-gray-200 hover:border-green-400'
            }`}
          >
            <h3 className="font-bold text-gray-900">{building.address}</h3>
            <p className="text-sm text-gray-600 mt-1">{building.square_feet} sq ft • {building.type}</p>
            <div className="mt-3 flex justify-between items-center">
              <span className="text-lg font-bold text-orange-600">{building.annual_cost}/year</span>
              <button className="text-sm bg-green-600 text-white px-3 py-1 rounded hover:bg-green-700">
                Analyze
              </button>
            </div>
          </div>
        ))}
      </div>

      <div className="text-center py-6 text-gray-600">
        <p className="text-sm">Select a building to see AI-powered energy analysis and recommendations</p>
      </div>
    </div>
  );

  const renderAnalysis = () => (
    <div className="bg-white rounded-lg shadow p-6">
      {selectedBuilding && (
        <>
          <div className="mb-6">
            <h2 className="text-2xl font-bold text-gray-900">Energy Analysis</h2>
            <p className="text-sm text-gray-600 mt-1">{selectedBuilding.address}</p>
          </div>

          <div className="grid grid-cols-1 md:grid-cols-2 gap-4 mb-6">
            <div className="p-4 bg-red-50 border border-red-200 rounded-lg">
              <div className="text-sm text-red-600 font-semibold">Current Annual Spend</div>
              <div className="text-3xl font-bold text-red-700 mt-2">{mockAnalysis.current_annual_spend}</div>
            </div>
            <div className="p-4 bg-green-50 border border-green-200 rounded-lg">
              <div className="text-sm text-green-600 font-semibold">Estimated Annual Savings</div>
              <div className="text-3xl font-bold text-green-700 mt-2">{mockAnalysis.estimated_savings}</div>
            </div>
            <div className="p-4 bg-blue-50 border border-blue-200 rounded-lg">
              <div className="text-sm text-blue-600 font-semibold">Return on Investment</div>
              <div className="text-3xl font-bold text-blue-700 mt-2">{mockAnalysis.roi_percent}</div>
            </div>
            <div className="p-4 bg-purple-50 border border-purple-200 rounded-lg">
              <div className="text-sm text-purple-600 font-semibold">Average Payback Period</div>
              <div className="text-3xl font-bold text-purple-700 mt-2">{mockAnalysis.payback_period_years} years</div>
            </div>
          </div>

          <div className="mb-6">
            <h3 className="text-lg font-bold text-gray-900 mb-4">🎯 AI Recommendations (Ranked by ROI)</h3>

            <div className="space-y-3">
              {mockAnalysis.recommendations.map((rec) => (
                <div
                  key={rec.id}
                  className={`p-4 border-l-4 rounded-lg ${
                    rec.priority === 'high'
                      ? 'border-l-red-500 bg-red-50'
                      : rec.priority === 'medium'
                        ? 'border-l-yellow-500 bg-yellow-50'
                        : 'border-l-gray-400 bg-gray-50'
                  }`}
                >
                  <div className="flex justify-between items-start">
                    <div className="flex-1">
                      <div className="flex items-center gap-2 mb-1">
                        <h4 className="font-bold text-gray-900">{rec.title}</h4>
                        <span
                          className={`text-xs px-2 py-1 rounded ${
                            rec.priority === 'high'
                              ? 'bg-red-200 text-red-800'
                              : rec.priority === 'medium'
                                ? 'bg-yellow-200 text-yellow-800'
                                : 'bg-gray-200 text-gray-800'
                          }`}
                        >
                          {rec.priority.toUpperCase()}
                        </span>
                      </div>
                      <p className="text-sm text-gray-600 mb-2">{rec.category}</p>
                      <div className="grid grid-cols-3 gap-4 text-sm">
                        <div>
                          <span className="text-gray-600">Annual Savings:</span>
                          <div className="font-bold text-green-600">{rec.savings_per_year}</div>
                        </div>
                        <div>
                          <span className="text-gray-600">Cost:</span>
                          <div className="font-bold text-blue-600">{rec.implementation_cost}</div>
                        </div>
                        <div>
                          <span className="text-gray-600">Payback:</span>
                          <div className="font-bold text-purple-600">{rec.payback_years} yrs</div>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
              ))}
            </div>
          </div>

          <div className="p-4 bg-blue-50 border border-blue-200 rounded-lg">
            <h4 className="font-semibold text-blue-900 mb-2">📊 Next Steps</h4>
            <ol className="text-sm text-blue-800 space-y-1 list-decimal list-inside">
              <li>Start with LED + HVAC (quick payback, highest impact)</li>
              <li>Schedule site survey for insulation assessment</li>
              <li>Explore solar feasibility and local incentives</li>
              <li>Generate formal report for board/finance approval</li>
            </ol>
          </div>
        </>
      )}
    </div>
  );

  return (
    <div className="min-h-screen bg-gray-100">
      <nav className="bg-white shadow">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="flex justify-between items-center h-16">
            <h1 className="text-2xl font-bold text-green-600">⚡ Energy Platform</h1>
            <div className="flex space-x-4">
              {(['clients', 'buildings', 'analysis'] as const).map((page) => (
                <button
                  key={page}
                  onClick={() => setCurrentPage(page)}
                  disabled={(page === 'buildings' && !selectedClient) || (page === 'analysis' && !selectedBuilding)}
                  className={`px-3 py-2 rounded-md text-sm font-medium transition ${
                    currentPage === page
                      ? 'bg-green-100 text-green-700'
                      : ((page === 'buildings' && !selectedClient) || (page === 'analysis' && !selectedBuilding))
                        ? 'text-gray-400 cursor-not-allowed'
                        : 'text-gray-700 hover:bg-gray-100'
                  }`}
                >
                  {page === 'clients' && 'Clients'}
                  {page === 'buildings' && 'Buildings'}
                  {page === 'analysis' && 'Analysis'}
                </button>
              ))}
            </div>
          </div>
        </div>
      </nav>

      <main className="max-w-7xl mx-auto py-6 sm:px-6 lg:px-8">
        {currentPage === 'clients' && renderClients()}
        {currentPage === 'buildings' && renderBuildings()}
        {currentPage === 'analysis' && renderAnalysis()}
      </main>
    </div>
  );
}
