import { Button, TextField, Box } from '@material-ui/core';
import React, { useEffect } from 'react';

import AppBar from '@material-ui/core/AppBar';
import Toolbar from '@material-ui/core/Toolbar';
import Typography from '@material-ui/core/Typography';
import Autocomplete from '@material-ui/lab/Autocomplete';

import { useHistory } from 'react-router-dom';

import {
  BrowserRouter as Router,
  Switch,
  Route,
  Link
} from "react-router-dom";

const data = [
  {
    "id": '1',
    "channel_name": "channel 1",
  },
  {
    "id": '2',
    "channel_name": "channel 2",
  },
  {
    "id": '3',
    "channel_name": "channel 3",
  },
  
]

function HomePage({PageContents}) {

  let history = useHistory();
  return (
    <Box>
    <AppBar position="relative">
        <Toolbar>
          {/*Probs logo here idk*/}
          <Typography variant="h6" color="inherit" noWrap style={{margin:"5px"}}>
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
        <Autocomplete
          id="combo-box"
          options={data}
          getOptionLabel={(option) => option.channel_name}
          style={{ width: 300, background:"white", margin:"10px"}}
          renderInput={(params) => <TextField {...params} label="Channel Search" variant="outlined" />}
          onChange={(e, channelOption) => {
            
            // console.log(channelOption.id);
            if (channelOption) {
              history.push("/lectures/" + channelOption.id)
            }
          }}
        />
        </Toolbar>
        
      </AppBar>
      
 
    {PageContents}
    </Box>
  );
}

export default HomePage;