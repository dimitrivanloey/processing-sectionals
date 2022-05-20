line_list = []
ordered_list = []

meetings_list = [
  {
    'name': 'GOO', 
    'operator': 'MAX', 
    'type': 'flat', 
    'races': 
      {
        '13.10': 12, 
        '13.45': 12, 
        '14.15': 9, 
        '14.50': 9, 
        '15.25': 6, 
        '16.00': 10, 
        '16.35': 12, 
        }
      
    },
    {
    'name': 'HAY', 
    'operator': 'Simon', 
    'type': 'flat', 
    'races': 
      {
        '13.25': 11, 
        '14.00': 12, 
        '14.35': 10, 
        '15.10': 11, 
        '15.45': 12, 
        '16.20': 16, 
        '16.55': 13, 
        }
      
    },
    {
    'name': 'MUS', 
    'operator': 'Fraser', 
    'type': 'flat', 
    'races': 
      {
        '13.53': 7, 
        '14.28': 8, 
        '15.03': 7, 
        '15.38': 9, 
        '16.13': 9, 
        '16.48': 12, 
        '17.23': 9, 
        }
      
    },
    {
    'name': 'STR', 
    'operator': 'Neil', 
    'type': 'jumps', 
    'races': 
      {
        '17.30': 5, 
        '18.00': 7, 
        '18.30': 4, 
        '19.00': 6, 
        '19.30': 8, 
        '20.00': 7, 
        '20.30': 9, 
        },
    },
    {
    'name': 'YORK', 
    'operator': 'Pete', 
    'type': 'flat', 
    'races': 
      {
        '13.40': 13, 
        '14.20': 20, 
        '14.55': 14, 
        '15.30': 6, 
        '16.07': 11, 
        '16.42': 10, 
        '17.15': 20, 
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
    
  



