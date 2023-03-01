line_list = []
ordered_list = []

meetings_list = [
  {
    'name': 'NAAS', 
    'operator': 'Elaine', 
    'type': 'jumps', 
    'races': 
      {
        '11.50': 25, 
        '12.20': 23, 
        '12.55': 5, 
        '13.30': 19, 
        '14.05': 5, 
        '14.40': 12,
        '15.15': 15,
        '15.50': 11,
        }
      
    },
    {
    'name': 'WET', 
    'operator': 'Pete', 
    'type': 'jumps', 
    'races': 
      {
        '12.08': 15, 
        '12.43': 5, 
        '13.18': 12, 
        '13.53': 10, 
        '14.28': 5, 
        '15.03': 9, 
        '15.38': 8, 
        }
      
    },{
    'name': 'CHE', 
    'operator': 'Neil', 
    'type': 'jumps', 
    'races': 
      {
        '12.35': 10, 
        '13.10': 14, 
        '13.45': 6, 
        '14.20': 15, 
        '14.55': 13, 
        '15.30': 12, 
        '16.05': 17,
       
        }
      
    },
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
    
  



