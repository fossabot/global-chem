#!/usr/bin/env python3
#
# GlobalChem - Schedule Four
#
# -----------------------------------

class ScheduleFour(object):

    def __init__(self):

        pass

    @staticmethod
    def get_smiles():

        smiles = {
            'dextropropoxyphene': 'CCC(=O)OC(CC1=CC=CC=C1)(C2=CC=CC=C2)C(C)CN(C)C',
            '2-[(dimethylamino)methyl]-1-(3-methoxyphenyl)cyclohexanol': 'CN(C)CC1CCCCC1(C2=CC(=CC=C2)OC)O',
            'alfaxalone': 'CC(=O)C1CCC2C1(CC(=O)C3C2CCC4C3(CCC(C4)O)C)C',
            'alprazolam': 'CC1=NN=C2N1C3=C(C=C(C=C3)Cl)C(=NC2)C4=CC=CC=C4',
            'barbital': 'CCC1(C(=O)NC(=O)NC1=O)CC',
            'brexanolone': 'CC(=O)C1CCC2C1(CCC3C2CCC4C3(CCC(C4)O)C)C',
            'bromazepam': 'C1C(=O)NC2=C(C=C(C=C2)Br)C(=N1)C3=CC=CC=N3',
            'camazepam': 'CN1C2=C(C=C(C=C2)Cl)C(=NC(C1=O)OC(=O)N(C)C)C3=CC=CC=C3',
            'carisoprodol': 'CCCC(C)(COC(=O)N)COC(=O)NC(C)C',
            'chloralbetaine': 'C[N+](C)(C)CC(=O)[O-].C(C(Cl)(Cl)Cl)(O)O',
            'chloralhydrate': 'C(C(Cl)(Cl)Cl)(O)O',
            'chlordiazepoxide': 'CN=C1CN(C(=C2C=C(C=CC2=N1)Cl)C3=CC=CC=C3)O',
            'clobazam': 'CN1C(=O)CC(=O)N(C2=C1C=CC(=C2)Cl)C3=CC=CC=C3',
            'clonazepam': 'C1C(=O)NC2=C(C=C(C=C2)[N+](=O)[O-])C(=N1)C3=CC=CC=C3Cl',
            'clorazepate': 'C1=CC=C(C=C1)C2=NC(C(=O)NC3=C2C=C(C=C3)Cl)C(=O)O',
            'clotiazepam': 'CCC1=CC2=C(S1)N(C(=O)CN=C2C3=CC=CC=C3Cl)C',
            'cloxazolam': 'C1COC2(N1CC(=O)NC3=C2C=C(C=C3)Cl)C4=CC=CC=C4Cl',
            'delorazepam': 'C1C(=O)NC2=C(C=C(C=C2)Cl)C(=N1)C3=CC=CC=C3Cl',
            'diazepam': 'CN1C(=O)CN=C(C2=C1C=CC(=C2)Cl)C3=CC=CC=C3',
            'dichloralphenazone': 'CC1=CC(=O)N(N1C)C2=CC=CC=C2.C(C(Cl)(Cl)Cl)(O)O.C(C(Cl)(Cl)Cl)(O)O',
            'estazolam': 'C1C2=NN=CN2C3=C(C=C(C=C3)Cl)C(=N1)C4=CC=CC=C4',
            'ethchlorvynol': 'CCC(C=CCl)(C#C)O',
            'ethinamate': 'O=C(OC1(C#C)CCCCC1)N',
            'ethyl loflazepate': 'CCOC(=O)C1C(=O)NC2=C(C=C(C=C2)Cl)C(=N1)C3=CC=CC=C3F',
            'fludiazepam': 'CN1C(=O)CN=C(C2=C1C=CC(=C2)Cl)C3=CC=CC=C3F',
            'flunitrazepam': 'CN1C(=O)CN=C(C2=C1C=CC(=C2)[N+](=O)[O-])C3=CC=CC=C3F',
            'flurazepam': 'CCN(CC)CCN1C(=O)CN=C(C2=C1C=CC(=C2)Cl)C3=CC=CC=C3F',
            'fospropofol': 'CC(C)C1=C(C(=CC=C1)C(C)C)OCOP(=O)(O)O',
            'halazepam': 'C1C(=O)N(C2=C(C=C(C=C2)Cl)C(=N1)C3=CC=CC=C3)CC(F)(F)F',
            'haloxazolam': 'C1COC2(N1CC(=O)NC3=C2C=C(C=C3)Br)C4=CC=CC=C4F',
            'ketazolam': 'CC1=CC(=O)N2CC(=O)N(C3=C(C2(O1)C4=CC=CC=C4)C=C(C=C3)Cl)C',
            'lemborexant': 'CC1=NC(=NC=C1OCC2(CC2C(=O)NC3=NC=C(C=C3)F)C4=CC(=CC=C4)F)C',
            'loprazolam': 'CN1CCN(CC1)C=C2C(=O)N3C(=N2)CN=C(C4=C3C=CC(=C4)[N+](=O)[O-])C5=CC=CC=C5Cl',
            'lorazepam': 'C1=CC=C(C(=C1)C2=NC(C(=O)NC3=C2C=C(C=C3)Cl)O)Cl',
            'lormetazepam': 'CN1C2=C(C=C(C=C2)Cl)C(=NC(C1=O)O)C3=CC=CC=C3Cl',
            'mebutamate': 'CCC(C)C(C)(COC(=O)N)COC(=O)N',
            'medazepam': 'CN1CCN=C(C2=C1C=CC(=C2)Cl)C3=CC=CC=C3',
            'meprobamate': 'CCCC(C)(COC(=O)N)COC(=O)N',
            'methohexital': 'CCC#CC(C)C1(C(=O)NC(=O)N(C1=O)C)CC=C',
            'methylphenobarbital': 'CCC1(C(=O)NC(=O)N(C1=O)C)C2=CC=CC=C2',
            'midazolam': 'CC1=NC=C2N1C3=C(C=C(C=C3)Cl)C(=NC2)C4=CC=CC=C4F',
            'nimetazepam': 'CN1C(=O)CN=C(C2=C1C=CC(=C2)[N+](=O)[O-])C3=CC=CC=C3',
            'nitrazepam': 'C1C(=O)NC2=C(C=C(C=C2)[N+](=O)[O-])C(=N1)C3=CC=CC=C3',
            'nordiazepam': 'C1C(=O)NC2=C(C=C(C=C2)Cl)C(=N1)C3=CC=CC=C3',
            'oxazepam': 'C1=CC=C(C=C1)C2=NC(C(=O)NC3=C2C=C(C=C3)Cl)O',
            'oxazolam': 'CC1CN2CC(=O)NC3=C(C2(O1)C4=CC=CC=C4)C=C(C=C3)Cl',
            'paraldehyde': 'CC1OC(OC(O1)C)C',
            'petrichloral': 'C(C(COC(C(Cl)(Cl)Cl)O)(COC(C(Cl)(Cl)Cl)O)COC(C(Cl)(Cl)Cl)O)OC(C(Cl)(Cl)Cl)O',
            'phenobarbital': 'CCC1(C(=O)NC(=O)NC1=O)C2=CC=CC=C2',
            'pinazepam': 'C#CCN1C(=O)CN=C(C2=C1C=CC(=C2)Cl)C3=CC=CC=C3',
            'prazepam': 'C1CC1CN2C(=O)CN=C(C3=C2C=CC(=C3)Cl)C4=CC=CC=C4',
            'quazepam': 'C1C(=S)N(C2=C(C=C(C=C2)Cl)C(=N1)C3=CC=CC=C3F)CC(F)(F)F',
            'remimazolam': 'CC1=CN=C2N1C3=C(C=C(C=C3)Br)C(=NC2CCC(=O)OC)C4=CC=CC=N4',
            'suvorexant': 'CC1CCN(CCN1C(=O)C2=C(C=CC(=C2)C)N3N=CC=N3)C4=NC5=C(O4)C=CC(=C5)Cl',
            'temazepam': 'CN1C2=C(C=C(C=C2)Cl)C(=NC(C1=O)O)C3=CC=CC=C3',
            'tetrazepam': 'CN1C(=O)CN=C(C2=C1C=CC(=C2)Cl)C3=CCCCC3',
            'triazolam': 'CC1=NN=C2N1C3=C(C=C(C=C3)Cl)C(=NC2)C4=CC=CC=C4Cl',
            'zaleplon': 'CCN(C1=CC=CC(=C1)C2=CC=NC3=C(C=NN23)C#N)C(=O)C',
            'zolpidem': 'CC1=CC=C(C=C1)C2=C(N3C=C(C=CC3=N2)C)CC(=O)N(C)C',
            'zopiclone': 'CN1CCN(CC1)C(=O)OC2C3=NC=CN=C3C(=O)N2C4=NC=C(C=C4)Cl',
            'fenfluramine': 'CCNC(C)CC1=CC(=CC=C1)C(F)(F)F',
            'lorcaserin': 'CC1CNCCC2=C1C=C(C=C2)Cl',
            '(+)-norpseudoephedrine': 'CC(C(C1=CC=CC=C1)O)N',
            'diethylpropion': 'CCN(CC)C(C)C(=O)C1=CC=CC=C1',
            'fencamfamin': 'CCNC1C2CCC(C2)C1C3=CC=CC=C3',
            'fenproporex': 'CC(CC1=CC=CC=C1)NCCC#N',
            'mazindol': 'C1CN2C(=N1)C3=CC=CC=C3C2(C4=CC=C(C=C4)Cl)O',
            'mefenorex': 'CC(CC1=CC=CC=C1)NCCCCl',
            'pemoline': 'C1=CC=C(C=C1)C2C(=O)N=C(O2)N',
            'phentermine': 'CC(C)(CC1=CC=CC=C1)N',
            'pipradrol': 'C1CCNC(C1)C(C2=CC=CC=C2)(C3=CC=CC=C3)O',
            'serdexmethylphenidate': 'COC(=O)C(C1CCCCN1C(=O)OC[N+]2=CC=CC(=C2)C(=O)NC(CO)C(=O)[O-])C3=CC=CC=C3',
            'sibutramine': 'CC(C)CC(C1(CCC1)C2=CC=C(C=C2)Cl)N(C)C',
            'solriamfetol': 'C1=CC=C(C=C1)CC(COC(=O)N)N',
            'spa((-)-1-dimethylamino-1,2-diphenylethane)': 'CN(C)C(CC1=CC=CC=C1)C2=CC=CC=C2',
            'pentazocine': 'CC1C2CC3=C(C1(CCN2CC=C(C)C)C)C=C(C=C3)O',
            'butorphanol': 'C1CCC2(C3CC4=C(C2(C1)CCN3CC5CCC5)C=C(C=C4)O)O',
        }

        return smiles

    @staticmethod
    def get_smarts():

        smarts = {
            'dextropropoxyphene': '[#6]-[#6]-[#6](=[#8])-[#8]-[#6](-[#6]-[#6]1:[#6]:[#6]:[#6]:[#6]:[#6]:1)(-[#6]1:[#6]:[#6]:[#6]:[#6]:[#6]:1)-[#6](-[#6])-[#6]-[#7](-[#6])-[#6]',
            '2-[(dimethylamino)methyl]-1-(3-methoxyphenyl)cyclohexanol': '[#6]-[#7](-[#6])-[#6]-[#6]1-[#6]-[#6]-[#6]-[#6]-[#6]-1(-[#6]1:[#6]:[#6](:[#6]:[#6]:[#6]:1)-[#8]-[#6])-[#8]',
            'alfaxalone': '[#6]-[#6](=[#8])-[#6]1-[#6]-[#6]-[#6]2-[#6]-1(-[#6]-[#6](=[#8])-[#6]1-[#6]-2-[#6]-[#6]-[#6]2-[#6]-1(-[#6]-[#6]-[#6](-[#6]-2)-[#8])-[#6])-[#6]',
            'alprazolam': '[#6]-[#6]1:[#7]:[#7]:[#6]2:[#7]:1-[#6]1:[#6](:[#6]:[#6](:[#6]:[#6]:1)-[#17])-[#6](=[#7]-[#6]-2)-[#6]1:[#6]:[#6]:[#6]:[#6]:[#6]:1',
            'barbital': '[#6]-[#6]-[#6]1(-[#6](=[#8])-[#7]-[#6](=[#8])-[#7]-[#6]-1=[#8])-[#6]-[#6]',
            'brexanolone': '[#6]-[#6](=[#8])-[#6]1-[#6]-[#6]-[#6]2-[#6]-1(-[#6]-[#6]-[#6]1-[#6]-2-[#6]-[#6]-[#6]2-[#6]-1(-[#6]-[#6]-[#6](-[#6]-2)-[#8])-[#6])-[#6]',
            'bromazepam': '[#6]1-[#6](=[#8])-[#7]-[#6]2:[#6](:[#6]:[#6](:[#6]:[#6]:2)-[#35])-[#6](=[#7]-1)-[#6]1:[#6]:[#6]:[#6]:[#6]:[#7]:1',
            'camazepam': '[#6]-[#7]1-[#6]2:[#6](:[#6]:[#6](:[#6]:[#6]:2)-[#17])-[#6](=[#7]-[#6](-[#6]-1=[#8])-[#8]-[#6](=[#8])-[#7](-[#6])-[#6])-[#6]1:[#6]:[#6]:[#6]:[#6]:[#6]:1',
            'carisoprodol': '[#6]-[#6]-[#6]-[#6](-[#6])(-[#6]-[#8]-[#6](=[#8])-[#7])-[#6]-[#8]-[#6](=[#8])-[#7]-[#6](-[#6])-[#6]',
            'chloralbetaine': '[#6]-[#7+](-[#6])(-[#6])-[#6]-[#6](=[#8])-[#8-].[#6](-[#6](-[#17])(-[#17])-[#17])(-[#8])-[#8]',
            'chloralhydrate': '[#6](-[#6](-[#17])(-[#17])-[#17])(-[#8])-[#8]',
            'chlordiazepoxide': '[#6]-[#7]=[#6]1-[#6]-[#7](-[#6](=[#6]2:[#6]:[#6](:[#6]:[#6]:[#6]:2=[#7]-1)-[#17])-[#6]1:[#6]:[#6]:[#6]:[#6]:[#6]:1)-[#8]',
            'clobazam': '[#6]-[#7]1-[#6](=[#8])-[#6]-[#6](=[#8])-[#7](-[#6]2:[#6]-1:[#6]:[#6]:[#6](:[#6]:2)-[#17])-[#6]1:[#6]:[#6]:[#6]:[#6]:[#6]:1',
            'clonazepam': '[#6]1-[#6](=[#8])-[#7]-[#6]2:[#6](:[#6]:[#6](:[#6]:[#6]:2)-[#7+](=[#8])-[#8-])-[#6](=[#7]-1)-[#6]1:[#6]:[#6]:[#6]:[#6]:[#6]:1-[#17]',
            'clorazepate': '[#6]1:[#6]:[#6]:[#6](:[#6]:[#6]:1)-[#6]1=[#7]-[#6](-[#6](=[#8])-[#7]-[#6]2:[#6]-1:[#6]:[#6](:[#6]:[#6]:2)-[#17])-[#6](=[#8])-[#8]',
            'clotiazepam': '[#6]-[#6]-[#6]1:[#6]:[#6]2:[#6](:[#16]:1)-[#7](-[#6](=[#8])-[#6]-[#7]=[#6]-2-[#6]1:[#6]:[#6]:[#6]:[#6]:[#6]:1-[#17])-[#6]',
            'cloxazolam': '[#6]1-[#6]-[#8]-[#6]2(-[#7]-1-[#6]-[#6](=[#8])-[#7]-[#6]1:[#6]-2:[#6]:[#6](:[#6]:[#6]:1)-[#17])-[#6]1:[#6]:[#6]:[#6]:[#6]:[#6]:1-[#17]',
            'delorazepam': '[#6]1-[#6](=[#8])-[#7]-[#6]2:[#6](:[#6]:[#6](:[#6]:[#6]:2)-[#17])-[#6](=[#7]-1)-[#6]1:[#6]:[#6]:[#6]:[#6]:[#6]:1-[#17]',
            'diazepam': '[#6]-[#7]1-[#6](=[#8])-[#6]-[#7]=[#6](-[#6]2:[#6]-1:[#6]:[#6]:[#6](:[#6]:2)-[#17])-[#6]1:[#6]:[#6]:[#6]:[#6]:[#6]:1',
            'dichloralphenazone': '[#6]-[#6]1:[#6]:[#6](=[#8]):[#7](:[#7]:1-[#6])-[#6]1:[#6]:[#6]:[#6]:[#6]:[#6]:1.[#6](-[#6](-[#17])(-[#17])-[#17])(-[#8])-[#8].[#6](-[#6](-[#17])(-[#17])-[#17])(-[#8])-[#8]',
            'estazolam': '[#6]1-[#6]2:[#7]:[#7]:[#6]:[#7]:2-[#6]2:[#6](:[#6]:[#6](:[#6]:[#6]:2)-[#17])-[#6](=[#7]-1)-[#6]1:[#6]:[#6]:[#6]:[#6]:[#6]:1',
            'ethchlorvynol': '[#6]-[#6]-[#6](-[#6]=[#6]-[#17])(-[#6]#[#6])-[#8]',
            'ethinamate': '[#8]=[#6](-[#8]-[#6]1(-[#6]#[#6])-[#6]-[#6]-[#6]-[#6]-[#6]-1)-[#7]',
            'ethyl loflazepate': '[#6]-[#6]-[#8]-[#6](=[#8])-[#6]1-[#6](=[#8])-[#7]-[#6]2:[#6](:[#6]:[#6](:[#6]:[#6]:2)-[#17])-[#6](=[#7]-1)-[#6]1:[#6]:[#6]:[#6]:[#6]:[#6]:1-[#9]',
            'fludiazepam': '[#6]-[#7]1-[#6](=[#8])-[#6]-[#7]=[#6](-[#6]2:[#6]-1:[#6]:[#6]:[#6](:[#6]:2)-[#17])-[#6]1:[#6]:[#6]:[#6]:[#6]:[#6]:1-[#9]',
            'flunitrazepam': '[#6]-[#7]1-[#6](=[#8])-[#6]-[#7]=[#6](-[#6]2:[#6]-1:[#6]:[#6]:[#6](:[#6]:2)-[#7+](=[#8])-[#8-])-[#6]1:[#6]:[#6]:[#6]:[#6]:[#6]:1-[#9]',
            'flurazepam': '[#6]-[#6]-[#7](-[#6]-[#6])-[#6]-[#6]-[#7]1-[#6](=[#8])-[#6]-[#7]=[#6](-[#6]2:[#6]-1:[#6]:[#6]:[#6](:[#6]:2)-[#17])-[#6]1:[#6]:[#6]:[#6]:[#6]:[#6]:1-[#9]',
            'fospropofol': '[#6]-[#6](-[#6])-[#6]1:[#6](:[#6](:[#6]:[#6]:[#6]:1)-[#6](-[#6])-[#6])-[#8]-[#6]-[#8]-[#15](=[#8])(-[#8])-[#8]',
            'halazepam': '[#6]1-[#6](=[#8])-[#7](-[#6]2:[#6](:[#6]:[#6](:[#6]:[#6]:2)-[#17])-[#6](=[#7]-1)-[#6]1:[#6]:[#6]:[#6]:[#6]:[#6]:1)-[#6]-[#6](-[#9])(-[#9])-[#9]',
            'haloxazolam': '[#6]1-[#6]-[#8]-[#6]2(-[#7]-1-[#6]-[#6](=[#8])-[#7]-[#6]1:[#6]-2:[#6]:[#6](:[#6]:[#6]:1)-[#35])-[#6]1:[#6]:[#6]:[#6]:[#6]:[#6]:1-[#9]',
            'ketazolam': '[#6]-[#6]1=[#6]-[#6](=[#8])-[#7]2-[#6]-[#6](=[#8])-[#7](-[#6]3:[#6](-[#6]-2(-[#8]-1)-[#6]1:[#6]:[#6]:[#6]:[#6]:[#6]:1):[#6]:[#6](:[#6]:[#6]:3)-[#17])-[#6]',
            'lemborexant': '[#6]-[#6]1:[#7]:[#6](:[#7]:[#6]:[#6]:1-[#8]-[#6]-[#6]1(-[#6]-[#6]-1-[#6](=[#8])-[#7]-[#6]1:[#7]:[#6]:[#6](:[#6]:[#6]:1)-[#9])-[#6]1:[#6]:[#6](:[#6]:[#6]:[#6]:1)-[#9])-[#6]',
            'loprazolam': '[#6]-[#7]1-[#6]-[#6]-[#7](-[#6]-[#6]-1)-[#6]=[#6]1-[#6](=[#8])-[#7]2-[#6](=[#7]-1)-[#6]-[#7]=[#6](-[#6]1:[#6]-2:[#6]:[#6]:[#6](:[#6]:1)-[#7+](=[#8])-[#8-])-[#6]1:[#6]:[#6]:[#6]:[#6]:[#6]:1-[#17]',
            'lorazepam': '[#6]1:[#6]:[#6]:[#6](:[#6](:[#6]:1)-[#6]1=[#7]-[#6](-[#6](=[#8])-[#7]-[#6]2:[#6]-1:[#6]:[#6](:[#6]:[#6]:2)-[#17])-[#8])-[#17]',
            'lormetazepam': '[#6]-[#7]1-[#6]2:[#6](:[#6]:[#6](:[#6]:[#6]:2)-[#17])-[#6](=[#7]-[#6](-[#6]-1=[#8])-[#8])-[#6]1:[#6]:[#6]:[#6]:[#6]:[#6]:1-[#17]',
            'mebutamate': '[#6]-[#6]-[#6](-[#6])-[#6](-[#6])(-[#6]-[#8]-[#6](=[#8])-[#7])-[#6]-[#8]-[#6](=[#8])-[#7]',
            'medazepam': '[#6]-[#7]1-[#6]-[#6]-[#7]=[#6](-[#6]2:[#6]-1:[#6]:[#6]:[#6](:[#6]:2)-[#17])-[#6]1:[#6]:[#6]:[#6]:[#6]:[#6]:1',
            'meprobamate': '[#6]-[#6]-[#6]-[#6](-[#6])(-[#6]-[#8]-[#6](=[#8])-[#7])-[#6]-[#8]-[#6](=[#8])-[#7]',
            'methohexital': '[#6]-[#6]-[#6]#[#6]-[#6](-[#6])-[#6]1(-[#6](=[#8])-[#7]-[#6](=[#8])-[#7](-[#6]-1=[#8])-[#6])-[#6]-[#6]=[#6]',
            'methylphenobarbital': '[#6]-[#6]-[#6]1(-[#6](=[#8])-[#7]-[#6](=[#8])-[#7](-[#6]-1=[#8])-[#6])-[#6]1:[#6]:[#6]:[#6]:[#6]:[#6]:1',
            'midazolam': '[#6]-[#6]1:[#7]:[#6]:[#6]2:[#7]:1-[#6]1:[#6](:[#6]:[#6](:[#6]:[#6]:1)-[#17])-[#6](=[#7]-[#6]-2)-[#6]1:[#6]:[#6]:[#6]:[#6]:[#6]:1-[#9]',
            'nimetazepam': '[#6]-[#7]1-[#6](=[#8])-[#6]-[#7]=[#6](-[#6]2:[#6]-1:[#6]:[#6]:[#6](:[#6]:2)-[#7+](=[#8])-[#8-])-[#6]1:[#6]:[#6]:[#6]:[#6]:[#6]:1',
            'nitrazepam': '[#6]1-[#6](=[#8])-[#7]-[#6]2:[#6](:[#6]:[#6](:[#6]:[#6]:2)-[#7+](=[#8])-[#8-])-[#6](=[#7]-1)-[#6]1:[#6]:[#6]:[#6]:[#6]:[#6]:1',
            'nordiazepam': '[#6]1-[#6](=[#8])-[#7]-[#6]2:[#6](:[#6]:[#6](:[#6]:[#6]:2)-[#17])-[#6](=[#7]-1)-[#6]1:[#6]:[#6]:[#6]:[#6]:[#6]:1',
            'oxazepam': '[#6]1:[#6]:[#6]:[#6](:[#6]:[#6]:1)-[#6]1=[#7]-[#6](-[#6](=[#8])-[#7]-[#6]2:[#6]-1:[#6]:[#6](:[#6]:[#6]:2)-[#17])-[#8]',
            'oxazolam': '[#6]-[#6]1-[#6]-[#7]2-[#6]-[#6](=[#8])-[#7]-[#6]3:[#6](-[#6]-2(-[#8]-1)-[#6]1:[#6]:[#6]:[#6]:[#6]:[#6]:1):[#6]:[#6](:[#6]:[#6]:3)-[#17]',
            'paraldehyde': '[#6]-[#6]1-[#8]-[#6](-[#8]-[#6](-[#8]-1)-[#6])-[#6]',
            'petrichloral': '[#6](-[#6](-[#6]-[#8]-[#6](-[#6](-[#17])(-[#17])-[#17])-[#8])(-[#6]-[#8]-[#6](-[#6](-[#17])(-[#17])-[#17])-[#8])-[#6]-[#8]-[#6](-[#6](-[#17])(-[#17])-[#17])-[#8])-[#8]-[#6](-[#6](-[#17])(-[#17])-[#17])-[#8]',
            'phenobarbital': '[#6]-[#6]-[#6]1(-[#6](=[#8])-[#7]-[#6](=[#8])-[#7]-[#6]-1=[#8])-[#6]1:[#6]:[#6]:[#6]:[#6]:[#6]:1',
            'pinazepam': '[#6]#[#6]-[#6]-[#7]1-[#6](=[#8])-[#6]-[#7]=[#6](-[#6]2:[#6]-1:[#6]:[#6]:[#6](:[#6]:2)-[#17])-[#6]1:[#6]:[#6]:[#6]:[#6]:[#6]:1',
            'prazepam': '[#6]1-[#6]-[#6]-1-[#6]-[#7]1-[#6](=[#8])-[#6]-[#7]=[#6](-[#6]2:[#6]-1:[#6]:[#6]:[#6](:[#6]:2)-[#17])-[#6]1:[#6]:[#6]:[#6]:[#6]:[#6]:1',
            'quazepam': '[#6]1-[#6](=[#16])-[#7](-[#6]2:[#6](:[#6]:[#6](:[#6]:[#6]:2)-[#17])-[#6](=[#7]-1)-[#6]1:[#6]:[#6]:[#6]:[#6]:[#6]:1-[#9])-[#6]-[#6](-[#9])(-[#9])-[#9]',
            'remimazolam': '[#6]-[#6]1:[#6]:[#7]:[#6]2:[#7]:1-[#6]1:[#6](:[#6]:[#6](:[#6]:[#6]:1)-[#35])-[#6](=[#7]-[#6]-2-[#6]-[#6]-[#6](=[#8])-[#8]-[#6])-[#6]1:[#6]:[#6]:[#6]:[#6]:[#7]:1',
            'suvorexant': '[#6]-[#6]1-[#6]-[#6]-[#7](-[#6]-[#6]-[#7]-1-[#6](=[#8])-[#6]1:[#6](:[#6]:[#6]:[#6](:[#6]:1)-[#6])-[#7]1:[#7]:[#6]:[#6]:[#7]:1)-[#6]1:[#7]:[#6]2:[#6](:[#8]:1):[#6]:[#6]:[#6](:[#6]:2)-[#17]',
            'temazepam': '[#6]-[#7]1-[#6]2:[#6](:[#6]:[#6](:[#6]:[#6]:2)-[#17])-[#6](=[#7]-[#6](-[#6]-1=[#8])-[#8])-[#6]1:[#6]:[#6]:[#6]:[#6]:[#6]:1',
            'tetrazepam': '[#6]-[#7]1-[#6](=[#8])-[#6]-[#7]=[#6](-[#6]2:[#6]-1:[#6]:[#6]:[#6](:[#6]:2)-[#17])-[#6]1=[#6]-[#6]-[#6]-[#6]-[#6]-1',
            'triazolam': '[#6]-[#6]1:[#7]:[#7]:[#6]2:[#7]:1-[#6]1:[#6](:[#6]:[#6](:[#6]:[#6]:1)-[#17])-[#6](=[#7]-[#6]-2)-[#6]1:[#6]:[#6]:[#6]:[#6]:[#6]:1-[#17]',
            'zaleplon': '[#6]-[#6]-[#7](-[#6]1:[#6]:[#6]:[#6]:[#6](:[#6]:1)-[#6]1:[#6]:[#6]:[#7]:[#6]2:[#6](:[#6]:[#7]:[#7]:1:2)-[#6]#[#7])-[#6](=[#8])-[#6]',
            'zolpidem': '[#6]-[#6]1:[#6]:[#6]:[#6](:[#6]:[#6]:1)-[#6]1:[#6](:[#7]2:[#6]:[#6](:[#6]:[#6]:[#6]:2:[#7]:1)-[#6])-[#6]-[#6](=[#8])-[#7](-[#6])-[#6]',
            'zopiclone': '[#6]-[#7]1-[#6]-[#6]-[#7](-[#6]-[#6]-1)-[#6](=[#8])-[#8]-[#6]1-[#6]2:[#7]:[#6]:[#6]:[#7]:[#6]:2-[#6](=[#8])-[#7]-1-[#6]1:[#7]:[#6]:[#6](:[#6]:[#6]:1)-[#17]',
            'fenfluramine': '[#6]-[#6]-[#7]-[#6](-[#6])-[#6]-[#6]1:[#6]:[#6](:[#6]:[#6]:[#6]:1)-[#6](-[#9])(-[#9])-[#9]',
            'lorcaserin': '[#6]-[#6]1-[#6]-[#7]-[#6]-[#6]-[#6]2:[#6]-1:[#6]:[#6](:[#6]:[#6]:2)-[#17]',
            '(+)-norpseudoephedrine': '[#6]-[#6](-[#6](-[#6]1:[#6]:[#6]:[#6]:[#6]:[#6]:1)-[#8])-[#7]',
            'diethylpropion': '[#6]-[#6]-[#7](-[#6]-[#6])-[#6](-[#6])-[#6](=[#8])-[#6]1:[#6]:[#6]:[#6]:[#6]:[#6]:1',
            'fencamfamin': '[#6]-[#6]-[#7]-[#6]1-[#6]2-[#6]-[#6]-[#6](-[#6]-2)-[#6]-1-[#6]1:[#6]:[#6]:[#6]:[#6]:[#6]:1',
            'fenproporex': '[#6]-[#6](-[#6]-[#6]1:[#6]:[#6]:[#6]:[#6]:[#6]:1)-[#7]-[#6]-[#6]-[#6]#[#7]',
            'mazindol': '[#6]1-[#6]-[#7]2-[#6](=[#7]-1)-[#6]1:[#6]:[#6]:[#6]:[#6]:[#6]:1-[#6]-2(-[#6]1:[#6]:[#6]:[#6](:[#6]:[#6]:1)-[#17])-[#8]',
            'mefenorex': '[#6]-[#6](-[#6]-[#6]1:[#6]:[#6]:[#6]:[#6]:[#6]:1)-[#7]-[#6]-[#6]-[#6]-[#17]',
            'pemoline': '[#6]1:[#6]:[#6]:[#6](:[#6]:[#6]:1)-[#6]1-[#6](=[#8])-[#7]=[#6](-[#8]-1)-[#7]',
            'phentermine': '[#6]-[#6](-[#6])(-[#6]-[#6]1:[#6]:[#6]:[#6]:[#6]:[#6]:1)-[#7]',
            'pipradrol': '[#6]1-[#6]-[#6]-[#7]-[#6](-[#6]-1)-[#6](-[#6]1:[#6]:[#6]:[#6]:[#6]:[#6]:1)(-[#6]1:[#6]:[#6]:[#6]:[#6]:[#6]:1)-[#8]',
            'serdexmethylphenidate': '[#6]-[#8]-[#6](=[#8])-[#6](-[#6]1-[#6]-[#6]-[#6]-[#6]-[#7]-1-[#6](=[#8])-[#8]-[#6]-[#7+]1:[#6]:[#6]:[#6]:[#6](:[#6]:1)-[#6](=[#8])-[#7]-[#6](-[#6]-[#8])-[#6](=[#8])-[#8-])-[#6]1:[#6]:[#6]:[#6]:[#6]:[#6]:1',
            'sibutramine': '[#6]-[#6](-[#6])-[#6]-[#6](-[#6]1(-[#6]-[#6]-[#6]-1)-[#6]1:[#6]:[#6]:[#6](:[#6]:[#6]:1)-[#17])-[#7](-[#6])-[#6]',
            'solriamfetol': '[#6]1:[#6]:[#6]:[#6](:[#6]:[#6]:1)-[#6]-[#6](-[#6]-[#8]-[#6](=[#8])-[#7])-[#7]',
            'spa((-)-1-dimethylamino-1,2-diphenylethane)': '[#6]-[#7](-[#6])-[#6](-[#6]-[#6]1:[#6]:[#6]:[#6]:[#6]:[#6]:1)-[#6]1:[#6]:[#6]:[#6]:[#6]:[#6]:1',
            'pentazocine': '[#6]-[#6]1-[#6]2-[#6]-[#6]3:[#6](-[#6]-1(-[#6]-[#6]-[#7]-2-[#6]-[#6]=[#6](-[#6])-[#6])-[#6]):[#6]:[#6](:[#6]:[#6]:3)-[#8]',
            'butorphanol': '[#6]1-[#6]-[#6]-[#6]2(-[#6]3-[#6]-[#6]4:[#6](-[#6]-2(-[#6]-1)-[#6]-[#6]-[#7]-3-[#6]-[#6]1-[#6]-[#6]-[#6]-1):[#6]:[#6](:[#6]:[#6]:4)-[#8])-[#8]',
        }

        return smarts