%% Generate Synthetic Data

train_ratio = 0.8;

n0 = 200;
mu0 = [4 4];
sigma0 = [1 0.5; 0.5 0.5];
class0 = mvnrnd(mu0, sigma0, n0);
label0 = zeros(n0,1);

n1 = 200;
mu1 = [1 2];
sigma1 = [1 0.5; 0.5 2];
class1 = mvnrnd(mu1, sigma1, n1);
label1 = ones(n1,1);

xtrain0 = class0(1:n0*train_ratio,:);
ytrain0 = label0(1:n0*train_ratio);
xtest0 = class0(n0*train_ratio+1:end,:);
ytest0 = label0(n0*train_ratio+1:end);
xtrain1 = class1(1:n1*train_ratio,:);
ytrain1 = label1(1:n1*train_ratio);
xtest1 = class1(n1*train_ratio+1:end,:);
ytest1 = label1(n1*train_ratio+1:end);

train_data = [xtrain0; xtrain1];
train_labels = [ytrain0; ytrain1];
test_data = [xtest0; xtest1];
test_labels = [ytest0; ytest1];

%% Visualize Data

figure(1);
scatter(xtrain0(:,1),xtrain0(:,2),'bo');
hold on;
scatter(xtrain1(:,1),xtrain1(:,2),'rx');
scatter(xtest0(:,1),xtest0(:,2),'g^');
scatter(xtest1(:,1),xtest1(:,2),'kv');
hold off
xlabel('Feature 1'); ylabel('Feature 2');
legend({'Train Class 0','Train Class 1','Test Class 0','Test Class 1'});


%% Train and Import Models Before Coming Here...
% load Models_with_Validation;
load Models_without_Validation;

% Calculate test accuracy

predictions = trainedModel_CoarseKNN.predictFcn(test_data);
test_accuracy = 100*sum(test_labels==predictions)/length(test_labels)

% Calculate training accuracy
predictions = trainedModel_CoarseKNN.predictFcn(train_data);
train_accuracy = 100*sum(train_labels == predictions)/length(train_labels)

%% Visualize Decision Boundary

xrange = linspace(min(train_data(:,1)),max(train_data(:,1)),100);
yrange = linspace(min(train_data(:,2)),max(train_data(:,2)),100);

idx = 0;
mesh = zeros(100*100,2);
for i = 1:100
    for j = 1:100
        idx = idx + 1;
        mesh(idx,1) = xrange(i);
        mesh(idx,2) = yrange(j);
    end
end

mesh_predictions = trainedModel_FineKNN.predictFcn(mesh);

figure(1); hold on;
scatter(mesh(mesh_predictions==0,1),mesh(mesh_predictions==0,2),'c.');
scatter(mesh(mesh_predictions==1,1),mesh(mesh_predictions==1,2),'m.');
hold off;