import axios from 'axios';

const apiClient = axios.create({
  baseURL: import.meta.env.VITE_FOOTBALL_API_BASE_URL,
});

export const getTeamDetails = async (teamNome) => {
  try {
    const response = await apiClient.get('api/statistics/');
    
    
    const teamDetails = response.data.find(team => team.nome === teamNome);
    
    
    if (!teamDetails) {
      throw new Error(`Time com nome ${teamNome} não encontrado.`);
    }
    
    return teamDetails;
  } catch (error) {
    console.error(`Erro ao buscar detalhes do time com nome ${teamNome}:`, error);
    throw error; 
  }
};

export const getAllTeams = async () => {
  try {
    const response = await apiClient.get('/api/statistics/');
    return response.data;
  } catch (error) {
    console.error("Erro ao obter os times:", error);
    throw error; 
  }
};