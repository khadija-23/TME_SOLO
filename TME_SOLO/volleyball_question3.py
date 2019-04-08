from soccersimulator import Strategy, SoccerAction, Vector2D, SoccerTeam
from soccersimulator import VolleySimulation, volley_show_simu,settings


from volleyball_question1 import SuperState,EchauffementStrategy
from volleyball_question2 import AttaquantStrategy

class DefenseurStrategy(Strategy):
    def __init__(self):
        Strategy.__init__(self, "defenseur")
        
    def compute_strategy(self, state, id_team, id_player):
        s= SuperState(state, id_team, id_player)
        
        action0=SoccerAction(acceleration=s.position_def-s.player)
        
        action1=SoccerAction(acceleration=s.ball-s.player)
        action3=SoccerAction(shoot=(s.position_oppose_opposant2-s.player).normalize()*0.5)
        action4=SoccerAction(shoot=(s.position_oppose_opposant2-s.player).normalize()*0.2)
        vec2=(s.position_oppose_opposant2-s.player).normalize()*0.5
        vec3=(s.position_oppose_opposant2-s.player).normalize()*0.2
        
        if((s.id_team==1 and s.ball.x>settings.GAME_WIDTH/2 and  s.ball.x<s.get_limite) or(s.id_team==2 and s.ball.x<settings.GAME_WIDTH/2 and  s.ball.x>s.get_limite) ):
            if(vec2.x<settings.GAME_WIDTH-10 and vec2.y<settings.GAME_HEIGHT-10 and vec2.x>10 and vec2.y>10):
                return action1+action3
            elif(vec3.x<settings.GAME_WIDTH-10 and vec3.y<settings.GAME_HEIGHT-10 and vec3.x>10 and vec3.y>10):
                return action1+action4
        else:
            return action0
        

    
    # Create teams
team1 = SoccerTeam(name="Team 1")
team2 = SoccerTeam(name="Team 2")

# Add players
team1.add("Player 1", AttaquantStrategy())  
team2.add("Player 2", DefenseurStrategy())  
# Create a match
simu = VolleySimulation(team1, team2)

# Simulate and display the match
volley_show_simu(simu)






