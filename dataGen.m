function [X,y] = dataGen(n,p)
w = ones(p,1);
X = randn(n,p);
y = (X * w) > 0;
save('train.mat','X','y')
