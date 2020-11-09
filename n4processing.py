import SimpleITK as sitk
from multiprocessing import Pool
import os
import h5py
import numpy as np
import scipy.io as scio
from scipy import ndimage as nd

def n4BiasCorr(img):
    #return img
    ori_type = img.GetPixelIDValue()
    corrector = sitk.N4BiasFieldCorrectionImageFilter();
    maskImage = sitk.OtsuThreshold(img,0,1,200)
    tmp = sitk.Cast(img,sitk.sitkFloat32)
    tmp = corrector.Execute(tmp, maskImage)
    tmp = sitk.Cast(tmp, ori_type)
    return tmp

def hist_match(img,temp):
    ''' histogram matching from img to temp '''
    matcher = sitk.HistogramMatchingImageFilter()
    matcher.SetNumberOfHistogramLevels(1024)
    matcher.SetNumberOfMatchPoints(7)
    matcher.ThresholdAtMeanIntensityOn()
    res = matcher.Execute(img,temp)
    return res

def main():

    data_path = '/***your data path here***/'
    items = os.listdir(".")
    newlist = []
    ids = set()
    for names in items:
        if names.endswith("_resize.nii.gz"):
            newlist.append(names)

    for f in newlist:
        ids.add(f.split("_resize.nii.gz")[0])
    ids = list(ids)
    print(ids)

    for idn in range(len(ids)):
        subject_name = ids[idn]
        print(subject_name)

        f_Img1 = os.path.join(data_path,'%s_resize.nii.gz'%subject_name);
        img1_Org = sitk.ReadImage(f_Img1) 
        Out = n4BiasCorr(img1_Org)
        Out.SetDirection(img1_Org.GetDirection())
        Out.SetOrigin(img1_Org.GetOrigin())
        Out.SetSpacing(img1_Org.GetSpacing())
        sitk.WriteImage(Out,'./%s_resize_n4.nii.gz'%subject_name)

if __name__ == '__main__':
    main()
