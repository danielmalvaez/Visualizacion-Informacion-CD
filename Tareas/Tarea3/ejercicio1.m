% Alumno : Axel Daniel Malváez Flores
% No. Cta: 318315126
% Visualización de la Información

t = -5:0.01:5;

% equations
eq1 = exp(7*t) - 2*exp(-2 * t);
eq2 = -exp(-2*t);
eq3 = exp(7*t) + 2 * exp(-2*t);

% we plot equations in R^3
plot3(eq1, eq2, eq3, '+');

xlim([-10,5]);
ylim([-5,5]);
zlim([0,10]);

xlabel('eq1');
ylabel('eq2');
zlabel('eq3');


sgtitle('Graph of differential equations in $R^3$', 'interpreter', 'latex');