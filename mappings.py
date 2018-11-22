#!/usr/bin/python3
# coding=utf-8

####################
# SZÓFAJ SZABÁLYOK #
####################

POS_RULES = {
    '/Adj': ('A', 'f'),
    '/Adj|Abbr': ('A', 'f'),
    '/Adj|Attr': ('A', 'f'),
    '/Adj|Attr|Abbr': ('A', 'f'),
    '/Adj|Attr|Pro': ('P', 'd'),
    '/Adj|Pred': ('A', 'f'),
    '/Adj|Pro': ('P', 'd'),
    '/Adj|Pro|Int': ('P', 'q'),
    '/Adj|Pro|Rel': ('P', 'r'),
    '/Adj|Unit': ('A', 'f'),
    '/Adj|col': ('A', 'f'),
    '/Adj|nat': ('A', 'f'),

    '/Adv': ('R', 'x'),
    '/Adv|(Adj)': ('R', 'x'),
    '/Adv|(Num)': ('R', 'x'),
    '/Adv|Abbr': ('R', 'x'),
    '/Adv|Acronx': ('R', 'x'),
    '/Adv|AdjMod': ('R', 'x'),
    '/Adv|Pro': ('R', 'd'),
    '/Adv|Pro|Int': ('R', 'q'),
    '/Adv|Pro|Rel': ('R', 'r'),

    '/Cnj': ('C', 'c'),
    '/Cnj|Abbr': ('C', 'c'),

    '/Det': ('R', 'x'),
    '/Det|Art.Def': ('T', 'f'),
    '/Det|Art.NDef': ('T', 'i'),
    '/Det|Pro': ('P', 'd'),
    '/Det|Pro|(Post)': ('P', 'd'),
    '/Det|Pro|Int': ('P', 'q'),
    '/Det|Pro|Rel': ('P', 'r'),
    '/Det|Pro|def': ('P', 'd'),
    '/Det|Q.NDef': ('P', 'g'),
	'/Det|Q|indef': ('P', 'g'),
    '/Det|Q': ('P', 'i'),

    '/Inj-Utt': ('I', 'o'),

    '/N': ('N', 'n'),
    '/N|Abbr': ('N', 'n'),
    '/N|Abbr|ChemSym': ('N', 'n'),
    '/N|Acron': ('N', 'n'),
    '/N|Acronx': ('N', 'n'),
    '/N|Ltr': ('N', 'n'),
    '/N|Pro': ('P', 'p'),
    '/N|Pro|(Post)': ('P', 'd'),
    '/N|Pro|Abbr': ('P', 'p'),
    '/N|Pro|Int': ('P', 'q'),
    '/N|Pro|Rel': ('P', 'r'),
    '/N|Unit': ('N', 'n'),
    '/N|Unit|Abbr': ('N', 'n'),
    '/N|lat': ('N', 'n'),
    '/N|mat': ('N', 'n'),

    '/Num': ('M', 'c'),
    '/Num|Abbr': ('M', 'c'),
    '/Num|Attr': ('M', 'c'),
    '/Num|Digit': ('M', 'c'),
    '/Num|Pro': ('P', 'd'),
    '/Num|Pro|Int': ('P', 'q'),
    '/Num|Pro|Rel': ('P', 'r'),
    '/Num|Roman': ('M', 'c'),

    '/Post': ('S', 't'),
    '/Post|(Abl)': ('S', 't'),
    '/Post|(All)': ('S', 't'),
    '/Post|(Ela)': ('S', 't'),
    '/Post|(Ins)': ('S', 't'),
    '/Post|(N0)': ('S', 't'),
    '/Post|(Poss)': ('S', 't'),
    '/Post|(Subl)': ('S', 't'),
    '/Post|(Supe)': ('S', 't'),
    '/Post|(Ter)': ('S', 't'),

    '/Prep': ('C', 'c'),
    '/Prev': ('R', 'p'),
    '/QPtcl': ('R', 'q'),

    '/V': ('V', 'm'),

    '/S|Abbr': ('X', '_'),
    '/X': ('X', '_'),
    '/X|Abbr': ('X', '_')
}

###################
# DERIV SZABÁLYOK #
###################

DERIV_RULES = {
    '_Abe/Adj': ('A', 'f'),                      # "-A?tlAn, -tAlAn" abessivus = melléknévképző (fosztóképző)
    '_AdjVbz_Ntr/V': ('V', 'm'),                 # "-Vs?Odik, -Ul" denominális (melléknévből) intranzitívige-képző
    '_AdjVbz_Tr/V': ('V', 'm'),                  # "-ít" denominális (melléknévből) tranzitívige-képző
    '_Adjz:i/Adj': ('A', 'f'),                   # "-i" melléknévképző
    '_VAdjz:nivaló/Adj': ('A', 'f'),             # "-nivaló" melléknévképző
    '_Adjz:s/Adj': ('A', 'f'),                   # "-Vs" melléknévképző
    '_Adjz:Ó/Adj': ('A', 'f'),                   # " -Ó" melléknévképző, mély hangrendű magánhangzók ragozott alakjaiban
    '_Adjz:Ú/Adj': ('A', 'f'),                   # " -Ú" melléknévképző
    '_Adjz_Hab/Adj': ('A', 'f'),                 # "-Ós" melléknévképző: habituális
    '_Adjz_Loc:beli/Adj': ('A', 'f'),            # "-beli" melléknévképző (helyjelölő)
    '_Adjz_Ord:VdlAgOs/Adj': ('A', 'f'),         # "-VdlAgOs" melléknévképző (számnévből)
    '_Adjz_Quant/Adj': ('A', 'f'),               # "-nyi" mennyiségnévképző
    '_Adjz_Type:fajta/Adj': ('A', 'f'),          # "-fajta" melléknévképző (típusjelölő)
    '_Adjz_Type:forma/Adj': ('A', 'f'),          # "-forma" melléknévképző (típusjelölő)
    '_Adjz_Type:féle/Adj': ('A', 'f'),           # "-féle" melléknévképző (típusjelölő)
    '_Adjz_Type:szerű/Adj': ('A', 'f'),          # "-szerű" melléknévképző (típusjelölő)
    '_AdvPerfPtcp/Adv': ('R', 'v'),              # "-vÁn" határozói igenév
    '_AdvPtcp/Adv': ('R', 'v'),                  # "-vA" határozói igenév
    '_AdvPtcp:ttOn/Adv': ('R', 'v'),             # "-ttOn" határozói igenév
    '_AdvPtcp:vÁst/Adv': ('R', 'v'),             # " -vÁst" határozói igenév
    '_Advz:rét/Adv': ('R', 'x'),                 # "-rét" számnévi határozóképző
    '_Advz_LocDistr:szerte/Adv': ('R', 'x'),     # "-szerte" határozóképző (térbeli fedés)
    '_Advz_Quant:szám/Adv': ('R', 'x'),          # "-szám" határozóképző mennyiségekre
    '_Aggreg/Adv': ('M', 'c'),                   # "-An" csoportszámosság-határozó
    '_Caus/V': ('V', 's'),                       # "-t?At" műveltetőige-képző
    # '_Com:stUl/Adv'                            # "-stUl" comitativusi (társhatározói) esetrag #  nem módosít szófajt
    # '_Comp/Adj': ('A', 'f'),                   # "-bb" középfok                               #  nem módosít szófajt
    # '_Comp/Adv': ('R', 'x'),                   # "-bb" középfok                               #  nem módosít szófajt
    # '_Comp/Adv|Pro': ('P', 'd'),               # "-bb" középfok                               #  nem módosít szófajt
    # '_Comp/Num': ('M', 'c'),                   # "-bb" középfok                               #  nem módosít szófajt
    # '_Comp/Post|(Abl)': ('R', 'x'),            # "-bb" középfok                               #  nem módosít szófajt
    # '_Design/Adj': ('A', 'f'),                 # "-(bb)ik" kijelölő                           #  nem módosít szófajt
    '_Des/N': (('N', 'n')),                        # "-hatnék" desiderativus
    # '_Dim:cskA/Adj': ('A', 'f'),               # "-VcskA" kicsinyítő képző                    # nem módosít szófajt
    # '_Dim:cskA/N': (('N', 'n')),                 # "-VcskA" kicsinyítő képző                    # nem módosít szófajt
    '_Distr:nként/Adv': ('R', 'x'),              # "-Vnként" disztributív
    '_DistrFrq:ntA/Adv': ('R', 'x'),             # "-VntA" gyakorisághatározó
    '_Frac/Num': ('M', 'f'),                     # "-Vd" törtszámnév
    '_Freq/V': ('V', 'f'),                       # "-O?gAt" gyakorítóképző
    '_FutPtcp/Adj': ('A', 'u'),                  # "-AndÓ" „beálló" melléknévi igenév
    '_Ger/N': (('N', 'n')),                        # "-Ás" nomen actionis igenominalizáló
    '_Ger:tA/N': (('N', 'n')),                     # "-tA" birtokos igenominalizáló
    '_ImpfPtcp/Adj': ('A', 'p'),                 # "-Ó" folyamatos melléknévi igenév
    # '_Manner/Adv',                             # "-An, -Ul" határozóképző: módhatározó        # nem módosít szófajt
    # '_Manner:0/Adv',                           # határozóképző: módhatározó (zéró)            # nem módosít szófajt
    # '_MedPass/V': ('V', 'm'),                  # "-Ódik" mediális ige                         # nem módosít szófajt
    # '_Mlt-Iter/Adv',                           # "-szOr" multiplikatív/iteratív               # nem módosít szófajt
    # '_MltComp/Adv',                            # "-szOrtA" összehasonlító multiplikatív       # nem módosít szófajt
    '_Mod/V': ('V', 'o'),                        # -hAt" modális („ható") igeképző
    '_ModPtcp/Adj': ('A', 'p'),                  # "-hAtÓ" modális melléknévi igenév
    # '_Mrs/N': ('N', 'p'),                      # "-né" asszonynévképző                        # nem módosít szófajt
    '_NAdvz:ilAg/Adv': ('A', 'f'),               # "-ilAg" denominális (főnévből) határozóképző
    '_NVbz_Ntr:zik/V': ('V', 'm'),               # "-zik" intranzitív igeképző
    '_NVbz_Tr:z/V': ('V', 'm'),                  # "-z" denominális (főnévből) tranzitívige-képző
    '_NegModPtcp/Adj': ('A', 'f'),               # "-hAtAtlAn" tagadó modális melléknévi igenév
    '_NegPtcp/Adj': ('A', 'f'),                  # "-AtlAn" tagadó passzív melléknévi igenév (igei fosztóképző)
    '_Nz:s/N': (('N', 'n')),                       # "-Vs" főnévképző
    '_Nz_Abstr/N': (('N', 'n')),                   # "-sÁg" főnévképző absztraktfőnév-képző
    # '_Nz_Type:féleség/N': (('N', 'n')),          # "-féleség" főnévképző (típusjelölő)       # nem módosít szófajt
    # '_Nz_Type:szerűség/N': (('N', 'n')),         # "-szerűség" főnévképző (típusjelölő)      # nem módosít szófajt
    '_Ord/Adj': ('M', 'o'),                      # "-Vdik" sorszámnév
    '_OrdDate/N': (('N', 'n')),                    # "-Vdika" dátumokban a nap sorszámnévképzője
    # '_Pass/V': ('V', 'm'),                     # "-t?Atik" passzív                         # nem módosít szófajt
    '_PerfPtcp/Adj': ('A', 's'),                 # "-O?tt" befejezett melléknévi igenév
    '_PerfPtcp_Subj=tA/Adj': ('A', 's'),         # "-tA" befejezett melléknévi igenév
    '_Tmp_Ante/Adv': (('N', 'n')),                 # "-jA" időbeli megelőzés
    '_Tmp_Loc/Adv': ('R', 'x'),                  # "-vAl, -0" időhatározói végződés
    '_VAdvz:ÓlAg/Adv': ('R', 'x'),               # "-ÓlAg" határozóképző: igéből
    '_VNz:nivaló/N': (('N', 'n')),                 # "-nivaló" főnévképző
    '_Vbz:kOd/V': ('V', 'm')                     # "-s?kOdik" denominális igeképző
}

#########################
# POS helyett INFL jegy #
#########################

POS_TO_INFL_FEAT = ('/Supl',
                    '/Num|Digit',
                    '/Num|Roman',
                    '/CmpdPfx'                  # ez a jegy elnyelődik (önállóan nem élő összetételi előtag (almenü)
)

###############
# SUPERLATIVE #
###############

SUPERLATIVE = ('/Supl', )

###########################
# DERIV helyett INFL jegy #
###########################

DERIV_TO_INFL_FEAT = (
    '_Comp/Adj',                    # "-bb" középfok
    '_Comp/Adv',                    # "-bb" középfok
    '_Comp/Adv|Pro',                # "-bb" középfok
    '_Comp/Post|(Abl)'              # "-bb" középfok 
    '_Design/Adj',                  # "-(bb)ik" kijelölő

    '_Aggreg/Adv',                  # "-An" csoportszámosság-határozó
    '_Com:stUl/Adv',                # "-stUl" comitativusi (társhatározói) esetrag
    '_Distr:nként/Adv',             # "-Vnként" disztributív
    '_Manner/Adv',                  # "-An, -Ul" határozóképző: módhatározó
    '_Manner:0/Adv',                # határozóképző: módhat ha zéró toldalékként realizálódik a "-A?tlAn/-tAlAn" után
    '_Mlt-Iter/Adv',                # "-szOr" multiplikatív/iteratív
    '_MltComp/Adv'                  # "-szOrtA" összehasonlító multiplikatív
)

##########################
# inflexiós jegyek: igei #
##########################

VERBAL_INFL_RULES = {
    'Inf': ['VForm=n'],
    
    'Sbjv': ['VForm=m', 'Tense=p'],
    'Cond': ['VForm=c', 'Tense=p'],
    'Prs': ['VForm=i', 'Tense=p'],
    'Pst': ['VForm=i', 'Tense=s'],

    '1Sg': ['Number=s', 'Person=1'],
    '1Sg›2': ['Definiteness=2', 'Number=s', 'Person=1'],
    '2Sg': ['Number=s', 'Person=2'],
    '3Sg': ['Number=s', 'Person=3'],
    '1Pl': ['Number=p', 'Person=1'],
    '1Pl*': ['Number=p', 'Person=1'],
    '2Pl': ['Number=p', 'Person=2'],
    '3Pl': ['Number=p', 'Person=3'],
    '3Pl*': ['Number=p', 'Person=3'],
    'Def': ['Definiteness=y'],
    'NDef': ['Definiteness=n']
}

#############################
# inflexiós jegyek: névszói #
#############################

NOMINAL_INFL_RULES = {
    '/Num|Digit': ['Form=d'],
    '/Num|Roman': ['Form=r'],
    '/Supl': ['Degree=s'],

    '_Comp/Adj': ['Degree=c'],
    '_Comp/Adv|Pro': ['Degree=c'],
    '_Comp/Adv': ['Degree=c'],
    '_Comp/Post|(Abl)': ['Degree=c'],
    '_Design/Adj': ['Degree=c'],

    '_Aggreg/Adv': ['Case=w'],
    '_Com:stUl/Adv': ['Case=q'],
    '_Distr:nként/Adv': ['Case=u'],
    '_Manner/Adv': ['Case=w'],           # Cas=w lehet A, N, M, P
    '_Manner:0/Adv': ['Case=w'],
    '_Mlt-Iter/Adv': ['Case=6'],
    '_MltComp/Adv': ['Case=6'],

    'Nom': ['Case=n'],
    'Acc': ['Case=a'],
    'Dat': ['Case=d'],
    'Ins': ['Case=i'],
    'Cau': ['Case=c'],
    'Ine': ['Case=2'],
    'Supe': ['Case=p'],
    'Ade': ['Case=3'],
    'Ill': ['Case=x'],
    'Ela': ['Case=e'],
    'Del': ['Case=h'],
    'Subl': ['Case=s'],
    'Abl': ['Case=b'],
    'All': ['Case=t'],
    'Ter': ['Case=9'],
    'Temp': ['Case=m'],
    'Loc': ['Case=l'],
    'Transl': ['Case=y'],
    'Ess': ['Case=w'],
    'EssFor:ként': ['Case=f'],
    'EssFor:képp': ['Case=f'],
    'EssFor:képpen': ['Case=f'],

    'Pl': ['Number=p'],
    'Fam.Pl': ['Number=p'],
    '1Sg': ['Number=s', 'Person=1'],
    '2Sg': ['Number=s', 'Person=2'],
    '3Sg': ['Number=s', 'Person=3'],
    '1Pl': ['Number=p', 'Person=1'],
    '2Pl': ['Number=p', 'Person=2'],
    '3Pl': ['Number=p', 'Person=3'],

    'Poss.1Sg': ['OwnerNumber=s', 'OwnerPerson=1'],
    'Poss.2Sg': ['OwnerNumber=s', 'OwnerPerson=2'],
    'Poss.3Sg': ['OwnerNumber=s', 'OwnerPerson=3'],
    'Poss.1Pl': ['OwnerNumber=p', 'OwnerPerson=1'],
    'Poss.2Pl': ['OwnerNumber=p', 'OwnerPerson=2'],
    'Poss.3Pl': ['OwnerNumber=p', 'OwnerPerson=3'],

    'Pl.Poss.1Sg': ['Number=p', 'OwnerNumber=s', 'OwnerPerson=1'],
    'Pl.Poss.2Sg': ['Number=p', 'OwnerNumber=s', 'OwnerPerson=2'],
    'Pl.Poss.3Sg': ['Number=p', 'OwnerNumber=s', 'OwnerPerson=3'],
    'Pl.Poss.1Pl': ['Number=p', 'OwnerNumber=p', 'OwnerPerson=1'],
    'Pl.Poss.2Pl': ['Number=p', 'OwnerNumber=p', 'OwnerPerson=2'],
    'Pl.Poss.3Pl': ['Number=p', 'OwnerNumber=p', 'OwnerPerson=3'],

    'AnP': ['OwnedNumber=s'],
    'AnP.Pl': ['OwnedNumber=p']
}

