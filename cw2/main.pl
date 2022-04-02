% This section details the initial production rules

% Sentence Rules
s(s(Tree1, Tree2)) --> np(Tree1, Pluralisation, Perspective, subject, Animacy), vp(Tree2, Pluralisation, Perspective, Animacy).

% Verb Phrase rules
vp(vp(Tree1, Tree2), Pluralisation, Perspective, Animacy) --> v(Tree1, tv, Pluralisation, Perspective, Animacy), np(Tree2, _, _, object, _).
vp(vp(Tree), Pluralisation, Perspective, Animacy) --> v(Tree, iv, Pluralisation, Perspective, Animacy).

% Verb Rules
v(v(Word), Transitive, Pluralisation, Perspective, Animacy) --> [Word], {lex(Word, Transitive, Pluralisation, Perspective, Animacy)}.

% Noun phrase rules
np(np(Tree1, Tree2, Tree3), Pluralisation, 3, _, Animacy) --> det(Tree1, Pluralisation), nbar(Tree2, Pluralisation, Animacy), pp(Tree3).
np(np(Tree1, Tree2), Pluralisation, 3, _, Animacy) --> det(Tree1, Pluralisation), nbar(Tree2, Pluralisation, Animacy).
np(np(Tree), Pluralisation, Perspective, Argument, _) --> pro(Tree, Pluralisation, Perspective, Argument).
np(np(Tree1, Tree2), final, Pluralisation, 3, _, Animacy) --> det(Tree1, Pluralisation), nbar(Tree2, Pluralisation, Animacy).

% Determiner rules
det(det(Word), Pluralisation) --> [Word], {lex(Word, det, Pluralisation)}.

% Nbar rules
nbar(nbar(Tree), Pluralisation, Animacy) --> n(Tree, Pluralisation, Animacy).
nbar(nbar(Tree), Pluralisation, Animacy) --> jp(Tree, Pluralisation, Animacy).

% Noun rules
n(n(Word), Pluralisation, Animacy) --> [Word], {lex(Word, n, Pluralisation, Animacy)}.

% Pronoun rules
pro(pro(Word), Pluralisation, Perspective, Argument) --> [Word], {lex(Word, pro, Pluralisation, Perspective, Argument)}.

% Adjective Phrase Rules
jp(jp(Tree1, Tree2), Pluralisation, Animacy) --> adj(Tree1), n(Tree2, Pluralisation, Animacy).
jp(jp(Tree1, Tree2), Pluralisation, Animacy) --> adj(Tree1), jp(Tree2, Pluralisation, Animacy).

% Adjective rules
adj(adj(Word)) --> [Word], {lex(Word, adj)}.

% Prepositional Phrase rules   TODO decide on pronoun prepositionals
pp(pp(Tree1, Tree2)) --> prep(Tree1), np(Tree2, _, 3, _, _). 
pp(pp(Tree1, Tree2, pp(Tree3, Tree4))) --> prep(Tree1), np(Tree2, final, _, 3, _, Animacy), prep(Tree3), np(Tree4, _, 3, _, Animacy).

% Preposition rules
prep(prep(Word)) --> [Word], {lex(Word, prep)}.



% This section details the lexicon, as specified in the CW brief. 
    % An animacy property has been added to nouns and verbs, with values of 'animate' or 'inanimate'
    % Otherwise, all properties are as provided in the coursework brief.

% Pronouns
lex(i,pro,singular,1,subject).
lex(you,pro,singular,2,subject).
lex(he,pro,singular,3,subject).
lex(she,pro,singular,3,subject).
lex(it,pro,singular,3,subject).
lex(we,pro,plural,1,subject).
lex(you,pro,plural,2,subject).
lex(they,pro,plural,3,subject).
lex(me,pro,singular,1,object).
lex(you,pro,singular,2,object).
lex(him,pro,singular,3,object).
lex(her,pro,singular,3,object).
lex(it,pro,singular,3,object).
lex(us,pro,plural,1,object).
lex(you,pro,plural,2,object).
lex(them,pro,plural,3,object).

% Verbs
lex(know,tv,singular,1,animate).
lex(know,tv,singular,2,animate).
lex(knows,tv,singular,3,animate).
lex(know,tv,plural,_,animate).
lex(see,tv,singular,1,animate).
lex(see,tv,singular,2,animate).
lex(sees,tv,singular,3,animate).
lex(see,tv,plural,_,animate).
lex(hire,tv,singular,1,animate).
lex(hire,tv,singular,2,animate).
lex(hires,tv,singular,3,animate).
lex(hire,tv,plural,_,animate).
lex(fall,iv,singular,1,_).
lex(fall,iv,singular,2,_).
lex(falls,iv,singular,3,_).
lex(fall,iv,plural,_,_).
lex(sleep,iv,singular,1,animate).
lex(sleep,iv,singular,2,animate).
lex(sleeps,iv,singular,3,animate).
lex(sleep,iv,plural,_,animate).

% Determiners
lex(the,det,_).
lex(a,det,singular).
lex(two,det,plural).

% Nouns
lex(man,n,singular,animate).
lex(woman,n,singular,animate).
lex(apple,n,singular,inanimate).
lex(chair,n,singular,inanimate).
lex(room,n,singular,inanimate).
lex(men,n,plural,animate).
lex(women,n,plural,animate).
lex(apples,n,plural,inanimate).
lex(chairs,n,plural,inanimate).
lex(rooms,n,plural,inanimate).

% Prepositions
lex(on,prep).
lex(in,prep).
lex(under,prep).

% Adjectives
lex(old,adj).
lex(young,adj).
lex(red,adj).
lex(short,adj).
lex(tall,adj).



% ------ Test Sentences & Outputs ------

/**
1.
s(Tree,[the,woman,sees,the,apples],[]).
Tree = s(np(det(the), nbar(n(woman))), vp(v(sees), np(det(the), nbar(n(apples))))) .

2.
s(Tree,[a,woman,knows,him],[]).
Tree = s(np(det(a), nbar(n(woman))), vp(v(knows), np(pro(him)))) .

3.
s(Tree,[two,woman,hires,a,man],[]).
false.

4.
s(Tree,[two,women,hire,a,man],[]).
Tree = s(np(det(two), nbar(n(women))), vp(v(hire), np(det(a), nbar(n(man))))) .

5.
s(Tree,[she,knows,her],[]).
Tree = s(np(pro(she)), vp(v(knows), np(pro(her)))) .

6.
s(Tree,[she,know,the,man],[]).
false.

7.
s(Tree,[us,see,the,apple],[]).
false.

8.
s(Tree,[we,see,the,apple],[]).
Tree = s(np(pro(we)), vp(v(see), np(det(the), nbar(n(apple))))) .

9.
s(Tree,[i,know,a,short,man],[]).
Tree = s(np(pro(i)), vp(v(know), np(det(a), nbar(jp(adj(short), n(man)))))) .

10.
s(Tree,[he,hires,they],[]).
false.

11.
s(Tree,[two,apples,fall],[]).
Tree = s(np(det(two), nbar(n(apples))), vp(v(fall))) .

12.
s(Tree,[the,apple,falls],[]).
Tree = s(np(det(the), nbar(n(apple))), vp(v(falls))) .

13.
s(Tree,[the,apples,fall],[]).
Tree = s(np(det(the), nbar(n(apples))), vp(v(fall))) .

14.
s(Tree,[i,sleep],[]).
Tree = s(np(pro(i)), vp(v(sleep))) .

15.
s(Tree,[you,sleep],[]).
Tree = s(np(pro(you)), vp(v(sleep))) .

16.
s(Tree,[she,sleeps],[]).
Tree = s(np(pro(she)), vp(v(sleeps))).

17.
s(Tree,[he,sleep],[]).
false.

18.
s(Tree,[them,sleep],[]).
false.

19.
s(Tree,[a,men,sleep],[]).
false.

20.
s(Tree,[the,tall,woman,sees,the,red],[]).
false.

21.
s(Tree,[the,young,tall,man,knows,the,old,short,woman],[]).
Tree = s(np(det(the), nbar(jp(adj(young), jp(adj(tall), n(man))))), vp(v(knows), np(det(the), nbar(jp(adj(old), jp(adj(short), n(woman))))))) .

22.
s(Tree,[a,man,tall,knows,the,short,woman],[]).
false.

23.
s(Tree,[a,man,on,a,chair,sees,a,woman,in,a,room],[]).
Tree = s(np(det(a), nbar(n(man)), pp(prep(on), np(det(a), nbar(n(chair))))), vp(v(sees), np(det(a), nbar(n(woman)), pp(prep(in), np(det(a), nbar(n(room))))))) .

24.
s(Tree,[a,man,on,a,chair,sees,a,woman,a,room,in],[]).
false.

25. N.B. For this one, the output length exceeds prolog's default depth, so 'w' was pressed after the query to write the entire output with prolog's write/1 function.
s(Tree,[the,tall,young,woman,in,a,room,on,the,chair,in,a,room,in,the,room,sees,the,red,apples,under,the,chair],[]).
Tree = s(np(det(the), nbar(jp(adj(tall), jp(adj(young), n(woman)))), pp(prep(in), np(det(a), nbar(n(room)), pp(prep(on), np(det(the), nbar(n(chair)), pp(prep(in), np(det(a), nbar(n(...)), pp(prep(...), np(..., ...))))))))), vp(v(sees), np(det(the), nbar(jp(adj(red), n(apples))), pp(prep(under), np(det(the), nbar(n(chair))))))) [write]
Tree = s(np(det(the), nbar(jp(adj(tall), jp(adj(young), n(woman)))), pp(prep(in), np(det(a), nbar(n(room)), pp(prep(on), np(det(the), nbar(n(chair)), pp(prep(in), np(det(a), nbar(n(room)), pp(prep(in), np(det(the), nbar(n(room))))))))))), vp(v(sees), np(det(the), nbar(jp(adj(red), n(apples))), pp(prep(under), np(det(the), nbar(n(chair)))))))

26.
s(Tree,[the,woman,sees,the,apples],[]).
Tree = s(np(det(the), nbar(n(woman))), vp(v(sees), np(det(the), nbar(n(apples))))) .

27.
s(Tree,[a,woman,knows,him],[]).
Tree = s(np(det(a), nbar(n(woman))), vp(v(knows), np(pro(him)))) .

28.
s(Tree,[the,man,sleeps],[]).
Tree = s(np(det(the), nbar(n(man))), vp(v(sleeps))) .

29.
s(Tree,[the,room,sleeps],[]).
false.

30.
s(Tree,[the,apple,sees,the,chair],[]).
false.

31.
s(Tree,[the,rooms,know,the,man],[]).
false.

32.
s(Tree,[the,apple,falls],[]).
Tree = s(np(det(the), nbar(n(apple))), vp(v(falls))) .

33.
s(Tree,[the,man,falls],[]).
Tree = s(np(det(the), nbar(n(man))), vp(v(falls))) .
**/
