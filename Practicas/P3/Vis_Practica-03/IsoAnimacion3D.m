% Animación 3D de una Isosuperficie

[x, y, z] = meshgrid(-3:0.25:3);
v = x.*exp(-x.^2 - y.^2 - z.^2);

vals = logspace(-1, -5, 25);  % 20 puntos desde 1e-1 a 1e-5
h = patch(isosurface(x, y, z, v, vals(1)), ...
   'facecolor', 'g', 'edgecolor', 'none');
axis([-3 3 -3 3 -3 3]);

camlight; lighting phong
for id = vals
   [faces, vertices] = isosurface(x, y, z, v, id);
   set(h, 'Faces', faces, 'Vertices', vertices);
   pause(1); % tiempo
end

close;