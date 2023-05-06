import os
import json

def main():
    origin = 'Simulations'
    simulation_dict = {}
    for root, dirs, files in os.walk(origin):
        for dir in dirs:
            path = os.path.join(root,dir)
            split_1 = path.split('\\')
            split_2 = split_1[1].split('-')
            index = split_2[0]

            simulation_dict[index] = {'FormFactor': None, 'TotalDensity': None, 'apl': None, 'thickness': None}

            for file in os.listdir(path):
                data = open(os.path.join(path,file))
                simulation_dict[index][file.split('.')[0]] = json.load(data)
                data.close()
            
    simulations_json = open('simulations.json', 'w')
    json.dump(simulation_dict,simulations_json, indent=2)
    simulations_json.close()
     
if __name__ == "__main__":
    main()