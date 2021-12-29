############################################################################################################################
#
# CSE 231
# Project 08
#
#   Algorithm
#       
#       def open_file():
#        prompt for a file_name
#        while loop to repeatedly prompt for a file_name:
#           use try-except method to prevent the program from running errors
#           try :
#               break from the loop if a file is successfully opened
#           except:
#               print Invalid filename  and prompt for a file name
#               go back to the while loop to start from the beginning
#              
#        return file_pointer
#
#       def read_file(fp):
#           for loop through the file
#               use try except method to covert the electricity,fertility,gdp,life expectancy into float
#           create list for every region         
#           for loop through the dictionary:          
#               for each region append all the values to that specific list based on region
#               append all that values to a dictionary with key as the region
#   
#       def get_min_max(D,region,option):
#           if region not in D:
#               return min_tup,max_tup = None
#           elif option > 4 or option < 1:
#               return min_tup, max_tup = None
#           else:
#               initialize min_tup, max_tup = ()
#               create 2 list = list_reglist_tup
#               for loop through the dictionary:
#                   if key == region, 
#                       append the values to the list_reg
#               for loop through the list_reg:
#                   if - elif statements based on the option:
#                       append specific values using index based on the option
#               sort the list based on the data such as gdp,electricity,fertility rate or life expectancy
#               assign the first value of the list to min_tuple
#               assign the last value of the list to max_tuple
#               return min_tuple , max_tuple
#
#       def display_all_countries(master_dict,region):
#           print the formats directed by the project
#           create count_list
#           for loop through the keys and val of master_dict:
#               if key == region:
#                   append the values to count_lis
#           sort the count_lis based on alphabetic order
#           for loop through the count_lis:
#               print the elements of the list based on the format directed by the project
#
#       def get_top10(D):
#           create a list = top_gdp
#           for loop through the keys,val of the D:
#               append 1st and the 3rd value to top_gdp
#           sort the list using lambda key
#           create a list = top_ten, count = 0
#           for loop through the top_gdp:
#               if count is less than 10:
#                   append the elements to top_ten
#               if count  > 10:
#                   break
#           return top_ten
#
#       def main():
#           call open_file() and read_file
#           prompts the user to enter a region
#           while loop till the user enters q:
#               while loop till the user enters valid region
#        
#                   call display_option to print all options
#               while loop till the user enter valid option
#                   if user enters q, break the loop
#                   while loop if user enters a number that is not an option:
#                       if user enters q, break the loop
#                       print ("Invalid")
#                   if-else statements based on user input(option 1,2,3,4,5,6)
#                       call get min_max for option 1,2,3,4 
#                       print the results based on the format directed by the project
#                   if option 5 
#                       call display function to display all the data of that region
#                   if option 6
#                       call get_top10 function 
#                       print the data based on the format directed by the project
#               prompt for user to enter an option
#            break the loop if user enters q or continue
#
#
##############################################################################################################################


import csv
from operator import itemgetter
# do NOT import sys

REGION_LIST = ['East Asia & Pacific',
                'Europe & Central Asia',
                'Latin America & Caribbean',
                'Middle East & North Africa',
                'North America',
                'South Asia',
                'Sub-Saharan Africa']

PROMPT = "\nSpecify a region from this list or 'q' to quit -- \nEast Asia & Pacific,Europe & Central Asia,Latin America & Caribbean,Middle East & North Africa,North America,South Asia,Sub-Saharan Africa: "

def open_file():
    """
    

    Returns
    -------
    filepointer : cvs file
        prompts for a file
        while loop till right file is found
            try except method to keep asking for a valid file.

    """
    
    
    
    
    file_name = input("Input a file: ")
    check = True
    
    while check == True:
        try:
            filepointer = open(file_name)
            break
        except FileNotFoundError:
            print("Invalid filename, please try again.")
            file_name = input("Input a file: ")
            continue
    
    return filepointer
    
    
    

def read_file(fp):
    
    """
    

    Parameters
    ----------
    fp : cvs file
        file with all the data.

    Returns
    -------
    Dictionary with regions as key and values as list of country,electricity %, fertility rate, gdp,life expectancy.

    """
     

    reader = csv.reader(fp) 
    next(reader,None)
    D = {}
    l = []
    n = []
    s = []
    sh = []
    e_ca = []
    me = []
    ea_p = []
     
     
    
    for col in reader:
        
        
       
        try:                        # convert to float and make a list

            region = col[6].strip()
            country = col[0].strip()
            elec = float(col[2])
            fert = float(col[3])
            gdp = float(col[4])
            life = float(col[5])
            
            L = [country,elec,fert,gdp,life]
            
            
        except ValueError:          # skip the line if error
            
            continue
          
      
        if region == "Latin America & Caribbean":
           
            l.append(L)
            D[region] = l 
      
      
           
        elif region == "North America":
            n.append(L)
            D[region] = n
       
           
       
        elif region == "South Asia":
           
            s.append(L)
            D[region] = s
           
        elif region == "Sub-Saharan Africa":
   
            sh.append(L)
            D[region] = sh
           
        elif region == "Europe & Central Asia":
           
            e_ca.append(L)
            D[region] = e_ca
           
        elif region == "Middle East & North Africa":
   
            me.append(L)
            D[region] = me
           
        elif region == "East Asia & Pacific":
   
            ea_p.append(L)
            D[region] = ea_p
                

      
    return D
     

     
     

def get_min_max(D, region, option):
    
    """
    

    Parameters
    ----------
    D : master_dictionary
        dictionary with regions as keys and values as list of country,electricity %, fertility rate, gdp,life expectancy.
    region : region prompt from the user 
        find this region in dictionary to extract the data.
    option : option the user enters
        states whether the user wants min and max of electricity %, fertility rate, gdp,life expectancy .

    Returns
    -------
    min_tup : tuple
        tuple that has country name and data of the minimum rate among all the countries in that region .
    max_tup : tuple
        tuple that has country name and data of the maximum rate among all the countries in that region ..

    """
     
     
    option = int(option)
    
    if region not in D:
        min_tup = None
        max_tup = None
        return min_tup, max_tup
        
    
    elif option > 4 or option < 1:
        min_tup = None
        max_tup = None
        return min_tup, max_tup
    else:
        
        
        min_tup = ()
        max_tup = ()
        
        list_reg = []
        list_tup = []
        
        
        for key in D.keys():
            
            if key == region:
                
                list_reg.append(D[key]) # Append the values of the key
                
        
        for i in list_reg:
            
            for j in i:
                
                if option == 1:
                    list_tup.append((j[0],j[1])) # For option 1 append index 0 and 1
                
                elif option == 2:
                    list_tup.append((j[0],j[2])) # For option 2 append index 0 and 2
                
                elif option == 3:
                    list_tup.append((j[0],j[3])) # For option 3 append index 0 and 3
                    
                elif option == 4:
                    list_tup.append((j[0],j[4])) # For option 4  append index 0 and 4
                
                    
                
        org_list = sorted(list_tup, key = itemgetter(1))
        
        
        min_tup = org_list[0]
        max_tup = org_list[-1]
        
        
        return min_tup, max_tup
        
    

    
def display_all_countries(D,region):
    """
    

    Parameters
    ----------
    D : master_dictionary
        dictionary with regions as keys and values as list of country,electricity %, fertility rate, gdp,life expectancy.
    region : region entered by the user
        extracts data from that regions and prints all that data.

    Returns
    -------
    None.

    """
     
     
    print("\nDisplaying {} Region:\n".format(region))
    
    print("{:32s}{:>20s}{:>20s}{:>17s}{:>18s}".format("Country","Electricity Access","Fertility rate","GDP per capita","Life expectancy"))
    
    count_lis = []
    
    for reg,val in D.items():
        
        
        
        if reg == region:
            
            for i in val:
                
                count_lis.append((i[0],i[1],i[2],i[3],i[4]))
               
         
    count_lis = sorted(count_lis, key = lambda x: x[0])         # sorts the list based on index[0]
    
    for i in count_lis:
        print("{:32s}{:>20.2f}{:>20.2f}{:>17.2f}{:>18.2f}".format(i[0],i[1],i[2],i[3],i[4]))

    
def get_top10(D):
    """
    

    Parameters
    ----------
    D : master_dictionary
        dictionary with regions as keys and values as list of country,electricity %, fertility rate, gdp,life expectancy.

    Returns
    -------
    top_ten : list of tuples
        sorts the top_gdp which has top 10 countries with most gdp per capita.

    """
     
     
    
    top_gdp = []
    
    for key,val in D.items():
        
        count = 0
        for i in val:
            
            top_gdp.append((i[0],i[3]))
            
            
            
     
    top_gdp = sorted(top_gdp,key = lambda x: x[1], reverse = True) # sorts the list based on index[1] and reverses the list so it is in decreasing order
    
    top_ten = []
    
    count = 0
    for i in top_gdp:
        
        if count < 10:                  # if count less than 10 append to top_ten
            
           top_ten.append(i)
       
        count += 1
               
    return top_ten
        
    
     
     
     
        
def display_options():
    """
    DO NOT CHANGE
    Display menu of options for program
    """
    OPTIONS = """\nMenu
    1: Minimum and Maximum Countries Access to Electricity
    2: Minimum and Maximum Countries Fertility Rate
    3: Minimum and Maximum Countries GDP per Capita
    4: Minimum and Maximum Countries Life Expectancy
    5: List of countries in a region
    6: Top 10 Countries in the world by GDP per Capita\n"""
    print(OPTIONS)


def main():
    """
    call open_file() and read_file
    prompts the user to enter a region
    while loop till the user enters q:
        while loop till the user enters valid region
        
        call display_option to print all options
        while loop till the user enter valid option
            if user enters q, break the loop
            while loop if user enters a number that is not an option:
                if user enters q, break the loop
                print ("Invalid")
            if-else statements based on user input(option 1,2,3,4,5,6)
                call get min_max for option 1,2,3,4 
                print the results based on the format directed by the project
                option 5 
                    call display function to display all the data of that region
                option 6
                    call get_top10 function 
                    print the data based on the format directed by the project
            prompt for user to enter an option
        break the loop if user enters q or continue
                

    Returns
    -------
    None.

    """
     
    
    fp = open_file()
    D = read_file(fp)
    
    
    region = input(PROMPT)
    option_list = ["q","Q","r","R"]
    
    while region != "q" and region != "Q":
        
         while region not in REGION_LIST and region != "q" and region != "Q":
            
            
             region = input(PROMPT)
            
         print("\nRegion: ", region)
         display_options()
         
         option = input('\n\nChoose an option, R to select a different region, q to quit: ')
         
         
         
         while option not in option_list:
             
             option = int(option)
             
             while  option > 6 or option <1:
                 
                 if option in option_list:
                     
                     break
                     
                 print("Invalid option. Please try again.")
                 option = input('\n\nChoose an option, R to select a different region, q to quit: ')
                 if option.isdigit():
                     option = int(option)
                 else:
                     break
                 
                 
            
               
             if option == "q" or option == "Q":
                 
                 break
             
             if option == "R" or option == "r":
                 
                 break
                 
                 
             option = int(option) 
             
             if option == 1:
                 
                
                 min_tup,max_tup = get_min_max(D, region, option)
                 print("\n{:s} has the highest access to electricity of {:.2f}%".format(max_tup[0],max_tup[1]))
                 print("{:s} has the lowest access to electricity of {:.2f}%".format(min_tup[0],min_tup[1]))
                
                 
             if option == 2:
                 
                 
                 min_tup,max_tup = get_min_max(D, region, option)
                 
                 print("\n{:s} has the highest fertility rate of {:.2f} births per woman".format(max_tup[0],max_tup[1]))
                 print("{:s} has the lowest fertility rate of {:.2f} births per woman".format(min_tup[0],min_tup[1]))
                
             
             if option == 3:
                 
                
                 min_tup,max_tup = get_min_max(D, region, option)
                 print("\n{:s} has the highest GDP per capita at ${:.2f}".format(max_tup[0],max_tup[1]))
                 print("{:s} has the lowest GDP per capita at ${:.2f}".format(min_tup[0],min_tup[1]))
                 
                 
             if option == 4:

                 
                 min_tup,max_tup = get_min_max(D, region, option)
                 print("\n{:s} has the highest life expectancy of {:.2f} years".format(max_tup[0],max_tup[1]))
                 print("{:s} has the lowest life expectancy of {:.2f} years".format(min_tup[0],min_tup[1]))
                
             
             if option == 5:
                 
                 display_all_countries(D, region)
                 
                 
             if option == 6:
                 
                 print("\nTop 10 Countries by GDP")
                 print("\n{:32s}{:>18s}".format('Country', 'GDP per capita'))
                 lis_gdp = get_top10(D)
                 
                 for i in lis_gdp:
                     
                     print("{:32s}{:>18.2f}".format(i[0],i[1]))
                
             option = input('\n\nChoose an option, R to select a different region, q to quit: ')
             
         
         if option == "q" or option == "Q":
             break
         if option == "R" or option == "r":
             region = input(PROMPT)
             



if __name__ == '__main__':
    main()
    
