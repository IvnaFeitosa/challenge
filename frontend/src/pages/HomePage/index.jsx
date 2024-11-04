import Standings from './components/Standings';
import TeamDetails from './components/TeamDetails';
import { Container } from 'react-bootstrap';
import './style.css';

const Home = () => (
  <Container className="home-container">
    <h1 className="text-center mb-4">Campeonato Brasileiro Série A</h1>
    <div className="standings-section mb-5">
      <Standings />
    </div>
    <div className="team-details-section">
      <TeamDetails />
    </div>
  </Container>
);

export default Home;
