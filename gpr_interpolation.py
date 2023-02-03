import pandas as pd
import numpy as np
import json
import pickle
from matplotlib import pyplot as plt
from scipy.fft import fft
import GPy

data2=pd.read_pickle("datapoints_dict.pkl")
X=[]
Y=[]
X_output=[]
Y_output=[]
problems=[]
for i,x in enumerate(list(data2.keys())):
    print(i)
    sim=data2[x]
    if np.isnan(sim["form_factor"]).any() or np.isnan(sim["total_density"]).any().any():
        problems.append(i)
        continue
    X.append(sim["form_factor"])
    Y.append(sim["total_density"])
    ed=sim["total_density"]
    x=ed[0].values.reshape(-1,1)
    y=ed[1].values.reshape(-1,1)
    kernel=GPy.kern.RBF(input_dim=1,variance=1,lengthscale=1)
    m=GPy.models.GPRegression(x,y,kernel)
    m.optimize(messages=True)
    m.optimize_restarts(num_restarts = 5)
    N=1000
    xrange=np.linspace(min(x),max(x),N)
    ypred=m.predict(xrange)[0]
    X_output.append(xrange.ravel())
    Y_output.append(ypred.ravel())
ff=pd.DataFrame(X).reset_index().drop(columns="index")
dens_x=pd.DataFrame(X_output).reset_index().drop(columns="index")
dens_y=pd.DataFrame(Y_output).reset_index().drop(columns="index")

ff.to_csv("form_factors.csv",index=False)
dens_x.to_csv("gpr_total_density_x.csv",index=False)
dens_y.to_csv("gpr_total_density_y.csv",index=False)

for i in problems:
    print(data2[list(data2.keys())[i]]["total_density"])
