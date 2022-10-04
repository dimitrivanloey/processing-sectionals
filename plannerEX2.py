line_list = []
ordered_list = []

meetings_list = [
  {
    'name': 'NOTT', 
    'operator': 'Pete', 
    'type': 'flat', 
    'races': 
      {
        '13.10': 12, 
        '13.45': 8, 
        '14.20': 6, 
        '14.55': 6, 
        '15.25': 8, 
        '15.55': 4,
        '16.25': 7 
        
        }
      
    },
    {
    'name': 'NEWB', 
    'operator': 'Neil', 
    'type': 'flat', 
    'races': 
      {
        '13.25': 14, 
        '14.00': 13, 
        '14.35': 8, 
        '15.10': 12, 
        '15.40': 6, 
        '16.10': 6, 
        '16.40': 5, 
        }
      
    },{
    'name': 'CORK', 
    'operator': 'Elaine', 
    'type': 'flat', 
    'races': 
      {
        '17.00': 9, 
        '17.30': 14, 
        '18.00': 8, 
        '18.30': 7, 
        '19.05': 16, 
        '19.40': 8, 
        '20.15': 15, 
        }
      
    },{
    'name': 'NEWM', 
    'operator': 'Simon', 
    'type': 'flat', 
    'races': 
      {
        '17.10': 6, 
        '17.45': 8, 
        '18.15': 9, 
        '18.48': 9, 
        '19.23': 8, 
        '19.58': 11, 
        
        }
      
    },{
    'name': 'THIRSK', 
    'operator': 'Fraser', 
    'type': 'flat', 
    'races': 
      {
        '17.37': 12, 
        '18.07': 8, 
        '18.40': 7, 
        '19.15': 11, 
        '19.50': 13, 
        '20.25': 7, 
      
        }
      
    }
  ]

num_meetings = len(meetings_list)
num_races = 0
num_runners = 0

for meeting in meetings_list:
  name = meeting['name']
  type = meeting['type']
  operator = meeting['operator']
  runners = sum(race for race in meeting['races'].values())
  races = len(meeting['races'])
  print(f"{name} - {type} - {runners} runners in {races} races - {operator}")


for meeting in meetings_list:
  # print(meeting) # meetings dict
  # print(meeting['races']) # races dict
  # print([keys for keys in meeting['races']]) # keys in races dict
  # print([v for v in meeting['races'].values() ]) # values in races dict

  num_runners += sum([v for v in meeting['races'].values() ])
  num_races += len([keys for keys in meeting['races']])
  
print(f"{num_meetings} meetings - {num_races} races - {num_runners} runners")
print('')

line_list = []
for meeting in meetings_list:
    teller = 1
    # print(meeting['races'])
    for race in meeting['races']:
      num_runners = meeting['races'][race]
      type = meeting['type']
      operator = meeting['operator']
      extra = ''
      if type == 'flat':
        extra = 'U/O: '
      elif type == 'jumps':
        extra = 'Manual start'
      line1 = f"{race} {meeting['name']} R{teller} - {num_runners} runners - {type} - {operator} - {extra}\n"
      teller += 1
      num_line = ''
      for num in range(1, int(num_runners) + 1):
          num_line += str(num) + 'p     '
      num_line2 = f'\n'
      for num in range(1, int(num_runners) + 1):
            num_line2 += str(num) + 's     '

      line_list.append(line1 + num_line + num_line2)
      

for line in sorted(line_list):
    print(f"{line}")
    print('')
    
  



