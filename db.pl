
enggerm(table, tisch, m).
enggerm(chair, stuhl, m).
enggerm(bed, bet, n).
enggerm(child, kind, n).
enggerm(brother, bruder, m).
enggerm(sister, schwester, f).
enggerm(house, haus, n).
enggerm(sun, sonne, f).
enggerm(cloud, wolke, f).
enggerm(wind, wind, m).
enggerm(rain, regen, m).

engit(table, tavolo, m).
engit(chair, sedia, f).
engit(bed, letto, m).
engit(child, bambino, m).
engit(child, bambina, f).
engit(brother, fratello, m).
engit(sister, sorella, f).
engit(house, casa, f).
engit(sun, sone, f).
engit(cloud, nube, f).
engit(wind, vento, m).
engit(rain, pioggia, f).

article( f, die ).
article( m, der ).
article( n, das ).


gerwitharticle( E, A, G ) :- enggerm(E, G, S), enggerm(E, G, S), article(S, A).

gerit( G, I ) :- enggerm(E, G, S), engit(E,I,S).

samegender(E) :- enggerm(A, G, E), engit(A, I, E).

male(carl_gustaf). 
male(daniel). 
male(carl_philip). 
male(christopher_o_neill). 
male(oscar). 
male(alexander). 
male(gabriel). 
male(julian). 
male(nicolas).
female(silvia). 
female(victoria). 
female(sofia). 
female(madeleine). 
female(estelle). 
female(leonore). 
female(adrienne). 
 
parent(carl_gustaf, victoria). 
parent(carl_gustaf, carl_philip). 
parent(carl_gustaf, madeleine). 
parent(silvia, victoria). 
parent(silvia, carl_philip). 
parent(silvia, madeleine). 
parent(daniel, estelle). 
parent(daniel, oscar). 
parent(victoria, estelle). 
parent(victoria, oscar). 
parent(carl_philip, alexander). 
parent(carl_philip, gabriel). 
parent(carl_philip, julian). 
parent(sofia, alexander). 
parent(sofia, gabriel). 
parent(sofia, julian). 
parent(christopher_o_neill, leonore). 
parent(christopher_o_neill, adrienne). 
parent(christopher_o_neill, nicolas). 
parent(madeleine, leonore). 
parent(madeleine, adrienne).
parent(madeleine, nicolas).
 
rulesover(carl_gustaf, sweden). 
rulesover(silvia, sweden). 
rulesover(daniel, vastergotland). 
rulesover(victoria, vastergotland). 
rulesover(carl_philip, varmland). 
rulesover(sofia, varmland). 
rulesover(madeleine, halsingland_and_gastrikland). 
rulesover(estelle, ostergotland). 
rulesover(oscar, skane). 
rulesover(alexander, sodermanland). 
rulesover(leonore, gotland). 
rulesover(nicolas, angermanland).

sibling(X, Y) :- parent(D, N), parent(D, N).
brother(X, Y) :- sibling(X, Y), male(Y).
sister(X, Y) :- sibling(X, Y), female(Y).

father(carl_gustaf).
father(carl_philip).
father(daniel).
father(christopher_o_neill).
mother(silvia).
mother(sofia).
mother(madeleine).
mother(victoria).

son(carl_philip).
son(nicolas).
son(oscar).
son(alexander).
son(gabriel).
son(juan).
daughter(madeleine).
daughter(victoria).
daughter(estelle).
daughter(leonore).
daughter(adrienne).

king(carl_gustaf).
queen(silvia).

duke(daniel).
duke(oscar).
duke(carl_philip).
duke(nicolas).
duke(alexander).
duchess(victoria).
duchess(estelle).
duchess(sofia).
duchess(madeleine).
duchess(leonore).



