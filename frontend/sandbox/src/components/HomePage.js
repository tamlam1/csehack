import { Button, TextField, Box } from '@material-ui/core';
import React, { useEffect } from 'react';

import AppBar from '@material-ui/core/AppBar';

import Card from '@material-ui/core/Card';
import CardActions from '@material-ui/core/CardActions';
import CardContent from '@material-ui/core/CardContent';
import CardMedia from '@material-ui/core/CardMedia';
import CssBaseline from '@material-ui/core/CssBaseline';
import Grid from '@material-ui/core/Grid';
import Toolbar from '@material-ui/core/Toolbar';
import Typography from '@material-ui/core/Typography';
import { makeStyles } from '@material-ui/core/styles';
import Container from '@material-ui/core/Container';


import {
  BrowserRouter as Router,
  Switch,
  Route,
  Link
} from "react-router-dom";


const useStyles = makeStyles((theme) => ({
  icon: {
    marginRight: theme.spacing(2),
  },
  heroContent: {
    backgroundColor: theme.palette.background.paper,
    padding: theme.spacing(8, 0, 6),
  },
  heroButtons: {
    marginTop: theme.spacing(4),
  },
  cardGrid: {
    paddingTop: theme.spacing(8),
    paddingBottom: theme.spacing(8),
  },
  card: {
    height: '100%',
    display: 'flex',
    flexDirection: 'column',
  },
  cardMedia: {
    paddingTop: '70%', // 16:9
  },
  cardContent: {
    flexGrow: 1,
  },
  footer: {
    backgroundColor: theme.palette.background.paper,
    padding: theme.spacing(6),
  },
}));

const cards = [1, 2, 3, 4, 5, 6, 7, 8, 9];
const categories = 
[{cat: "Chemistry", 
  img: "chemistry.png",
  desc: "Why does a cake rise in the oven? What are fireworks made from? Chemistry deals with the properties, composition, and structure of substances and the transformations they undergo."
  }, 

  {cat: "Physics", 
  img: "physics.png",
  desc: "Imagine the following scenario: A cartoon character keeps running off the edge of a cliff and onto thin air before suddenly falling straight to the ground. Could this happen in real life?"
  }, 
  
  {cat: "Biology",
  img: "bio.png",
  desc: "When did human life first begin and are we really related to monkeys? Biology is the study of living things including plants, animals, and bacteria."
  }, 
  
  {cat: "Maths", 
  img: "maths.png",
  desc: "People have used math since ancient times - the Egyptians could not have built the pyramids without maths. Some of the main branches of maths are algebra, calculus, geometry, and statistics"
  }, 
  
  {cat: "PDHPE", 
  img: "pdhpe.png",
  desc: "A variety issues can have an impact on your future health and wellbeing. PDHPE (Personal Development, Health, and Physical Education), attempts to contribute to the ognitive, social, emotional, physical and spiritual development of students."
  }, 
  
  {cat: "Geography", 
  img: "geo.png",
  desc: "The word Geography comes from the Greek words 'geo', meaning 'Earth', and 'graphy', meaning 'writing or description'. Geography aims to teach us about the science of the Earth’s surface, its atmosphere, and its features."
  }, 
  
  {cat: "Ancient History", 
  img: "ahist.png",
  desc: "Ancient history is all the events we know about between the invention of writing and the start of the Middle Ages. Archeologists study early human history and ancient history by discovering artifacts that give us clues about our past.  Historians study primary and secondary resources and connect ideas and make theories."
  }, 
  
  {cat: "Modern History", 
  img: "mhist.png",
  desc: "Modern history is the history of the world beginning after the Middle Ages. It is the start of recognizable nations that we know today"
  }, 
  
  {cat: "English", 
  img: "eng.png",
  desc: "English includes the study of literature and language. English is used in films, literature, songs, sports, trade, products, science and technology, and through these areas many English words and expressions have found their way into our own languages."
  }]

function HomePage() {

  const classes = useStyles();

  return (
    <React.Fragment>
      <CssBaseline />
      
      <main>
        {/* Hero unit */}
        <div className={classes.heroContent}>
          <Container maxWidth="sm">
            <Typography component="h1" variant="h2" align="center" color="textPrimary" gutterBottom>
            SAND BOX
            </Typography>
            <Typography variant="h5" align="center" color="textSecondary" paragraph>
              Welcome to Sandbox! Get started by browsing the categories below!
            </Typography>
            <div className={classes.heroButtons}>
              <Grid container spacing={2} justifyContent="center">
                <Grid item>
                  <Button variant="contained" color="primary">
                    Button
                  </Button>
                </Grid>
                <Grid item>
                  <Button variant="outlined" color="primary">
                    Other Button
                  </Button>
                </Grid>
              </Grid>
            </div>
          </Container>
        </div>
        <Container className={classes.cardGrid} maxWidth="lg">
          {/* End hero unit */}
          <Grid container spacing={4}>
            {categories.map(({cat, img, desc}) => (
              <Grid item key={cat} xs={12} sm={6} md={4}>
                <Card className={classes.card}>
                  <CardMedia
                    className={classes.cardMedia}
                    image={process.env.PUBLIC_URL + img}
                  />
                  <CardContent className={classes.cardContent}>
                    <Typography gutterBottom variant="h5" component="h2">
                      {cat}
                    </Typography>
                    <Typography>
                      {desc}
                    </Typography>
                  </CardContent>
                  <CardActions>
                    <Button size="small" color="primary">
                      View Channels
                    </Button>
                  </CardActions>
                </Card>
              </Grid>
            ))}
          </Grid>
        </Container>
      </main>

      <footer className={classes.footer}>
        <Typography variant="subtitle1" align="center" color="textSecondary" component="p">
          By Samsun Tech
        </Typography>
      </footer>
    </React.Fragment>
  );
}


export default HomePage;