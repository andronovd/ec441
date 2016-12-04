p = [ 0.2, 0.4 ];
a = [ 0.3, 1.0, 3.0];

for x in p:
    for y in a:
        print( x, y, (1 - x)/(1 + 2*y ) );
