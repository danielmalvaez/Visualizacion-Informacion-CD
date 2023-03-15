% Un gráfico de malla es una superficie 3D que crea diferentes 
% tipos de mallas para diferentes tipos de expresión. 
% Para crear una malla tenemos que dar los valores x,y para z, 
% z= f(x, y). Para trazar el gráfico de malla, tiene "mesh()"
% que generará la superficie 3D. 
% Tiene color de borde sólido pero no color de cara.

% Valores de "x" y "y".
[x,y]= meshgrid(0:0.1:5);

% Función z=f(x,y)
z= sin(x).*cos(y);

% mesh() se usa para la gráfica 3D
mesh(z);
