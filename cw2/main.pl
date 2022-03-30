% This section will cover the initial production rules

% Sentence Rules
s(s(Tree1, Tree2)) --> np(Tree1, Pluralisation, Perspective), vp(Tree2, Pluralisation, Perspective).

% Verb Phrase rules
vp(vp(Tree1, Tree2), Pluralisation, Perspective) --> v(Tree1, tv, Pluralisation, Perspective), np(Tree2, Pluralisation2, _).
vp(vp(Tree), Pluralisation, Perspective) --> v(Tree, iv, Pluralisation, Perspective).

% Verb Rules
v(v(Word), Transitive, Pluralisation, Perspective) --> [Word], {lex(Word, Transitive, Pluralisation, Perspective)}.

% Noun phrase rules
np(np(Tree1, Tree2), Pluralisation, 3) --> det(Tree1, Pluralisation), nbar(Tree2, Pluralisation).
np(np(Tree), Pluralisation, Perspective) --> pro(Tree, Pluralisation, Perspective, Argument).

% Determiner rules
det(det(Word), Pluralisation) --> [Word], {lex(Word, det, Pluralisation)}.

% Nbar rules
nbar(nbar(Tree), Pluralisation) --> n(Tree, Pluralisation).
nbar(nbar(Tree1, Tree2), Pluralisation) --> jp(Tree1), n(Tree2, Pluralisation).

% Noun rules
n(n(Word), Pluralisation) --> [Word], {lex(Word, n, Pluralisation)}.

% Pronoun rules
pro(pro(Word), Pluralisation, Perspective, Argument) --> [Word], {lex(Word, pro, Pluralisation, Perspective, Argument)}.

% Adjective Phrase Rules
jp(jp(Tree)) --> adj(Tree).

% Adjective rules
adj(adj(Word)) --> [Word], {lex(Word, adj)}.


% This section will detail the lexicon, as specified in the CW brief. 
% TODO: Add animacy check!!!!

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
lex(know,tv,singular,1).
lex(know,tv,singular,2).
lex(knows,tv,singular,3).
lex(know,tv,plural,_).
lex(see,tv,singular,1).
lex(see,tv,singular,2).
lex(sees,tv,singular,3).
lex(see,tv,plural,_).
lex(hire,tv,singular,1).
lex(hire,tv,singular,2).
lex(hires,tv,singular,3).
lex(hire,tv,plural,_).
lex(fall,iv,singular,1).
lex(fall,iv,singular,2).
lex(falls,iv,singular,3).
lex(fall,iv,plural,_).
lex(sleep,iv,singular,1).
lex(sleep,iv,singular,2).
lex(sleeps,iv,singular,3).
lex(sleep,iv,plural,_).

% Determiners
lex(the,det,_).
lex(a,det,singular).
lex(two,det,plural).

% Nouns
lex(man,n,singular).
lex(woman,n,singular).
lex(apple,n,singular).
lex(chair,n,singular).
lex(room,n,singular).
lex(men,n,plural).
lex(women,n,plural).
lex(apples,n,plural).
lex(chairs,n,plural).
lex(rooms,n,plural).

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