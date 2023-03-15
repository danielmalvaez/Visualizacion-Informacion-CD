% Gráfica de superficie (con sombreado): 

% Es la gráfica de superficie que crea una gráfica de superficie tridimensional 
% que tiene colores sólidos de borde y colores sólidos de cara y 
% también sombreado. 
% En superficie con sombreado, tenemos que dar los valores x,y para z, 
% (z= f(x, y)). Para trazar el gráfico de superficie, tiene surf(z) 
% que se utiliza para el trazado en 3D.

% Valores x,y
[x,y]= meshgrid(0:0.1:5);

% Función z=f(x,y)
z= sin(x).*cos(y);

% Usar surfl() para la gráfica
surfl(z)
shading faceted
title('Sombreado facetado')

% Usar "Flat Shading" para cada malla
% Segmento de línea y cara tienen color constante
%surfl(z)
%shading flat
%title('Sombreado plano')

% Para variar el color en cada segmento de línea y cara
% mediante interpolación
%surfl(z)
%shading interp
%title('Sombreado interpolado')

str='$$ z=f(x,y)=\sin(x)\cos(y) $$';
text(20,10,str,'Interpreter','latex')
