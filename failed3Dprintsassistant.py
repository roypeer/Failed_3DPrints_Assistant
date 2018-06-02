########### FAILED 3D PRINTS RESCUER ########### 
# Tool to fix gcode
# Written by Roy Pe'er, 2018





open_screen = '''

  ______    _ _          _   ____  _____    _____      _       _                          _ _              _   
 |  ____|  (_) |        | | |___ \|  __ \  |  __ \    (_)     | |           /\           (_) |            | |  
 | |__ __ _ _| | ___  __| |   __) | |  | | | |__) | __ _ _ __ | |_ ___     /  \   ___ ___ _| |_ __ _ _ __ | |_ 
 |  __/ _` | | |/ _ \/ _` |  |__ <| |  | | |  ___/ '__| | '_ \| __/ __|   / /\ \ / __/ __| | __/ _` | '_ \| __|
 | | | (_| | | |  __/ (_| |  ___) | |__| | | |   | |  | | | | | |_\__ \  / ____ \\__ \__ \ | || (_| | | | | |_ 
 |_|  \__,_|_|_|\___|\__,_| |____/|_____/  |_|   |_|  |_|_| |_|\__|___/ /_/    \_\___/___/_|\__\__,_|_| |_|\__|
                                                                                                               
 ##############################################################################################################                                                                                                              
                                                                                                          
'''

print(open_screen)



gcode_loc = input("Enter location of original GCODE (save as txt file ! e.g. C:\car.txt): ")
gcode = open(str(gcode_loc),'r')
gcode = gcode.readlines()

approx_z = float(input("Enter approximated Z value where print stopped (e.g. 24.7): "))
z_vals_location = []
for i in range(len(gcode)):
    if(('Z' + str(int(approx_z-1))) in gcode[i]):
            z_val = gcode[i][gcode[i].find('Z'):]
            z_val = z_val[:z_val.find(' ')]
            z_vals_location.append((z_val,i)) # Location and Z values.
    if(('Z' + str(int(approx_z))) in gcode[i]):
            z_val = gcode[i][gcode[i].find('Z'):]
            z_val = z_val[:z_val.find(' ')]
            z_vals_location.append((z_val,i)) # Location and Z values.
    if(('Z' + str(int(approx_z+1))) in gcode[i]):
            z_val = gcode[i][gcode[i].find('Z'):]
            z_val = z_val[:z_val.find(' ')]
            z_vals_location.append((z_val,i)) # Location and Z values.



print("\nHere are some possible initial Z values to restart the print with: ")
for i in range(len(z_vals_location)):
    print( str(i + 1) +  '. ' + str(z_vals_location[i][0]))

choice = input('Enter the number of initial Z value you would like to use: ')

z_val_andloc = z_vals_location[int(choice) - 1]


def new_gcode(current_gcode,loc,newfilename):
    current_gcode = current_gcode[loc:]
    newcode = open(newfilename + '.txt','w')
    newcode.writelines(current_gcode)
    newcode.close()


filename = input("How would you like the new gcode file to be named (e.g. carfixed) ? ")
new_gcode(gcode,z_val_andloc[1],filename)
print('Saved new gcode starting from z height ' + z_val_andloc[0] + ' as a txt file called ' + filename + '.txt')
print('Warm up your printer, make sure it is aware of its location (Home all axis if needed), copy the new gcode to the host software and continue the print ')
print('Good Luck !')





