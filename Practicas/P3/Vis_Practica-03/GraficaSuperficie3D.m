% Un gráfico de superficie es una superficie 3D que crea diferentes 
% tipos de superficies para diferentes expresiones. 
% Para crear una superficie tenemos que dar los valores x,y para z, 
% z= f(x, y). Para trazar el gráfico de superficie tiene "surf()" 
% que generará la superficie 3D. 
% Tiene color de borde sólido y color de cara sólido.

% Valores de "x" y "y"
[x,y]= meshgrid(0:0.1:5);

% Función z=f(x,y).
z= sin(x).*cos(y);

% surf() se usa para la gráfica 3D
surf(z)

% surf() se usa para multiples gráficas 3D
% subplot(2,2,1); surf(peaks(60)); view(-37.5,30) % ángulo azimutal y elevación
% subplot(2,2,2); surf(peaks(60)); view(-7,80)
% subplot(2,2,3); surf(peaks(60)); view(-90,0)
% subplot(2,2,4); surf(peaks(60)); view(-7,10)

% Nota adicional
str='$$ z=f(x,y)=\sin(x)\cos(y) $$';
text(20,10,str,'Interpreter','latex')

% Iluminación
% lighting gouraud
% camlight(0,0)