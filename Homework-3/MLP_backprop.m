%% Multi-layer perception back propagation 
function [W1_new, W2_new, b_new] = MLP_backprop(x, t, W1, W2, b, alpha)
    % Lambda function for the partial derivative solving
    % This isn't actually useful, but I thought it was neat. Leaving it in
    % anyway. 
    % partial = @(x) (1./(1+exp(-1.*x))).*(1-(1./(1-exp(-1.*x))));
    % Before the actual code, I apologize to whomever has to read this. 
    % The naming convention seemed like a good idea when I started. It was
    % not a good idea. 
    % Get results from multi-layer forward pass
    [y,h] = MLP_forward_pass(x, W1, W2, b);
    % Begin calculating partial derivatives 
    partialError_partialOutput = y - t;
    partialOutput_partialOuputIn = y.*(1-y);
    partialHidden2_partialWeight2 = h;
    % Calculate updated weights for the second layer
    W2_new = W2 - alpha*(partialHidden2_partialWeight2' * (partialError_partialOutput .* partialOutput_partialOuputIn));
    % Calculate last partials 
    partialHidden1_partialHidden1In = h.*(1-h);
    partialError_partialHidden = (partialError_partialOutput .* partialOutput_partialOuputIn) * W2';
    % Calculate updated weights for the first layer
    W1_new = W1 - (alpha * (x' * (partialError_partialHidden .* partialHidden1_partialHidden1In)));
    
    % Update biases
    b_new = [b(1) - alpha * (sum(partialError_partialHidden .* partialHidden1_partialHidden1In)), b(2) - alpha * (sum(partialError_partialOutput .* partialOutput_partialOuputIn))];
end