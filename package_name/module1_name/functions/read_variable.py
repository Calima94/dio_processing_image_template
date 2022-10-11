import sys
import os


def resource_path(relative_path):
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

def transform_data(dataframe,attribute,np,pd):
    variable = dataframe.loc[attribute]
    variable = variable.dropna()
    variable = variable.to_numpy()
    try:
        for i in range(len(variable)):
            variable[i] = float(variable[i])
        if len(variable) == 1:
            variable = float(variable)
    except:
        if len(variable) == 1:
            variable = np.array2string(variable)
    
    return variable  


class Transform_variables:
    def __init__(self,np,pd):
        config_path = resource_path('config.csv')
        df = pd.read_csv(config_path,index_col ="Name_variables")
        self.screen_scale_x = transform_data(df,'screen_scale_x',np,pd)
        self.screen_scale_y = transform_data(df,'screen_scale_y',np,pd)
        self.screen_res = transform_data(df,'screen_res',np,pd)
        self.auto_mode = transform_data(df,'auto_mode',np,pd)
        

def main(np,pd):
        
    parameters_game = Transform_variables(np,pd)
    return parameters_game  
    
    
if __name__ == "__main__":
    main()
    
