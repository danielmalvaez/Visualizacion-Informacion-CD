% Alumno : Axel Daniel Malváez Flores
% No. Cta: 318315126
% Visualización de la Información

% Definimos el rango que tomara el valor x
x = -2:0.1:2;
y = -2:0.8:2;

[X, Y] = meshgrid(x,y);
Z = X .* exp(-((X-(Y.^2)).^2 + Y.^2));

subplot(2,2,1);
plot3(X,Y,Z);
view(3);
title('Gráfica plot3');

subplot(2,2,2);
surf(X,Y,Z);
view(3);
title('Gráfica surf');

subplot(2,2,3);
mesh(X,Y,Z);
view(180,20);
title('Gráfica mesh');

subplot(2,2,4);
plot3(X,Y,Z);
view(90,0);
title('Gráfica plot3 - 2D');

% Caracteristicas de nuestra gráfica
xlabel('x');
ylabel('y');
zlabel('z');
sgtitle('Grafica de $z = xe^{-[(x-y^2)^2 + y^2]}$ con diferentes angulos de vista', 'interpreter', 'latex');