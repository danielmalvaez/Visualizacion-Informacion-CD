% Gráfica de dos funciones

% Parámetros a definir de una gráfica bien etiquetada:
% Intervalo de la gráfica
% Tipo, ancho y color de línea
% Título de gráfica y ejes
% Notas adicionales

% Gráfica de función 1
t=0:1:25*pi;
x1=(25/2).*exp(-t./25)+(25/2).*exp(-3.*t/25);
plot(t,x1,'+','LineWidth',1.5,'color','blue')
title('Gráfica de dos funciones')
xlabel('tiempo (seg)')
ylabel('x_1(t), x_2(t)')
grid

hold on

% Gráfica de función 2
x2=25.*exp(-t./25)-25.*exp(-3.*t./25);
plot(t,x2,'--','LineWidth',1.5,'color','red')

% Nota adicional 1
legend('x_1(t)','x_2(t)')

hold off

% Nota adicional 2
str='$$ x_1(t)=\frac{25}{2}e^{\frac{-t}{25}}+\frac{25}{2}e^{\frac{-3t}{25}} $$';
text(10,5,str,'Interpreter','latex')

str='$$ x_2(t)=25e^{\frac{-t}{25}}-25e^{\frac{-3t}{25}} $$';
text(20,10,str,'Interpreter','latex')
