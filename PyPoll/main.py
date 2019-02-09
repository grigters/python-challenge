#import libraries
import os
import csv

#create variables for the candidates after finding unique candidates (see unique_list)
khan = 0
correy = 0
li = 0
otooley = 0

#-1 for num so header is not counted
num = -1
unique_list = [] 

csvpath = os.path.join('Resources', 'election_data.csv')

with open(csvpath, newline='') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    for row in csvreader:
        #get total votes
        num += 1
        if row[2] not in unique_list: 
            unique_list.append(row[2])
        
        #after locating unique candidates, count their votes
        if row[2] == 'Khan':
            khan += 1
        elif row[2] == 'Correy':
            correy += 1
        elif row[2] == 'Li':
            li += 1
        elif row[2] == "O'Tooley":
            otooley += 1
  
#------------------- 
file = 'output.txt'

with open(file, 'w') as text:

    print('Election Results')
    print('------------------------')
    print(f'Total Votes: {num}')
    print('------------------------')
    text.write('Election Results\n')
    text.write('------------------------\n')
    text.write(f'Total Votes: {num}\n')
    text.write('------------------------\n')
    
    #calculate the percentage of votes by candidate
    khan_pct = round(((khan/num)*100),3)
    correy_pct = round(((correy/num)*100),3)
    li_pct = round(((li/num)*100),3)
    otooley_pct = round(((otooley/num)*100),3)

    #remove index 0 which contains the headet
    unique_list.pop(0)

    #create a dictionary to making printing out the results easier
    kha_dict = {'name': unique_list[0],'percent': khan_pct, 'votes': khan}
    cor_dict = {'name': unique_list[1],'percent': correy_pct, 'votes': correy}
    li_dict = {'name': unique_list[2],'percent': li_pct, 'votes': li}
    oto_dict = {'name': unique_list[3],'percent': otooley_pct, 'votes': otooley}

    #print and write to terminal and text file
    print(f"{kha_dict['name']}: {kha_dict['percent']}% ({kha_dict['votes']})")
    print(f"{cor_dict['name']}: {cor_dict['percent']}% ({cor_dict['votes']})")
    print(f"{li_dict['name']}: {li_dict['percent']}% ({li_dict['votes']})")
    print(f"{oto_dict['name']}: {oto_dict['percent']}% ({oto_dict['votes']})")
    text.write(f"{kha_dict['name']}: {kha_dict['percent']}% ({kha_dict['votes']})\n")
    text.write(f"{cor_dict['name']}: {cor_dict['percent']}% ({cor_dict['votes']})\n")
    text.write(f"{li_dict['name']}: {li_dict['percent']}% ({li_dict['votes']})\n")
    text.write(f"{oto_dict['name']}: {oto_dict['percent']}% ({oto_dict['votes']})\n")

    #create list to find winner
    winner = [khan, correy, li, otooley]

    print('------------------------')
    text.write('------------------------\n')

    #if statement to find the winner by popular vote
    if max(winner) == kha_dict['votes']:
        print('Winner: Khan')
        text.write('Winner: Khan\n')
    elif max(winner) == cor_dict['votes']:
        print('Winner: Correy')
        text.write('Winner: Correy\n')
    elif max(winner) == li_dict['votes']:
        print('Winner: Li')
        text.write('Winner: Li\n')
    else:
        print("Winner: O'Tooley")
        text.write("Winner: O'Tooley\n")
    
    print('------------------------')
    text.write('------------------------\n')