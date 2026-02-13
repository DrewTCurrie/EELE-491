%% Drew Currie 
%% EELE-491 Spring 2026 MSU
%% Homework 4

clear; clc; close all hidden;

%% Problem 1
%Sigmoid Function
sigma = @(x) 1./(1+exp(-1*x));
sigma_prime = @(x) sigma(x).*(1-sigma(x));

% Plot Sigmoid function
figure("name","Sigmoid Function")
x = linspace(-10, 10, 100);
y = sigma(x);
subplot(2,1,1);
plot(x, y, 'LineWidth', 2);
xlabel('Input (x)');
ylabel('Sigmoid Output');
title('Sigmoid Function');
grid on;
% Plot Sigmoid Derivative function
subplot(2,1,2);
y = sigma_prime(x);
plot(x,y,'LineWidth', 2);
xlabel('Input (x)');
ylabel('Sigmoid Derivative');
title('Derivative of Sigmoid Function');
grid on;

%Hyperbolic Tangent Function
tan_h = @(x) tanh(x);
tan_h_prime = @(x) sech(x).^2;

% Plot Hyperbolic Tangent function
figure("name","Hyperbolic Tangent Function")
x = linspace(-10, 10, 100);
y = tan_h(x);
subplot(2,1,1);
plot(x, y, 'LineWidth', 2);
xlabel('Input (x)');
ylabel('Hyperbolic Tangent Output');
title('Hyperbolic Tangent Function');
grid on;
% Plot Hyperbolic Tangent Derivative function
subplot(2,1,2);
y = tan_h_prime(x);
plot(x,y,'LineWidth', 2);
xlabel('Input (x)');
ylabel('Hyperbolic Tangent Derivative');
title('Derivative of Hyperbolic Tangent Function');
grid on;

%Rectified Linear Unit Function
ReLU = @(x) max(0,x);
ReLU_prime = @(x) heaviside(x);

% Plot Rectified Linear Unit function
figure("name","Rectified Linear Unit Function")
x = linspace(-10, 10, 100);
y = tan_h(x);
subplot(2,1,1);
plot(x, y, 'LineWidth', 2);
xlabel('Input (x)');
ylabel('Rectified Linear Unit Function Output');
title('Rectified Linear Unit Function');
grid on;
% Plot Hyperbolic Tangent Derivative function
subplot(2,1,2);
y = tan_h_prime(x);
plot(x,y,'LineWidth', 2);
xlabel('Input (x)');
ylabel('Rectified Linear Unit Function Derivative');
title('Derivative of Rectified Linear Unit Function');
grid on;