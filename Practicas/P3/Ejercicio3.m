% Práctica 3 de Visualización de la Información
% Alumno: Axel Daniel Malváez Flores
% Ejercicios de Clase

% We define the range for x and y
x = -8:0.01:8;
y = -8:0.01:8;

% We create a meshgrid
[X,Y] = meshgrid(x,y);

% We assing values for r and Z
r = sqrt(X.^2 + Y.^2);
Z = sin(r) ./ r ;

% Plotting functions in  la función con cuatro diferentes tipos de vista
subplot(2,2,1);
surf(X,Y,Z,EdgeColor='interp');
view(2);
title('Vista 2D');

subplot(2,2,2);
surf(X,Y,Z, EdgeColor="flat");
view(90,0);
title('Vista Frente');

subplot(2,2,3);
surf(X,Y,Z, EdgeColor="texturemap");
view(-30,30);
title('Vista lado 1');

subplot(2,2,4);
surf(X,Y,Z, EdgeColor="flat");
view(-68.1986, 42.8760);
title('Vista lado 2');

% Caracteristicas de nuestra gráfica
xlabel('x');
ylabel('y');
zlabel('z');
sgtitle('Grafica de $z = \frac{sin(r)}{r}$ con diferentes angulos de vista', 'interpreter', 'latex');