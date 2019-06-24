import React, { Component } from 'react';
import "bootstrap/dist/css/bootstrap.min.css";
import { BrowserRouter as Router, Route, Link } from "react-router-dom";

import "bootstrap/dist/css/bootstrap.min.css";

import ClassSearch from "./components/class-search.component";
import PopularCourses from "./components/popular-courses.component";
import PopularSchools from "./components/popular-schools.component";
import SelectSchool from "./components/select-school.component"
import logo from "./logo.png"


class App extends Component{
  render(){
    return(
      <Router>
        <div className="container">
          <nav className="navbar navbar-expand-lg navbar-light bg-light">
            <img src={logo} width="30" height = "30" alt="Logo" />
            <Link to="/" className="navbar-brand">Summer Registrar</Link>
            <div className="collpase navbar-collapse">
              <ul className="navbar-nav mr-auto">
                <li className="navbar-item">
                  <Link to="/popular-courses" className="nav-link">Search for Classes</Link>
                </li>
                <li className="navbar-item">
                  <Link to="/popular-schools" className="nav-link">Popular Schools</Link>
                </li>
              </ul>
            </div>
          </nav>
          <Route path="/" exact component={ClassSearch} />
          <Route path="/popular-courses" component={PopularCourses} />
          <Route path="/popular-schools" component={PopularSchools} />

        </div>
      </Router>


    )
  }
}

export default App;
