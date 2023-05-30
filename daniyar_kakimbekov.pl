

/*didn't finish*/
cartesian([], [], []).
cartesian([P], [Q|T], R):-
    makepairs(P, [Q|T], R).

/*works*/
makepairs(P, [], []).
makepairs(P, [Q|T], [R|S]):-
    R = pair(P,Q),
    makepairs(P, T, S).

/*works*/
deepmember(P , [P | Q]).
deepmember(P,  [L | T]):-
    deepmember(P , L);
    deepmember(P , T).

/*works*/
notcontains(P, [L]):- P\=L.
notcontains(P, [Q|L]):- P\=Q, notcontains(P, L).

/*not sure if it works*/
/*1st case*/
setinsertion(Q, [], [Q]).
/*2nd case*/
setinsertion(Q, [Q|T], [Q|T]):- Q\=L.
/*3rd case*/
setinsertion(Q, [R|L],[R|T]):-
    setinsertion(Q, T, L).


graph1( [ edge( 1, 2 ), edge( 2, 3 ), edge( 3, 4 ), edge( 4, 1 ) ] ).
graph2( [ edge( 1, 2 ), edge( 2, 3 ), edge( 2, 4 ), edge( 3, 4 ),
edge( 4, 3 ), edge( 3, 1 ), edge( 4, 1 ) ] ).
graph3( [ edge( 1, 2 ), edge( 1, 3 ), edge( 2, 3 ), edge( 3, 2 ),
edge( 3, 4 ), edge( 2, 4 ), edge( 4, 6 ), edge( 4, 5 ),
edge( 5, 6 ), edge( 6, 5 ), edge( 6, 7 ), edge( 5, 7 ),
edge( 7, 1 ) ] ).

/*has to work, but not sure*/
allnodes([], []).
allnodes([edge(E1,E2)|T], L):-allnodes(T, R),
    setinsertion(E1, R, P),
    setinsertion(E2, P, L).

/*not sure*/
neighbour([edge(E1, E2)|R], E1, E2).
neighbour([edge(P,Q)|T], E1, E2):- neighbour(T, E1, E2).

/*didn't finish*/
pathextension(P, Q, 0, R).

/*didn't finish*/
hamiltonian(G, Circ).









