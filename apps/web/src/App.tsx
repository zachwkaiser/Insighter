import { Routes, Route } from 'react-router-dom'
import { Login } from './pages/Login/Login.tsx'
import { SignUp } from './pages/Signup/SignUp.tsx'
import { Dashboard } from './pages/Dashboard/Dashboard.tsx'

function App() {
  return (
    <Routes>
      <Route path="/" element={<Login />} />
      <Route path="/signup" element={<SignUp />} />
      <Route path="/dashboard" element={<Dashboard />} />
    </Routes>
  )
}

export default App
