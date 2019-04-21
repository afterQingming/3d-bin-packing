from shortcuts import pack_products_into_restrictions

day = 200

CargoBay = {
  'type1' : {
    'depth': 8,
    'width': 10,
    'height': 14,
  },
  'type2' : {
    'depth': 24,
    'width': 20,
    'height': 20,
  } 
} 

# 2 * E + 1*F + ?B
Drone = {
  'B': {
    'dim':{
        'depth': 30,
        'width': 30,
        'height': 22,
    },
    'cargobay': CargoBay['type1'],
    'quantity':3
  },
  'E': {
    'dim':{
        'depth': 25,
        'width': 20,
        'height': 27,
    },
    'cargobay': CargoBay['type2'],
    'quantity':2
  },
  'F': {
    'dim':{
        'depth': 40,
        'width': 40,
        'height': 25,
    },
    'cargobay': CargoBay['type2'],
    'quantity':1
  }
}
boxes = [{
  'depth': 14,
  'width': 7,
  'height': 5,
  'quantity': 7*day
}, {
  'depth': 5,
  'width': 8,
  'height': 5,
  'quantity': 2*day
},{
  'depth': 12,
  'width': 7,
  'height': 4,
  'quantity': 4 * day
},{
  'depth': 5,
  'width': 8,
  'height': 5,
  'quantity': 2*day
},{
  'depth': Drone['B']['dim']['depth'],
  'width': Drone['B']['dim']['depth'],
  'height': Drone['B']['dim']['depth'],
  'quantity': Drone['B']['quantity']
},{
  'depth': Drone['E']['dim']['depth'],
  'width': Drone['E']['dim']['depth'],
  'height': Drone['E']['dim']['depth'],
  'quantity': Drone['E']['quantity']
},{
  'depth': Drone['F']['dim']['depth'],
  'width': Drone['F']['dim']['depth'],
  'height': Drone['F']['dim']['depth'],
  'quantity': Drone['F']['quantity']
}

]

conataner_max_sizes = {
  'width': 92,
  'depth': 231,
  'height': 94
}

pack_products_into_restrictions(
    boxes,
    conataner_max_sizes,
    500,
    1,
    2
)