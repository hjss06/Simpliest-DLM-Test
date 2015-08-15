function w = per( w, alpha )
%APSVM do perceptron update
if ~exist('alpha','var')
    alpha = 0.1;
end
load('train.mat');
fout = fopen(sprintf('res/20000per-alpha=%.3f.txt',alpha),'w');
m = size(X,1);
for i = 1:m
    acc = sum((X*w > 0) == y) / length(y);
    fprintf(fout,'Accuracy: %f\n',acc);
    x = X(i,:);
    
    yW = x*w > 0;
    dw = (yW - y(i)) * x;
    w = w - alpha .* dw';
end
fclose(fout);
end

