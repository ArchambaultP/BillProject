import React, { Component } from 'react';
import logo from './logo.svg';
import { BrowserRouter as Router, Redirect, Route, Switch } from 'react-router-dom';
import Login  from './components/Login/Login';
import Register from './components/Login/Register'
import './App.css';

class App extends Component {
  render() {

      return (
              <Router>
              <Switch>
              <Route path="/" component={null} exact={true} />
              <Route path="/login" component={Login} exact={true} />
              <Route path="/register" component={Register} exact={true} />
              <Redirect to="/" />
              </Switch>
              </Router>

      );
  }
}

export default App;
