#tutorialBot
import math



def do_turn(pw):
    if len(pw.my_planets())==0:
        return
    if pw.turn_number()%2 == 0:
        return
    if pw.turn_number()%3 == 0:
        return
    else:
        for pl in pw.my_planets():
            pw.issue_order(pl, closest_not_mine(pw, pl), pl.num_ships()/2)
            continue


    return

def closest_not_mine(pw, p):
    if len(pw.not_my_planets())==0:
        pl = pw.my_planets()[0]
    else:
        pl = pw.not_my_planets()[0]
    for planet in pw.not_my_planets():
        if pw.distance(p,planet) < pw.distance(p,pl):
            pl = planet
    return pl

def get_highest_growth_rate_not_mine(pw, exclude):
    pl = None

    #pw.debug(exclude)
    #pw.debug("----exclude")
    if len(pw.neutral_planets()) >= 1:
        pl = pw.neutral_planets()[0]
    else:
        pl = pw.enemy_planets()[0]
        pw.debug("attacking enemy")
    for planet in pw.not_my_planets():
        if planet.growth_rate() >= pl.growth_rate():
                    pl = planet

    return pl

def find_my_closest_planet(pw, planet):

    if len(pw.my_planets()) >= 1:
        #pw.debug("\n\nlen more than one\n\n")
        x = pw.distance(planet, pw.my_planets()[0])
        #pw.debug(x)
        for pl in pw.my_planets():
            if x <= pw.distance(planet, pl):
                pl2 = pl
        return pl2

def fleets_in_x_turns(x,pw,planet):
    #pw.debug("\n\n\n fleets_in_x_turns------------------ \n\n\n")
    finFleets = planet.num_ships()
    for i in range (1,x):
        finFleets = finFleets + planet.growth_rate()

    return finFleets