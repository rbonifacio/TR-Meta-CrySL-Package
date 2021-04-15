# Dealing with Variability in API Misuse Specification (Artifact)

This is the **replication package** for the artifact evaluation
of our paper *Dealing with Variability in API Misuse Specification*,
accepted for publication at the 35th European
Conference on Object-Oriented Programming (ECOOP 2021).

## Authors

   * Rodrigo Bonifácio
   * Stefan Krüger
   * Krishna Narasimhan
   * Eric Bodden
   * Mira Mezini

## Abstract

APIs are the primary mechanism for developers to gain access to externally defined services and tools. However, previous research has revealed API misuses that violate the contract of APIs to be prevalent. Such misuses can have disastrous consequences, especially in the context of cryptographic libraries. To address this issue, various API-misuse detectors have been proposed. CogniCrypt, one of the most versatile of such detectors, involves a specification language(CrySL), to specify API usage contracts. APIs evolve over time, though, and any specification describes API usages only for a single version of an API in a single context. There are various sources of variability that affect how an API should be used. For example, a new release may introduce breaking changes. Many APIs have a provider architecture promoting extensibility through pluggable implementations. In the context of cryptography, different standards require different usages of the same API. Currently, little is known about how such variability impacts the specification of correct API usage. In this paper, we investigate this question by analysing the impact of various sources of variability on the most widely used cryptographic library in Java, the JCA. The results of our investigation show that sources of variability like new versions of the API, security standards and pluggable providers significantly impact the specifications and introduce number of breaking changes. We then use the insights gained from our investigation to motivate extensions to the CrySL language called MetaCrySL, which builds on the concept of meta variables and feature modelling. We evaluate MetaCrySL by specifying usage rules for a family of Android versions, and illustrate that our DSL extension, MetaCrySL is not only able to model all forms of variability we identified, but also drastically simplify specifying a large family of APIs and maintaining these specifications when compared to the CrySL.

## Link to the package

   * [ECOOP artifact package](https://htmlpreview.github.io/?https://github.com/rbonifacio/TR-Meta-CrySL-Package/blob/master/artifact.html)