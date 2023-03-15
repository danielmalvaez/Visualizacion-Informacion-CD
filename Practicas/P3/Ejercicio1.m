% Práctica 3 de Visualización de la Información
% Alumno: Axel Daniel Malváez Flores
% Ejercicios de Clase

% rango de x
x = 0:0.1:2*pi;

% Calculando la primera función
y1 = cos(x);
plot(x, y1);

hold on;

% Calculando la segunda función
y2 = sin(x);

% Plotting las dos funciones en la misma gráfica
plot(x, y2,'+');

hold off;

xlabel('x');
ylabel('y');
title('Graph of y = cos(x) and y = sin(x)');
legend('cos(x)', 'sin(x)');