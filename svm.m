function w = svm(w, alpha )
%APSVM do apsvm update
if ~exist('alpha','var')
    alpha = 0.1;
end
load('train.mat')
fout = fopen(sprintf('res/20000svm-alpha=%.3f.txt',alpha),'w');
m = size(X,1);
for i = 1:m
    acc = sum((X*w>0) == y) / length(y);
    fprintf(fout,'Accuracy: %f\n',acc);
    x = X(i,:);
    if x*w + (y(i)~=1) > (y(i)~=0)
        yDirect = 1;
    else
        yDirect = 0;
    end       
    
    dw = (yDirect - y(i)) * x;
    w = w - alpha .* dw';
end
fclose(fout);
end