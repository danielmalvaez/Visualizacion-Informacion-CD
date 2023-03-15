% Práctica 3 de Visualización de la Información
% Alumno: Axel Daniel Malváez Flores
% Ejercicios de Clase

% Definimos el rango que tomara el valor theta
theta = 0:0.01:5*pi;

% Definimos p en funcion de theta
p = theta.^2;

% Graficamos p con la funcion polar
polar(theta, p);

% Parametros de Graficacion

xlabel('x');
ylabel('y');
title('Graph of p = \theta^2 in polar coordinates');
legend('p');