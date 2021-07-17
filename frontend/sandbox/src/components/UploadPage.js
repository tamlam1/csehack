import { Button, TextField, Box } from '@material-ui/core';
import React, { useEffect } from 'react';
import {
  BrowserRouter as Router,
  Switch,
  Route,
  Link
} from "react-router-dom";
import {useForm} from 'react-hook-form'

function UploadPage() {
  const [transcript, setTranscript] = React.useState(''); 
  const {register, handleSubmit} = useForm();

  React.useEffect(() => {
    fetch('/api/home').then(r => r.json()).then((data) => {
      console.log(data.hi);
    })
  }, []);

  const sendData = () => {
    fetch('/api/get_data', {
      method: 'POST',
      headers: {
          accept: 'application/json',
          'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        "text" : "this is some text"
      }),
    }).then(r => r.json()).then((data) => {
      console.log(data.hi);
    })
  };

  return (
    <Box display="flex" flexDirection="column" className="App" alignItems="center" justifyContent="center">
      <h1>SAND BOX</h1>
      <Box display="flex" flexDirection="column" className="App" alignItems="center" justifyContent="center">
        <TextField
          name="transcript"
          placeholder="Enter lecture transcript here..."
          variant="outlined"
          multiline
          rows={10}
          rowsMax={10}
          style={{margin:"5px", width:"800px"}}
          onChange={(e) => {
            setTranscript(e.target.value);
           
          
          }}
          // className={classes.textarea}
          value={transcript}
        />
        <Button 
          variant="contained"
          color="primary"
          style={{margin:"5px"}}
          onClick={() => console.log(transcript)}
        >
          Print input
        </Button>
        <Button 
          variant="contained"
          color="primary"
          style={{margin:"5px"}}
          onClick={() => sendData(transcript)}
        >
          Upload
        </Button>
      </Box>
    </Box>
  );
}

export default UploadPage;
