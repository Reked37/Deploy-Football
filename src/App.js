import React from "react";
import {Routes, Route } from "react-router-dom";
import Home from "./components/Home";
import PlayersContainer from './components/PlayersConatiner'
import NavBar from "./components/NavBar";
import TeamsContainer from "./components/TeamsContainer";
import CoachesContainer from "./components/CoachesContainer";
import Add from "./components/Add"
import UpdatePlayer from "./components/UpdatePlayer";
import PlayersCoaches from "./components/PlayersCoaches";
import CoachesPlayers from "./components/CoachesPlayer";
import TeamCoaches from "./components/TeamCoaches";
import TeamPlayers from "./components/TeamPlayers";
import 'semantic-ui-css/semantic.min.css'
import {Provider} from 'react-redux'
import store from "./Redux/Store";
import MatchesContainer from "./components/MatchesContainer";
import UpdateCoach from "./components/UpdateCoach";

function App() {

  return(
    <Provider store={store}>
    <div class='background'>
      <NavBar />
      <Routes>
        <Route path="/" element={<Home />}></Route>
        <Route path="/players" element={<PlayersContainer />}></Route>
        <Route path="/coaches" element={<CoachesContainer />}></Route>
        <Route path="/teams" element={<TeamsContainer />}></Route>
        <Route path='/matches' element={<MatchesContainer />}></Route>
        <Route path="/add" element={<Add />}></Route>
        <Route path='/players/:id' element={<UpdatePlayer />}></Route>
        <Route path='/playerscoaches/:id' element={<PlayersCoaches />}/>
        <Route path='/coachesplayers/:id' element={<CoachesPlayers />}/>
        <Route path='/teamcoaches/:id' element={<TeamCoaches />}/> 
        <Route path='/teamplayers/:id' element={<TeamPlayers />}/>
        <Route path='/coaches/:id' element={<UpdateCoach/>}/>
      </Routes> 
    </div>
    </Provider>
  );
}

export default App;
