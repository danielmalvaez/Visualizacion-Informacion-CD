% Cortes de Contorno

[x, y, z] = meshgrid(-3:0.25:3);
v = x.*exp(-x.^2 - y.^2 - z.^2);

 contourslice(x, y, z, v, [], [], 0, 20);      % z=0, 20 líneas de contorno
% contourslice(x, y, z, v, [], 0, [-1 1], 10);  % y=0, z=-1, z=1

view(3); grid on;                              % 3 para 3D, 2 para 2D
colorbar;