%Spring 2026 EELE-491
%Drew Currie Homework-2
%Problem 3

%% Part 1

%Generate mesh data

DecisionBoundryPlotter_3D(Question3TrilayerNeuralNetwork, 'TriLayeredNeuralNetwork', meas)
DecisionBoundryPlotter_3D(Question3MediumKNN, 'Medium KNN', meas)
DecisionBoundryPlotter_3D(Question3WeightedKNN, 'Weighted KNN', meas)
DecisionBoundryPlotter_3D(Question3LinearSVM, 'Linear SVM', meas)
DecisionBoundryPlotter_3D(Question3QuadraticSVM, 'Quadratic SVM', meas)
DecisionBoundryPlotter_3D(Question3MediumGaussianSVM, 'Medium Gaussian SVM', meas)
DecisionBoundryPlotter_3D(Question3FineTree, 'Fine Tree', meas)
DecisionBoundryPlotter_3D(Question3CoarseTree, 'Coarse Tree', meas)
