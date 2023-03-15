t = -10:0.01:10;

k1 = 1;
k2 = 4;
k3 = 8;

eq4 = 4 .* exp(t) .* sin(t);

eq1 = 1.*exp(2*t) + 4.*exp(t).* cos(t) + 8.*exp(t).*sin(t);
eq2 = (k2 + k3).*exp(t).*cos(t) + (k3 - k2).*exp(t).*sin(t);
eq3 = k1.*exp(2*t) + 3*k2.*exp(t).*cos(t) + 3*k3.*exp(t).*sin(t);

% plot equations individually but in the same graph
plot(t,eq1, '+');
hold on;
plot(t,eq2, '--');
hold on;
plot(t,eq3, 'o');
hold off;

xlim([-4,4]);
ylim([-20,30]);

xlabel('x');
ylabel('y');

legend('eq1', 'eq2', 'eq3');
sgtitle('Graph of the equation system with k constants', 'interpreter', 'latex');