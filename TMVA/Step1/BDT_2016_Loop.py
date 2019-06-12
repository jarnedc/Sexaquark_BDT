import ROOT
from ROOT import *
import os
import shutil
import glob
import sys

############################################
######HERE DEFINE ALL INPUT#################
############################################

#input signal and background file
MCSignalFile = "/user/jdeclerc/CMSSW_8_0_30/src/SexaQAnalysis/AnalyzerAllSteps/test/FlatTreeProducer/test_FlatTreeProducerMC10062019.root"
BkgFile      = "/user/jdeclerc/CMSSW_8_0_30/src/SexaQAnalysis/AnalyzerAllSteps/test/FlatTreeProducer/test_FlatTreeProducerData10062019.root"

#predefined cuts:
#error_lxy_cut = ROOT.TCut("Alt$(_S_error_lxy_interaction_vertex,0) < 0.1")
#lxy_cut = ROOT.TCut("Alt$(_S_lxy_interaction_vertex,0) > 1.9")
#mass_cut = ROOT.TCut("Alt$(_S_mass,0) > 0.")
MasterCut = ROOT.TCut("Alt$(_S_error_lxy_interaction_vertex,0) < 0.1 && Alt$(_S_lxy_interaction_vertex,0) > 1.9 && Alt$(_S_mass,0) > 0. && Alt$(_S_chi2_ndof,0) < 4." )
#MasterCut = error_lxy_cut and lxy_cut and mass_cut and S_chi2_ndof_cut
#MasterCut = ROOT.TCut("(Alt$(_S_error_lxy_interaction_vertex[0],0) < 0.1) and (Alt$(_S_lxy_interaction_vertex[0],0) > 1.9) and  (Alt$(_S_mass[0],0) > 0.) and (Alt$(_S_chi2_ndof[0],0) < 4.)")
#define ratio for training to testing:
trainTestSplit = 0.8

###########################################
####NOW RUN THE REAL STUFF#################
###########################################
localoutputdir = sys.argv[2]
#os.mkdir(localoutputdir)

#outputdir = sys.argv[3]
#os.mkdir(outputdir)

SignFile = ROOT.TFile.Open(MCSignalFile)
BkgFile  = ROOT.TFile.Open(BkgFile)


#helper function to move all files from one dir to another
def moveAllFilesinDir(srcDir, dstDir):
    # Check if both the are directories
    if os.path.isdir(srcDir) and os.path.isdir(dstDir) :
        # Iterate over all the files in source directory
        for filePath in glob.glob(srcDir + '\*'):
            # Move each file to destination Directory
            shutil.move(filePath, dstDir);
    else:
        print("srcDir & dstDir should be Directories")


def SingleTraining(kin_variables,iteration):
	# define the dataloader
	dataloader = ROOT.TMVA.DataLoader(localoutputdir+'/dataset_BDT_v'+str(iteration))

	# Add variables to dataloader
	for variable in kin_variables:
		dataloader.AddVariable(variable)

	# Add trees to dataloader
	SignalTree     = SignFile.Get("FlatTreeProducer/FlatTree")
	BkgTree        = BkgFile.Get("FlatTreeProducer/FlatTree")
	dataloader.AddSignalTree(SignalTree, 1)
	dataloader.AddBackgroundTree(BkgTree, 1)

	#adding the cuts and so
	dataloader.PrepareTrainingAndTestTree(MasterCut,\
		'TrainTestSplit_Signal={}:'.format(trainTestSplit)+\
		'TrainTestSplit_Background={}:'.format(trainTestSplit)+'SplitMode=Random')

	# Setup TMVA
	ROOT.TMVA.Tools.Instance()
	ROOT.TMVA.PyMethodBase.PyInitialize()

	outputFile = ROOT.TFile.Open(localoutputdir+'/plots_BDT_v'+str(iteration)+'.root', 'RECREATE')
	factory = ROOT.TMVA.Factory('TMVAClassification', outputFile,
		'!V:!Silent:Color:Transformations=I;D;P;G,D:'+\
		'AnalysisType=Classification')


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
	#canvas = factory.GetROCCurve(dataloader)
	#canvas.Draw()
	#canvas.SaveAs("BDT_2016_v"+str(iteration)+".root")
	outputFile.Close()
	#moveAllFilesinDir(localoutputdir, outputdir)

#list of variables to cut on
AllKinVariables = [
"_S_error_lxy_interaction_vertex",
"_S_lxy_interaction_vertex",
"_S_chi2_ndof",
"_S_daughters_deltaphi",
"_S_daughters_deltaeta",
"_S_daughters_openingsangle",
"_S_eta",
"_S_dxy_over_lxy",
"_Ks_dxy_over_lxy",
"_Lambda_dxy_over_lxy",
"_S_dz",
"_Ks_dz",
"_Lambda_dz",
"_S_pt",
"_Ks_pt",
"_Lambda_pt",
"_S_pz",
"_Ks_pz",
"_Lambda_pz",
"_S_vz_interaction_vertex"]

#run SingleTraining a few times by always dropping one of the KinVariables, the variables which will be dropped is the one corresponding to the index 'i_var'
#for i_var in range(0,len(AllKinVariables)) :
#	kinVariablesSubset = []
#	for i_var_subset in range(0,len(AllKinVariables)):
#		if(i_var_subset is not i_var):#the only variable not to add is the one corresponding to the index 'i_var'
#			kinVariablesSubset.append(AllKinVariables[i_var_subset])
#	print "-----> The full Kin Variable list is: "
#	print AllKinVariables
#	print "-----> But will for now only train on: "
#	print kinVariablesSubset
#	SingleTraining(kinVariablesSubset,i_var) 
	

kinVariablesSubset = []
i_var = int(sys.argv[1])
for i_var_subset in range(0,len(AllKinVariables)):
	if(i_var_subset is not i_var):#the only variable not to add is the one corresponding to the index 'i_var'
		kinVariablesSubset.append(AllKinVariables[i_var_subset])
print "-----> The full Kin Variable list is: "
print AllKinVariables
print "-----> But will for now only train on: "
print kinVariablesSubset
SingleTraining(kinVariablesSubset,i_var) 
