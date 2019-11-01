import React from 'react';
import Navbar from 'react-bootstrap/Navbar';
import Home from './containers/Home';
import { library } from '@fortawesome/fontawesome-svg-core';
import { faSpinner } from '@fortawesome/free-solid-svg-icons';
import './App.css';

library.add(faSpinner);


function App() {
  return (
     <div className="App container-fluid">
        <Navbar bg="dark" variant="dark" expand="lg" collapseOnSelect>
          <Navbar.Collapse id="basic-navbar-nav">
            <Navbar.Brand href={'https://www.ginkgobioworks.com/'}>
              {' GINKGO BIOWORKS'}
            </Navbar.Brand>
          </Navbar.Collapse>
        </Navbar>
        <Home/>
      </div>
  );
}

export default App;


