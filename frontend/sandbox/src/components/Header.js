import { Button, TextField, Box } from '@material-ui/core';
import React, { useEffect } from 'react';
import {
  BrowserRouter as Router,
  Switch,
  Route,
  Link
} from "react-router-dom";

function HomePage({PageContents}) {


  return (
    <Box display="flex" flexDirection="column" className="App" alignItems="center" justifyContent="center">
      This is the homepage.
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
    {PageContents}
    </Box>
  );
}

export default HomePage;