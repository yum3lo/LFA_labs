# Intro to formal languages. Regular grammars. Finite Automata.

### Course: Formal Languages & Finite Automata

### Author: Cucoș Maria

## Theory
A formal language is a set of strings of symbols drawn from some alphabet. These languages are used to describe the syntax of programming languages, regular expressions, and many other areas. An alphabet is a finite set of symbols used to form strings. Strings are sequences of symbols from an alphabet. In computer science, this formal language is essential for the definition of computer programs and the expression of algorithmic problems. 

Formal Languages are classified into different levels based on the Chomsky hierarchy. These levels include Recursively enumerable languages (type 0), Context-free languages (type 1), Context-sensitive languages (type 2) and Regular languages (type 3). These languages all have different sets of rules for construction and provide different levels of expressibility. Furthermore, formal language theory provides systematic ways to determine whether a given string adheres to the rules of a language, which is fundamental for the creation of software like compilers or interpreters. Regular grammars are formal systems used to describe regular languages. Components of Regular Grammars are terminals, non-terminals, productions and the start symbol. 

Finite Automata are abstract computational devices used to recognize patterns within strings. It’s characterised by limited memory and the potential to change from one state to another when triggered by external inputs. 

## Objectives
1. Discover what a language is and what it needs to have in order to be considered a formal one;
2. For a grammar definition do the following:
(a) Implement a type/class for the grammar;
(b) Add one function that would generate 5 valid strings from the language expressed by the given
grammar;
(c) Implement some functionality that would convert and object of type Grammar to one of type
Finite Automaton;
(d) For the Finite Automaton add a method that checks if an input string can be obtained via the state
transition from it;
