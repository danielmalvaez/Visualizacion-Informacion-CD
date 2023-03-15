% Animación 3D de un Corte de Isosuperficie

[x, y, z] = meshgrid(-3:0.25:3);
v = x.*exp(-x.^2 - y.^2 - z.^2);

vals = -3:0.25:3;
h= slice(x, y, z, v, [], [], vals(1));
axis([-3 3 -3 3 -3 3]);
colorbar;
for id = vals
   delete(h);
   h= slice(x, y, z, v, [], [], id);
   axis([-3 3 -3 3 -3 3]);
   colorbar;
   pause(0.3); % tiempo
end

close;