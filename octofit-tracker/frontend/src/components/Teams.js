import React, { useState, useEffect } from 'react';

function Teams() {
  const [teams, setTeams] = useState([]);
  const [users, setUsers] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchData = async () => {
      const teamsUrl = `https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api/teams/`;
      const usersUrl = `https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api/users/`;
      console.log('Fetching teams from:', teamsUrl);
      console.log('Fetching users from:', usersUrl);
      
      try {
        const [teamsResponse, usersResponse] = await Promise.all([
          fetch(teamsUrl),
          fetch(usersUrl)
        ]);
        
        if (!teamsResponse.ok) {
          throw new Error(`HTTP error fetching teams! status: ${teamsResponse.status}`);
        }
        if (!usersResponse.ok) {
          throw new Error(`HTTP error fetching users! status: ${usersResponse.status}`);
        }
        
        const teamsData = await teamsResponse.json();
        const usersData = await usersResponse.json();
        
        console.log('Teams data received:', teamsData);
        console.log('Users data received:', usersData);
        
        // Handle both paginated (.results) and plain array responses
        const teamsArray = teamsData.results || teamsData;
        const usersArray = usersData.results || usersData;
        
        setTeams(teamsArray);
        setUsers(usersArray);
        setLoading(false);
      } catch (err) {
        console.error('Error fetching data:', err);
        setError(err.message);
        setLoading(false);
      }
    };

    fetchData();
  }, []);

  // Function to count members for a team
  const getMemberCount = (teamId) => {
    return users.filter(user => user.team_id === teamId).length;
  };

  if (loading) return <div className="container mt-4"><div className="loading">Loading teams...</div></div>;
  if (error) return <div className="container mt-4"><div className="error">Error: {error}</div></div>;

  return (
    <div className="container mt-4">
      <div className="d-flex justify-content-between align-items-center mb-4">
        <h2>Teams</h2>
        <button className="btn btn-success">
          <i className="bi bi-people"></i> Create Team
        </button>
      </div>
      <div className="table-responsive">
        <table className="table table-striped table-hover">
          <thead>
            <tr>
              <th>Team Name</th>
              <th>Description</th>
              <th>Members</th>
              <th>Created</th>
              <th>Actions</th>
            </tr>
          </thead>
          <tbody>
            {teams.length === 0 ? (
              <tr>
                <td colSpan="5" className="text-center">No teams found.</td>
              </tr>
            ) : (
              teams.map((team) => (
                <tr key={team.id}>
                  <td><strong>{team.name}</strong></td>
                  <td>{team.description || <span className="text-muted">No description</span>}</td>
                  <td>
                    <span className="badge bg-primary">{getMemberCount(team.id)}</span>
                  </td>
                  <td>{team.created_at ? new Date(team.created_at).toLocaleDateString() : '-'}</td>
                  <td>
                    <button className="btn btn-sm btn-outline-primary me-1">View</button>
                    <button className="btn btn-sm btn-outline-secondary me-1">Edit</button>
                    <button className="btn btn-sm btn-outline-danger">Delete</button>
                  </td>
                </tr>
              ))
            )}
          </tbody>
        </table>
      </div>
    </div>
  );
}

export default Teams;
