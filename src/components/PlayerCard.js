import React from 'react'

function PlayerCard({passPlayer}){
    const {name, jersey_number, team}=passPlayer

    return(
        <div className="ui five wide column">
            <div className='ui-card'>
                <h3 className="name">{name}</h3>
                <h3 className='number'>#{jersey_number}</h3>
                <h3 className='description'>Team: {team.name}</h3>
                <div>
                </div>
                
            </div>
            
        </div>
    )
}
export default PlayerCard