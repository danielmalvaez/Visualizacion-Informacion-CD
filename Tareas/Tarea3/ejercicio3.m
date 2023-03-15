% Alumno : Axel Daniel Malváez Flores
% No. Cta: 318315126
% Visualización de la Información

% Definimos el rango que tomara el valor x
x = -3:0.8:3;
y = -3:0.8:13;

% Creamos nuestra malla con la x y la y
[X,Y] = meshgrid(x,y);

Z = X.^4 + 3.*X.^2 + Y.^2 - 2.*X - 2.*Y - 2*X.^2.*Y + 6;

subplot(2,2,1);
h = surf(X,Y,Z, FaceColor="blue", EdgeColor="black", LineStyle="--");
set(h, "FaceAlpha", 0.3)
view(3);
title('Gráfica con surf');

subplot(2,2,2);
mesh(X,Y,Z, EdgeColor="flat");
view(3);
title('Gráfica con mesh');
colorbar;

subplot(2,2,3);
surf(X,Y,Z, EdgeColor="black", FaceColor="interp");
view(3);
title('Gráfica con interp colores surf');

subplot(2,2,4);
mesh(X,Y,Z, EdgeColor="black", FaceColor="interp");
view(90,0);
title('Gráfica con interp colores mesh');

sgtitle('Graphs of the surface with different views', 'interpreter', 'latex')