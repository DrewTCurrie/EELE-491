%Spring 2026 EELE-491
%Drew Currie Homework-2
%Problem 1

BOOSTING_RATE = 1;
UNDERSAMPLE_RATE = 0.5;

%% Question 1, part 1
predicitions = basicLinearSVM.predictFcn(test_data);
CMat = confusionmat(test_labels, predicitions);
TP = CMat(2,2);
TN = CMat(1,1);
FP = CMat(1,2);
FN = CMat(2,1);

%Calculate Accuracy, Precision, Recall, and F1
accuracy = (TP+TN)/(TP+TN+FP+FN);
precision = TP / (TP+FP);
recall = TP/(TP+FN);
F1 = 2*(precision*recall)/(precision+recall);

% Display the results
fprintf('Accuracy: %.2f%%\n', accuracy * 100);
fprintf('Precision: %.2f%%\n', precision * 100);
fprintf('Recall: %.2f%%\n', recall * 100);
fprintf('F1 Score: %.2f\n', F1);

%% Part 2
%Create more data of minority class via boosting
minorityClass = train_data(1:100,1:2);
majorityClass = train_data(100:end, 1:2);
newData = [minorityClass; minorityClass(1:(100*BOOSTING_RATE), 1:2) + 0.01*randn(1,2)];
undersampledData = majorityClass(1:(length(majorityClass)*UNDERSAMPLE_RATE),1:2);
newTrainingData = [newData;undersampledData];
newTrainingLabels = [zeros(length(newData),1);ones(length(undersampledData),1)];
%% Part 3
%Create new SVM

%% Part 4
%Results of new Linear SVM
predicitions = boostedUndersampledLinearSVM.predictFcn(test_data);
CMat = confusionmat(test_labels, predicitions);
TP = CMat(2,2);
TN = CMat(1,1);
FP = CMat(1,2);
FN = CMat(2,1);

%Calculate Accuracy, Precision, Recall, and F1
accuracy = (TP+TN)/(TP+TN+FP+FN);
precision = TP / (TP+FP);
recall = TP/(TP+FN);
F1 = 2*(precision*recall)/(precision+recall);

% Display the results <- MATLAB AI added this section automatically. 
% I don't know how I feel that MATLAB now has an AI always reading my code
% and making suggestions on what to write next, including trying to
% complete thsi comment for me...
fprintf('Accuracy: %.2f%%\n', accuracy * 100);
fprintf('Precision: %.2f%%\n', precision * 100);
fprintf('Recall: %.2f%%\n', recall * 100);
fprintf('F1 Score: %.2f\n', F1);

%% Part 5
%Additional tuning: I found a boosting rate of 1, or doubling the minority
%class, and undersampling of 50% worked quite well. 
% This was 200 of class 0 and 2450 of class 1.
