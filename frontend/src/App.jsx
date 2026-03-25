import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Dashboard from './pages/Dashboard';
import Login from './pages/login';
import Placement from "./pages/Placement"
import ProtectedRoute from './components/ProtectedRoute';
import Register from './pages/Register';

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/placement" element={<ProtectedRoute><Placement /></ProtectedRoute>} />
        <Route path="/dashboard" element={<ProtectedRoute><Dashboard /></ProtectedRoute>} />
        <Route path="/login" element={<Login />} />
        <Route path="/register" element={<Register />} />
        <Route path="/" element={
          <ProtectedRoute>
            <div className="min-h-screen flex items-center justify-center bg-blue-500">
              <h1 className="text-white text-4xl font-bold">
                EasyLearn.
              </h1>
              <p className="text-white text-2xl font-bold">Making your life easier.</p>
            </div>
          </ProtectedRoute>
        } />
      </Routes>
    </Router>
  )
}

export default App
