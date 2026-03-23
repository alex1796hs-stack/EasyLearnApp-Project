import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Dashboard from './pages/Dashboard';
import Login from './pages/login';
import Placement from "./pages/Placement"

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/placement" element={<Placement />} />
        <Route path="/dashboard" element={<Dashboard />} />
        <Route path="/login" element={<Login />} />
        <Route path="/" element={
          <div className="min-h-screen flex items-center justify-center bg-blue-500">
            <h1 className="text-white text-4xl font-bold">
              EasyLearn.
            </h1>
            <p className="text-white text-2xl font-bold">Making your life easier.</p>
          </div>
        } />
      </Routes>
    </Router>
  )
}

export default App
