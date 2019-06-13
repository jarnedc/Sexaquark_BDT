from ROOT import TFile, TH1F, TH2F, TEfficiency, TCanvas


#fIn = TFile('/user/jdeclerc/Analysis/SexaQuark/CMSSW_9_4_7/src/SexaQAnalysis/AnalyzerAllSteps/test/wihtMatchingOnHits/test_TrackMatchingOnHits.root', 'read')
fIn = TFile('/user/jdeclerc/Analysis/SexaQuark/CMSSW_9_4_9/src/TMVA/Step2/BDT/DiscrApplied_test_FlatTreeProducerMC12062019.root', 'read')
fOut = TFile('AnalyzerFlatTreeMC.root','RECREATE')


inTree = fIn.Get('FlatTree')

h2_BDT_mass = TH2F('h2_BDT_mass','h2_BDT_mass; S mass (GeV); BDT variable;',200,0,20,200,-1,1)
for branch in inTree.GetListOfBranches():
	print branch.GetName()
for i in range(inTree.GetEntries()):
	inTree.GetEntry(i)
	h2_BDT_mass.Fill(inTree._S_mass[0],inTree.SexaqBDT)
h2_BDT_mass.Write()

fOut.Write()
fOut.Close()
