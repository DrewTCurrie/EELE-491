%% Single layer perception forward pass calculation
function [out] = SLP_forward_pass(in, weights, bias)
    out = in*weights + bias;
    mask = out > 0;
    out(mask) = 1;
    mask = out < 0;
    out(mask) = 0;
end
