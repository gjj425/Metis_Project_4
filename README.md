# Metis Project 4: An NLP Analysis of Governor Cuomo's Daily COVID Updates

## Description
Starting March 10, 2020, New York Governor Andrew Cuomo provided daily COVID-19 updates to the public, providing insights to his concerns, goals, and policy making logic for the duration of the crisis to date. Project 4 uses LDA to conduct a topic analysis on trascripts of these meetings through October 26, 2020. Please note that the governor switches from a schedule of daily updates to an "as-needed" basis, generally providing new updates every 2-4 days. 

## Features and Target Variables
The current iteration of this project isolated 11 topics. Although I believe that 11 topics is the most efficient delineator, I also believe some of these topics can be isloated and re-processed on a stand alone basis to create sub-topics.

## Data Used
Transcripts were web scraped from the following website: https://www.rev.com/blog/transcript-tag/andrew-cuomo-transcripts

## Tools Used
SpaCy, Sklearn (LDA, pyLDAvis, matplotlib; also used but did not contribute to conclusion: LSA, NMF)

## Snapshots

![image](https://user-images.githubusercontent.com/65420143/122335078-b814f000-cf08-11eb-9347-3acfbcea62f3.png)

![image](https://user-images.githubusercontent.com/65420143/122335037-a895a700-cf08-11eb-8425-b8adccf77822.png)

## Possible impacts
The analysis unveils patterns showing how the governor responds given a certain scenario. Particulary striking is the Enforcement and political topics measured against a timeline of events, as well as the Political COVID topic and State Mandate topics measured against coronavirus contraction/hospitalization statistics as well as eachother. Given the immediacey and lack of ability to plan, the NLP analysis of Governor Cuomo's COVID Updates could provide future leaders with guidance on the proper way to effectively communicate with its consitiuents. 
