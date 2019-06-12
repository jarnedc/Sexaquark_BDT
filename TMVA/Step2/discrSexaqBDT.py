

import optparse
import os
import sys
import ROOT
import numpy
import array
import re
import warnings
import os.path
from math import *
import math


def clone():
    

    #dirname = "BDT"

    #os.mkdir(dirname)

    #cwd = os.getcwd()

    iDir = '/pnfs/iihe/cms/store/user/jdeclerc/crmc_Sexaq/Skimmed/CRAB_SimSexaq_Skimmed_completely_disabled_cosThetaXYCut_innerHitPosCut_25052019_v1/FlatTree/'

#    for fileIn in os.listdir(iDir):
    fileIn = 'test_FlatTreeProducerMC.root' 
    print fileIn
    fileH  = ROOT.TFile.Open(iDir+fileIn)
    inTree = fileH.Get('FlatTreeProducer/FlatTree')
    
    #fileOut = cwd+'/'+dirname+'/test.root'
    #	ofile   = ROOT.TFile(fileOut, 'recreate')
    #	print inTree.GetEntries()
    return inTree.CloneTree()

    #	ofile.Write()
    #	ofile.Close()

def __init__(self):
    pass


def createBDTSexaqDiscr(self):
    self.getBDTSexaqDiscr    = ROOT.TMVA.Reader();

   
    self.getBDTSexaqDiscr.AddVariable("_S_error_lxy_interaction_vertex",           (self.var1))   
    self.getBDTSexaqDiscr.AddVariable("_S_lxy_interaction_vertex",           (self.var2))   
    self.getBDTSexaqDiscr.AddVariable("_S_chi2_ndof",      (self.var3))   
    self.getBDTSexaqDiscr.AddVariable("_S_daughters_deltaphi",      (self.var4))   
    self.getBDTSexaqDiscr.AddVariable("_S_daughters_deltaeta",     (self.var5))   
    self.getBDTSexaqDiscr.AddVariable("_S_daughters_openingsangle",          (self.var6))   
    self.getBDTSexaqDiscr.AddVariable("_S_eta", (self.var7))   
    self.getBDTSexaqDiscr.AddVariable("_S_dxy_over_lxy",         (self.var8))   
    self.getBDTSexaqDiscr.AddVariable("_Ks_dxy_over_lxy",  (self.var9))   
    self.getBDTSexaqDiscr.AddVariable("_Lambda_dxy_over_lxy",          (self.var10))   
    self.getBDTSexaqDiscr.AddVariable("_S_dz",(self.var11))   
    self.getBDTSexaqDiscr.AddVariable("_Ks_dz",           (self.var12))   
    self.getBDTSexaqDiscr.AddVariable("_Lambda_dz",           (self.var13))   
    self.getBDTSexaqDiscr.AddVariable("_S_pt",           (self.var14))   
    self.getBDTSexaqDiscr.AddVariable("_Ks_pt",           (self.var15))   
    self.getBDTSexaqDiscr.AddVariable("_Lambda_pt",           (self.var16))   
    self.getBDTSexaqDiscr.AddVariable("_S_pz",           (self.var17))   
    self.getBDTSexaqDiscr.AddVariable("_Ks_pz",           (self.var18))   
    self.getBDTSexaqDiscr.AddVariable("_Lambda_pz",           (self.var19))   
    self.getBDTSexaqDiscr.AddVariable("_S_vz_interaction_vertex",           (self.var20))   



    # dymva trainined xml
    #baseCMSSW = os.getenv('CMSSW_BASE')
    self.getBDTSexaqDiscr.BookMVA("BDT","/user/jdeclerc/Analysis/SexaQuark/CMSSW_9_4_9/src/TMVA/Step1/LoopCut20Var2016/dataset_BDT_v0/weights")


def help(self):
    return '''Add dy mva variables'''


def addOptions(self,parser):
    #description = self.help()
    #group = optparse.OptionGroup(parser,self.label, description)
    #group.add_option('-b', '--branch',   dest='branch', help='Name of something that is not used ... ', default='boh')
    #parser.add_option_group(group)
    #return group
    pass


def checkOptions(self,opts):
    pass

#def process(self,**kwargs):
def process():

    #self.getBDTSexaqDiscr    = None

    var1 = array.array('f',[0])
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
   
    #tree  = kwargs['tree']
    #input = kwargs['input']
    #output = kwargs['output']


    #newbranches = ['BDTSexaq']
    dirname = "BDT"

    os.mkdir(dirname)
    cwd = os.getcwd()
    fileOut = cwd+'/'+dirname+'/test.root'
    otree = clone()

    BDTSexaq      = numpy.ones(1, dtype=numpy.float32)

    otree.Branch('BDTSexaq',  BDTSexaq,  'BDTSexaq/F')

    #self.createBDTSexaqDiscr()
    getBDTSexaqDiscr    = ROOT.TMVA.Reader();

   
    getBDTSexaqDiscr.AddVariable("_S_error_lxy_interaction_vertex",           (var1))   
    getBDTSexaqDiscr.AddVariable("_S_lxy_interaction_vertex",           (var2))   
    getBDTSexaqDiscr.AddVariable("_S_chi2_ndof",      (var3))   
    getBDTSexaqDiscr.AddVariable("_S_daughters_deltaphi",      (var4))   
    getBDTSexaqDiscr.AddVariable("_S_daughters_deltaeta",     (var5))   
    getBDTSexaqDiscr.AddVariable("_S_daughters_openingsangle",          (var6))   
    getBDTSexaqDiscr.AddVariable("_S_eta", (var7))   
    getBDTSexaqDiscr.AddVariable("_S_dxy_over_lxy",         (var8))   
    getBDTSexaqDiscr.AddVariable("_Ks_dxy_over_lxy",  (var9))   
    getBDTSexaqDiscr.AddVariable("_Lambda_dxy_over_lxy",          (var10))   
    getBDTSexaqDiscr.AddVariable("_S_dz",(var11))   
    getBDTSexaqDiscr.AddVariable("_Ks_dz",           (var12))   
    getBDTSexaqDiscr.AddVariable("_Lambda_dz",           (var13))   
    getBDTSexaqDiscr.AddVariable("_S_pt",           (var14))   
    getBDTSexaqDiscr.AddVariable("_Ks_pt",           (var15))   
    getBDTSexaqDiscr.AddVariable("_Lambda_pt",           (var16))   
    getBDTSexaqDiscr.AddVariable("_S_pz",           (var17))   
    getBDTSexaqDiscr.AddVariable("_Ks_pz",           (var18))   
    getBDTSexaqDiscr.AddVariable("_Lambda_pz",           (var19))   
    getBDTSexaqDiscr.AddVariable("_S_vz_interaction_vertex",           (var20))   

    nentries = otree.GetEntries()
    print 'Total number of entries: ',nentries 

    # avoid dots to go faster
    #itree     = self.itree
    #otree     = self.otree


    print '- Starting eventloop'
    step = 5000
    for i in xrange(nentries):
        otree.GetEntry(i)

        ## print event count
        if i > 0 and i%step == 0.:
            print i,'events processed.'

        BDTSexaq[0] = -9999.
       

        S_error_lxy = otree._S_error_lxy_interaction_vertex
        S_lxy = otree._S_lxy_interaction_vertex
        S_mass = otree._S_mass
        S_chi2_ndof = otree._S_chi2_ndof

        if S_error_lxy < 0.1 and S_lxy > 1.9 and S_mass > 0. and S_chi2_ndof < 4.: 
                # nvtx/F:mth/F:ptll/F:projtkmet/F:projpfmet/F:jetpt1_cut/F:uperp/F:upara/F:mtw1/F:PfMetDivSumMet/F:metPuppi/F:dphillmet/F:recoil/F:dphilljet_cut/F:dphilmet1/F:mpmet/
                var1[0] =  otree._S_error_lxy_interaction_vertex
                var2[0] =  otree._S_lxy_interaction_vertex
                var3[0] =  otree._S_chi2_ndof
                var4[0] =  otree._S_daughters_deltaphi
                var5[0] =  otree._S_daughters_deltaeta
                var6[0] =  otree._S_daughters_openingsangle
                var7[0] =  otree._S_eta
                var8[0] =  otree._S_dxy_over_lxy
                var9[0] =  otree._Ks_dxy_over_lxy
                var10[0] = otree._Lambda_dxy_over_lxy
                var11[0] = otree._S_dz
                var12[0] = otree._Ks_dz
                var13[0] = otree._Lambda_dz
                var14[0] = otree._S_pt
                var15[0] = otree._Ks_pt
                var16[0] = otree._Lambda_pt
                var17[0] = otree._S_pz
                var18[0] = otree._Ks_pz
                var19[0] = otree._Lambda_pz
                var20[0] = otree._S_vz_interaction_vertex

                BDTSexaq[0] = getBDTSexaqDiscr.EvaluateMVA("BDT")

          
        otree.Fill()
         
    fileOut.Write()
    fileOut.Close()
    print '- Eventloop completed'
