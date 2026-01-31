%% Code to plot the decision boundry of a provided decision model
function DecisionBoundryPlotter_3D(Model, modelName, measuredData)
    
    xrange = linspace(min(measuredData(:,1)),max(measuredData(:,1)),100);
    yrange = linspace(min(measuredData(:,2)),max(measuredData(:,2)),100);
    zrange = linspace(min(measuredData(:,3)),max(measuredData(:,3)),100);
    
    idx = 0;
    mesh = zeros(100*100,3);
    for i = 1:100
        for j = 1:100
            for k = 1:100
                idx = idx + 1;
                mesh(idx,1) = xrange(i);
                mesh(idx,2) = yrange(j);
                mesh(idx, 3) = zrange(k);
            end
        end
    end
    
    mesh_predictions = Model.predictFcn(mesh);
    figure()
    hold on;
    for i = 1:length(mesh)
        if mesh_predictions(i) == "setosa"
            scatter3(mesh(i,1), mesh(i,2),mesh(i,3), "y.")
        elseif mesh_predictions(i) == "versicolor"
            scatter3(mesh(i,1), mesh(i,2),mesh(i,3), "c.")
        elseif mesh_predictions(i) == "virginica"
            scatter3(mesh(i,1), mesh(i,2),mesh(i,3), "r.")
        end
    end
    
    % Plot measured training data and label name
    scatter3(measuredData(1:50,1), measuredData(1:50, 2),measuredData(1:50, 3),"y^")
    hold on;
    scatte3r(measuredData(51:100, 1), measuredData(51:100,2),measuredData(51:100,3), "cX")
    hold on;
    scatter3(measuredData(101:end, 1), measuredData(101:end, 2),measuredData(101:end, 3),"r", "diamond")
    hold off;
    title(sprintf('Model Decision Boundry %s: model', modelName))

end