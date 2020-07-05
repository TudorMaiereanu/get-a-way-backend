import pandas as pd

def weights(p_weather=0, p_corona=0, p_cost=0, p_CO2=0, p_time=0, p_act_hike=0, p_act_surf=0):
    
    # Base Weights
    # weather, corona, cost, act_hike, act_surf, act_both, CO2, Time
    base = pd.DataFrame([0.228, 0.251, 0.228, 0, 0, 0, 0.065, 0.228])
    
    # Logic:
    # If no activity (na) chosen, then base weights = 25% and preferences = 75%
    na_base_per = 0.25
    na_pref_per = 0.75
    
    # If activity (a) is chosen, then base weights = 12.5%, preferenecs = 37.5% and activity = 50%
    a_base_per = 0.125
    a_pref_per = 0.375
    a_per = 0.5
    
    # Handle case: all 0: weather, corona, cost, CO2, Time
    if p_weather == 0 and p_corona == 0 and p_cost == 0 and p_CO2 == 0 and p_time == 0:
        if (p_act_hike == 0) and (p_act_surf == 0):
            weights = base
        else: 
            a_base_per = 0.5
            # set weights of activity features
            w_act_both = 0
            w_act_hike = 0
            w_act_surf = 0

            if (p_act_hike == 1) and (p_act_surf == 1):
                w_act_both = a_per
            elif p_act_hike == 1:
                w_act_hike = a_per
            elif p_act_surf == 1:
                w_act_surf = a_per
            
            # adjust weights vector
            weights = base*a_base_per
            weights.at[3, 0] += w_act_hike
            weights.at[4, 0] += w_act_surf
            weights.at[5, 0] += w_act_both
    else:

        # if no prefernce is 2 change weights
        if p_weather < 2 and p_corona < 2 and p_cost < 2 and p_CO2 < 2 and p_time < 2:
            na_base_per = 0.5
            na_pref_per = 0.5
            a_base_per = 0.25
            a_pref_per = 0.25


        if (p_act_hike == 0) and (p_act_surf == 0):

            # Calulate weights of individual preferences
            # Initially we distribute a total bucket of 1. Each feature can reach a value of up to 0.2.
            if p_weather == 1:
                w_weather = 0.1
            elif p_weather == 2:
                w_weather = 0.2
            else:
                w_weather = 0

            if p_corona == 1:
                w_corona = 0.1
            elif p_corona == 2:
                w_corona = 0.2
            else:
                w_corona = 0

            if p_cost == 1:
                w_cost = 0.1
            elif p_cost == 2:
                w_cost = 0.2
            else:
                w_cost = 0
            
            if p_CO2 == 1:
                w_CO2 = 0.1
            elif p_CO2 == 2:
                w_CO2 = 0.2
            else:
                w_CO2 = 0

            if p_time == 1:
                w_time = 0.1
            elif p_time == 2:
                w_time = 0.2
            else:
                w_time = 0

            # Then these features are normalized and scaled depending on their importance
            weight_sum = w_weather + w_corona + w_cost + w_CO2 + w_time

            w_weather = (w_weather/weight_sum)*na_pref_per
            w_corona = (w_corona/weight_sum)*na_pref_per
            w_cost = (w_cost/weight_sum)*na_pref_per
            w_CO2 = (w_CO2/weight_sum)*na_pref_per
            w_time = (w_time/weight_sum)*na_pref_per

            # Then we add everything together to create the new user weights
            weights = base*na_base_per # Here is the mistake

            # weather, corona, cost, act_hike, act_surf, act_both, CO2, Time
            weights.at[0,0] += w_weather
            weights.at[1,0] += w_corona
            weights.at[2,0] += w_cost
            weights.at[6,0] += w_CO2
            weights.at[7,0] += w_time

        else:
            # set weights of activity features
            w_act_both = 0
            w_act_hike = 0
            w_act_surf = 0

            if (p_act_hike == 1) and (p_act_surf == 1):
                w_act_both = a_per
            elif p_act_hike == 1:
                w_act_hike = a_per
            elif p_act_surf == 1:
                w_act_surf = a_per

            # Calulate weights of individual features (non-activity)
            # Initially we distribute a total bucket of 1. Each feature can reach a value of up to 0.2.
            if p_weather == 1:
                w_weather = 0.1
            elif p_weather == 2:
                w_weather = 0.2
            else:
                w_weather = 0

            if p_corona == 1:
                w_corona = 0.1
            elif p_corona == 2:
                w_corona = 0.2
            else:
                w_corona = 0

            if p_cost == 1:
                w_cost = 0.1
            elif p_cost == 2:
                w_cost = 0.2
            else:
                w_cost = 0

            if p_CO2 == 1:
                w_CO2 = 0.1
            elif p_CO2 == 2:
                w_CO2 = 0.2
            else:
                w_CO2 = 0

            if p_time == 1:
                w_time = 0.1
            elif p_time == 2:
                w_time = 0.2
            else:
                w_time = 0

            # Then these features are normalized and scaled depending on their importance
            weight_sum = w_weather + w_corona + w_cost + w_CO2 + w_time

            w_weather = (w_weather/weight_sum)*a_pref_per
            w_corona = (w_corona/weight_sum)*a_pref_per
            w_cost = (w_cost/weight_sum)*a_pref_per
            w_CO2 = (w_CO2/weight_sum)*a_pref_per
            w_time = (w_time/weight_sum)*a_pref_per

            # Then we add everything together to create the new user weights
            weights = base*a_base_per

            # weather, corona, cost, act_hike, act_surf, act_both, CO2, Time
            weights.at[0,0] += w_weather
            weights.at[1,0] += w_corona
            weights.at[2,0] += w_cost
            weights.at[3,0] += w_act_hike
            weights.at[4,0] += w_act_surf
            weights.at[5,0] += w_act_both
            weights.at[6,0] += w_CO2
            weights.at[7,0] += w_time
        
    return weights

