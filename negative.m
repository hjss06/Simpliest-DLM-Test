function w = negative(w, alpha, epsilon )
%POSITIVE do negative DLM update
if ~exist('epsilon','var')
    epsilon = 0.1;
end

if ~exist('alpha','var')
    alpha = 0.1;
end
load('train.mat')
fout = fopen(sprintf('res/20000n-alpha=%.3f-epsilon=%.3f.txt',alpha,epsilon),'w');
m = size(X,1);
for i = 1:m
    acc = sum((X*w > 0) == y) / length(y);
    fprintf(fout,'Accuracy: %f\n',acc);
    
    x = X(i,:);
    if x*w - epsilon*(y(i)~=1) > -epsilon*(y(i)~=0)
        yDirect = 1;
    else
        yDirect = 0;
    end
    
    yW = (x*w) > 0;
    
    dw = (yDirect - yW) * x ./ epsilon;
    w = w + alpha .* dw';
end
fclose(fout);
end

