% Cortes a través de datos volumétricos

% Como puede ver, cuanto mayor sea la resolución, 
% más difícil será visualizar. 
% Una forma de entender los datos volumétricos es 
% tomar un corte ("slice") de ellos.

% Resolución aún más alta
[x, y, z] = meshgrid(-3:0.25:3);
v = x.*exp(-x.^2 - y.^2 - z.^2);

 scatter3(x(:), y(:), z(:), 30, v(:), 'filled');

% slice(x, y, z, v, [], [], 0);        % corte a lo largo de z=0
% slice(x, y, z, v, [], 0, 0);         % cortes a lo largo de y=0, z=0
% slice(x, y, z, v, [1.5 -1.5], 0, 0); % cortes a lo largo de x=-1.5, x=1.5, y=0, z=0
colorbar;