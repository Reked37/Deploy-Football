import React from "react"
// import { useDispatch } from "react-redux"
// import { useNavigate } from "react-router-dom"
// import { deleteCoach } from "../Redux/coachAction"
// import axios from "axios"

function CoachCard({passCoach}){
    const {name, coaching_position, team}=passCoach

    return (
        <div class='ui four wide column'>
            <div class='ui-card'>
                <h3 class='name'>{name}</h3>
                <h3 class='meta'>Coaching Position: {coaching_position}</h3>
                <h3 class='description'> Team: {team.name}</h3>

            </div>
        </div>
    )}


export default CoachCard