import { useState } from 'react';
import './App.css';

interface RiskFlag {
  severity: 'red' | 'yellow' | 'green';
  title: string;
  description: string;
}

interface Contract {
  id: string;
  name: string;
  upload_date: string;
  status: 'analyzed' | 'pending';
  risks_count: number;
}

interface AnalysisResult {
  parties: string[];
  start_date: string;
  end_date: string;
  amount: string;
  payment_terms: string;
  key_obligations: string[];
  risks: RiskFlag[];
}

type Page = 'upload' | 'contracts' | 'analysis';

export function App() {
  const [currentPage, setCurrentPage] = useState<Page>('upload');
  const [selectedContract, setSelectedContract] = useState<Contract | null>(null);

  // Mock contracts
  const mockContracts: Contract[] = [
    {
      id: '1',
      name: 'ServiceAgreement_TechCorp_2026.pdf',
      upload_date: '2026-10-05',
      status: 'analyzed',
      risks_count: 2,
    },
    {
      id: '2',
      name: 'LicenseAgreement_SoftwareVendor.pdf',
      upload_date: '2026-10-03',
      status: 'analyzed',
      risks_count: 3,
    },
    {
      id: '3',
      name: 'NDA_PartnerCorp.pdf',
      upload_date: '2026-10-01',
      status: 'analyzed',
      risks_count: 0,
    },
  ];

  const mockAnalysis: AnalysisResult = {
    parties: ['Your Company Inc.', 'TechCorp Solutions LLC'],
    start_date: '2026-10-15',
    end_date: '2027-10-14',
    amount: '$50,000/year',
    payment_terms: 'Net 30, Annual upfront',
    key_obligations: [
      'Provide 24/7 technical support',
      'Maintain 99.9% uptime SLA',
      'Deliver monthly reports',
      'Limit liability to contract value',
    ],
    risks: [
      {
        severity: 'red',
        title: 'Unlimited Liability Clause',
        description: 'Section 5.3 allows unlimited indemnification claims. Recommend cap at 1x contract value.',
      },
      {
        severity: 'yellow',
        title: 'Vague Termination Rights',
        description: 'Termination clause lacks specific notice periods. Recommend 30-day minimum notice.',
      },
      {
        severity: 'yellow',
        title: 'IP Ownership Ambiguous',
        description: 'Work product ownership not clearly defined. Ensure your ownership is explicit.',
      },
    ],
  };

  const renderUpload = () => (
    <div className="bg-white rounded-lg shadow p-6">
      <h2 className="text-2xl font-bold text-gray-900 mb-6">Upload Contract</h2>

      <div className="border-4 border-dashed border-gray-300 rounded-lg p-12 text-center hover:border-blue-500 transition cursor-pointer">
        <div className="text-4xl mb-4">📄</div>
        <p className="text-xl font-semibold text-gray-900 mb-2">Drop your contract here</p>
        <p className="text-sm text-gray-600 mb-4">or click to browse</p>
        <p className="text-xs text-gray-500">Supports PDF, Word, and text files</p>
      </div>

      <div className="mt-6 p-4 bg-blue-50 rounded-lg border border-blue-200">
        <p className="text-sm text-blue-900">
          <strong>💡 Tip:</strong> Upload any contract and our AI will instantly extract key terms, flag risks, and compare against safe templates.
        </p>
      </div>

      <div className="mt-6 grid grid-cols-1 md:grid-cols-3 gap-4">
        <div className="p-4 bg-gray-50 rounded-lg">
          <div className="text-2xl mb-2">⚡</div>
          <h3 className="font-semibold text-gray-900">Instant Analysis</h3>
          <p className="text-sm text-gray-600 mt-1">AI analyzes in seconds</p>
        </div>
        <div className="p-4 bg-gray-50 rounded-lg">
          <div className="text-2xl mb-2">🚩</div>
          <h3 className="font-semibold text-gray-900">Risk Flagging</h3>
          <p className="text-sm text-gray-600 mt-1">Identifies problematic clauses</p>
        </div>
        <div className="p-4 bg-gray-50 rounded-lg">
          <div className="text-2xl mb-2">📋</div>
          <h3 className="font-semibold text-gray-900">Template Comparison</h3>
          <p className="text-sm text-gray-600 mt-1">Compares to safe templates</p>
        </div>
      </div>
    </div>
  );

  const renderContracts = () => (
    <div className="bg-white rounded-lg shadow p-6">
      <h2 className="text-2xl font-bold text-gray-900 mb-6">Analyzed Contracts</h2>

      <div className="space-y-3">
        {mockContracts.map((contract) => (
          <div
            key={contract.id}
            onClick={() => {
              setSelectedContract(contract);
              setCurrentPage('analysis');
            }}
            className="p-4 border-2 border-gray-200 rounded-lg hover:border-blue-300 hover:bg-blue-50 transition cursor-pointer"
          >
            <div className="flex justify-between items-center">
              <div className="flex-1">
                <h3 className="font-bold text-gray-900">{contract.name}</h3>
                <p className="text-sm text-gray-600">Uploaded: {contract.upload_date}</p>
              </div>
              <div className="text-right">
                <div
                  className={`text-sm font-semibold mb-2 ${
                    contract.risks_count === 0
                      ? 'text-green-600'
                      : contract.risks_count <= 2
                        ? 'text-yellow-600'
                        : 'text-red-600'
                  }`}
                >
                  {contract.risks_count} risks
                </div>
                <span className="text-xs bg-green-100 text-green-800 px-2 py-1 rounded">
                  Analyzed
                </span>
              </div>
            </div>
          </div>
        ))}
      </div>
    </div>
  );

  const renderAnalysis = () => (
    <div className="bg-white rounded-lg shadow p-6">
      {selectedContract && (
        <>
          <div className="mb-6">
            <h2 className="text-2xl font-bold text-gray-900">{selectedContract.name}</h2>
            <p className="text-sm text-gray-600 mt-1">Analyzed on {selectedContract.upload_date}</p>
          </div>

          <div className="grid grid-cols-1 md:grid-cols-2 gap-6 mb-6">
            <div className="p-4 bg-gray-50 rounded-lg">
              <h3 className="font-semibold text-gray-900 mb-3">Contract Parties</h3>
              <div className="space-y-2">
                {mockAnalysis.parties.map((party, idx) => (
                  <div key={idx} className="text-sm text-gray-700">
                    <span className="font-medium">{idx === 0 ? '👤 You:' : '👤 Counterparty:'}</span> {party}
                  </div>
                ))}
              </div>
            </div>

            <div className="p-4 bg-gray-50 rounded-lg">
              <h3 className="font-semibold text-gray-900 mb-3">Key Terms</h3>
              <div className="space-y-2 text-sm text-gray-700">
                <div>
                  <span className="font-medium">Duration:</span> {mockAnalysis.start_date} to {mockAnalysis.end_date}
                </div>
                <div>
                  <span className="font-medium">Amount:</span> {mockAnalysis.amount}
                </div>
                <div>
                  <span className="font-medium">Payment:</span> {mockAnalysis.payment_terms}
                </div>
              </div>
            </div>
          </div>

          <div className="mb-6 p-4 bg-blue-50 rounded-lg border border-blue-200">
            <h3 className="font-semibold text-gray-900 mb-2">Key Obligations</h3>
            <ul className="list-disc list-inside space-y-1 text-sm text-gray-700">
              {mockAnalysis.key_obligations.map((ob, idx) => (
                <li key={idx}>{ob}</li>
              ))}
            </ul>
          </div>

          <div className="mb-6">
            <h3 className="font-semibold text-gray-900 mb-4 text-lg">⚠️ Risk Analysis</h3>

            <div className="space-y-3">
              {mockAnalysis.risks.map((risk, idx) => (
                <div
                  key={idx}
                  className={`p-4 rounded-lg border-2 ${
                    risk.severity === 'red'
                      ? 'bg-red-50 border-red-200'
                      : 'bg-yellow-50 border-yellow-200'
                  }`}
                >
                  <div className="flex items-start">
                    <span className="text-2xl mr-3">
                      {risk.severity === 'red' ? '🚨' : '⚠️'}
                    </span>
                    <div className="flex-1">
                      <h4 className={`font-bold ${
                        risk.severity === 'red' ? 'text-red-900' : 'text-yellow-900'
                      }`}>
                        {risk.title}
                      </h4>
                      <p className={`text-sm mt-1 ${
                        risk.severity === 'red' ? 'text-red-800' : 'text-yellow-800'
                      }`}>
                        {risk.description}
                      </p>
                    </div>
                  </div>
                </div>
              ))}
            </div>
          </div>

          <div className="p-4 bg-green-50 border border-green-200 rounded-lg">
            <h4 className="font-semibold text-green-900 mb-2">✅ Safe Clauses Found</h4>
            <p className="text-sm text-green-800">
              The following clauses align with industry-standard safe language: dispute resolution, confidentiality, and audit rights.
            </p>
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
            <h1 className="text-2xl font-bold text-red-600">⚖️ Contract Analyzer</h1>
            <div className="flex space-x-4">
              {(['upload', 'contracts', 'analysis'] as const).map((page) => (
                <button
                  key={page}
                  onClick={() => setCurrentPage(page)}
                  disabled={page === 'analysis' && !selectedContract}
                  className={`px-3 py-2 rounded-md text-sm font-medium transition ${
                    currentPage === page
                      ? 'bg-red-100 text-red-700'
                      : page === 'analysis' && !selectedContract
                        ? 'text-gray-400 cursor-not-allowed'
                        : 'text-gray-700 hover:bg-gray-100'
                  }`}
                >
                  {page === 'upload' && 'Upload'}
                  {page === 'contracts' && 'My Contracts'}
                  {page === 'analysis' && 'Analysis'}
                </button>
              ))}
            </div>
          </div>
        </div>
      </nav>

      <main className="max-w-7xl mx-auto py-6 sm:px-6 lg:px-8">
        {currentPage === 'upload' && renderUpload()}
        {currentPage === 'contracts' && renderContracts()}
        {currentPage === 'analysis' && renderAnalysis()}
      </main>
    </div>
  );
}
