def build_pyramid(height:int) -> None:
  """Print een piramide van de gegeven hoogte

  Args:
      height (int): de hoogte van de piramide
      
  >>> build_pyramid(3)
    ##
   ###
  ####
  >>> build_pyramid(2)
   ##
  ###
  >>> build_pyramid(0)
  >>> build_pyramid(23)
                        ##
                       ###
                      ####
                     #####
                    ######
                   #######
                  ########
                 #########
                ##########
               ###########
              ############
             #############
            ##############
           ###############
          ################
         #################
        ##################
       ###################
      ####################
     #####################
    ######################
   #######################
  ########################
  """
  for i in range(height):
    print(('#'*(i+2)).rjust(height+1))


if __name__ == '__main__':
  u_height = int(input('Hoe hoog moet de piramide zijn? (> 0 en <= 23)'))
  while u_height < 0 or u_height > 23:
    u_height = int(input('Hoe hoog moet de piramide zijn? (> 0 en <= 23)'))
    
  build_pyramid(height=u_height)