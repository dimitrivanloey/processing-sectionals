line_list = []
ordered_list = []

meetings_list = [
  {
    'name': 'KMP', 
    'operator': 'Pete', 
    'type': 'flat', 
    'races': 
      {
        '13.00': 5, 
        '13.30': 10, 
        '14.00': 5, 
        '14.30': 1, 
        '15.00': 4, 
        '15.30': 10, 
        '16.00': 5, 
        '16.30': 10
        }
      
    },
    {
    'name': 'WIN', 
    'operator': 'Max', 
    'type': 'jumps', 
    'races': 
      {
        '13.15': 7, 
        '13.45': 10, 
        '14.15': 5, 
        '14.45': 12, 
        '15.15': 7, 
        '15.45': 9, 
        '16.15': 12, 
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

line_list = []
for meeting in meetings_list:
    teller = 1
    # print(meeting['races'])
    for race in meeting['races']:
      num_runners = meeting['races'][race]
      type = meeting['type']
      operator = meeting['operator']
      # print(f"{race} {meeting['name']} R{teller} - {num_runners} runners - {type} - {operator}")
      line1 = f"{race} {meeting['name']} R{teller} - {num_runners} runners - {type} - {operator}"
      teller += 1
      line_list.append(line1)

for line in sorted(line_list):
    print(f"{line}")
    print('')
    
  



