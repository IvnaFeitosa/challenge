import { useState, useEffect } from 'react';
import { Container, Table } from 'react-bootstrap';
import { getAllTeams } from '../../../../services/footballService.js'; 

const calculatePoints = (vitorias, empates) => {
  return vitorias * 3 + empates;
};

const Standings = () => {
  const [teams, setTeams] = useState([]);

  useEffect(() => {
    const fetchTeams = async () => {
      try {
        const data = await getAllTeams();
        
        
        const sortedData = data
          .map((team) => ({
            ...team,
            pontos: calculatePoints(team.vitorias, team.empates),
          }))
          .sort((a, b) => b.pontos - a.pontos); 

        setTeams(sortedData);
      } catch (error) {
        console.error("Erro ao buscar times:", error);
      }
    };

    fetchTeams();
  }, []);

  return (
    <Container>
      <h2 className="text-center mb-3">Classificação</h2>
      <Table striped bordered hover className="standings-table">
        <thead>
          <tr>
            <th>Posição</th>
            <th>Time</th>
            <th>Pontos</th>
          </tr>
        </thead>
        <tbody>
          {teams.map((team, index) => (
            <tr key={team.id}>
              <td>{index + 1}</td>
              <td>{team.nome}</td>
              <td>{team.pontos}</td>
            </tr>
          ))}
        </tbody>
      </Table>
    </Container>
  );
};

// eslint-disable-next-line no-irregular-whitespace
export default Standings;