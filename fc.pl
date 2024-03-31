% Define facts and rules
:- dynamic hypothesis/1.

hypothesis(has_fever) :- symptom(fever).
hypothesis(has_cough) :- symptom(cough).
hypothesis(has_headache) :- symptom(headache).
hypothesis(has_runny_nose) :- symptom(runny_nose).

symptom(fever) :- body_temperature(high).
symptom(cough) :- congestion(chest), irritation(throat).
symptom(headache) :- congestion(head), irritation(eyes).
symptom(runny_nose) :- congestion(nose).

% Provide initial facts
body_temperature(high).
congestion(chest).
congestion(head).
congestion(nose).
irritation(throat).
irritation(eyes).

% Define forward chaining algorithm
forward_chaining :-
    hypothesis(Disease),
    write('Patient may have: '), write(Disease), nl,
    retract(hypothesis(Disease)),
    fail.
forward_chaining.
