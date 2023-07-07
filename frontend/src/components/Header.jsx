import { Link } from 'react-router-dom';

function Header() {
  return (
  <header>
    <div>
      <Link to="/">Web Link</Link>
      <Link to="/graph">Graph</Link>
    </div>
  </header>
  );
}

export default Header;


