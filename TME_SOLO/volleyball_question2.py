from soccersimulator import Strategy, SoccerAction, Vector2D, SoccerTeam
from soccersimulator import VolleySimulation, volley_show_simu,settings


from volleyball_question1 import SuperState,EchauffementStrategy

class AttaquantStrategy(Strategy):
    def __init__(self):
        Strategy.__init__(self, "attaquant")
        
    def compute_strategy(self, state, id_team, id_player):
        s= SuperState(state, id_team, id_player)
        
        action2=SoccerAction(shoot=s.position_oppose_opposant2-s.player)
        action1=SoccerAction(acceleration=s.ball-s.player)
        action3=SoccerAction(shoot=(s.position_oppose_opposant2-s.player).normalize()*0.5)
        
        vec=s.position_oppose_opposant2-s.player
        vec2=(s.position_oppose_opposant2-s.player).normalize()*0.5
        
        if(vec.x<settings.GAME_WIDTH-10 and vec.y<settings.GAME_HEIGHT-10 and vec.x>10 and vec.y>10):
            return action1+action2
        elif(vec2.x<settings.GAME_WIDTH-10 and vec2.y<settings.GAME_HEIGHT-10 and vec2.x>10 and vec2.y>10):
            return action1+action3
        else: 
            return action1
        

    
    # Create teams
team1 = SoccerTeam(name="Team 1")
team2 = SoccerTeam(name="Team 2")

# Add players
team1.add("Player 1", AttaquantStrategy())  
team2.add("Player 2", AttaquantStrategy())  
# Create a match
#simu = VolleySimulation(team1, team2)

# Simulate and display the match
#volley_show_simu(simu)
