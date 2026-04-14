%% Transformer Forward Pass
close all; clear all; clc;


%% Define Network Parameters

Nhead = 8; % Number of heads in multi-headed attention
Nlayers = 6; % Number of sequencial encoder blocks (and decoder blocks)
Ntokens = 512; % Number of input/output tokens to consider
Vocab = 37000; % Vocabulary size
dmodel = 512; % Dimension of embedded vectors
dK = 64; % Dimension of query and key
dV = 64; % Dimension of value
dFF = 2048; % Dimension of feed-forward hidden layer


%% Initialize learned weight matrices
% Encoder

W_embedding_input = 2*rand(Vocab,dmodel)-1; % one

WQ_encoder_self_full = randn(dmodel, dK, Nhead, Nlayers); % per head, per layer
WK_encoder_self_full = randn(dmodel, dK, Nhead, Nlayers); % per head, per layer
WV_encoder_self_full = randn(dmodel, dK, Nhead, Nlayers); % per head, per layer
W_encoder_post_attention_full = randn(Nhead*dV,dmodel, Nlayers); % per layer

WQ_encoder_decoder_full = randn(dmodel, dK, Nhead, Nlayers);
Wk_encoder_decoder_full = randn(dmodel, dK, Nhead, Nlayers);
Wv_encoder_decoder_full = randn(dmodel, dK, Nhead, Nlayers);
W_decoder_post_attention_full = randn(Nhead*dv, dmodel, Nlayers);

W_encoder_FFN1_full = randn(dmodel, dFF, Nlayers); % per layer
b_encoder_FFN1_full = randn(1,dFF, Nlayers); % per layer
W_encoder_FFN2_full = randn(dFF,dmodel, Nlayers); % per layer
b_encoder_FFN2_full = randn(1,dmodel,Nlayers); % per layer

W = randn(dmodel, Vocab);

% Decoder

W_embedding_output = 2*rand(Vocab,dmodel)-1; % one

WQ_decoder_self = randn(dmodel,dK); % per head, per layer
WK_decoder_self = randn(dmodel,dK); % per head, per layer
WV_decoder_self = randn(dmodel,dV); % per head, per layer
W_decoder_post_self_attention = randn(Nhead*dV,dmodel); % per layer

WQ_encoder_decoder = randn(dmodel,dK); % per head, per layer
WK_encoder_decoder = randn(dmodel,dK); % per head, per layer
WV_encoder_decoder = randn(dmodel,dV); % per head, per layer
W_decoder_post_attention = randn(Nhead*dV,dmodel); % per layer

W_decoder_FFN1 = randn(dmodel,dFF); % per layer
b_decoder_FFN1 = randn(1,dFF); % per layer
W_decoder_FFN2 = randn(dFF,dmodel); % per layer
b_decoder_FFN2 = randn(1,dmodel); % per layer

W_final = randn(dmodel,Vocab); % one

%% Define Tokenized Inputs and Outputs
input_tokens = randperm(Vocab,Ntokens)
% input_tokens =  fliplr([40, 5895, 1148, 3492, 690, 387, 19698, 1306, 420, 11914, 1701, 6724, 4288, 584, 343, 66777, 25]);
input = zeros(Ntokens,Vocab);
for i = 1:Ntokens
    input(i,input_tokens(i)) = 1;
end
% Optional: visualize one-hot encoded input
%imagesc(input)

output_tokens = [randperm(Vocab,1), input_tokens(1:Ntokens-1)]
% output_tokens = [8415, input_tokens(1:Ntokens-1)]
output = zeros(Ntokens,Vocab);
for i = 1:Ntokens
    output(i,output_tokens(i)) = 1;
end    

%% Apply Input Embedding and Positional Encoding
% Define positional encoding matrix
PE = positional_encoding(Ntokens,dmodel);

% Optional: visualize positional encoding
imagesc(PE)
imagesc(positional_encoding(100,512))

% Apply input embedding weights and add positional encoding info
X = input*W_embedding_input + PE;

% Optional: Compare input*W to W
tmp = input*W_embedding_input;
tmp(1,:)
W_embedding_input(input_tokens(1),:)

Encoder Self-Attention
Q = X*WQ_encoder_self;
K = X*WK_encoder_self;
V = X*WV_encoder_self;

softmax_input = Q*K'/sqrt(dK);
softmax_output = softmax_row(softmax_input);
Attention = softmax_output*V;


%% Encoder (Concatenate) Add and Normalize
% Define positional encoding matrix
PE = positional_encoding(Ntokens,dmodel);

% Optional: visualize positional encoding
%imagesc(PE)

% Apply input embedding weights and add positional encoding info
X = input*W_embedding_input + PE;

% Optional: Compare input*W to W
%tmp = output*W_embedding_output;
%tmp(1,:)
%W_embedding_output(output_tokens(1),:)

for layer = 1:Nlayers
    WQ_layer = WQ_encoder_self_full(:,:,:,layer);
    WK_layer = WK_encoder_self_full(:,:,:,layer);
    WV_layer = WV_encoder_self_full(:,:,:,layer);
    Wpost_layer = W_encoder_post_attention_full(:,:,layer);
    attention = multi_head_attention_block(X, WQ_layer, WK_layer, WV_layer,dK, Nhead, []);
    
    X = normalize(X+attention);
    % Forward
    
    W1 = W_encoder_FFN1_full(:,:,layer);
    b1 = b_encoder_FFN1_full(:,:,layer);
    W2 = W_encoder_FFN2_full(:,:,layer);
    b2 = b_encoder_FFN2_full(:,:,layer);
    
    X = normalize(X + max(0, X*W1 + b1)*W2+b2);
end

EncoderOutput = X;
%% Decoder Self-Attention (Concatenate) Add and Normalize

PE = positional_encoding(Ntokens, dmodel);
X = output*W_embedding_output + PE;
mask = tril(ones(Ntokens));

for layer = 1:Nlayers
    % Masked self-attention
    WQ_layer = WQ_decoder_self_full(:,:,:,layer);
    WK_layer = WK_decoder_self_full(:,:,:,layer);
    WV_layer = WV_decoder_self_full(:,:,:,layer);
    Wpost_layer = W_decoder_post_self_attention_full(:,:,layer);

    attention = multi_head_attention_block(X, WQ_layer, WK_layer, WV_layer, Wpost_layer, dK, Nhead, mask);
    X = normalize(X + attention);

    % Encoder-decoder attention:
    
    Ntokens = size(X,1);
    dV = size(WV_encoder_decoder_all,2);
    Head_out = zeros(Ntokens,dV,Nhead);

    for head = 1:Nhead
        WQ = WQ_encoder_decoder_all(:,:,head,layer);
        WK = WK_encoder_decoder_all(:,:,head,layer);
        WV = WV_encoder_decoder_all(:,:,head,layer);

        Q = X*WQ;             % decoder queries
        K = EncoderOutput*WK; % encoder keys
        V = EncoderOutput*WV; % encoder values

        softmax_input = Q*K'/sqrt(dK);
        softmax_output = softmax_row(softmax_input);
        Head_out(:,:,head) = softmax_output*V;
    end

    Attention_concat = zeros(Ntokens, Nhead*dV);
    for head = 1:Nhead
        idx1 = (head-1)*dV + 1;
        idx2 = head*dV;
        Attention_concat(:,idx1:idx2) = Head_out(:,:,head);
    end

    Attention = Attention_concat * W_decoder_post_attention_all(:,:,layer);
    X = normalize(X + Attention);

    % Feed-forward
    W1 = W_decoder_FFN1_all(:,:,layer);
    b1 = b_decoder_FFN1_all(:,:,layer);
    W2 = W_decoder_FFN2_all(:,:,layer);
    b2 = b_decoder_FFN2_all(:,:,layer);

    X = normalize(X + max(0, X*W1 + b1)*W2 + b2);
end



% Apply linear weights
Attention = Attention*W_decoder_post_self_attention;

% Add to input and normalize
X = normalize(X + Attention);

%% Encoder-Decoder Attention
Q = EncoderOutput*WQ_decoder_self;
K = EncoderOutput*WK_decoder_self;
V = X*WV_decoder_self;

softmax_input = Q*K'/sqrt(dK);
softmax_output = softmax_row(softmax_input);
Attention = softmax_output*V;


%% Encoder-Decoder Attention (Concatenate) Add and Normalize
% For multi-headed attention, concatenate outputs from each head
% N/A for this demo

% Apply linear weights
Attention = Attention*W_decoder_post_attention;

% Add to input and normalize
X = normalize(X + Attention);

Decoder Feed-Forward Network
DecoderOutput = normalize(X + max(0,X*W_decoder_FFN1+b_decoder_FFN1)*W_decoder_FFN2+b_decoder_FFN2);
Output Probabilities
OutputProbabilities = softmax_row(DecoderOutput*W_final);


Output Prediction
[predicted_tokens,~] = find(OutputProbabilities'==max(OutputProbabilities'));
predicted_tokens = predicted_tokens'

Helper Function: Positional Encoding
function PE = positional_encoding(Npos,Ndim)
    PE = zeros(Npos,Ndim);
    for i = 1:Npos
        for j = 1:ceil(Ndim/2)
            PE(i,2*j-1) = sin(i/(10000^((2*j-1)/Ndim)));
            PE(i,2*j) = cos(i/(10000^((2*j-1)/Ndim)));
        end
    end

    % Remove half of the last pair if we have an odd dimension
    if mod(Ndim,2)
        PE(:,end) = [];
    end
end


%% Helper Function: Row-wise Softmax
function out = softmax_row(in)
    out = softmax(in')';
end

%% Attention helper function
function Attention_out = multi_head_attention_block(X_in, WQ_full, WK_full, WV_full, W_post, dK, Nhead, mask)
    
    Ntokens = size(X_in, 1);
    dV = size(WV_full, 2);
    head_Out = zeros(Ntokens, dV, Nhead);

    parfor head = 1:Nhead
        WQ = WQ_full(:,:,head);
        WK = WK_full(:,:,head);
        WV = WV_full(:,:,head);
    
        Q = X_in*WQ;
        K = X_in*WK;
        V = X_in*WV;
    
        softmax_in = Q*K'/sqrt(dK);
    
        if ~isempty(mask)
            softmax_in = softmax_in .* mask;
        end
    
        softmax_out = softmax_row(softmax_in);
        head_Out(:,:,head) = softmax_out*V;
    end
    
    attention_cat = zeros(Ntokens, Nhead*dV);
    for head = 1:Nhead
        idx = (head-1)*dV + 1;
        idx1 = head*dV;
        attention_cat(:, idx, idx1) = head_Out(:,:,head);
    end
    Attention_out = attention_cat * W_post;
end