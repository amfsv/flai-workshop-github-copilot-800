import React, { useState, useEffect } from 'react';

function Leaderboard() {
  const [leaderboard, setLeaderboard] = useState([]);
  const [users, setUsers] = useState([]);
  const [teams, setTeams] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchData = async () => {
      const leaderboardUrl = `https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api/leaderboard/`;
      const usersUrl = `https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api/users/`;
      const teamsUrl = `https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api/teams/`;
      
      console.log('Fetching leaderboard from:', leaderboardUrl);
      console.log('Fetching users from:', usersUrl);
      console.log('Fetching teams from:', teamsUrl);
      
      try {
        const [leaderboardResponse, usersResponse, teamsResponse] = await Promise.all([
          fetch(leaderboardUrl),
          fetch(usersUrl),
          fetch(teamsUrl)
        ]);
        
        if (!leaderboardResponse.ok) {
          throw new Error(`HTTP error fetching leaderboard! status: ${leaderboardResponse.status}`);
        }
        if (!usersResponse.ok) {
          throw new Error(`HTTP error fetching users! status: ${usersResponse.status}`);
        }
        if (!teamsResponse.ok) {
          throw new Error(`HTTP error fetching teams! status: ${teamsResponse.status}`);
        }
        
        const leaderboardData = await leaderboardResponse.json();
        const usersData = await usersResponse.json();
        const teamsData = await teamsResponse.json();
        
        console.log('Leaderboard data received:', leaderboardData);
        console.log('Users data received:', usersData);
        console.log('Teams data received:', teamsData);
        
        // Handle both paginated (.results) and plain array responses
        const leaderboardArray = leaderboardData.results || leaderboardData;
        const usersArray = usersData.results || usersData;
        const teamsArray = teamsData.results || teamsData;
        
        setLeaderboard(leaderboardArray);
        setUsers(usersArray);
        setTeams(teamsArray);
        setLoading(false);
      } catch (err) {
        console.error('Error fetching data:', err);
        setError(err.message);
        setLoading(false);
      }
    };

    fetchData();
  }, []);

  // Helper functions to get user and team names
  const getUserName = (userId) => {
    const user = users.find(u => u.id === userId);
    return user ? user.name : `User ${userId}`;
  };

  const getTeamName = (userId) => {
    const user = users.find(u => u.id === userId);
    if (!user || !user.team_id) return 'N/A';
    const team = teams.find(t => t.id === user.team_id);
    return team ? team.name : 'N/A';
  };

  if (loading) return <div className="container mt-4"><div className="loading">Loading leaderboard...</div></div>;
  if (error) return <div className="container mt-4"><div className="error">Error: {error}</div></div>;

  return (
    <div className="container mt-4">
      <div className="d-flex justify-content-between align-items-center mb-4">
        <h2>🏆 Leaderboard</h2>
        <div>
          <button className="btn btn-outline-primary me-2">Filter by Team</button>
          <button className="btn btn-outline-secondary">Refresh</button>
        </div>
      </div>
      <div className="table-responsive">
        <table className="table table-striped table-hover">
          <thead>
            <tr>
              <th>Rank</th>
              <th>User</th>
              <th>Team</th>
              <th>Total Calories</th>
              <th>Activities</th>
              <th>Actions</th>
            </tr>
          </thead>
          <tbody>
            {leaderboard.length === 0 ? (
              <tr>
                <td colSpan="6" className="text-center">No leaderboard data found.</td>
              </tr>
            ) : (
              leaderboard.map((entry, index) => (
                <tr key={entry.id}>
                  <td>
                    <span className={`rank-badge ${
                      index === 0 ? 'rank-1' :
                      index === 1 ? 'rank-2' :
                      index === 2 ? 'rank-3' : ''
                    }`}>
                      {index === 0 ? '🥇' : index === 1 ? '🥈' : index === 2 ? '🥉' : index + 1}
                    </span>
                  </td>
                  <td><strong>{getUserName(entry.user_id)}</strong></td>
                  <td>{getTeamName(entry.user_id)}</td>
                  <td><span className="badge bg-primary">{entry.total_calories || 0} cal</span></td>
                  <td>{entry.total_activities || 0}</td>
                  <td>
                    <button className="btn btn-sm btn-outline-primary me-1">View Profile</button>
                    <button className="btn btn-sm btn-outline-info">Activities</button>
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

export default Leaderboard;
