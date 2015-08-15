# -*- coding: utf-8 -*-
"""
Created on Thu Jul 30 10:16:39 2015

@author: yangsong
"""

import re
import matplotlib.pylab as pl
import numpy as np

def getinfo(name):
    #fin = open('log-n-test-0.1-0.01.txt','r')
    fin = open(name,'r')
    txt = fin.read()
    pap = re.compile(r'([0-9]+\.[0-9]+)',re.MULTILINE)
    
    ap = re.findall(pap,txt)
    ap = [float(x) for x in ap]

    return ap
    
def plot(ap):
    n = len(ap)
    x = np.r_[0:n]      
    pl.plot(x,ap)
    pl.ylabel('Accuracy on train')    
    pl.xlabel('# of iteration')    
    
def positive():        
    alphas = [1,0.3,0.1,0.03,0.01,0.003,0.001]
    betas = [1,0.1,0.01,0.001]
    epsilons = [10,1,0.1,0.01]
    for alpha in alphas:
        for beta in betas:
            pl.figure()            
            tags = []            
            for epsilon in epsilons:
                name = "10000p-"+str(alpha)+"-"+str(beta)+"-"+str(epsilon)+".txt"
                tags.append(str(alpha)+"-"+str(beta)+"-"+str(epsilon))
                ap,norm = getinfo(name)
                plot(ap,norm)
            pl.legend(tags)
            name = 'Positive'+'-alpha='+str(alpha)+'-beta='+str(beta)+'.png'
            pl.savefig(name,bbox_inches='tight')
            pl.close()
            
    for alpha in alphas:
        for epsilon in epsilons:
            pl.figure()
            tags = []            
            for beta in betas:
                name = "10000p-"+str(alpha)+"-"+str(beta)+"-"+str(epsilon)+".txt"
                tags.append(str(alpha)+"-"+str(beta)+"-"+str(epsilon))
                ap, norm = getinfo(name)
                plot(ap,norm)
            pl.legend(tags)
            name = 'Positive'+'-alpha='+str(alpha)+'-epsilon='+str(epsilon)+'.png'
            pl.savefig(name,bbox_inches='tight')
            pl.close()
    
    for beta in betas:
        for epsilon in epsilons:
            pl.figure()
            tags = []            
            for alpha in alphas:
                name = "10000p-"+str(alpha)+"-"+str(beta)+"-"+str(epsilon)+".txt"
                tags.append(str(alpha)+"-"+str(beta)+"-"+str(epsilon))
                ap, norm = getinfo(name)
                plot(ap,norm)
            pl.legend(tags)
            name = 'Positive'+'-beta='+str(beta)+'-epsilon='+str(epsilon)+'.png'
            pl.savefig(name,bbox_inches='tight')
            pl.close()

def negative():
    alphas = [1,0.3,0.1,0.03,0.01,0.003,0.001]
    betas = [1,0.1,0.01,0.001]
    epsilons = [10,1,0.1,0.01]
    for alpha in alphas:
        for beta in betas:
            pl.figure()
            tags = []            
            for epsilon in epsilons:
                name = "10000n-"+str(alpha)+"-"+str(beta)+"-"+str(epsilon)+".txt"
                tags.append(str(alpha)+"-"+str(beta)+"-"+str(epsilon))
                ap,norm = getinfo(name)
                plot(ap,norm)
            pl.legend(tags)
            name = 'Negative'+'-alpha='+str(alpha)+'-beta='+str(beta)+'.png'
            pl.savefig(name,bbox_inches='tight')
            pl.close()
            
    for alpha in alphas:
        for epsilon in epsilons:
            pl.figure()
            tags = []            
            for beta in betas:
                name = "10000n-"+str(alpha)+"-"+str(beta)+"-"+str(epsilon)+".txt"
                tags.append(str(alpha)+"-"+str(beta)+"-"+str(epsilon))
                ap,norm = getinfo(name)
                plot(ap,norm)
            pl.legend(tags)
            name = 'Negative'+'-alpha='+str(alpha)+'-epsilon='+str(epsilon)+'.png'
            pl.savefig(name,bbox_inches='tight')
            pl.close()
    
    for beta in betas:
        for epsilon in epsilons:
            pl.figure()
            tags = []            
            for alpha in alphas:
                name = "10000n-"+str(alpha)+"-"+str(beta)+"-"+str(epsilon)+".txt"
                tags.append(str(alpha)+"-"+str(beta)+"-"+str(epsilon))
                ap,norm = getinfo(name)
                plot(ap,norm)
            pl.legend(tags)
            name = 'Negative'+'-beta='+str(beta)+'-epsilon='+str(epsilon)+'.png'
            pl.savefig(name,bbox_inches='tight')
            pl.close()

def per():
    alphas = [1,0.3,0.1,0.03,0.01,0.003,0.001]
    betas = [1,0.1,0.01,0.001]
    for alpha in alphas:
        pl.figure()
        tags = []
        for beta in betas:            
            name = "10000per-"+str(alpha)+"-"+str(beta)+".txt"
            tags.append(str(alpha)+"-"+str(beta))
            ap,norm = getinfo(name)
            plot(ap,norm)
        pl.legend(tags)
        name = 'Perceptron'+'-alpha='+str(alpha)+'.png'
        pl.savefig(name,bbox_inches='tight')
        pl.close()
            
    for beta in betas:
        pl.figure()
        tags = []
        for alpha in alphas:            
            name = "10000per-"+str(alpha)+"-"+str(beta)+".txt"
            tags.append(str(alpha)+"-"+str(beta))
            ap,norm = getinfo(name)
            plot(ap,norm)
        pl.legend(tags)
        name = 'Perceptron'+'-beta='+str(beta)+'.png'
        pl.savefig(name,bbox_inches='tight')
        pl.close()
        
def svm():
    alphas = [1,0.3,0.1,0.03,0.01,0.003,0.001]    
    betas = [1,0.1,0.01,0.001]
    for alpha in alphas:
        pl.figure()
        tags = []
        for beta in betas:            
            name = "10000svm-"+str(alpha)+"-"+str(beta)+".txt"
            tags.append(str(alpha)+"-"+str(beta))
            ap,norm = getinfo(name)
            plot(ap,norm)
        pl.legend(tags)
        name = 'APSVM'+'-alpha='+str(alpha)+'.png'
        pl.savefig(name,bbox_inches='tight')
        pl.close()
            
    for beta in betas:
        pl.figure()
        tags = []
        for alpha in alphas:            
            name = "10000svm-"+str(alpha)+"-"+str(beta)+".txt"
            tags.append(str(alpha)+"-"+str(beta))
            ap,norm = getinfo(name)
            plot(ap,norm)
        pl.legend(tags)
        name = 'APSVM'+'-beta='+str(beta)+'.png'
        pl.savefig(name,bbox_inches='tight')
        pl.close()
        
def combine():
    alphas = [1,0.3,0.1,0.03,0.01,0.003,0.001]
    betas = [1,0.1,0.01,0.001]
    epsilons = [10,1,0.1,0.01]
    for alpha in alphas:
        for beta in betas:            
            for epsilon in epsilons:
                names = ["10000p-"+str(alpha)+"-"+str(beta)+"-"+str(epsilon)+".txt",
                        "10000n-"+str(alpha)+"-"+str(beta)+"-"+str(epsilon)+".txt",
                        "10000svm-"+str(alpha)+"-"+str(beta)+".txt",
                        "10000per-"+str(alpha)+"-"+str(beta)+".txt",
                        ]
                pl.figure()
                for name in names:
                    ap,norm = getinfo(name)
                    plot(ap,norm)
                pl.legend(['P','N','SVM','PER'])
                name = "combine " + str(alpha)+"-"+str(beta)+"-"+str(epsilon)+'.png'
                pl.savefig(name,bbox_inches='tight')
                pl.close()                          

def bestAlphaPlot():
    alphas = [3,1,0.3,0.1,0.03,0.01,0.003]    
    epsilons = [30,10,3,1,0.3,0.1,0.03]
    
    for epsilon in epsilons:
        pmax = -np.Inf
        nmax = -np.Inf
        permax = -np.Inf
        svmmax = -np.Inf
        logimax = -np.Inf
        pname = ''
        nname = ''
        pername = ''
        svmname = ''
        loginame = ''
        for alpha in alphas:
            names = ["20000p-alpha=%.3f-epsilon=%.3f.txt" % (alpha,epsilon),
                    "20000n-alpha=%.3f-epsilon=%.3f.txt" % (alpha,epsilon),
                    "20000svm-alpha=%.3f.txt" % (alpha,),
                    "20000per-alpha=%.3f.txt" % (alpha,),
                    "20000logi-alpha=%.3f.txt" % (alpha,),                    
                    ]
            ap = getinfo(names[0])
            if ap[-1] > pmax:
                pmax = ap[-1]
                pname = names[0]
            ap = getinfo(names[1])
            if ap[-1] > nmax:
                nmax = ap[-1]
                nname = names[1]
            ap = getinfo(names[2])
            if ap[-1] > svmmax:
                svmmax = ap[-1]
                svmname = names[2]
            ap = getinfo(names[3])
            if ap[-1] > permax:
                permax = ap[-1]
                pername = names[3]
            ap = getinfo(names[4])
            if ap[-1] > logimax:
                logimax = ap[-1]
                loginame = names[4]
                
        pl.figure()
        names = [pname,nname,svmname,pername,loginame]
        for name in names:
            ap = getinfo(name)
            plot(ap)
        pl.legend(['P','N','SVM','PER','LOGI'])
        name = "combine-epsilon="+str(epsilon)+'.png'
        pl.savefig(name,bbox_inches='tight')
        pl.close()            
if __name__ == '__main__':
    #positive()
    #negative()
    #per()
    #svm()
    #combine()
    bestAlphaPlot()
    