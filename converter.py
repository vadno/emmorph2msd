#!/usr/bin/python3
# coding=utf-8

import sys
import mappings as cd
import lex_lists as ls
import defaults as df


default_features = {'df.A_DEFAULT': df.A_DEFAULT,
                    'df.N_DEFAULT': df.N_DEFAULT,
                    'df.P_DEFAULT': df.P_DEFAULT,
                    'df.M_DEFAULT': df.M_DEFAULT,
                    'df.R_DEFAULT': df.R_DEFAULT,
                    'df.V_DEFAULT': df.V_DEFAULT,
                    'df.C_DEFAULT': df.C_DEFAULT}


def feats_to_dict(msdfeature, msdfeature_dict):
    """
    elrendezi a meglévő jegyeket a jegy-érték struktúrába
    :param msdfeature: a jegy-érték sztringek listája
    :param msdfeature_dict: dictonary-be rendezve
    """

    for inflex_feat in msdfeature:
        key, attribute = inflex_feat.split('=')
        msdfeature_dict[key] = attribute
    del msdfeature[:]


def del_feat(featname, feats):
    """
    kitölri az adott jegyet a jegy-érték párok dictionary-jéből
    :param featname: a törlendő jegy
    :param feats: a jegy-érték párok dictionary-je
    """

    try:
        del feats[featname]
    except KeyError:
        pass


def defaults(msdfeature_dict, pos):
    """

    :param msdfeature_dict:
    :param pos:
    :return:
    """

    pos_def = 'df.' + pos + '_DEFAULT'
    for feat in default_features[pos_def]:
        msdfeature_dict[feat] = default_features[pos_def][feat]


def parse(token, lemma, emmorph):
    """
    az emmorph címke feldolgozása
    :param token: szóalak
    :param lemma: tő
    :param emmorph: az emmorph címke
    :return: ud szófajcímke és formázott ud jegy-érték párok
    """

    # az emmorph kód szétvágása szófajra, derivációs és inflexiós jegyekre
    emmorph_features = emmorph.rstrip(']').lstrip('[').split('][')
    pos_feats = [feat for feat in emmorph_features if feat.startswith('/') or feat == 'OTHER']
    deriv_feats = [feat for feat in emmorph_features if feat.startswith('_')]
    infl_feats = [feat for feat in emmorph_features if feat not in pos_feats + deriv_feats]

    # punktuáció önmagában, vagy szóra tapadó punct
    punct_feat = False
    if emmorph_features[-1] == 'Punct' and len(emmorph_features) > 1:
        punct_feat = True

    # a felsőfok jele szófaj volt, átkerül az inflexiós jegyek közé
    for feat in pos_feats:
        if feat in cd.POS_TO_INFL_FEAT:
            if feat in cd.SUPERLATIVE:
                pos_feats.remove(feat)
            infl_feats.append(feat)

    # a középfok jele és az ige néhány jegye (műveltető, gyakoritó, ható)
    # és az igenevek jegyei átkerülnek az inflexiós jegyek közé
    # de megmaradnak a deriv jegyek között is a megfelelő szófaj miatt
    for feat in deriv_feats:
        if feat in cd.DERIV_TO_INFL_FEAT:
            infl_feats.append(feat)

    if not pos_feats:
        pos_feats.append('ERROR')

    # POS tagek feldolgozása
    pos_feat = pos_feats[0]
    msdpos = ''
    msdtype = '-'
    if pos_feat in cd.POS_RULES:
        msdpos, msdtype = cd.POS_RULES[pos_feat]

    if pos_feat == 'PUNCT':
        if token in ('!', ',', '-', '.', ':', ';', '?', '–'):
            return token
        else:
            return 'K'

    for deriv_feat in deriv_feats:
        if deriv_feat in cd.DERIV_RULES:
            msdpos, msdtype = cd.DERIV_RULES[deriv_feat]

    if not msdpos:
        return 'Z'
    elif msdpos in ('Y', 'X'):
        return msdpos

    # feature-ök feldolgozása
    msdfeature_dict = {}

    # default jegyek
    if msdpos in ('V', 'A', 'N', 'M', 'P', 'R', 'O', 'C'):
        defaults(msdfeature_dict, msdpos)

    # névmástípusok a lex_listből a névmásokra és a határozószókra
    if msdpos in ('P', 'R'):
        msdfeature_dict['Person'] = '3'
        if lemma in ls.PRON_DEM:
            msdtype = 'd'
        elif lemma in ls.PRON_IND:
            msdtype = 'i'
        elif lemma in ls.PRON_TOT:
            msdtype = 'g'
        if msdpos == 'P':
            if lemma in ls.PRON_PRS:
                msdtype = 'p'
            elif lemma in ls.PRON_RCP:
                msdtype = 'y'
            elif lemma in ls.PRON_POSS:
                msdtype = 's'
            elif lemma in ls.PRON_REFL:
                msdtype = 'x'
        elif msdpos == 'R':
            if lemma in ls.NEG:
                msdtype = 'm'

    # ha olyan sorszámnév, amit az emmorph nem sorszámnévnek elemzett
    if msdpos == 'M' and punct_feat:
        msdtype = 'o'

    # inflexiós jegyek feldolgozása
    msdfeature = []
    for infl_feat in infl_feats:

        if msdpos == 'V' and '.' in infl_feat:
            subfeats = infl_feat.split('.')
            for subfeat in subfeats:
                if subfeat in cd.VERBAL_INFL_RULES:
                    msdfeature.extend(cd.VERBAL_INFL_RULES[subfeat])

        elif infl_feat in cd.VERBAL_INFL_RULES:
            msdfeature.extend(cd.VERBAL_INFL_RULES[infl_feat])

        elif infl_feat in cd.NOMINAL_INFL_RULES:
            msdfeature.extend(cd.NOMINAL_INFL_RULES[infl_feat])

    feats_to_dict(msdfeature, msdfeature_dict)

    if msdpos == 'V' and msdfeature_dict['VForm'] == 'n':
        if '.' in infl_feat:
            del_feat('Definiteness', msdfeature_dict)
        else:
            del_feat('Tense', msdfeature_dict)
            del_feat('Person', msdfeature_dict)
            del_feat('Number', msdfeature_dict)
            del_feat('Definiteness', msdfeature_dict)

    elif msdpos == 'R':
        if msdtype in ('i', 'g', 'v', 'p', 'r', 'm', 'q'):
            del_feat('Degree', msdfeature_dict)
        if msdtype in ('x', 'v', 'p'):
            del_feat('Person', msdfeature_dict)
            del_feat('Number', msdfeature_dict)

    elif msdpos == 'S':
        msdfeature_dict = {}


    return str(msdpos + msdtype + ''.join(msdfeature_dict[feat] for feat in msdfeature_dict).rstrip('-'))


def main():

    for line in sys.stdin:
        token, lemma, elemzes = line.strip().split('\t')[:3]
        msd = parse(token, lemma, elemzes)
        print(msd)


if __name__ == "__main__":
    main()
