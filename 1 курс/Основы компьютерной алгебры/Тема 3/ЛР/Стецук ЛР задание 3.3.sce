a=10; b=20; x=a:b; y=sqrt(x)/2;
inttrap(x,y)
h=5e-2; x=a:h:b; y =sqrt(x)/2;
inttrap(x,y)
integrate('sqrt(x)/2','x',10,20)
h=5e-2; x=a:h:b; y =sqrt(x)/2;
integrate('sqrt(x)/2','x',10,20)
h=5;x=10:5:35;
y=sqrt(x)/2
y1=diff(y)
y2=diff(y,2)
y3=diff(y,3)
function f=my(x), f=sqrt(x)/2, endfunction;
numdiff(my,1)
