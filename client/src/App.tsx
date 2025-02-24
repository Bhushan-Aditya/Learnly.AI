import { BrowserRouter, Route, Routes } from 'react-router-dom';
import 'regenerator-runtime/runtime';
import Dashboard from './components/dashboard';
import { LampDemo } from './components/error';
import Landing from './components/landing';
import Login from './components/login';
import { Toaster } from './components/ui/sonner';

function App() {
    return (
        <BrowserRouter>
            <Routes>
                <Route path="/" element={<Landing />} />
                <Route path="/login" element={<Login />} />
                <Route path="/dashboard" element={<Dashboard />} />
                <Route path="*" element={<LampDemo />} />
            </Routes>
            <Toaster />
        </BrowserRouter>
    );
}

export default App;