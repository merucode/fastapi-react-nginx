import { BrowserRouter, Routes, Route } from 'react-router-dom';
import App from "./components/App";
import HomePage from "./pages/HomePage/HomePage";

function Main() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={ <App /> }>
          <Route index element={ <HomePage />} />
        </Route>
      </Routes>
    </BrowserRouter>
  );
}

export default Main;
