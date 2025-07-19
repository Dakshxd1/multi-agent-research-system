# AI Research Report Generator


An autonomous multi-agent research system that explores complex topics, gathers and validates claims from the web, and generates professional Word reports with clickable citations.

##  Objective
Build an autonomous AI system that:
- Accepts any research topic
- Automatically breaks it into subtopics
- Collects web data and validates claims
- Generates a professional Word document with citations, images, and insights
  
##  AGENTS 

- **disambiguator_agent** : Refine the topic is it related to health,company,or fruit ex (apple , apple.ltd)

- **Planner**: Decomposes the topic into subtopics ex: Subtopics: ['Here are 4 detailed subtopics for researching "Universal Basic Income Field Experiments," focusing on key areas and offering specific avenues for investigation:', '**1. Economic Impacts: Productivity, Labor Market Participation, and Entrepreneurship**'.
- **Researchers**: Scrape and summarize relevant content  : Searching for: **1. Economic Impacts: Productivity, Labor Market Participation, and Entrepreneurship**
                                                                             Found URL: https://wol.iza.org/articles/entrepreneurs-and-their-impact-on-jobs-and-economic-growth/long
                                                                            Searching for: *   **Description:** This subtopic delves into how UBI impacts the economic behavior of recipients. It examines changes in labor market participation (employment rates, hours worked, job search activities), entrepreneurial activities (business creation, self-employment), and productivity (efficiency, skill development).
                                                                                  Found URL: https://www.roosevelthouse.hunter.cuny.edu/?forum-post=universal-basic-income-ubi-may-affect-labor-market

  - **Critic**: Validates claims against source content Trough Gemini.
  - **Report Writer**: Generates clean, readable `.docx` reports  : use gemini for competitor analysis and conclusion.
  - **competitor_agent**: Finds a real-world competitor for the topic (e.g., Apple → Samsung) and compares.

## 🚀 Features

- Pulls accurate claims directly from trusted online sources

- Adds clickable links to original sources wherever available

- Cleans up formatting by removing bold asterisks while keeping the text

- Ends with a polished conclusion written by Gemini AI

- Automatically adds an image from Wikipedia’s infobox to the report

- Includes a competitor comparison table for relevant topics

- Generates a well-structured and easy-to-read Word document

- Reviews and fixes weak claims by revalidating them automatically

## orchestrator : use this file to run.

# output : A word doucument with hyperlinks.

**using gemini api** for the concultion ,makeing of sub-topic,validating the claims.(AIzaSyCs5fIyQsGb0BGYOuCCFEmHA_6HeQjoeBQ)
**serper ai** for do web search the topic and subtopic find the valid links.(9f74a262b571fb746b74aff9103d4296e33b3e51)



