// command-center/frontend/src/App.jsx
import React, { useState, useEffect } from 'react';
import './App.css';

function App() {
  const [activeTab, setActiveTab] = useState('mesh'); // 'mesh', 'sonar', 'mhd', 'radar'
  const [nodes, setNodes] = useState(Array.from({ length: 12 }, (_, i) => ({ id: i + 1, status: 'active', x: Math.random() * 80 + 10, y: Math.random() * 80 + 10 })));
  const [threatDetected, setThreatDetected] = useState(false);
  const [mhdCurrent, setMhdCurrent] = useState(12.5);
  const [waterCurrentSpeed, setWaterCurrentSpeed] = useState(0.6);

  // सिमुलेटेड मेश नोड फेल्योर और सेल्फ-हीलिंग
  const triggerNodeFailure = (nodeId) => {
    setNodes(prev => prev.map(n => n.id === nodeId ? { ...n, status: 'destroyed' } : n));
    setTimeout(() => {
      // सेल्फ हीलिंग री-रूटिंग
      console.log(`[Mesh OS] Node #${nodeId} lost. Rerouting mesh packets...`);
    }, 1000);
  };

  return (
    <div className="war-room-container">
      {/* नेविगेशन हेडर */}
      <header className="war-room-header">
        <div className="logo-area">
          <h1>🛡️ UNDERWATER DEFENSE SHIELD — COMMAND & VISUALIZER</h1>
          <p className="sub-title">Indian Ocean Autonomous Sub-Surface Surveillance Grid (SwarmOS)</p>
        </div>
        <div className="system-status">
          <span className="dot pulse"></span> SYSTEM SECURE | MESH INTEGRITY: 99.8%
        </div>
      </header>

      {/* नेवी कंट्रोल टैब्स (यह दिखाता है कि सिस्टम काम कैसे करता है) */}
      <nav className="control-tabs">
        <button className={activeTab === 'mesh' ? 'active' : ''} onClick={() => setActiveTab('mesh')}>🌐 Mesh Network Topology (Self-Healing)</button>
        <button className={activeTab === 'sonar' ? 'active' : ''} onClick={() => setActiveTab('sonar')}>🔊 Passive Sonar & Edge AI Filter</button>
        <button className={activeTab === 'mhd' ? 'active' : ''} onClick={() => setActiveTab('mhd')}>⚡ MHD Stealth & Physics Sim</button>
        <button className={activeTab === 'radar' ? 'active' : ''} onClick={() => setActiveTab('radar')}>🛰️ Live War Room Radar</button>
      </nav>

      {/* मुख्य कंटेंट एरिया */}
      <main className="dashboard-content">
        
        {/* TAB 1: मेश नेटवर्क टोपोलॉजी */}
        {activeTab === 'mesh' && (
          <div className="tab-pane">
            <h2>🔗 Autonomous Acoustic Mesh Network (Self-Healing Architecture)</h2>
            <p className="desc">यहाँ देखें कि पानी के नीचे बिना तारों के कैसे हजारों ड्रोन आपस में जुड़े हैं। किसी भी ड्रोन पर क्लिक करके उसे 'तबाही' (Simulate Attack) मानकर देखें कि बाकी मेश खुद को कैसे री-कॉन्फ़िगर करता है।</p>
            <div className="mesh-visualizer-box">
              {nodes.map(node => (
                <div 
                  key={node.id} 
                  className={`mesh-node ${node.status}`} 
                  style={{ top: `${node.y}%`, left: `${node.x}%` }}
                  onClick={() => triggerNodeFailure(node.id)}
                  title={`Click to destroy Node #${node.id}`}
                >
                  <span>#{node.id}</span>
                </div>
              ))}
            </div>
          </div>
        )}

        {/* TAB 2: पैसिव सोनार और एज एआई */}
        {activeTab === 'sonar' && (
          <div className="tab-pane">
            <h2>🧠 Edge AI Acoustic Classifier (Filtering Marine Life vs Submarines)</h2>
            <p className="desc">ड्रोन का पैसिव सोनार खुद कोई आवाज नहीं निकालता। यह केवल बाहरी शोर सुनता है और एज एआई तय करता है कि यह व्हेल मछली की आवाज है या दुश्मन की पनडुब्बी का प्रोपेलर।</p>
            <div className="sonar-analyzer-grid">
              <div className="analyzer-card">
                <h3>Ambient Sound Wave</h3>
                <div className="waveform-box">
                  <div className="wave"></div>
                </div>
                <p><strong>Frequency:</strong> 45.2 Hz (Low-Frequency Propeller Signature)</p>
                <p><strong>Harmonicity:</strong> 0.88 (High Mechanical Uniformity)</p>
              </div>
              <div className="analyzer-card ai-result">
                <h3>AI Inference Decision</h3>
                <p className="ai-verdict threat">⚠️ CONFIRMED HOSTILE SUB-SURFACE THREAT</p>
                <p>Confidence Score: <strong>98.4%</strong></p>
                <p>Action Taken: <em>Acoustic Mesh Packet Broadcast Triggered.</em></p>
              </div>
            </div>
          </div>
        )}

        {/* TAB 3: MHD स्टेल्थ और फिजिक्स सिमुलेशन */}
        {activeTab === 'mhd' && (
          <div className="tab-pane">
            <h2>⚡ Magnetohydrodynamic (MHD) Silent Propulsion & Stability</h2>
            <p className="desc">इन ड्रोन्स में कोई घूमने वाला मोटर या प्रोपेलर नहीं होता। इलेक्ट्रोमैग्नेटिक लोर्त्ज फोर्स से पानी को पीछे धकेला जाता है। यहाँ पानी की धारा बदलकर चेक करें कि MHD थ्रस्ट कैसे काम करता है:</p>
            <div className="mhd-control-panel">
              <div className="control-group">
                <label>Water Current Speed: {waterCurrentSpeed} m/s</label>
                <input 
                  type="range" min="0.1" max="2.0" step="0.1" 
                  value={waterCurrentSpeed} 
                  onChange={(e) => setWaterCurrentSpeed(parseFloat(e.target.value))} 
                />
              </div>
              <div className="control-group">
                <label>MHD Applied Current: {mhdCurrent} Amps</label>
                <input 
                  type="range" min="5.0" max="30.0" step="0.5" 
                  value={mhdCurrent} 
                  onChange={(e) => setMhdCurrent(parseFloat(e.target.value))} 
                />
              </div>
              <div className="physics-output-box">
                <p><strong>Generated Lorentz Force:</strong> {(mhdCurrent * 0.5 * 5.0).toFixed(2)} Newtons</p>
                <p><strong>Stealth Status:</strong> {waterCurrentSpeed < 1.5 ? '🟢 100% Silent (Zero Cavitation)' : '🟡 High Resistance Mode Active'}</p>
              </div>
            </div>
          </div>
        )}

        {/* TAB 4: लाइव वॉर रूम रडार */}
        {activeTab === 'radar' && (
          <div className="tab-pane">
            <h2>🛰️ Indian Ocean Real-Time Gateway Uplink (GSAT-7A Rukmini)</h2>
            <p className="desc">गेटवे बॉय से सैटेलाइट के जरिए विशाखापट्टनम कमांड सेंटर तक पहुँचने वाला लाइव फीड:</p>
            <div className="war-radar-screen">
              <div className="radar-sweep"></div>
              <div className="radar-blip" onClick={() => setThreatDetected(!threatDetected)}></div>
              <div className="radar-info">
                <p>Sector: IOR-East (Bay of Bengal)</p>
                <p>Gateway Buoy: Online (#GB-09)</p>
                {threatDetected ? (
                  <span className="threat-text">🚨 INTRUDER SUBMARINE LOCKED AT LAT 12.97, LON 80.25</span>
                ) : (
                  <span className="safe-text">🟢 All Sectors Clear. Monitoring Active.</span>
                )}
              </div>
            </div>
          </div>
        )}

      </main>
    </div>
  );
}

export default App;



