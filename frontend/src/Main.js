import { BrowserRouter, Routes, Route } from 'react-router-dom';

import App from "./components/App";
import HomePage from "./pages/HomePage/HomePage";
import GraphPage from "./pages/GraphPage/GraphPage";

function Main() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={ <App /> }>
          <Route index element={ <HomePage />} />
          <Route path="/graph" element={ <GraphPage />} />
        </Route>
      </Routes>
    </BrowserRouter>
  );
}

export default Main;
