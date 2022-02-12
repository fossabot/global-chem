#!/usr/bin/env python3
#
# GlobalChem - IUPAC Blue Book
#
# -----------------------------------

class IUPACBlueBook(object):

    def __init__(self):

        pass

    @staticmethod
    def get_smiles():

        smiles = {
            'acetamido': 'O=C(N)C',
            'acetoacetyl': 'O=C(C)CC(=O)O',
            'acetyl': 'C(C)=O',
            'acryloyl': 'C=CC(C)=O',
            'alanyl': 'N[CH](C)C(C)=O',
            'beta-alanyl': 'NCCC(C)=O',
            'allyl': '[CH2]C=C',
            'allylidene': '[CH]C=C',
            'amidino': 'NC=N',
            'amino': 'N',
            'amyl': '[CH2]CCCC',
            'anilino': 'NC1=CC=CC=C1',
            'anisidino': 'NC1=CC=C(OC)C=C1',
            'anthranoyl': 'NC1=CC=CC=C1[C](C)=O',
            'arsino': '[AsH3]',
            'azelaoyl': 'O=CCCCCCCCC=O',
            'azido': '[N]=[N+]=[N-]',
            'azo': 'C/N=N/C',
            'azoxy': 'C/N=[N+]([O-])/C',
            'benzal': '[CH]C1=CC=CC=C1',
            'benzamido': 'O=C(N)C1=CC=CC=C1',
            'benzhydrol': 'OC(C1=CC=CC=C1)C2=CC=CC=C2',
            'benzoxy': '[O]CC1=CC=CC=C1',
            'benzoyl': 'O=[C]C1=CC=CC=C1',
            'benzyl': '[CH2]C1=CC=CC=C1',
            'benzylidene': '[CH]C1=CC=CC=C1',
            'benzylidyne': '[C]C1=CC=CC=C1',
            'biphenylyl': 'C1(C2=CC=CC=C2)=CC=CC=[C]1',
            'biphenylene': 'C12=C3C=CC=CC3=C1C=CC=C2',
            'butoxy': '[O]CCCC',
            'sec-butoxy': '[O]C(C)CC',
            'tert-butoxy': '[O]C(C)(C)C',
            'butyl': '[CH2]CCC',
            'sec-butyl': 'CC[CH]C',
            'tert-butyl': 'C[C](C)C',
            'butyryl': 'O=[C]CCC',
            'caproyl': 'CCCCC[C]=O',
            'capryl': 'CCCCCCCC',
            'capryloyl': 'CCCCCCC[C]=O',
            'carbamido': 'C(=O)(N)N',
            'carbamoyl': 'N[C]=O',
            'carbamyl': 'N[C]=O',
            'carbazoyl': 'NN[C]=O',
            'carbethoxy': 'O=[C]OCC',
            'carbonyl': '[CH]=O',
            'carboxy': 'O=[C]O',
            'cetyl': '[CH2]CCCCCCCCCCCCCCC',
            'chloroformyl': 'O=[C]Cl',
            'cinnamoyl': 'O=[C]C=CC1=CC=CC=C1',
            'cinnamyl': '[CH2]C=CC1=CC=CC=C1',
            'cinnamylidene': '[CH]C=CC1=CC=CC=C1',
            'cresyl': 'OC1=CC=C(C)C=C1',
            'crotonoyl': 'C/C=C/[C]=O',
            'crotyl': '[CH2]/C=C/C',
            'cyanamido': '[NH]C#N',
            'cyanato': '[O]C#N',
            'cyano': '[C]#N',
            'decanedioyl': 'O=[C]CCCCCCCC[C]=O',
            'decanoyl': 'CCCCCCCCC[C]=O',
            'diazo': '[N+]=[N-]',
            'diazoamino': 'N=NN',
            'disilanyl': '[SiH2][SiH3]',
            'disiloxanyloxy': '[O][SiH2]O[SiH3]',
            'disulfinyl': 'O=[S]S=O',
            'dithio': '[S]S',
            'enanthoyl': 'CCCCCC[C]=O',
            'epoxy': '[O]',
            'ethenyl': '[CH]=C',
            'ethynyl': '[C]#C',
            'ethoxy': '[O]CC',
            'ethyl': '[CH2]C',
            'ethylene': 'C=C',
            'ethylidene': '[CH]C',
            'ethylthio': '[S]CC',
            'formamido': 'O=C[NH]',
            'formyl': '[CH]=O',
            'furmaroyl': 'O=CO',
            'furfuryl': '[CH2]C1=CC=CO1',
            'furfurylidene': '[CH]C1=CC=CO1',
            'glutamoyl': 'N[C@@H](CC[C]=O)[C]=O',
            'glutaryl': 'O=[C]CCC[C]=O',
            'glycylamino': '[NH]C(CN)=O',
            'glycoloyl': 'OC[C]=O',
            'glycyl': 'NC[C]=O',
            'glyoxyoyl': 'O=[C]C=O',
            'guanidino': '[NH]C(N)=N',
            'guanyl': 'N=[C]N',
            'heptadecanoyl': 'CCCCCCCCCCCCCCCC[C]=O',
            'heptanamido': 'CCCCCCC([NH])=O',
            'heptanoyl': 'CCCCCC[C]=O.CCCCCCC([NH])=O',
            'hexadecanoyl': 'CCCCCCCCCCCCCCC[C]=O.CCCCCC[C]=O.CCCCCCC([NH])=O',
            'hexamethylene': 'CCCCCC',
            'hexanedioyl': 'O=[C]CCCC[C]=O',
            'hippuryl': '[CH2]CNC(C1=CC=CC=C1)=O',
            'hydrazino': 'N[NH]',
            'hydrazo': 'NN',
            'hydrocinnamoyl': 'O=[C]CCC1=CC=CC=C1',
            'hydroperoxy': '[O]O',
            'hydroxyamino': '[NH]O',
            'imino': '[NH]',
            'iodoso': 'I=O',
            'iodyl': 'O=I=O',
            'isoamyl': '[CH2]CC(C)C',
            'isobutenyl': '[CH]=C(C)C',
            'isobutoxy': '[O]CC(C)C',
            'isobutyl': '[CH2]C(C)C',
            'isobutylidene': '[CH]C(C)C',
            'isobutyryl': 'O=[C]C(C)C',
            'isocyanato': '[N]=C=O',
            'isocyano': '[N+]#[C-]',
            'isohexyl': '[CH2]CCC(C)C',
            'isoleucyl': 'N[C@@H]([C@@H](C)CC)[C]=O',
            'isonitroso': '[N]O',
            'isopentyl': '[CH2]CC(C)C',
            'isopentylidene': '[CH]CC(C)C',
            'isopropenyl': 'C=[C]C',
            'isopropoxy': '[O]C(C)C',
            'isopropyl': 'C[CH]C',
            'isopropylidene': 'C[C]C',
            'isothiocynato': 'N=C=S',
            'isovaleryl': 'O=[C]CC(C)C',
            'lactoyl': 'OC(C)[C]=O',
            'lauroyl': 'CCCCCCCCCCC[C]=O',
            'lauryl': '[CH2]CCCCCCCCCCC',
            'leucyl': 'N[C@@H](CC(C)C)[C]=O',
            'levulinoyl': 'O=C(C)CC[C]=O',
            'malonyl': 'O=[C]C[C]=O',
            'mandeloyl': 'OC(C1=CC=CC=C1)[C]=O',
            'mercapto': '[SH]',
            'mesityl': 'CC1=CC(C)=CC(C)=[C]1',
            'methacryloyl': 'CC([C]=O)=C',
            'methallyl': '[CH2]C(C)=C',
            'methionyl': 'N[C@@H](CCSC)[C]=O',
            'methoxy': '[O]C',
            'methyl': '[CH3]',
            'methylene': '[CH2]',
            'methylthio': '[S]C',
            'myristoyl': 'CCCCCCCCCCCCC[C]=O',
            'myristyl': '[CH2]CCCCCCCCCCCCC',
            'naphthyl': 'C12=CC=C[C]=C1C=CC=C2',
            'naphthylene': 'C12=CC=CC=C1C=CC=C2',
            'neopentyl': '[CH2]C(C)(C)C',
            'nitramino': '[NH][N+]([O-])=O',
            'nitro': 'O=[N+][O-]',
            'nitrosamino': '[NH]N=O',
            'nitroso': '[N]=O',
            'nonanoyl': 'CCCCCCCC[C]=O',
            'oleoyl': 'CCCCCCCC/C=C\CCCCCCC[C]=O',
            'oxalyl': 'O=[C]C=O',
            'oxo': '[O]',
            'palmitoyl': 'CCCCCCCCCCCCCCC[C]=O',
            'pentamethylene': 'O=C1C(C=C)[C@@]2([H])SCCN12',
            'pentyl': '[CH2]CCCC',
            'tert-pentyl': 'CC[C](C)C',
            'phenacyl': '[CH2]C(C1=CC=CC=C1)=O',
            'phenacylidene': '[CH]C(C1=CC=CC=C1)=O',
            'phenethyl': '[CH2]CC1=CC=CC=C1',
            'phenoxy': '[O]C1=CC=CC=C1',
            'phenyl': '[C]1=CC=CC=C1',
            'phenylene': 'C1=C[C]=CC=[C]1',
            'phosphino': '[PH2]',
            'phosphinyl': '[PH2]=O',
            'phospho': 'O=[P](O)O',
            'phosphono': 'O=[P](O)O',
            'phthaloyl': 'O=[C]C1=CC=CC=C1[C]=O',
            'picryl': '[O-][N+](C1=CC([N+]([O-])=O)=CC([N+]([O-])=O)=[C]1)=O',
            'pimeloyl': 'O=[C]CCCCC[C]=O',
            'piperidino': '[N]1CCCCC1',
            'pivaloyl': 'CC(C)(C)[C]=O',
            'prenyl': '[CH2]/C=C(C)\C',
            'propargyl': '[CH2]C#C',
            '1-propenyl': '[CH]=CC',
            '2-propenyl': '[CH2]C=C',
            'propionyl': 'O=[C]CC',
            'propoxy': '[O]CCC',
            'propyl': '[CH2]CC',
            'propylidene': '[CH]CC',
            'pyrryl': 'N1[C]=CC=C1',
            'salicyloyl': 'OC1=CC=CC=C1[C]=O',
            'selenyl': '[SeH]',
            'seryl': 'N[C@@H](CO)[C]=O',
            'siloxy': '[O][SiH3]',
            'silyl': '[SiH3]',
            'silyene': '[SiH2]',
            'sorboyl': 'CC=CC=CC(O)=O',
            'stearoyl': 'CCCCCCCCCCCCCCCCC[C]=O',
            'stearyl': '[CH2]CCCCCCCCCCCCCCCCC',
            'styryl': '[CH]=CC1=CC=CC=C1',
            'suberoyl': 'O=[C]CCCCCC[C]=O',
            'succinyl': 'O=[C]CC[C]=O',
            'sulfamino': '[NH]S(=O)(O)=O',
            'sulfamoyl': 'O=[S](N)=O',
            'sulfanilyl': 'O=[S](C1=CC=C(N)C=C1)=O',
            'sulfeno': '[S]O',
            'sulfhydryl': '[SH]',
            'sulfinyl': 'S=O',
            'sulfo': 'O=[S](O)=O',
            'sulfonyl': 'O=S=O',
            'terephthaloyl': 'O=[C]C1=CC=C([C]=O)C=C1',
            'tetramethylene': 'CCCC',
            'thienyl': '[C]1=CC=CS1',
            'thiocarbonyl': '[CH]=S',
            'thiocarboxy': 'S=[C]O',
            'thiocyanato': '[S]C#N',
            'thionyl': 'S=O',
            'threonyl': 'N[C@@H]([C@H](O)C)[C]=O',
            'toluidino': '[NH]C1=CC=C(C)C=C1',
            'toluoyl': 'CC1=CC=C([C]=O)C=C1',
            'tolyl': 'CC1=CC=[C]C=C1',
            'alpha-tolyl': '[C]C1=CC=CC=C1',
            'tolylene': '[CH]C1=CC=CC=C1',
            'tosyl': 'O=[S](C1=CC=C(C)C=C1)=O',
            'triazano': '[NH]N[NH]',
            'trimethylene': 'CCC',
            'trityl': '[C](C1=CC=CC=C1)(C2=CC=CC=C2)C3=CC=CC=C3',
            'valeryl': 'O=[C]CCCC',
            'valyl': 'N[C@@H](C(C)C)[C]=O',
            'vinyl': '[CH]=C',
            'vinylidene': '[C]=C',
            'xylidino': '[NH]C1=CC=C(C)C=C1C',
            'xylyl': 'CC1=CC=[C]C(C)=C1',
            'xylylene': 'NCC1=CC=CC(CN)=C1',
        }

        return smiles

    @staticmethod
    def get_smarts():

        smarts = {
            'acetamido':'[#8]=[#6](-[#7])-[#6]',
            'acetoacetyl':'[#8]=[#6](-[#6])-[#6]-[#6](=[#8])-[#8]',
            'acetyl':'[#6](-[#6])=[#8]',
            'acryloyl':'[#6]=[#6]-[#6](-[#6])=[#8]',
            'alanyl':'[#7]-[#6H](-[#6])-[#6](-[#6])=[#8]',
            'beta-alanyl':'[#7]-[#6]-[#6]-[#6](-[#6])=[#8]',
            'allyl':'[#6H2]-[#6]=[#6]',
            'allylidene':'[#6H]-[#6]=[#6]',
            'amidino':'[#7]-[#6]=[#7]',
            'amino':'[#7]',
            'amyl':'[#6H2]-[#6]-[#6]-[#6]-[#6]',
            'anilino':'[#7]-[#6]1:[#6]:[#6]:[#6]:[#6]:[#6]:1',
            'anisidino':'[#7]-[#6]1:[#6]:[#6]:[#6](-[#8]-[#6]):[#6]:[#6]:1',
            'anthranoyl':'[#7]-[#6]1:[#6]:[#6]:[#6]:[#6]:[#6]:1-[#6](-[#6])=[#8]',
            'arsino':'[AsH3]',
            'azelaoyl':'[#8]=[#6]-[#6]-[#6]-[#6]-[#6]-[#6]-[#6]-[#6]-[#6]=[#8]',
            'azido':'[#7]=[#7+]=[#7-]',
            'azo':'[#6]/[#7]=[#7]/[#6]',
            'azoxy':'[#6]/[#7]=[#7+](\[#8-])-[#6]',
            'benzal':'[#6H]-[#6]1:[#6]:[#6]:[#6]:[#6]:[#6]:1',
            'benzamido':'[#8]=[#6](-[#7])-[#6]1:[#6]:[#6]:[#6]:[#6]:[#6]:1',
            'benzhydrol':'[#8]-[#6](-[#6]1:[#6]:[#6]:[#6]:[#6]:[#6]:1)-[#6]1:[#6]:[#6]:[#6]:[#6]:[#6]:1',
            'benzoxy':'[#8]-[#6]-[#6]1:[#6]:[#6]:[#6]:[#6]:[#6]:1',
            'benzoyl':'[#8]=[#6]-[#6]1:[#6]:[#6]:[#6]:[#6]:[#6]:1',
            'benzyl':'[#6H2]-[#6]1:[#6]:[#6]:[#6]:[#6]:[#6]:1',
            'benzylidene':'[#6H]-[#6]1:[#6]:[#6]:[#6]:[#6]:[#6]:1',
            'benzylidyne':'[#6]-[#6]1:[#6]:[#6]:[#6]:[#6]:[#6]:1',
            'biphenylyl':'[#6]1(-[#6]2:[#6]:[#6]:[#6]:[#6]:[#6]:2):[#6]:[#6]:[#6]:[#6]:[#6]:1',
            'biphenylene':'[#6]12=[#6]3:[#6]:[#6]:[#6]:[#6]:[#6]:3=[#6]:1:[#6]:[#6]:[#6]:[#6]:2',
            'butoxy':'[#8]-[#6]-[#6]-[#6]-[#6]',
            'sec-butoxy':'[#8]-[#6](-[#6])-[#6]-[#6]',
            'tert-butoxy':'[#8]-[#6](-[#6])(-[#6])-[#6]',
            'butyl':'[#6H2]-[#6]-[#6]-[#6]',
            'sec-butyl':'[#6]-[#6]-[#6H]-[#6]',
            'tert-butyl':'[#6]-[#6](-[#6])-[#6]',
            'butyryl':'[#8]=[#6]-[#6]-[#6]-[#6]',
            'caproyl':'[#6]-[#6]-[#6]-[#6]-[#6]-[#6]=[#8]',
            'capryl':'[#6]-[#6]-[#6]-[#6]-[#6]-[#6]-[#6]-[#6]',
            'capryloyl':'[#6]-[#6]-[#6]-[#6]-[#6]-[#6]-[#6]-[#6]=[#8]',
            'carbamido':'[#6](=[#8])(-[#7])-[#7]',
            'carbamoyl':'[#7]-[#6]=[#8]',
            'carbamyl':'[#7]-[#6]=[#8]',
            'carbazoyl':'[#7]-[#7]-[#6]=[#8]',
            'carbethoxy':'[#8]=[#6]-[#8]-[#6]-[#6]',
            'carbonyl':'[#6H]=[#8]',
            'carboxy':'[#8]=[#6]-[#8]',
            'cetyl':'[#6H2]-[#6]-[#6]-[#6]-[#6]-[#6]-[#6]-[#6]-[#6]-[#6]-[#6]-[#6]-[#6]-[#6]-[#6]-[#6]',
            'chloroformyl':'[#8]=[#6]-[#17]',
            'cinnamoyl':'[#8]=[#6]-[#6]=[#6]-[#6]1:[#6]:[#6]:[#6]:[#6]:[#6]:1',
            'cinnamyl':'[#6H2]-[#6]=[#6]-[#6]1:[#6]:[#6]:[#6]:[#6]:[#6]:1',
            'cinnamylidene':'[#6H]-[#6]=[#6]-[#6]1:[#6]:[#6]:[#6]:[#6]:[#6]:1',
            'cresyl':'[#8]-[#6]1:[#6]:[#6]:[#6](-[#6]):[#6]:[#6]:1',
            'crotonoyl':'[#6]/[#6]=[#6]/[#6]=[#8]',
            'crotyl':'[#6H2]/[#6]=[#6]/[#6]',
            'cyanamido':'[#7H]-[#6]#[#7]',
            'cyanato':'[#8]-[#6]#[#7]',
            'cyano':'[#6]#[#7]',
            'decanedioyl':'[#8]=[#6]-[#6]-[#6]-[#6]-[#6]-[#6]-[#6]-[#6]-[#6]-[#6]=[#8]',
            'decanoyl':'[#6]-[#6]-[#6]-[#6]-[#6]-[#6]-[#6]-[#6]-[#6]-[#6]=[#8]',
            'diazo':'[#7+]=[#7-]',
            'diazoamino':'[#7]=[#7]-[#7]',
            'disilanyl':'[SiH2]-[SiH3]',
            'disiloxanyloxy':'[#8]-[SiH2]-[#8]-[SiH3]',
            'disulfinyl':'[#8]=[#16]-[#16]=[#8]',
            'dithio':'[#16]-[#16]',
            'enanthoyl':'[#6]-[#6]-[#6]-[#6]-[#6]-[#6]-[#6]=[#8]',
            'epoxy':'[#8]',
            'ethenyl':'[#6H]=[#6]',
            'ethynyl':'[#6]#[#6]',
            'ethoxy':'[#8]-[#6]-[#6]',
            'ethyl':'[#6H2]-[#6]',
            'ethylene':'[#6]=[#6]',
            'ethylidene':'[#6H]-[#6]',
            'ethylthio':'[#16]-[#6]-[#6]',
            'formamido':'[#8]=[#6]-[#7H]',
            'formyl':'[#6H]=[#8]',
            'furmaroyl':'[#8]=[#6]-[#8]',
            'furfuryl':'[#6H2]-[#6]1:[#6]:[#6]:[#6]:[#8]:1',
            'furfurylidene':'[#6H]-[#6]1:[#6]:[#6]:[#6]:[#8]:1',
            'glutamoyl':'[#7]-[#6@@H](-[#6]-[#6]-[#6]=[#8])-[#6]=[#8]',
            'glutaryl':'[#8]=[#6]-[#6]-[#6]-[#6]-[#6]=[#8]',
            'glycylamino':'[#7H]-[#6](-[#6]-[#7])=[#8]',
            'glycoloyl':'[#8]-[#6]-[#6]=[#8]',
            'glycyl':'[#7]-[#6]-[#6]=[#8]',
            'glyoxyoyl':'[#8]=[#6]-[#6]=[#8]',
            'guanidino':'[#7H]-[#6](-[#7])=[#7]',
            'guanyl':'[#7]=[#6]-[#7]',
            'heptadecanoyl':'[#6]-[#6]-[#6]-[#6]-[#6]-[#6]-[#6]-[#6]-[#6]-[#6]-[#6]-[#6]-[#6]-[#6]-[#6]-[#6]-[#6]=[#8]',
            'heptanamido':'[#6]-[#6]-[#6]-[#6]-[#6]-[#6]-[#6](-[#7H])=[#8]',
            'heptanoyl':'[#6]-[#6]-[#6]-[#6]-[#6]-[#6]-[#6]=[#8].[#6]-[#6]-[#6]-[#6]-[#6]-[#6]-[#6](-[#7H])=[#8]',
            'hexadecanoyl':'[#6]-[#6]-[#6]-[#6]-[#6]-[#6]-[#6]-[#6]-[#6]-[#6]-[#6]-[#6]-[#6]-[#6]-[#6]-[#6]=[#8].[#6]-[#6]-[#6]-[#6]-[#6]-[#6]-[#6]=[#8].[#6]-[#6]-[#6]-[#6]-[#6]-[#6]-[#6](-[#7H])=[#8]',
            'hexamethylene':'[#6]-[#6]-[#6]-[#6]-[#6]-[#6]',
            'hexanedioyl':'[#8]=[#6]-[#6]-[#6]-[#6]-[#6]-[#6]=[#8]',
            'hippuryl':'[#6H2]-[#6]-[#7]-[#6](-[#6]1:[#6]:[#6]:[#6]:[#6]:[#6]:1)=[#8]',
            'hydrazino':'[#7]-[#7H]',
            'hydrazo':'[#7]-[#7]',
            'hydrocinnamoyl':'[#8]=[#6]-[#6]-[#6]-[#6]1:[#6]:[#6]:[#6]:[#6]:[#6]:1',
            'hydroperoxy':'[#8]-[#8]',
            'hydroxyamino':'[#7H]-[#8]',
            'imino':'[#7H]',
            'iodoso':'[#53]=[#8]',
            'iodyl':'[#8]=[#53]=[#8]',
            'isoamyl':'[#6H2]-[#6]-[#6](-[#6])-[#6]',
            'isobutenyl':'[#6H]=[#6](-[#6])-[#6]',
            'isobutoxy':'[#8]-[#6]-[#6](-[#6])-[#6]',
            'isobutyl':'[#6H2]-[#6](-[#6])-[#6]',
            'isobutylidene':'[#6H]-[#6](-[#6])-[#6]',
            'isobutyryl':'[#8]=[#6]-[#6](-[#6])-[#6]',
            'isocyanato':'[#7]=[#6]=[#8]',
            'isocyano':'[#7+]#[#6-]',
            'isohexyl':'[#6H2]-[#6]-[#6]-[#6](-[#6])-[#6]',
            'isoleucyl':'[#7]-[#6@@H](-[#6@@H](-[#6])-[#6]-[#6])-[#6]=[#8]',
            'isonitroso':'[#7]-[#8]',
            'isopentyl':'[#6H2]-[#6]-[#6](-[#6])-[#6]',
            'isopentylidene':'[#6H]-[#6]-[#6](-[#6])-[#6]',
            'isopropenyl':'[#6]=[#6]-[#6]',
            'isopropoxy':'[#8]-[#6](-[#6])-[#6]',
            'isopropyl':'[#6]-[#6H]-[#6]',
            'isopropylidene':'[#6]-[#6]-[#6]',
            'isothiocynato':'[#7]=[#6]=[#16]',
            'isovaleryl':'[#8]=[#6]-[#6]-[#6](-[#6])-[#6]',
            'lactoyl':'[#8]-[#6](-[#6])-[#6]=[#8]',
            'lauroyl':'[#6]-[#6]-[#6]-[#6]-[#6]-[#6]-[#6]-[#6]-[#6]-[#6]-[#6]-[#6]=[#8]',
            'lauryl':'[#6H2]-[#6]-[#6]-[#6]-[#6]-[#6]-[#6]-[#6]-[#6]-[#6]-[#6]-[#6]',
            'leucyl':'[#7]-[#6@@H](-[#6]-[#6](-[#6])-[#6])-[#6]=[#8]',
            'levulinoyl':'[#8]=[#6](-[#6])-[#6]-[#6]-[#6]=[#8]',
            'malonyl':'[#8]=[#6]-[#6]-[#6]=[#8]',
            'mandeloyl':'[#8]-[#6](-[#6]1:[#6]:[#6]:[#6]:[#6]:[#6]:1)-[#6]=[#8]',
            'mercapto':'[#16H]',
            'mesityl':'[#6]-[#6]1:[#6]:[#6](-[#6]):[#6]:[#6](-[#6]):[#6]:1',
            'methacryloyl':'[#6]-[#6](-[#6]=[#8])=[#6]',
            'methallyl':'[#6H2]-[#6](-[#6])=[#6]',
            'methionyl':'[#7]-[#6@@H](-[#6]-[#6]-[#16]-[#6])-[#6]=[#8]',
            'methoxy':'[#8]-[#6]',
            'methyl':'[#6H3]',
            'methylene':'[#6H2]',
            'methylthio':'[#16]-[#6]',
            'myristoyl':'[#6]-[#6]-[#6]-[#6]-[#6]-[#6]-[#6]-[#6]-[#6]-[#6]-[#6]-[#6]-[#6]-[#6]=[#8]',
            'myristyl':'[#6H2]-[#6]-[#6]-[#6]-[#6]-[#6]-[#6]-[#6]-[#6]-[#6]-[#6]-[#6]-[#6]-[#6]',
            'naphthyl':'[#6]12:[#6]:[#6]:[#6]:[#6]:[#6]:1:[#6]:[#6]:[#6]:[#6]:2',
            'naphthylene':'[#6]12:[#6]:[#6]:[#6]:[#6]:[#6]:1:[#6]:[#6]:[#6]:[#6]:2',
            'neopentyl':'[#6H2]-[#6](-[#6])(-[#6])-[#6]',
            'nitramino':'[#7H]-[#7+](-[#8-])=[#8]',
            'nitro':'[#8]=[#7+]-[#8-]',
            'nitrosamino':'[#7H]-[#7]=[#8]',
            'nitroso':'[#7]=[#8]',
            'nonanoyl':'[#6]-[#6]-[#6]-[#6]-[#6]-[#6]-[#6]-[#6]-[#6]=[#8]',
            'oleoyl':'[#6]-[#6]-[#6]-[#6]-[#6]-[#6]-[#6]-[#6]/[#6]=[#6]\[#6]-[#6]-[#6]-[#6]-[#6]-[#6]-[#6]-[#6]=[#8]',
            'oxalyl':'[#8]=[#6]-[#6]=[#8]',
            'oxo':'[#8]',
            'palmitoyl':'[#6]-[#6]-[#6]-[#6]-[#6]-[#6]-[#6]-[#6]-[#6]-[#6]-[#6]-[#6]-[#6]-[#6]-[#6]-[#6]=[#8]',
            'pentamethylene':'[#8]=[#6]1-[#6](-[#6]=[#6])-[#6@H]2-[#16]-[#6]-[#6]-[#7]-1-2',
            'pentyl':'[#6H2]-[#6]-[#6]-[#6]-[#6]',
            'tert-pentyl':'[#6]-[#6]-[#6](-[#6])-[#6]',
            'phenacyl':'[#6H2]-[#6](-[#6]1:[#6]:[#6]:[#6]:[#6]:[#6]:1)=[#8]',
            'phenacylidene':'[#6H]-[#6](-[#6]1:[#6]:[#6]:[#6]:[#6]:[#6]:1)=[#8]',
            'phenethyl':'[#6H2]-[#6]-[#6]1:[#6]:[#6]:[#6]:[#6]:[#6]:1',
            'phenoxy':'[#8]-[#6]1:[#6]:[#6]:[#6]:[#6]:[#6]:1',
            'phenyl':'[#6]1:[#6]:[#6]:[#6]:[#6]:[#6]:1',
            'phenylene':'[#6]1:[#6]:[#6]:[#6]:[#6]:[#6]:1',
            'phosphino':'[#15H2]',
            'phosphinyl':'[#15H2]=[#8]',
            'phospho':'[#8]=[#15](-[#8])-[#8]',
            'phosphono':'[#8]=[#15](-[#8])-[#8]',
            'phthaloyl':'[#8]=[#6]-[#6]1:[#6]:[#6]:[#6]:[#6]:[#6]:1-[#6]=[#8]',
            'picryl':'[#8-]-[#7+](-[#6]1:[#6]:[#6](-[#7+](-[#8-])=[#8]):[#6]:[#6](-[#7+](-[#8-])=[#8]):[#6]:1)=[#8]',
            'pimeloyl':'[#8]=[#6]-[#6]-[#6]-[#6]-[#6]-[#6]-[#6]=[#8]',
            'piperidino':'[#7]1-[#6]-[#6]-[#6]-[#6]-[#6]-1',
            'pivaloyl':'[#6]-[#6](-[#6])(-[#6])-[#6]=[#8]',
            'prenyl':'[#6H2]-[#6]=[#6](-[#6])-[#6]',
            'propargyl':'[#6H2]-[#6]#[#6]',
            '1-propenyl':'[#6H]=[#6]-[#6]',
            '2-propenyl':'[#6H2]-[#6]=[#6]',
            'propionyl':'[#8]=[#6]-[#6]-[#6]',
            'propoxy':'[#8]-[#6]-[#6]-[#6]',
            'propyl':'[#6H2]-[#6]-[#6]',
            'propylidene':'[#6H]-[#6]-[#6]',
            'pyrryl':'[#7H]1:[#6]:[#6]:[#6]:[#6]:1',
            'salicyloyl':'[#8]-[#6]1:[#6]:[#6]:[#6]:[#6]:[#6]:1-[#6]=[#8]',
            'selenyl':'[SeH]',
            'seryl':'[#7]-[#6@@H](-[#6]-[#8])-[#6]=[#8]',
            'siloxy':'[#8]-[SiH3]',
            'silyl':'[SiH3]',
            'silyene':'[SiH2]',
            'sorboyl':'[#6]-[#6]=[#6]-[#6]=[#6]-[#6](-[#8])=[#8]',
            'stearoyl':'[#6]-[#6]-[#6]-[#6]-[#6]-[#6]-[#6]-[#6]-[#6]-[#6]-[#6]-[#6]-[#6]-[#6]-[#6]-[#6]-[#6]-[#6]=[#8]',
            'stearyl':'[#6H2]-[#6]-[#6]-[#6]-[#6]-[#6]-[#6]-[#6]-[#6]-[#6]-[#6]-[#6]-[#6]-[#6]-[#6]-[#6]-[#6]-[#6]',
            'styryl':'[#6H]=[#6]-[#6]1:[#6]:[#6]:[#6]:[#6]:[#6]:1',
            'suberoyl':'[#8]=[#6]-[#6]-[#6]-[#6]-[#6]-[#6]-[#6]-[#6]=[#8]',
            'succinyl':'[#8]=[#6]-[#6]-[#6]-[#6]=[#8]',
            'sulfamino':'[#7H]-[#16](=[#8])(-[#8])=[#8]',
            'sulfamoyl':'[#8]=[#16](-[#7])=[#8]',
            'sulfanilyl':'[#8]=[#16](-[#6]1:[#6]:[#6]:[#6](-[#7]):[#6]:[#6]:1)=[#8]',
            'sulfeno':'[#16]-[#8]',
            'sulfhydryl':'[#16H]',
            'sulfinyl':'[#16]=[#8]',
            'sulfo':'[#8]=[#16](-[#8])=[#8]',
            'sulfonyl':'[#8]=[#16]=[#8]',
            'terephthaloyl':'[#8]=[#6]-[#6]1:[#6]:[#6]:[#6](-[#6]=[#8]):[#6]:[#6]:1',
            'tetramethylene':'[#6]-[#6]-[#6]-[#6]',
            'thienyl':'[#6]1:[#6]:[#6]:[#6]:[#16]:1',
            'thiocarbonyl':'[#6H]=[#16]',
            'thiocarboxy':'[#16]=[#6]-[#8]',
            'thiocyanato':'[#16]-[#6]#[#7]',
            'thionyl':'[#16]=[#8]',
            'threonyl':'[#7]-[#6@@H](-[#6@H](-[#8])-[#6])-[#6]=[#8]',
            'toluidino':'[#7H]-[#6]1:[#6]:[#6]:[#6](-[#6]):[#6]:[#6]:1',
            'toluoyl':'[#6]-[#6]1:[#6]:[#6]:[#6](-[#6]=[#8]):[#6]:[#6]:1',
            'tolyl':'[#6]-[#6]1:[#6]:[#6]:[#6]:[#6]:[#6]:1',
            'alpha-tolyl':'[#6]-[#6]1:[#6]:[#6]:[#6]:[#6]:[#6]:1',
            'tolylene':'[#6H]-[#6]1:[#6]:[#6]:[#6]:[#6]:[#6]:1',
            'tosyl':'[#8]=[#16](-[#6]1:[#6]:[#6]:[#6](-[#6]):[#6]:[#6]:1)=[#8]',
            'triazano':'[#7H]-[#7]-[#7H]',
            'trimethylene':'[#6]-[#6]-[#6]',
            'trityl':'[#6](-[#6]1:[#6]:[#6]:[#6]:[#6]:[#6]:1)(-[#6]1:[#6]:[#6]:[#6]:[#6]:[#6]:1)-[#6]1:[#6]:[#6]:[#6]:[#6]:[#6]:1',
            'valeryl':'[#8]=[#6]-[#6]-[#6]-[#6]-[#6]',
            'valyl':'[#7]-[#6@@H](-[#6](-[#6])-[#6])-[#6]=[#8]',
            'vinyl':'[#6H]=[#6]',
            'vinylidene':'[#6]=[#6]',
            'xylidino':'[#7H]-[#6]1:[#6]:[#6]:[#6](-[#6]):[#6]:[#6]:1-[#6]',
            'xylyl':'[#6]-[#6]1:[#6]:[#6]:[#6]:[#6](-[#6]):[#6]:1',
            'xylylene':'[#7]-[#6]-[#6]1:[#6]:[#6]:[#6]:[#6](-[#6]-[#7]):[#6]:1',
        }

        return smarts
