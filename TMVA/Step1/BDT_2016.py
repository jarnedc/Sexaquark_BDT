import ROOT
from ROOT import *

# Select Theano as backend for Keras
from os import environ
#environ['KERAS_BACKEND'] = 'theano'
environ['KERAS_BACKEND'] = 'tensorflow'

# Set architecture of system (AVX instruction set is not supported on SWAN)
#environ['THEANO_FLAGS'] = 'gcc.cxxflags=-march=corei7'

from keras.models import Sequential
from keras.layers.core import Dense, Dropout, Activation
from keras.regularizers import l2
from keras import initializers
from keras.optimizers import Adam
from keras.optimizers import Adadelta
from keras.optimizers import Adagrad
from keras.optimizers import Nadam
from keras.optimizers import RMSprop
from keras.optimizers import SGD
from keras.constraints import maxnorm

# Open file
SignFile = ROOT.TFile.Open("/eos/user/j/jdeclerc/SSearch/BDTFiles/2016/test_FlatTreeProducerMC.root")
BkgFile  = ROOT.TFile.Open("/eos/user/j/jdeclerc/SSearch/BDTFiles/2016/test_FlatTreeProducerBkg.root")

# Get signal and background trees from file
SignalTree     = SignFile.Get("FlatTreeProducer/FlatTree")
BkgTree        = BkgFile.Get("FlatTreeProducer/FlatTree")

# Add variables to dataloader
dataloader = ROOT.TMVA.DataLoader('dataset_BDT_2016')
numVariables = 11
#nvtx/F:mth/F:ptll/F:projtkmet/F:projpfmet/F:jetpt1_cut/F:uperp/F:upara/F:mtw1/F:PfMetDivSumMet/F:metPuppi/F:dphillmet/F:recoil/F:dphilljet_cut/F:dphilmet1/F:mpmet/F
dataloader.AddVariable("_S_error_lxy_interaction_vertex")
dataloader.AddVariable("_S_lxy_interaction_vertex")
dataloader.AddVariable("_S_chi2_ndof")
dataloader.AddVariable("_S_daughters_deltaphi")
dataloader.AddVariable("_S_daughters_deltaeta")
dataloader.AddVariable("_S_daughters_openingsangle")
dataloader.AddVariable("_S_eta")
dataloader.AddVariable("_S_dxy_over_lxy")
dataloader.AddVariable("_Ks_dxy_over_lxy")
dataloader.AddVariable("_Lambda_dxy_over_lxy")
dataloader.AddVariable("_S_dz")
#dataloader.AddVariable("_Ks_dz")
#dataloader.AddVariable("_Lambda_dz")
#dataloader.AddVariable("_S_vz_interaction_vertex")
#weight = "XSWeight*SFweight2l*LepSF2l__ele_mvaFall17Iso_WP90__mu_cut_Tight_HWWW*LepCut2l__ele_mvaFall17Iso_WP90__mu_cut_Tight_HWWW*PrefireWeight*GenLepMatch2l*METFilter_MC"
#dataloader.SetSignalWeightExpression(weight)
#dataloader.SetBackgroundWeightExpression(weight)

#TCut 0j_cuts = "Alt$(CleanJet_pt[0],0)<30"
error_lxy_cut = ROOT.TCut("Alt$(_S_error_lxy_interaction_vertex,0) < 0.1")
lxy_cut = ROOT.TCut("Alt$(_S_lxy_interaction_vertex,0) > 1.9")
mass_cut = ROOT.TCut("Alt$(_S_mass,0) > 0.")
S_chi2_ndof_cut = ROOT.TCut("Alt$(_S_chi2_ndof,0) < 4.")

#################
# Add trees to dataloader
dataloader.AddSignalTree(SignalTree, 1)
dataloader.AddBackgroundTree(BkgTree, 1)
trainTestSplit = 0.8
dataloader.PrepareTrainingAndTestTree(ROOT.TCut(error_lxy_cut and lxy_cut and mass_cut and S_chi2_ndof_cut),
#dataloader.PrepareTrainingAndTestTree(ROOT.TCut(mass_cut),
        'TrainTestSplit_Signal={}:'.format(trainTestSplit)+\
        'TrainTestSplit_Background={}:'.format(trainTestSplit)+\
        'SplitMode=Random')

# Setup TMVA
ROOT.TMVA.Tools.Instance()
ROOT.TMVA.PyMethodBase.PyInitialize()

outputFile = ROOT.TFile.Open('BDTOutput_2016_v7.root', 'RECREATE')
factory = ROOT.TMVA.Factory('TMVAClassification', outputFile,
        '!V:!Silent:Color:Transformations=I;D;P;G,D:'+\
        'AnalysisType=Classification')


# Define model
#model = Sequential()
#model.add(Dense(72, init='glorot_normal', activation='relu', input_dim=numVariables))
#model.add(Dense(48, init='glorot_normal', activation='relu', W_constraint=maxnorm(1)))
#model.add(Dropout(0.1))
#model.add(Dense(32, init='glorot_normal', activation='relu', input_dim=48))
#model.add(Dropout(0.1))
#model.add(Dense(32, init='glorot_normal', activation='relu'))
#model.add(Dropout(0.1))
#model.add(Dense(24, init='glorot_normal', activation='relu', W_constraint=maxnorm(1)))
#model.add(Dense(4, init='glorot_normal', activation='relu', W_constraint=maxnorm(1)))
#model.add(Dense(2, init='glorot_uniform', activation='softmax'))

# Set loss and optimizer
#model.compile(loss='categorical_crossentropy', optimizer=Adam(),
#        metrics=['categorical_accuracy',])
#
## Store model to file
#model.save('model_2017_0j.h5')
#
## Print summary of model
#model.summary()
#
#factory.BookMethod(dataloader, ROOT.TMVA.Types.kPyKeras, 'PyKeras_2017_0j',
#        'H:!V:VarTransform=N:FilenameModel=model_2017_0j.h5:'+\
#        'NumEpochs=400:BatchSize=1000:')
#        #'ContinueTraining=false:SaveBestOnly=true:')

# BDT method
factory.BookMethod(dataloader,'BDT', 'BDT',
        'H:!V:VarTransform=None:'+\
        'NTrees=400:BoostType=AdaBoost:SeparationType=GiniIndex:nCuts=20:PruneMethod=CostComplexity:PruneStrength=12')

factory.TrainAllMethods()

factory.TestAllMethods()

factory.EvaluateAllMethods()

# Enable Javascript for ROOT so that we can draw the canvas
#ROOT.enableJSVis()
#%jsroot on
# Print ROC
canvas = factory.GetROCCurve(dataloader)
canvas.Draw()
canvas.SaveAs("BDT_2016_v7.root")
