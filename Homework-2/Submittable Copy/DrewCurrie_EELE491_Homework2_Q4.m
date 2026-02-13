%Spring 2026 EELE-491
%Drew Currie Homework-2
%Problem 4

%% Recording performance of each model. 
% For my sanity while clicking through menus I opted for doing this one
% at a time after learning that the hardway on the last two problems. 
clc

trainDataPredictions = trainedModel.predictFcn(x_train);
testDataPredictions = trainedModel.predictFcn(x_test);

% Training data
CMat = confusionmat(trainDataPredictions, y_train);
TP = CMat(2,2);
TN = CMat(1,1);
FP = CMat(1,2);
FN = CMat(2,1);

%Calculate Accuracy, Precision, Recall, and F1
accuracy = (TP+TN)/(TP+TN+FP+FN);
precision = TP / (TP+FP);
recall = TP/(TP+FN);
F1 = 2*(precision*recall)/(precision+recall);

% Print results 
fprintf('Accuracy: %.2f%%\n', accuracy * 100);
fprintf('Precision: %.2f%%\n', precision * 100);
fprintf('Recall: %.2f%%\n', recall * 100);
fprintf('F1 Score: %.2f\n', F1);

% Test data
CMat = confusionmat(testDataPredictions, y_test);
TP = CMat(2,2);
TN = CMat(1,1);
FP = CMat(1,2);
FN = CMat(2,1);

%Calculate Accuracy, Precision, Recall, and F1
accuracy = (TP+TN)/(TP+TN+FP+FN);
precision = TP / (TP+FP);
recall = TP/(TP+FN);
F1 = 2*(precision*recall)/(precision+recall);

% Print results 
fprintf('Accuracy: %.2f%%\n', accuracy * 100);
fprintf('Precision: %.2f%%\n', precision * 100);
fprintf('Recall: %.2f%%\n', recall * 100);
fprintf('F1 Score: %.2f\n', F1);
