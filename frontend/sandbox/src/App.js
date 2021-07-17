import { Button, TextField, Box } from '@material-ui/core';
import React, { useEffect } from 'react';
import HomePage from './components/HomePage';
import UploadPage from './components/UploadPage';
import Header from './components/Header';
import Channels from './components/Channels';

import {
  BrowserRouter as Router,
  Switch,
  Route,
  Link
} from "react-router-dom";


function App() {


  return (
    <Router>
        <Switch>
          <Route path="/upload">
            <Header PageContents={<UploadPage />} />
          </Route>
          <Route path="/channels">
            <Header PageContents={<Channels />} />
          </Route>
          <Route path="/">
            <Header PageContents={<HomePage />} />
          </Route>
        </Switch>
    </Router>
  );
}

export default App;
