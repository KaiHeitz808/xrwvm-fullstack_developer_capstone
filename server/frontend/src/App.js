import LoginPanel from "./components/Login/Login"
import { Routes, Route } from "react-router-dom";

function App() {
  return (
    <Routes>
      <Route path="/login" element={<LoginPanel />} />
    </Routes>
  );
}

const App = () => {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Home />} />  {/* Default home route */}
        <Route path="/register" element={<Register />} />  {/* Register page */}
      </Routes>
    </Router>
  );
};

export default App;

