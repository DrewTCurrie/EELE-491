%% Code to plot the decision boundry of a provided decision model
function DecisionBoundryPlotter_2D(Model, modelName, measuredData)
    
    xrange = linspace(min(measuredData(:,1)),max(measuredData(:,1)),100);
    yrange = linspace(min(measuredData(:,2)),max(measuredData(:,2)),100);
    
    idx = 0;
    mesh = zeros(100*100,2);
    for i = 1:100
        for j = 1:100
            idx = idx + 1;
            mesh(idx,1) = xrange(i);
            mesh(idx,2) = yrange(j);
        end
    end
    
    mesh_predictions = Model.predictFcn(mesh);
    figure()
    hold on;
    for i = 1:length(mesh)
        if mesh_predictions(i) == "setosa"
            scatter(mesh(i,1), mesh(i,2), "y.")
        elseif mesh_predictions(i) == "versicolor"
            scatter(mesh(i,1), mesh(i,2), "c.")
        elseif mesh_predictions(i) == "virginica"
            scatter(mesh(i,1), mesh(i,2),"r.")
        end
    end
    
    % Plot measured training data and label name
    scatter(measuredData(1:50,1), measuredData(1:50, 2),"y^")
    hold on;
    scatter(measuredData(51:100, 1), measuredData(51:100,2), "cX")
    hold on;
    scatter(measuredData(101:end, 1), measuredData(101:end, 2),"r", "diamond")
    hold off;
    title(sprintf('Model Decision Boundry %s: model', modelName))

end