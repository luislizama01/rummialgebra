#!/usr/bin/env python3
"""Independent reference enumerator for six published RummiAlgebra puzzles.
This script does not import or call the HTML implementation.
It checks small instances with individual physical tile identities.
"""
from itertools import combinations, permutations
from collections import defaultdict

SCENARIOS = [
    ('Rearrange', '3R 4R 5R 6R', '7R 6A 6V', 12, False),
    ('Initial meld', '', '3R 4R 5R 6A 6V 6N 7R 8R', 30, True),
    ('Regroup', '6R 6A 6V', '5R 7R 8R 6N 8A 8V', 42, False),
    ('Bridge joker', '', '5R 7R J', 18, False),
    ('Group joker', '', '9R 9A J', 27, False),
    ('Two jokers', '', '4R 7R J J', 24, False),
]
COLORS=('R','A','V','N')

def parse(table,hand):
    ret=[]
    for origin,s in [('mesa',table),('mano',hand)]:
        for tok in s.split():
            if tok=='J': ret.append((0,'J',origin))
            else: ret.append((int(tok[:-1]),tok[-1],origin))
    return ret

def meld_candidates(tiles):
    n=len(tiles)
    for length in range(3,min(n,13)+1):
        for inds in combinations(range(n),length):
            regular=[tiles[i] for i in inds if tiles[i][1]!='J']
            joker_idx=[i for i in inds if tiles[i][1]=='J']
            if length<=4 and regular and len({t[0] for t in regular})==1 and len({t[1] for t in regular})==len(regular):
                val=regular[0][0]
                avail=[c for c in COLORS if c not in {t[1] for t in regular}]
                for picks in permutations(avail,len(joker_idx)):
                    ass=dict(zip(joker_idx,[(val,c) for c in picks]))
                    yield 'group',inds,ass
            for color in COLORS:
                if any(t[1]!=color for t in regular):continue
                values=[t[0] for t in regular]
                if len(values)!=len(set(values)):continue
                for start in range(1,15-length):
                    seq=set(range(start,start+length))
                    if not set(values).issubset(seq):continue
                    missing=sorted(seq-set(values))
                    if len(missing)!=len(joker_idx):continue
                    for vals in permutations(missing,len(joker_idx)):
                        ass=dict(zip(joker_idx,[(v,color) for v in vals]))
                        yield 'run',inds,ass

def brute(tiles,opening=False):
    n=len(tiles); tabmask=sum(1<<i for i,t in enumerate(tiles) if t[2]=='mesa')
    choices=defaultdict(list); unique=set()
    for kind,inds,assign in meld_candidates(tiles):
        mask=sum(1<<i for i in inds)
        points=sum((assign[i][0] if tiles[i][1]=='J' else tiles[i][0]) for i in inds if tiles[i][2]=='mano')
        sig=(kind,mask,tuple(sorted(assign.items())))
        if sig in unique:continue
        unique.add(sig); choices[mask].append((points,kind,inds,assign))
    D={0:(0,[])}
    for mask in range(1<<n):
        if mask not in D:continue
        val,path=D[mask]
        for m,opts in choices.items():
            if mask&m:continue
            for pts,kind,inds,ass in opts:
                nm=mask|m; candidate=val+pts
                if nm not in D or candidate>D[nm][0]:
                    D[nm]=(candidate,path+[(kind,inds,ass)])
    valid=[(value,path) for m,(value,path) in D.items() if m&tabmask==tabmask and (not opening or value>=30)]
    if not valid:return None
    return max(valid,key=lambda x:x[0])

if __name__=='__main__':
    print('Independent exhaustive reference checks for RummiAlgebra V2')
    for name,table,hand,expect,opening in SCENARIOS:
        result=brute(parse(table,hand),opening)
        got=None if result is None else result[0]
        print(f'{name:17s}: expected={expect:2d}, computed={got}, match={got==expect}')
        if result is None or got!=expect: raise AssertionError(name)
    print('PASS: 6/6')
