import SimpleITK as sitk
from multiprocessing import Pool
import os
import h5py
import numpy as np
import scipy.io as scio
from scipy import ndimage as nd

def hist_match(img,temp):
    ''' histogram matching from img to temp '''
    matcher = sitk.HistogramMatchingImageFilter()
    matcher.SetNumberOfHistogramLevels(1024)
    matcher.SetNumberOfMatchPoints(7)
    matcher.ThresholdAtMeanIntensityOn()
    res = matcher.Execute(img,temp)
    return res

def main():

    data_path = '***/your data path here/***'
    img_standard_forhis = os.path.join(data_path,'***Image for histogram matching***')
    img_standard_Org = sitk.ReadImage(img_standard_forhis)
    items = os.listdir(".")
    newlist = []
    ids = set()
    for names in items:
        if names.endswith("_resize_n4.nii.gz"):
            newlist.append(names)

    for f in newlist:
        ids.add(f.split('_resize_n4.nii.gz')[0])
    ids = list(ids)
    print ids

    for idn in range(len(ids)):
        subject_name = ids[idn]
        print(subject_name)

        f_Img1 = os.path.join(data_path,'%s_resize_n4.nii.gz'%subject_name);
        img1_Org = sitk.ReadImage(f_Img1)
        Out = hist_match(img1_Org,img_standard_Org)

        Out.SetDirection(img1_Org.GetDirection())
        Out.SetOrigin(img1_Org.GetOrigin())
        Out.SetSpacing(img1_Org.GetSpacing())
        sitk.WriteImage(Out,'./%s_resize_n4_his.nii.gz'%subject_name)

if __name__ == '__main__':
    main()
