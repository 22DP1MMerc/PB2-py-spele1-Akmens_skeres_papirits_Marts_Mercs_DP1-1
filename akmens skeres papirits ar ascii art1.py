from ASP_multi_player import spele2
from ASP_single_player import spele1

izvele = input('Ja gribat spēlēt ar datoru, ievadiet 1, ja gribat spēlēt ar citu spēlētāju, ievadiet 2: ')
if izvele=='1':
    spele1()
elif izvele=='2':
    spele2()
else:
    print('Tāds variants nepastāv.')