% Definiremos los datos volumétricos asignando un valor 
% a cada punto de una cuadrícula 3D. 
% Veamos un ejemplo simple y de grano grueso (72)

[x, y, z] = meshgrid([-1 0 1]); % -3:0.5:3
v = x .* exp(-x.^2 - y.^2 - z.^2);

% Usaremos "scatter3" para visualizar los valores 
% en cada punto de la cuadrícula.

scatter3(x(:), y(:), z(:), 72, v(:), 'filled'); % 30 
view(-15, 35);                                  % ángulo azimutal y elevación
colorbar;