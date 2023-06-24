families={'yochana':
            {'pilli':{'chinna pillilu'},
             'dog':{'puppies'}},
    'asha':
        {'teju':{'biryani'},
          'uma':{'rahul'},
          'gayathri':{'manchi pilla'}},
    'anki':
            {'rishi':{'AR'}}
    }
for parent,children in families.items():
    print(f"{parent} has {len(children)} favs(s):")
    print(f"{', and '.join([str(child) for child in[*children]])}")