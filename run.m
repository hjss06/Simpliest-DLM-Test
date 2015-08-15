function ans = run(flag)

load('train.mat')
w = randn(size(X,2),1);

alphas = [3,1,0.3,0.1,0.03,0.01,0.003];
epsilons = [30,10,3,1,0.3,0.1,0.03];
na = length(alphas);
ne = length(epsilons);

switch flag
    case 1,        
        parfor n = 1 : na*ne                     
            w = randn(100,1);
            alpha = alphas(mod(n-1,na) + 1);
            epsilon = epsilons(floor((n-1)/na)+1);
            w = positive(w,alpha,epsilon);
        end
    case -1,
        parfor n = 1 : na*ne             
            w = randn(100,1);
            alpha = alphas(mod(n-1,na) + 1);
            epsilon = epsilons(floor((n-1)/na)+1);
            w = negative(w,alpha,epsilon);
        end
    case 2,
        parfor n = 1:na
            
            w = randn(100,1);
            alpha = alphas(n);
            w = svm(w,alpha);
        end
    case 3,        
        parfor n = 1:na
            
            w = randn(100,1);
            alpha = alphas(n);
            w = logistic(w,alpha);
        end
    case 0,        
        parfor n = 1:na
            
            w = randn(100,1);
            alpha = alphas(n);
            w = per(w,alpha);
        end
end  
