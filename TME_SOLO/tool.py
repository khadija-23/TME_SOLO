class tool(object):
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
    def x_pres_filet(self):
        if(self.id_team==1):
            return Vector2D((settings.GAME_HEIGHT/2)-1,settings.GAME_HEIGHT)
        else:
            return Vector2D(settings.GAME_WIDTH,settings.GAME_HEIGHT/2)
