%% Code to plot the decision boundry of a provided decision model
function DecisionBoundryPlotter_3D(Model, modelName, measuredData)
   
    % -- Nested for loops replaced with the assistance of generative AI
    n = 100;
    xrange = linspace(min(measuredData(:,1)), max(measuredData(:,1)), n);
    yrange = linspace(min(measuredData(:,2)), max(measuredData(:,2)), n);
    zrange = linspace(min(measuredData(:,3)), max(measuredData(:,3)), n);
    
    [X, Y, Z] = ndgrid(xrange, yrange, zrange);
    mesh = [X(:), Y(:), Z(:)];
    % --
    mesh_predictions = Model.predictFcn(mesh);

    figure()
    hold on;
    plotSetosa = (mesh_predictions == "setosa");
    plotVersicolor = (mesh_predictions == "versicolor");
    plotVirginica = (mesh_predictions == "virginica");
    
    view(3)
    scatter3(mesh(plotSetosa, 1), mesh(plotSetosa, 2), mesh(plotSetosa,3), "y.")
    scatter3(mesh(plotVersicolor, 1), mesh(plotVersicolor, 2), mesh(plotVersicolor,3), "c.")
    scatter3(mesh(plotVirginica, 1), mesh(plotVirginica, 2), mesh(plotVirginica,3), "r.")

    % Plot measured training data and label name
    scatter3(measuredData(1:50,1), measuredData(1:50, 2),measuredData(1:50, 3),"y^")
    hold on;
    scatter3(measuredData(51:100, 1), measuredData(51:100,2),measuredData(51:100,3), "cX")
    hold on;
    scatter3(measuredData(101:end, 1), measuredData(101:end, 2),measuredData(101:end, 3),"r", "diamond")
    hold off;
    title(sprintf('Model Decision Boundry %s: model', modelName))

end