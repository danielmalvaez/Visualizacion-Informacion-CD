% Alumno : Axel Daniel Malváez Flores
% No. Cta: 318315126
% Visualización de la Información

t = -5:0.01:5;

% equations
eq1 = exp(7*t) - 2*exp(-2 * t);
eq2 = -exp(-2*t);
eq3 = exp(7*t) + 2 * exp(-2*t);

% plot equations individually but in the same graph
plot(t,eq1, '+');
hold on;
plot(t,eq2, '--');
hold on;
plot(t,eq3, 'o');
hold off;

% Setting the limits for our axes
xlim([-3,3]);
ylim([-6,20]);

xlabel('x');
ylabel('y');

legend('Eq1','Eq2', 'Eq3');
sgtitle('Graph of the equations system in 2D', 'interpreter', 'latex');