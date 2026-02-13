%% Multi-layer perception forward pass

function [y, h] = MLP_forward_pass(x, W1, W2, b)
    h = x*W1+b(1);
    h = 1./(1+exp(-1.*h));
    y = h*W2+b(2);
    y = 1./(1+exp(-1.*y));

end
