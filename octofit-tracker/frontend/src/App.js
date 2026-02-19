import React from 'react';
import { BrowserRouter as Router, Routes, Route, Link, useNavigate } from 'react-router-dom';
import './App.css';
import Activities from './components/Activities';
import Leaderboard from './components/Leaderboard';
import Teams from './components/Teams';
import Users from './components/Users';
import Workouts from './components/Workouts';

function HomePage() {
  const navigate = useNavigate();

  return (
    <div className="container mt-4">
      <div className="home-welcome">
        <h1 className="display-4">Welcome to OctoFit Tracker</h1>
        <p className="lead">Track your fitness journey, compete with your team, and achieve your goals!</p>
        <hr className="my-4" />
        <div className="row mt-5">
          <div className="col-md-3 mb-4">
            <div className="card text-center" onClick={() => navigate('/users')} style={{ cursor: 'pointer' }}>
              <div className="card-body">
                <h5 className="card-title">👤 Users</h5>
                <p className="card-text">View and manage user profiles</p>
                <Link to="/users" className="btn btn-info" onClick={(e) => e.stopPropagation()}>View Users</Link>
              </div>
            </div>
          </div>
          <div className="col-md-3 mb-4">
            <div className="card text-center" onClick={() => navigate('/activities')} style={{ cursor: 'pointer' }}>
              <div className="card-body">
                <h5 className="card-title">🏋️ Activities</h5>
                <p className="card-text">Log your workouts and monitor your progress</p>
                <Link to="/activities" className="btn btn-primary" onClick={(e) => e.stopPropagation()}>View Activities</Link>
              </div>
            </div>
          </div>
          <div className="col-md-3 mb-4">
            <div className="card text-center" onClick={() => navigate('/teams')} style={{ cursor: 'pointer' }}>
              <div className="card-body">
                <h5 className="card-title">👥 Teams</h5>
                <p className="card-text">Collaborate with others to reach your fitness goals</p>
                <Link to="/teams" className="btn btn-success" onClick={(e) => e.stopPropagation()}>View Teams</Link>
              </div>
            </div>
          </div>
          <div className="col-md-3 mb-4">
            <div className="card text-center" onClick={() => navigate('/leaderboard')} style={{ cursor: 'pointer' }}>
              <div className="card-body">
                <h5 className="card-title">🏆 Leaderboard</h5>
                <p className="card-text">Check the leaderboard and see how you rank</p>
                <Link to="/leaderboard" className="btn btn-warning" onClick={(e) => e.stopPropagation()}>View Leaderboard</Link>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}

function App() {
  return (
    <Router>
      <div className="App">
        <nav className="navbar navbar-expand-lg navbar-dark bg-dark">
          <div className="container-fluid">
            <Link className="navbar-brand" to="/">
              <img src="/octofitapp-small.png" alt="OctoFit Logo" className="navbar-logo" />
              OctoFit Tracker
            </Link>
            <button className="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav">
              <span className="navbar-toggler-icon"></span>
            </button>
            <div className="collapse navbar-collapse" id="navbarNav">
              <ul className="navbar-nav">
                <li className="nav-item">
                  <Link className="nav-link" to="/">Home</Link>
                </li>
                <li className="nav-item">
                  <Link className="nav-link" to="/users">Users</Link>
                </li>
                <li className="nav-item">
                  <Link className="nav-link" to="/teams">Teams</Link>
                </li>
                <li className="nav-item">
                  <Link className="nav-link" to="/activities">Activities</Link>
                </li>
                <li className="nav-item">
                  <Link className="nav-link" to="/workouts">Workouts</Link>
                </li>
                <li className="nav-item">
                  <Link className="nav-link" to="/leaderboard">Leaderboard</Link>
                </li>
              </ul>
            </div>
          </div>
        </nav>

        <Routes>
          <Route path="/" element={<HomePage />} />
          <Route path="/users" element={<Users />} />
          <Route path="/teams" element={<Teams />} />
          <Route path="/activities" element={<Activities />} />
          <Route path="/workouts" element={<Workouts />} />
          <Route path="/leaderboard" element={<Leaderboard />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;
