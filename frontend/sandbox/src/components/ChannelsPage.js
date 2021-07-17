import { Button, TextField, Box, Typography } from '@material-ui/core';
import React, { useEffect } from 'react';
import {
  BrowserRouter as Router,
  Switch,
  Route,
  Link
} from "react-router-dom";
import { makeStyles, ThemeProvider, useTheme } from '@material-ui/core/styles';


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
import AddCircleOutlineIcon from '@material-ui/icons/AddCircleOutline';
import Tooltip from '@material-ui/core/Tooltip';
import {
  createTheme,
  MuiThemeProvider,
  withStyles
} from "@material-ui/core/styles";
import { useHistory, useParams } from 'react-router-dom';

import Dialog from '@material-ui/core/Dialog';
import DialogActions from '@material-ui/core/DialogActions';
import DialogContent from '@material-ui/core/DialogContent';
import DialogContentText from '@material-ui/core/DialogContentText';
import DialogTitle from '@material-ui/core/DialogTitle';

import PhoneInput from 'react-phone-input-2'
import 'react-phone-input-2/lib/style.css'

import RemoveCircleOutlineIcon from '@material-ui/icons/RemoveCircleOutline';

const useStyles1 = makeStyles((theme) => ({
  root: {
    flexShrink: 0,
    marginLeft: theme.spacing(2.5),
  },
}));

const titleTheme = createTheme();

titleTheme.typography.h3 = {
  fontSize: '1.5rem',
  '@media (min-width:600px)': {
    fontSize: '1.5rem',
  },
  [titleTheme.breakpoints.up('md')]: {
    fontSize: '2rem',
  },
  fontWeight: '600',
};


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



function ChannelsPage() {

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



  const [openRemove, setOpenRemove] = React.useState(false);

  const handleClickOpenRemove = () => {
    setOpenRemove(true);
  };

  const handleCloseRemove = () => {
    setOpenRemove(false);
  };



  const [phoneNumber, setPhoneNumber] = React.useState();
  const [currChannel, setCurrChannel] = React.useState('');
  // =========================================================

  const submitPhoneNumber = () => {
    fetch('/api/subscribe_user', {
      method: 'POST',
      headers: {
          accept: 'application/json',
          'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        "phone_number" : '+' + [phoneNumber],
        "channel_id": [currChannel],
      }),
    }).then(r => r.json()).then((data) => {
      console.log(data.hi);
    })
    // console.log(phoneNumber);
  };

  const submitPhoneNumberRemove = () => {
    fetch('/api/unsubscribe_user_web', {
      method: 'POST',
      headers: {
          accept: 'application/json',
          'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        "phone_number" : '+' + [phoneNumber],
        "channel_id": [currChannel],
      }),
    }).then(r => r.json()).then((data) => {
      console.log(data.hi);
    })
    // console.log(phoneNumber);
  };

  return (
    <Box display="flex" flexDirection="column" className="App" alignItems="center" justifyContent="center">
      <MuiThemeProvider theme={theme}>
        <ThemeProvider theme={titleTheme}>
          <Typography variant='h3'>This is the channels page.</Typography>
        </ThemeProvider>
      <TableContainer component={Paper} className={classes.card}>
        <Table className={classes.table} aria-label="custom pagination table">
          <TableHead>
            <TableRow>
              <TableCell width="3%" align="center">
                
              </TableCell>
              <TableCell width="3%" align="center">
                
              </TableCell>
              <TableCell width="94%">
                Topic
              </TableCell>
              
            </TableRow>
          </TableHead>
          <TableBody>
            {(rowsPerPage > 0
              ? data.slice(page * rowsPerPage, page * rowsPerPage + rowsPerPage)
              : data
            ).map((channel) => (
              <TableRow key={channel.id}>
                <TableCell width="3%" align="right">
                  <Button
                    onClick={() => {
                      handleClickOpen();
                      setCurrChannel(channel.id);
                    }}
                  >
                    <Tooltip title={'Subscribe to channel ' + channel.channel_name}><AddCircleOutlineIcon /></Tooltip>
                    
                  </Button>
                  <Dialog open={open} onClose={handleClose} aria-labelledby="form-dialog-title">
                    <DialogTitle id="form-dialog-title">Subscribe</DialogTitle>
                    <DialogContent>
                      <DialogContentText>
                        Please enter you phone number to subscribe to the channel.
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
                        Subscribe
                      </Button>
                    </DialogActions>
                  </Dialog>
                </TableCell>
                <TableCell width="3%" align="left">
                  <Button
                    onClick={() => {
                      handleClickOpenRemove();
                      setCurrChannel(channel.id);
                    }}
                  >
                    <Tooltip title={'Unsubscribe to channel ' + channel.channel_name}><RemoveCircleOutlineIcon /></Tooltip>
                    
                  </Button>
                  <Dialog open={openRemove} onClose={handleCloseRemove} aria-labelledby="form-dialog-title">
                    <DialogTitle id="form-dialog-title">Unsubscribe</DialogTitle>
                    <DialogContent>
                      <DialogContentText>
                        Please enter you phone number to unsubscribe to the channel.
                      </DialogContentText>
                      <PhoneInput
                        country={'au'}
                        value={phoneNumber}
                        onChange={setPhoneNumber}
                      />
                    </DialogContent>
                    <DialogActions>
                      <Button onClick={handleCloseRemove} color="primary">
                        Cancel
                      </Button>
                      <Button onClick={() => {
                        handleCloseRemove();
                        submitPhoneNumberRemove();
                        }}
                        color="primary">
                        Unsubscribe
                      </Button>
                    </DialogActions>
                  </Dialog>
                </TableCell>
                <TableCell width="94%">
                  <Link to={/lectures/ + channel.id} style={{textDecoration:"none", color:"#1165ed"}}>
                    {channel.channel_name}
                  </Link>
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

export default ChannelsPage;