import { Button, TextField, Box } from '@material-ui/core';
import React, { useEffect } from 'react';

import AppBar from '@material-ui/core/AppBar';
import Toolbar from '@material-ui/core/Toolbar';
import Typography from '@material-ui/core/Typography';

import {
  BrowserRouter as Router,
  Switch,
  Route,
  Link
} from "react-router-dom";

function HomePage({PageContents}) {


  return (
    <Box>
    <AppBar position="relative">
        <Toolbar>
          {/*Probs logo here idk*/}
          <Typography variant="h6" color="inherit" noWrap>
            SAND BOX
          </Typography>
          <Link to="/upload">
      <Button 
        variant="contained"
        color="primary"
        style={{margin:"5px"}}
      >
        Upload Lecture
      </Button>
    </Link>
    <Link to="/">
      <Button 
        variant="contained"
        color="primary"
        style={{margin:"5px"}}
      >
        Home
      </Button>
    </Link>
    <Link to="/channels">
      <Button 
        variant="contained"
        color="primary"
        style={{margin:"5px"}}
      >
        Channels
      </Button>
    </Link>
        </Toolbar>
      </AppBar>
      
 
    {PageContents}
    </Box>
  );
}

export default HomePage;