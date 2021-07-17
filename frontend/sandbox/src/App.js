import { Button, TextField, Box } from '@material-ui/core';
import React, { useEffect } from 'react';
import HomePage from './components/HomePage';
import UploadPage from './components/UploadPage';
import Header from './components/Header';
import ChannelsPage from './components/ChannelsPage';
import LecturePage from './components/LecturePage';

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
          <Route path="/lectures/:channelId">
            <Header PageContents={<LecturePage />} />
          </Route>
          <Route path="/channels">
            <Header PageContents={<ChannelsPage />} />
          </Route>
          <Route path="/">
            <Header PageContents={<HomePage />} />
          </Route>
        </Switch>
    </Router>
  );
}

export default App;
