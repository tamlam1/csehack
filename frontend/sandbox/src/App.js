import { Button, TextField, Box } from '@material-ui/core';
import './App.css';
import React from 'react';


function App() {
  const [transcript, setTranscript] = React.useState(''); 
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
          Upload
        </Button>
        
      </Box>
    </Box>
  );
}

export default App;
