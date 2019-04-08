from soccersimulator import Strategy, SoccerAction, Vector2D, SoccerTeam
from soccersimulator import VolleySimulation, volley_show_simu,settings


class SuperState(object):
    def __init__(self,state,id_team,id_player):
        self.state=state
        self.id_team=id_team
        self.id_player=id_player
    
    def __get_attr__(self,attr):
        return getattr(self.state, attr)
        
    @property
    def ball(self):
        return self.state.ball.position
   
    @property
    def ball_norm(self):
        return self.state.ball.position.norm
    
    @property
    def ball_vitesse(self):
        return self.state.ball.vitesse

    @property
    def player(self):
        return self.state.player_state(self.id_team, self.id_player).position

    @property
    def liste_op(self):
        return [self.state.player_state(id_team,id_player).position for (id_team, id_player) in self.state.players
                if id_team != self.id_team]

    @property
    def liste_opposant_player(self):
        return [self.state.player_state(id_team,id_player) for (id_team, id_player) in self.state.players if id_team != self.id_team ]


    @property
    def liste_opposant_player_ID(self):
        return [(id_team,id_player) for (id_team, id_player) in self.state.players if id_team != self.id_team]
    
    @property
    def op_lePlusProche(self):# distance de l'opposant le + proche 
        return min([(self.player.distance(player),player) for player in self.liste_op])[0] 
                     


    @property
    def position_opposant_lePlusProche(self):#position de l'opposant le + proche 
        v=Vector2D(0,0)
        min_dist=settings.GAME_WIDTH*2
        for k in self.liste_op[0:-1]:
            if(k.distance(self.player)<min_dist and k!=self.player):
                min_dist=k.distance(self.player)
                v=k
        return v   


    @property
    def pos(self):
        if(self.id_team==1):
            return Vector2D(settings.GAME_WIDTH/2 -1,self.player.y)  
        else:
            return Vector2D(settings.GAME_WIDTH/2 +1,self.player.y) 
            
#    @property
#    def (self):
#        if(self.id_team==1):
#            return Vector2D(settings.GAME_WIDTH/2 -1,self.player.y)  
#        else:
#            return Vector2D(settings.GAME_WIDTH/2 +1,self.player.y) 


class EchauffementStrategy(Strategy):
    def __init__(self):
        Strategy.__init__(self, "echauffement")
        
    def compute_strategy(self, state, id_team, id_player):
        s= SuperState(state, id_team, id_player)
        
        action2=SoccerAction(shoot=s.position_opposant_lePlusProche-s.player)
        
        action1=SoccerAction(acceleration=s.ball-s.player)
        return action1+action2







# Create teams
team1 = SoccerTeam(name="Team 1")
team2 = SoccerTeam(name="Team 2")

# Add players
team1.add("Player 1", EchauffementStrategy())  
team2.add("Player 2", EchauffementStrategy())  
# Create a match
simu = VolleySimulation(team1, team2)

# Simulate and display the match
volley_show_simu(simu)






## coding: utf-8
#from soccersimulator import Strategy, SoccerAction, Vector2D, SoccerTeam
#from soccersimulator import VolleySimulation, volley_show_simu
#
#
#class RandomStrategy(Strategy):
#    def __init__(self):
#        Strategy.__init__(self, "Random")
#
#    def compute_strategy(self, state, id_team, id_player):
#        return SoccerAction(acceleration=Vector2D.create_random(-1, 1),
#                            shoot=Vector2D.create_random(-1, 1))
#
#
## Create teams
#team1 = SoccerTeam(name="Team 1")
#team2 = SoccerTeam(name="Team 2")
#
## Add players
#team1.add("Player 1", RandomStrategy())  # Random strategy
#team2.add("Player 2", RandomStrategy())   # Random strategy
#
## Create a match
#simu = VolleySimulation(team1, team2)
#
## Simulate and display the match
#volley_show_simu(simu)