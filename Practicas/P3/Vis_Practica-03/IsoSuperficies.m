% Isosuperficies

% A diferencia de hacer cortes (ya sean planos o no lineales), 
% una forma diferente de explorar datos volumétricos es ver los 
% "límites". Si conectas todos los puntos con el mismo valor, 
% obtienes una isosuperficie:

[x, y, z] = meshgrid(-3:0.25:3);
v = x.*exp(-x.^2 - y.^2 - z.^2);

 isosurface(x, y, z, v, 1e-5); % Isosuperficie donde V=1e-5
% isosurface(x, y, z, v, -1e-4);

axis([-3 3 -3 3 -3 3]);

str='$$ v=xe^{(-x^2 - y^2 - z^2)} $$';
text(3,-3,str,'Interpreter','latex')