
    x = 0:0.01:10;  // Define interval with step size
    deff('y=f(x)', 'x^2 - 4*x + 3');  // Define the equation
    roots = roots(f);
    disp(roots);  // Display roots
    