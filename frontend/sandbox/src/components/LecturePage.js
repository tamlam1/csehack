import { Button, TextField, Box } from '@material-ui/core';
import React, { useEffect } from 'react';
import {
  BrowserRouter as Router,
  Switch,
  Route,
  Link
} from "react-router-dom";
import { useHistory, useParams } from 'react-router-dom';
import { makeStyles, useTheme } from '@material-ui/core/styles';
import {
  createTheme,
  MuiThemeProvider,
  withStyles
} from "@material-ui/core/styles";

import PropTypes from 'prop-types';

import Table from '@material-ui/core/Table';
import TableBody from '@material-ui/core/TableBody';
import TableCell from '@material-ui/core/TableCell';
import TableHead from '@material-ui/core/TableHead';
import TableContainer from '@material-ui/core/TableContainer';
import TableFooter from '@material-ui/core/TableFooter';
import TablePagination from '@material-ui/core/TablePagination';
import TableRow from '@material-ui/core/TableRow';
import Paper from '@material-ui/core/Paper';
import IconButton from '@material-ui/core/IconButton';
import FirstPageIcon from '@material-ui/icons/FirstPage';
import KeyboardArrowLeft from '@material-ui/icons/KeyboardArrowLeft';
import KeyboardArrowRight from '@material-ui/icons/KeyboardArrowRight';
import LastPageIcon from '@material-ui/icons/LastPage';

import KeyboardArrowDownIcon from '@material-ui/icons/KeyboardArrowDown';
import KeyboardArrowUpIcon from '@material-ui/icons/KeyboardArrowUp';
import PhonelinkRingIcon from '@material-ui/icons/PhonelinkRing';
import PhoneCallbackIcon from '@material-ui/icons/PhoneCallback';

import Tooltip from '@material-ui/core/Tooltip';

import Dialog from '@material-ui/core/Dialog';
import DialogActions from '@material-ui/core/DialogActions';
import DialogContent from '@material-ui/core/DialogContent';
import DialogContentText from '@material-ui/core/DialogContentText';
import DialogTitle from '@material-ui/core/DialogTitle';

import PhoneInput from 'react-phone-input-2'
import 'react-phone-input-2/lib/style.css'

const defaultTheme = createTheme();
const theme = createTheme({
  overrides: {
    MuiTooltip: {
      tooltip: {
        fontSize: "0.9em",
      }
    }
  }
});

const useStyles1 = makeStyles((theme) => ({
  root: {
    flexShrink: 0,
    marginLeft: theme.spacing(2.5),
  },
}));

// const data = {
//   "data": [
//     {
//       "id": '1',
//       "lecture_name": "lecture 1",
//       "time_uploaded": "17/07/21",
//     },
//     {
//       "id": '2',
//       "lecture_name": "lecture 2",
//       "time_uploaded": "18/07/21",
//     },
//     {
//       "id": '3',
//       "lecture_name": "lecture 3",
//       "time_uploaded": "19/07/21",
//     },
//   ]
// };

const data = [
  {
    "id": '1',
    "lecture_name": "lecture 1",
    "time_uploaded": "17/07/21",
  },
  {
    "id": '2',
    "lecture_name": "lecture 2",
    "time_uploaded": "18/07/21",
  },
  {
    "id": '3',
    "lecture_name": "lecture 3",
    "time_uploaded": "19/07/21",
  },
  {
    "id": '4',
    "lecture_name": "lecture 1",
    "time_uploaded": "17/07/21",
  },
  {
    "id": '5',
    "lecture_name": "lecture 2",
    "time_uploaded": "18/07/21",
  },
  {
    "id": '6',
    "lecture_name": "lecture 3",
    "time_uploaded": "19/07/21",
  },
  {
    "id": '7',
    "lecture_name": "lecture 1",
    "time_uploaded": "17/07/21",
  },
  {
    "id": '8',
    "lecture_name": "lecture 2",
    "time_uploaded": "18/07/21",
  },
  {
    "id": '9',
    "lecture_name": "lecture 3",
    "time_uploaded": "19/07/21",
  },
  {
    "id": '10',
    "lecture_name": "lecture 1",
    "time_uploaded": "17/07/21",
  },
  {
    "id": '11',
    "lecture_name": "lecture 2",
    "time_uploaded": "18/07/21",
  },
  
]

function TablePaginationActions(props) {
  const classes = useStyles1();
  const theme = useTheme();
  const { count, page, rowsPerPage, onPageChange } = props;

  const handleFirstPageButtonClick = (event) => {
    onPageChange(event, 0);
  };

  const handleBackButtonClick = (event) => {
    onPageChange(event, page - 1);
  };

  const handleNextButtonClick = (event) => {
    onPageChange(event, page + 1);
  };

  const handleLastPageButtonClick = (event) => {
    onPageChange(event, Math.max(0, Math.ceil(count / rowsPerPage) - 1));
  };

  return (
    <div className={classes.root}>
      <IconButton
        onClick={handleFirstPageButtonClick}
        disabled={page === 0}
        aria-label="first page"
      >
        {theme.direction === 'rtl' ? <LastPageIcon /> : <FirstPageIcon />}
      </IconButton>
      <IconButton onClick={handleBackButtonClick} disabled={page === 0} aria-label="previous page">
        {theme.direction === 'rtl' ? <KeyboardArrowRight /> : <KeyboardArrowLeft />}
      </IconButton>
      <IconButton
        onClick={handleNextButtonClick}
        disabled={page >= Math.ceil(count / rowsPerPage) - 1}
        aria-label="next page"
      >
        {theme.direction === 'rtl' ? <KeyboardArrowLeft /> : <KeyboardArrowRight />}
      </IconButton>
      <IconButton
        onClick={handleLastPageButtonClick}
        disabled={page >= Math.ceil(count / rowsPerPage) - 1}
        aria-label="last page"
      >
        {theme.direction === 'rtl' ? <FirstPageIcon /> : <LastPageIcon />}
      </IconButton>
    </div>
  );
}

TablePaginationActions.propTypes = {
  count: PropTypes.number.isRequired,
  onPageChange: PropTypes.func.isRequired,
  page: PropTypes.number.isRequired,
  rowsPerPage: PropTypes.number.isRequired,
};




const useStyles2 = makeStyles({
  table: {
    minWidth: 500,
    width: "100%",
  },
  card: {
    maxWidth: "90%",
    margin: "40px",
  },
});



function LecturePage() {
  let {channelId} = useParams();
  const classes = useStyles2();
  const [page, setPage] = React.useState(0);
  const [rowsPerPage, setRowsPerPage] = React.useState(5);

  const emptyRows = rowsPerPage - Math.min(rowsPerPage, data.length - page * rowsPerPage);

  const handleChangePage = (event, newPage) => {
    setPage(newPage);
  };

  const handleChangeRowsPerPage = (event) => {
    setRowsPerPage(parseInt(event.target.value, 10));
    setPage(0);
  };


  // functions for dialog box =================================
  const [open, setOpen] = React.useState(false);

  const handleClickOpen = () => {
    setOpen(true);
  };

  const handleClose = () => {
    setOpen(false);
  };

  const [phoneNumber, setPhoneNumber] = React.useState('');
  const [currLecture, setCurrLecture] = React.useState('');
  // =========================================================

  const submitPhoneNumber = () => {
    fetch('/api/play_lecture', {
      method: 'POST',
      headers: {
          accept: 'application/json',
          'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        "phone_number" : '+' + [phoneNumber],
        "lecture_id": [currLecture],
      }),
    }).then(r => r.json()).then((data) => {
      console.log(data.hi);
    })
    // console.log(phoneNumber);
  };

  return (
    <Box display="flex" flexDirection="column" className="App" alignItems="center" justifyContent="center">
      This is the channels page.
      <MuiThemeProvider theme={theme}>
      <TableContainer component={Paper} className={classes.card}>
        <Table className={classes.table} aria-label="custom pagination table">
          <TableHead>
            <TableRow>
              <TableCell width="70%">
                Lecture
              </TableCell>
              <TableCell width="20%" align="center">
                Time Uploaded
              </TableCell>
              <TableCell width="10%" align="center">
                
              </TableCell>
            </TableRow>
          </TableHead>
          <TableBody>
            {(rowsPerPage > 0
              ? data.slice(page * rowsPerPage, page * rowsPerPage + rowsPerPage)
              : data
            ).map((lecture) => (
              <TableRow key={lecture.id}>
                <TableCell width="70%">
                  {lecture.lecture_name}
                </TableCell>
                <TableCell width="20%" align="center">
                  {lecture.time_uploaded}
                </TableCell>
                <TableCell width="10%" align="center">
                  <Button 
                    onClick={() => {
                      handleClickOpen();
                      setCurrLecture(lecture.id);
                    }}
                  >
                  <Tooltip title="Play via phone call"><PhoneCallbackIcon /></Tooltip>
                  </Button>


                  <Dialog open={open} onClose={handleClose} aria-labelledby="form-dialog-title">
                    <DialogTitle id="form-dialog-title">Play on phone</DialogTitle>
                    <DialogContent>
                      <DialogContentText>
                        Please enter you phone number to play the lecture.
                      </DialogContentText>
                      <PhoneInput
                        country={'au'}
                        value={phoneNumber}
                        onChange={setPhoneNumber}
                      />
                    </DialogContent>
                    <DialogActions>
                      <Button onClick={handleClose} color="primary">
                        Cancel
                      </Button>
                      <Button onClick={() => {
                        handleClose();
                        submitPhoneNumber();
                        }}
                        color="primary">
                        Play
                      </Button>
                    </DialogActions>
                  </Dialog>


                </TableCell>
              </TableRow>
            ))}

            {emptyRows > 0 && (
              <TableRow style={{ height: 53 * emptyRows }}>
                <TableCell colSpan={6} />
              </TableRow>
            )}
          </TableBody>
          <TableFooter>
            <TableRow>
              <TablePagination
                rowsPerPageOptions={[5, 10, 25, { label: 'All', value: -1 }]}
                colSpan={3}
                count={data.length}
                rowsPerPage={rowsPerPage}
                page={page}
                SelectProps={{
                  inputProps: { 'aria-label': 'rows per page' },
                  native: true,
                }}
                onPageChange={handleChangePage}
                onRowsPerPageChange={handleChangeRowsPerPage}
                ActionsComponent={TablePaginationActions}
              />
            </TableRow>
          </TableFooter>
        </Table>
      </TableContainer>












      </MuiThemeProvider>
    </Box>
  );
}

export default LecturePage;