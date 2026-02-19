import React, { useState, useEffect } from 'react';

function Workouts() {
  const [workouts, setWorkouts] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchWorkouts = async () => {
      const apiUrl = `https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api/workouts/`;
      console.log('Fetching workouts from:', apiUrl);
      
      try {
        const response = await fetch(apiUrl);
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
        const data = await response.json();
        console.log('Workouts data received:', data);
        
        // Handle both paginated (.results) and plain array responses
        const workoutsData = data.results || data;
        setWorkouts(workoutsData);
        setLoading(false);
      } catch (err) {
        console.error('Error fetching workouts:', err);
        setError(err.message);
        setLoading(false);
      }
    };

    fetchWorkouts();
  }, []);

  if (loading) return <div className="container mt-4"><div className="loading">Loading workouts...</div></div>;
  if (error) return <div className="container mt-4"><div className="error">Error: {error}</div></div>;

  return (
    <div className="container mt-4">
      <div className="d-flex justify-content-between align-items-center mb-4">
        <h2>Suggested Workouts</h2>
        <button className="btn btn-primary">
          <i className="bi bi-plus-circle"></i> Create Workout
        </button>
      </div>
      <div className="table-responsive">
        <table className="table table-striped table-hover">
          <thead>
            <tr>
              <th>Workout Name</th>
              <th>Type</th>
              <th>Description</th>
              <th>Duration (min)</th>
              <th>Calories</th>
              <th>Difficulty</th>
              <th>Actions</th>
            </tr>
          </thead>
          <tbody>
            {workouts.length === 0 ? (
              <tr>
                <td colSpan="7" className="text-center">No workouts found.</td>
              </tr>
            ) : (
              workouts.map((workout) => (
                <tr key={workout.id}>
                  <td><strong>{workout.name}</strong></td>
                  <td><span className="badge bg-secondary">{workout.activity_type}</span></td>
                  <td>{workout.description}</td>
                  <td>{workout.estimated_duration}</td>
                  <td>{workout.estimated_calories}</td>
                  <td>
                    <span className={`badge ${
                      workout.difficulty === 'Beginner' ? 'bg-success' :
                      workout.difficulty === 'Intermediate' ? 'bg-warning' :
                      'bg-danger'
                    }`}>
                      {workout.difficulty}
                    </span>
                  </td>
                  <td>
                    <button className="btn btn-sm btn-outline-primary me-1">Start</button>
                    <button className="btn btn-sm btn-outline-secondary me-1">View</button>
                    <button className="btn btn-sm btn-outline-info">Save</button>
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

export default Workouts;
