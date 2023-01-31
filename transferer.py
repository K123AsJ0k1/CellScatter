import os
import shutil

def main():
    origin = '..\Databank\Data\Simulations'
    target = 'Simulations'
    os.mkdir(target)
    copyable_files = []
    
    for root, dirs, files in os.walk(origin):
        for name in files:
            if 'FormFactor.json' in name:
                copyable_files.append(os.path.join(root,name))
            if 'apl.json' in name:
                copyable_files.append(os.path.join(root,name))
            if 'TotalDensity.json' in name:
                copyable_files.append(os.path.join(root,name))
            if 'thickness.json' in name:
                copyable_files.append(os.path.join(root,name))
    
    folder_index = 1
    index = 0
    folder_names = []
    previous = ''
    for file in copyable_files:
        split = file.split('\\')
        
        if not previous in split[7]:
            folder_index = folder_index + 1
        
        folder_name = str(folder_index) + '-' + split[4] + '-' + split[5] + '-' + split[6] + '-' + split[7]
        
        if not folder_name in folder_names:
            folder_names.append(folder_name)

        previous = split[7]
        index = index + 1
    
    folder_index = 0
    file_target = target + '\\' + folder_names[folder_index]
    os.mkdir(file_target)
    previous = ''
    for file in copyable_files:
        split = file.split('\\')
        
        if not previous in split[7]:
            folder_index = folder_index + 1
            file_target = target + '\\' + folder_names[folder_index]
            os.mkdir(file_target)

        shutil.copy2(file,file_target)
        previous = split[7]
    
if __name__ == "__main__":
    main()