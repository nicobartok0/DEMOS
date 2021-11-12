import {BrowserRouter as Router, Routes, Route} from 'react-router-dom'

import {About} from './components/About'
import {Users} from './components/Users'
function App() {
  return (
    <Router>

    <div>
      <Routes>
        <Route path="about" element={<About />} />
        <Route path="/" element={<Users />} />
      </Routes>
    </div>

    </Router>

  );
}

export default App;
