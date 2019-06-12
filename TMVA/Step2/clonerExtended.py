import os
import ROOT
import array
import numpy

class TreeCloner(object):
		
	#make a separate directory to store the result
	dirname = "BDT"
	if not os.path.exists(dirname):
    		os.makedirs(dirname)
	cwd = os.getcwd()

	#where to find the input data
	iDir = '/user/jdeclerc/CMSSW_8_0_30/src/SexaQAnalysis/AnalyzerAllSteps/test/FlatTreeProducer/test/'

	#get the reader
	getBDTSexaqReader    = ROOT.TMVA.Reader();

	#just define some variables
#        var1 = array('f',[0])
        var2 = array.array('f',[0])
        var3 = array.array('f',[0])
        var4 = array.array('f',[0])
        var5 = array.array('f',[0])
        var6 = array.array('f',[0])
        var7 = array.array('f',[0])
        var8 = array.array('f',[0])
        var9 = array.array('f',[0])
        var10 = array.array('f',[0])
        var11 = array.array('f',[0])
        var12 = array.array('f',[0])
        var13 = array.array('f',[0])
        var14 = array.array('f',[0])
        var15 = array.array('f',[0])
        var16 = array.array('f',[0])
        var17 = array.array('f',[0])
        var18 = array.array('f',[0])
        var19 = array.array('f',[0])
        var20 = array.array('f',[0])
	#add these variables to the reader
        #getBDTSexaqReader.AddVariable("_S_error_lxy_interaction_vertex",           (var1))   
        getBDTSexaqReader.AddVariable("_S_lxy_interaction_vertex",           (var2))   
        getBDTSexaqReader.AddVariable("_S_chi2_ndof",      (var3))   
        getBDTSexaqReader.AddVariable("_S_daughters_deltaphi",      (var4))   
        getBDTSexaqReader.AddVariable("_S_daughters_deltaeta",     (var5))   
        getBDTSexaqReader.AddVariable("_S_daughters_openingsangle",          (var6))   
        getBDTSexaqReader.AddVariable("_S_eta", (var7))   
        getBDTSexaqReader.AddVariable("_S_dxy_over_lxy",         (var8))   
        getBDTSexaqReader.AddVariable("_Ks_dxy_over_lxy",  (var9))   
        getBDTSexaqReader.AddVariable("_Lambda_dxy_over_lxy",          (var10))   
        getBDTSexaqReader.AddVariable("_S_dz",(var11))   
        getBDTSexaqReader.AddVariable("_Ks_dz",           (var12))   
        getBDTSexaqReader.AddVariable("_Lambda_dz",           (var13))   
        getBDTSexaqReader.AddVariable("_S_pt",           (var14))   
        getBDTSexaqReader.AddVariable("_Ks_pt",           (var15))   
        getBDTSexaqReader.AddVariable("_Lambda_pt",           (var16))   
        getBDTSexaqReader.AddVariable("_S_pz",           (var17))   
        getBDTSexaqReader.AddVariable("_Ks_pz",           (var18))   
        getBDTSexaqReader.AddVariable("_Lambda_pz",           (var19))   
        getBDTSexaqReader.AddVariable("_S_vz_interaction_vertex",           (var20))   

	#book the weights from the training to the Reader
        getBDTSexaqReader.BookMVA("BDT","/user/jdeclerc/Analysis/SexaQuark/CMSSW_9_4_9/src/TMVA/Step1/LoopCut20Var2016_10062019/dataset_BDT_v0/weights/TMVAClassification_BDT.weights.xml")
	#for each file in the directory now evaluate the weights
	for fileIn in os.listdir(iDir):
		print "the input file: ",fileIn

		fileH  = ROOT.TFile.Open(iDir+fileIn)
		inTree = fileH.Get('FlatTreeProducer/FlatTree')
		inTree.Show(18)

                print "number of entries in the input tree: ", inTree.GetEntries()
                fileOut = cwd+'/'+dirname+'/test.root'
                ofile   = ROOT.TFile(fileOut, 'recreate')
		#clone the input tree
                outTree = inTree.CloneTree(0)
		#add a branch to the tree where you will be adding the BDT variable
		SexaqBDT = numpy.ones(1, dtype=numpy.float32)
		outTree.Branch('SexaqBDT', SexaqBDT, 'SexaqBDT/F')
		#fill the BDT branch with -999 value
                SexaqBDT[0] = -999
                for i in range(inTree.GetEntries()):		      	 
                     inTree.GetEntry(i)
		     var2[0] = inTree._S_lxy_interaction_vertex[0]
		     var3[0] = inTree._S_chi2_ndof[0]
		     var4[0] = inTree._S_daughters_deltaphi[0]
		     var5[0] = inTree._S_daughters_deltaeta[0]
		     var6[0] = inTree._S_daughters_openingsangle[0]
		     var7[0] = inTree._S_eta[0]
		     var8[0] = inTree._S_dxy_over_lxy[0]
		     var9[0] = inTree._Ks_dxy_over_lxy[0]
		     var10[0] = inTree._Lambda_dxy_over_lxy[0]
		     var11[0] = inTree._S_dz[0]
		     var12[0] = inTree._Ks_dz[0]
		     var13[0] = inTree._Lambda_dz[0]
		     var14[0] = inTree._S_pt[0]
		     var15[0] = inTree._Ks_pt[0]
		     var16[0] = inTree._Lambda_pt[0]
		     var17[0] = inTree._S_pz[0]
		     var18[0] = inTree._Ks_pz[0]
		     var19[0] = inTree._Lambda_pz[0]
		     var20[0] = inTree._S_vz_interaction_vertex[0]
                     SexaqBDT[0] = getBDTSexaqReader.EvaluateMVA('BDT')
		     print 'SexaqBDT: ', SexaqBDT[0]
		     outTree.Fill()
		outTree.Show(18)
		#outTree.Print() 
		ofile.Write()
		ofile.Close()


