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

APIs are the primary mechanism for developers to gain access to externally defined services and tools. However, previous research has revealed API misuses that violate the contract of APIs to be prevalent. Such misuses can have harmful consequences, especially in the context of cryptographic libraries. Various API-misuse detectors have been proposed to address this issue—including CogniCrypt, one of the most versatile of such detectors and that uses a language (CrySL) to specify cryptographic API usage contracts. Nonetheless, existing approaches to detect API misuse had not been designed for systematic reuse, ignoring the fact that different versions of a library, different versions of a platform, and different recommendations/guidelines might introduce variability in the correct usage of an API. Yet, little is known about how such variability impacts the specification of the correct API usage. This paper investigates this question by analyzing the impact of various sources of variability on widely used Java cryptographic libraries (including JCA/JCE, Bouncy Castle, and Google Tink). The results of our investigation show that sources of variability like new versions of the API and security standards significantly impact the specifications. We then use the insights gained from our investigation to motivate an extension to the CrySL language (named MetaCrySL), which builds on meta-programming concepts. We evaluate MetaCrySL by specifying usage rules for a family of Android versions and illustrate that MetaCrySL can model all forms of variability we identified and drastically reduce the size of a family of specifications for the correct usage of cryptographic APIs.


## Content

This artifact package presents the MetaCrySL implementations and makes available all tools,
datasets, and scripts used in this research. Please, click in the following link to browse in the artifact description.

   * [ECOOP artifact package](https://htmlpreview.github.io/?https://github.com/rbonifacio/TR-Meta-CrySL-Package/blob/master/artifact.html)

We also prepared a Docker image for running MetaCrySL from the command line.


```{shell}
$ docker pull rbonifacio/mcsl-java8
$ docker run -it rbonifacio/mcsl-java8:v1 bash
root@...:/mcsl> cd MetaCrySL
root@...:/mcsl/MetaCrySL> rascal-shell
rascal> import generator::Main;
rascal> main(|cwd:///samples/jca/android/config/Android0108.config|);
```