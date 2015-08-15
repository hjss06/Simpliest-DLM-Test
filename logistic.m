function [ w] = logistic(w,alpha )
%LOGISTIC do logistic regression
if ~exist('alpha','var')
    alpha = 0.1;
end
load('train.mat');
fout = fopen(sprintf('res/20000logi-alpha=%.3f.txt',alpha),'w');
m = size(X,1);
for i = 1:m
    acc = sum((X*w > 0) == y) / m;
    fprintf(fout,'Accuracy: %f\n',acc);
    
    x = X(i,:);
    p = 1./(1 + exp(-x*w));
    dw = (p - y(i))*x;
    w = w - alpha.* dw';
end
fclose(fout);

end

