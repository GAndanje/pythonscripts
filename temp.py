# -*- coding: utf-8 -*-
# this script creates a file, writes to it via user input and loads the file by reading off it
class Robot:
    def __init__(self, instruction_file):
        self.instruction_file = instruction_file
        self.instruction_list = None
        self.empty_list = list()
        
    def write_to_file(self):
        file = open(self.instruction_file, 'w')
        while True:
            movement_x = input('Enter x movement or \'q\' to quit: ')
            if movement_x == 'q':
                break
            else:
                file.write(movement_x + '\n')
            movement_y = input('Enter y movement or \'q\' to quit: ')
            if movement_y == 'q':
                break
            else:
                file.write(movement_y + '\n')
        file.close()
    def read_from_file(self):
        try:
            fr = open(self.instruction_file, 'r')
        except FileNotFoundError as error:
            print(error)
        else:
            self.instruction_list = fr.readlines()
            fr.close()
        return(self.instruction_list)
    def get_location(self):
        position_x, position_y = 0, 0
        distance_x, distance_y = 0, 0
        self.read_from_file()
        if self.instruction_list != None:
            for values in self.instruction_list:
                temp = values[:-1]
                data = int(temp)
                
                if self.instruction_list.index(values) % 2 == 0:
                    position_x += data
                    distance_x += abs(data)
                else:
                    position_y += data
                    distance_y += abs(data)
                self.empty_list.append(data)
            print(f'The x position for the Robot is {position_x}')
            print(f'The y position for the Robot is {position_y}')
            print(f'The x distance covered is {distance_x}')
            print(f'The y distance covered is {distance_y}')
            print(self.empty_list)
              
    #def 
        #file.close()
my_robot_object = Robot('robot_instruction_file.txt')
#Robot.write_to_file(my_robot_object)
#print(Robot.read_from_file(my_robot_object))
#Robot.get_location(my_robot_object)
my_robot_object.write_to_file()
#my_robot_object.read_from_file()
my_robot_object.get_location()



                
            
            
