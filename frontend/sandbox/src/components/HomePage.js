import { Button, TextField, Box } from '@material-ui/core';
import React, { useEffect } from 'react';
import {
  BrowserRouter as Router,
  Switch,
  Route,
  Link
} from "react-router-dom";

function HomePage() {


  return (
    <Box display="flex" flexDirection="column" className="App" alignItems="center" justifyContent="center">
      This is the homepage.

    
    </Box>
  );
}

export default HomePage;